# dws minutes speaker replace

kind: command
completeness: full
usage: dws minutes speaker replace
description: Reassign speaker labels in a meeting note (e.g. map "Speaker 1" to a specific user).
example: dws minutes speaker replace --id <taskUuid> --from "张三" --to "李四"
use_when: When the agent cleans up speaker diarization after automatic labels came out wrong.
source: internal/helpers/minutes.go:1070
visible_flags: 4

## Flags
- --id <String>: 听记 taskUuid (必填)
- --from <String>: 源发言人昵称 (必填)
- --to <String>: 目标发言人昵称 (必填)
- --target-uid <String>: 目标发言人钉钉 UID (可选)

## Related
- dws minutes speaker summary
