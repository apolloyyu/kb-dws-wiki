# dws smart +free-slots

kind: shortcut
completeness: full
description: 找我某天工作时段内的空闲时间段（默认今天 09:00-18:00）
source: internal/shortcut/smart/free_slots.go:40
visible_flags: 3

## Flags
- --in-days <Int>: 几天后（可选，0=今天默认）
- --from <Int>: 工作时段起始小时（可选，默认 9）
- --to <Int>: 工作时段结束小时（可选，默认 18）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
