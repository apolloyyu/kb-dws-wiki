# dws ding message recall

kind: command
completeness: full
description: Recall (retract) a previously sent DING message.
use_when: When the agent sent a DING in error and must withdraw it before recipients act on it.
source: internal/helpers/ding.go:241
visible_flags: 2

## Flags
- --robot-code <String>: 机器人 ID (必填，或设 DINGTALK_DING_ROBOT_CODE)
- --id <String>: DING 消息 ID (必填)

## Related
- dws ding message receiver-status
- dws ding message send
