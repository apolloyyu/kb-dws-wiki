---
title: 事件系统的来源、投递与心跳边界
maintenance: manual
intents: event_runtime
triggers: event consume, event listen, 事件监听, 事件订阅, stream, 长连接, 个人事件, event bus, 事件总线, websocket, 心跳, 断连, heartbeat, ping, pong, IPC
---

# 事件系统的来源、投递与心跳边界

## 云端控制帧与本地心跳
- 个人源用 WebSocket 读取云端帧；SYSTEM ping 回复 pong 并回传 Data；disconnect 先确认，再返回可重试错误，由重连循环重新取票。不能把这条个人链路说成应用 Stream SDK 的行为。
  {{code: internal/event/source/personal.go | conn.ReadMessage()}}
  {{code: internal/event/source/personal.go | payload.NewDataFrameAckPong(df.GetMessageId())}}
  {{code: internal/event/source/personal.go | resp.Data = df.Data}}
  {{code: internal/event/source/personal.go | personal source: server requested reconnect}}
  {{code: internal/event/source/personal.go | 先确认控制帧，再由重连循环关闭本连接并重新申请 ticket。}}
- 上述 ping 分支只证明收到云端 ping 时回应，不证明服务端发送周期或“长时间没收到 ping 就断连”的超时策略。个人源读取失败会进入重连流程；服务器发 disconnect 也会要求重连。
  {{code: internal/event/source/personal.go | personal source: read websocket:}}
- 本地 IPC 定义了 heartbeat 帧类型，consume 读到时静默处理；v1 总线读循环忽略 heartbeat/future 入站帧。不能把协议类型或静默接收分支称为已经启用的周期性 IPC 健康检查，更不能用它证明云端存活。
  {{code: internal/event/transport/protocol.go | FrameTypeHeartbeat}}
  {{code: internal/event/consume/run.go | case transport.FrameTypeHeartbeat:}}
  {{code: internal/event/consume/run.go | // silent}}
  {{code: internal/event/bus/daemon.go | Heartbeat / future client→bus frames: ignored for v1.}}

## 令牌、取票与既有连接
- 取票前通过 AccessTokenProvider 取得访问令牌；取票收到401且配置了刷新回调时，刷新后重试一次。连接建立后的读取循环依赖读取结果和收到的系统控制帧，不能由取票刷新逻辑推导既有 WebSocket 在令牌过期瞬间的服务端行为，也不能承诺刷新过程事件绝不丢失。
  {{code: internal/event/source/personal.go | resolveSourceAccessToken(ctx, s.cfg.AccessTokenProvider}}
  {{code: internal/event/source/personal.go | if status == http.StatusUnauthorized && s.cfg.ForceRefreshToken != nil}}
  {{code: internal/event/source/personal.go | Retry once with the freshly rotated token; a second 401 stays fatal.}}
  {{code: internal/event/source/personal.go | messageType, data, err := conn.ReadMessage()}}

## ACK 与可靠性
- 个人源的非 SYSTEM 帧先构造 RawEvent 并 emit，再发送成功 ACK；ACK 写失败返回可重试错误。这里只证明客户端顺序，不能证明服务端如何重投、是否无限重试或消费者已经完成业务处理。
  {{code: internal/event/source/personal.go | emit(raw)}}
  {{code: internal/event/source/personal.go | resp := payload.NewSuccessDataFrameResponse()}}
  {{code: internal/event/source/personal.go | personal source: write ack:}}
- bus 在投递前用 RawEvent.DedupKey() 做 LRU 去重，默认容量 8192；配置可覆盖容量。不能据此承诺 exactly-once、持久去重或断线期间绝不丢事件。
  {{code: internal/event/bus/daemon.go | if dd.Seen(raw.DedupKey())}}
  {{code: internal/event/bus/daemon.go | dd := dedup.NewWithCapacity(cfg.DedupCapacity)}}
  {{code: internal/event/dedup/lru.go | const DefaultCapacity = 8192}}

## 多消费者与进程锁
- Hub.Deliver 收集全部匹配者（matcher 命中的消费者），再逐个投递，是匹配后的扇出；并非多个消费者自动独占一条事件。满缓冲采用 drop-oldest，因此 ACK 也不能证明每个消费者都收到了。
  {{code: internal/event/bus/hub.go | matched = append(matched, c)}}
  {{code: internal/event/bus/hub.go | for _, c := range matched}}
  {{code: internal/event/bus/hub.go | oldest entry in any full sendCh}}
- bus.lock 是 bus 工作目录内的单实例锁；目录包含 edition/source_kind/identity_hash。不能把它解释为只允许一个 consumer。
  {{code: internal/event/bus/lockfile.go | bus single-instance lock}}
  {{code: internal/event/bus/lockfile.go | (<ConfigDir>/events/<edition>/<source_kind>/<identity_hash>/).}}
- `--client-id` 是根命令的持久参数，不能因叶子命令卡没有重复列出就断言它不存在。它的语义是覆盖 OAuth 客户端 ID，不能单凭此参数承诺两条个人事件源相互隔离；隔离还要沿实际身份/源的选择路径核验。
  {{code: internal/app/flags.go | cmd.PersistentFlags().StringVar(&flags.ClientID, "client-id"}}

## 个人源的身份隔离
- 常规个人源把 Identity.Key() 哈希后作为 identity_hash。企业和用户均非空时，Key 包含 corpId、userId、clientId、sourceId；否则优先 LocalSubject，再使用 unknown 分支。应用 ID 与组织/用户 ID 是不同维度，不能用「每个 clientId 一条连接」概括所有个人源。runtime token 模式另接受传入的 identity-hash，不能用常规分支替它推导身份。
  {{code: internal/event/personal/client.go | "corp_user", corpID, userID, clientID, sourceID}}
  {{code: internal/event/personal/client.go | "local_subject", localSubject, clientID, sourceID}}
  {{code: internal/event/personal/client.go | "unknown", corpID, userID, clientID, sourceID}}
  {{code: internal/app/event_command.go | identityHash = dwsevent.IdentityHash(identity.Key())}}
  {{code: internal/app/event_command.go | identityHash = strings.TrimSpace(identityHashFlag)}}

## 平台与强制模式
- 停止订阅、清理本地状态与停止 bus 是不同步骤。当前个人事件 stop 的实现先逐个删除订阅，再清理本地状态和停止消费者，最后在无剩余订阅时停止 bus。因此不能只凭「signal bus ... not supported by windows」就推导订阅永远清理不掉、必定复用失效订阅或云端不再推送；历史报错仍需对照当时版本和逐步日志。发布说明只证明其明确写出的修复项，不证明这一整条因果链或修复已覆盖所有场景。
  {{code: internal/app/event_personal_command.go | if err := personalDeleteSubscription(client, ctx, id)}}
  {{code: internal/app/event_personal_command.go | if err := personalRemoveRunStates(workDir, subscribeIDs)}}
  {{code: internal/app/event_personal_command.go | if err := personalStopBus(busctl.StopConfig}}
- Windows IPC 使用命名管道，其余平台使用 Unix socket；不能把某个历史 stop 缺陷泛化为 Windows 不支持事件。具体修复版本另查 CHANGELOG。
  {{code: internal/event/endpoint.go | if goos == "windows"}}
  {{code: internal/event/endpoint.go | return `\\.\pipe\dws-event-`}}
- `--force` 只在 `--foreground` 模式生效，跳过单实例锁；帮助原文提示这可能让云事件随机切分，不是推荐的多消费者分发方式。
  {{code: internal/app/event_command.go | 仅 --foreground 模式生效：跳过单实例锁}}
