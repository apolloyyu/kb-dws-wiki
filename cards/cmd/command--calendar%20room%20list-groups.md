# dws calendar room list-groups

kind: command
completeness: full
description: List meeting room groups (usually by building or floor) available to the user.
use_when: When the agent is narrowing down rooms by location before running an availability search.
source: internal/helpers/calendar.go:1124
visible_flags: 2

## Flags
- --limit <String>: 页大小 (可选，不填默认 100，超过 100 按 100 处理)
- --page <String>: 分页起始位置 (可选，不填默认 0)

## Related
- dws calendar room add
- dws calendar room delete
- dws calendar room search
