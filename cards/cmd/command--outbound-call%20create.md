# dws outbound-call create

kind: command
completeness: partial
usage: dws outbound-call create
description: —
source: internal/helpers/outbound_call.go:48
visible_flags: 3
partial_reason: missing_description

## Flags
- --callee <String> required: 被呼叫人的钉钉 userId，原样发送给服务端
- --task <String> required: 本次外呼需要完成的事项与要求，包括需要告知的信息、需要询问或确认的问题
- --opening <String> required: 外呼开场白，用于向被呼叫人问好，并说明身份和来电目的。

## Related
- dws outbound-call detail
