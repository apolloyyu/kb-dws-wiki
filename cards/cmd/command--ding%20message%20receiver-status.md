# dws ding message receiver-status

kind: command
completeness: full
usage: dws ding message receiver-status
description: 查看 DING 接收状态
example: dws ding message receiver-status --ding-id <openDingId>
source: internal/helpers/ding.go:318
visible_flags: 1

## Flags
- --ding-id <String> required: DING 消息 openDingId (必填)

## Related
- dws ding message list
- dws ding message recall
- dws ding message recall-personal
- dws ding message send
- dws ding message send-by-message
- dws ding message send-personal
