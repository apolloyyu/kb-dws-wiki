# dws aitable +view-lock

kind: shortcut
completeness: full
usage: dws aitable +view-lock
description: 锁定视图（默认）或解锁（--off）
source: internal/shortcut/aitable/aitable.go:1432
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --view-id <String>: View ID
- --off <Bool>: 传入则解锁（unlock），默认锁定（lock）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
