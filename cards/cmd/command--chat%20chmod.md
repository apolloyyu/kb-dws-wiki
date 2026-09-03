# dws chat chmod

kind: command
completeness: full
usage: dws chat chmod <scope>
description: 授予 chat 高风险操作权限
example: dws chat chmod chat.message:send --agentCode agt-wukong-xxxx --grant-type timed --ttl 24h --permParam openCid=cidXXXXXXXXXX
source: internal/helpers/chat.go:2738
visible_flags: 9

## Flags
- --agentCode <String>: Agent 标识，默认 wukong
- --grant-type <String>: 授权策略: once|session|timed|permanent
- --ttl <String>: timed 授权有效期，如 1h/4h/24h/7d
- --permParam <StringArray>: 授权原始业务参数，格式 key=value，可重复传入
- --conversation-id <String>: 群聊 openConversationId
- --open-dingtalk-id <String>: 单聊目标 openDingTalkId
- --user <String>: 单聊目标 userId（与 --open-dingtalk-id 二选一）
- --session-id <String>: session 授权的会话标识
- --yes (-y) <Bool>: 确认执行 chat 高风险授权操作

## Related
- dws chat bot
- dws chat category
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
- dws chat conversation-file
