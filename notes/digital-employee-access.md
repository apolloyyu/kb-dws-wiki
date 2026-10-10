---
title: 数字员工的可见范围与对话白名单
source_refs: internal/helpers/deap_agent_runtime.go, internal/helpers/deap_agent_adapter.go, internal/helpers/deap_agent.go, internal/helpers/deap_agent_channel.go, internal/helpers/chat.go
intents: access
---

# 数字员工的可见范围与对话白名单

回答「群里谁能和数字员工对话 / 怎么让别人也能用 / 怎么把数字员工拉进群」时以本篇为准。本篇只覆盖 dws `dingtalk-tag` 数字员工(标识 `agentUuid`)。

## 两层控制:可见范围 ≠ 对话白名单

- **可见范围**:`dws dingtalk-tag manage set-visibility --agent-uuid <agentUuid> --visibility ALL|PARTIAL [--user-ids ...] [--dept-ids ...]`。改的是草稿、全量替换,`manage publish` 后才上线(`deap_agent.go` `newDeapAgentSetVisibilityCommand`,约 L456)。
- **对话白名单**:`dws dingtalk-tag connect` 接入普通本地 Agent 时的 `--allowed-users`、`--allowed-groups`(`deap_agent_adapter.go` `digitalEmployeeAgentFlags`,约 L224-L225)。

## 谁的消息会被处理(connect 接入普通本地 Agent)

- 白名单 = 执行 connect 的主管本人 + `--allowed-users` 里逐个精确解析的 userId(`deap_agent_adapter.go` `prepareDigitalEmployeeLocal`,约 L233-L246),即**默认仅主管可用**。
- 本地运行时对收到的每条消息先执行 `accept()`(`deap_agent_runtime.go` 约 L211-L228),与 `--response-mode` 无关:
  - 数字员工自己发的消息忽略;
  - 发送人不在白名单 → 丢弃;
  - 单聊:发送人在白名单即处理;
  - 群聊(含群内 @):发送人在白名单,**且**该群 openConversationId 在 `--allowed-groups` 中。
- 匹配是逐个精确比较(`employeeContains`,约 L202),**没有通配或「所有人」选项**。不在名单内的人 @ 它,消息被直接丢弃,不会有任何回复。

### 让一个群里的多人使用

```bash
dws dingtalk-tag connect --agent-uuid <agentUuid> --channel <agent> \
  --allowed-groups <openConversationId> --allowed-users <userId1>,<userId2> --dry-run --format json
```

确认后去掉 `--dry-run` 加 `--yes` 执行。要用的群成员须逐个列入 `--allowed-users`。

## 常见误解

- **「数字员工通过关联机器人的 robotCode,用 `chat group members add-bot` 入群」:无依据。** `add-bot` 是把自定义机器人加到当前用户有管理权限的群,必须传应用机器人的 `--robot-code`(`chat.go` 约 L3606);dingtalk-tag 命令面只用 `agentUuid`,文档明确不对用户暴露 uid/robotUid,dingtalk-tag 相关源码(`deap_agent*.go`)里没有 robotCode 字段,dws 不提供获取数字员工 robotCode 的途径。
- **把数字员工加入某个群的操作方式**:dws 源码与文档都没有提供。回答写「dws 文档未说明」,不要编造客户端菜单路径或开放平台接口。
- **`set-visibility --visibility ALL` ≠ 群里所有人都能对话**:可见范围与对话白名单是两层,互不替代。
- **未覆盖**:`--channel dsh` 由 DSH 宿主运行(另一条代码路径),`open_code` 由平台托管,这两种情况下群里谁能对话,dws 未说明。DEAP 智能体 / AI 助理与 dingtalk-tag 是什么关系,dws 也未说明(只知 dingtalk-tag 固定调用 MCP server `deap-dev`)。
