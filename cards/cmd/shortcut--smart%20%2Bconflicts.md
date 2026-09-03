# dws smart +conflicts

kind: shortcut
completeness: full
usage: dws smart +conflicts
description: 检测我某天日程的时间冲突（重叠/双重预订，默认今天）
source: internal/shortcut/smart/conflicts.go:39
visible_flags: 1

## Flags
- --in-days <Int>: 几天后（可选，0=今天默认，1=明天…）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
