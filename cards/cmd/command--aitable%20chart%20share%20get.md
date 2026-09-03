# dws aitable chart share get

kind: command
completeness: full
description: Retrieve the current public-sharing configuration of a chart, including share link and permissions.
use_when: When the agent needs to check whether a chart is already shared externally before issuing a link.
source: internal/helpers/aitable.go:1812
visible_flags: 1

## Flags
- --base-id <String>: Base 唯一标识。优先使用 base search / base list 返回值 (必填)

## Related
- dws aitable chart share update
