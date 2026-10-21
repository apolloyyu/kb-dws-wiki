---
title: 实时消息监听到回复的参数与标识契约
maintenance: manual
intents: realtime_reply
triggers: 实时回复, 自动回复, 实时响应, 监听并回复, 主动回复, 实时监听
contract:
  - 监听入口、输出结构和发送入口分别核验；不要混用consume与listen-im的参数，或把一个命令的参数搬到另一个命令。
---

# 实时消息监听到回复的参数与标识契约
- 官方流程是监听事件后把稳定标识交给发送入口，不是轮询历史消息；单聊发送人选择有明确示例。
  {{quote: docs/products/event.md | "监听并自动回复某人的单聊消息"}}
  {{quote: docs/products/event.md | "监听我和 userId test-user-001 的单聊消息"}}
- listen-im 自身已将个人事件消费配置为 Flatten=true 和 NDJSON；不接受 consume 的 flatten 参数。指定群的监听参数是 chat-id 或 chat-query，不是发送入口的 group；按源码中的种类和参数组合取值，不在示例中自行拼接其他入口的参数。
  {{code: internal/app/event_listen_im.go | f.StringVar(&opts.ChatID, "chat-id"}}
  {{code: internal/app/event_listen_im.go | f.StringVar(&opts.ChatQuery, "chat-query"}}
  {{code: internal/app/event_listen_im.go | --kind group 必须且只能指定 --chat-id 或 --chat-query 之一}}
  {{quote: docs/products/event.md | "监听 XX 群消息"}}
  {{quote: docs/products/event.md | "监听我的所有单聊消息"}}
  {{quote: docs/products/event.md | "监听我所在的所有群消息"}}
  {{code: internal/app/event_listen_im.go | Flatten:          true,}}
  {{code: internal/app/event_listen_im.go | FormatRaw: "ndjson",}}
- 必须先确定事件输出结构再解析字段；flatten与序列化格式不是同一个开关。
  {{quote: docs/products/event.md | `--flatten` 的 `jq_root_path` 为 `.`}}
  {{quote: docs/products/event.md | 群自动回复使用顶层 `conversation_id`}}
- 统一发送入口的群目标参数是group，而非根据别的命令猜conversation-id。单聊持有sender_open_dingtalk_id时使用open-dingtalk-id参数；user参数收userId，不能混用这两类标识。
  {{code: internal/shortcut/chat/unified_send.go | Name: "group", Type: shortcut.FlagString}}
  {{code: internal/shortcut/chat/unified_send.go | Name: "user", Type: shortcut.FlagString}}
  {{code: internal/shortcut/chat/unified_send.go | Name: "open-dingtalk-id", Type: shortcut.FlagString}}
