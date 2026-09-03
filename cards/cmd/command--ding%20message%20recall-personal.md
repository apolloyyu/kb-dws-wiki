# dws ding message recall-personal

kind: command
completeness: full
usage: dws ding message recall-personal
description: 以用户身份撤回 DING
example: dws ding message recall-personal --id <openDingId>
source: internal/helpers/ding.go:416
visible_flags: 1

## Flags
- --id <String> required: DING 消息 openDingId (必填)

## Related
- dws ding message list
- dws ding message recall
- dws ding message receiver-status
- dws ding message send
- dws ding message send-by-message
- dws ding message send-personal
