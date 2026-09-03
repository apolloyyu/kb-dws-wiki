# dws aitable +view-set-frozen-cols

kind: shortcut
completeness: full
description: 设置视图冻结列数（0 表示取消冻结）
source: internal/shortcut/aitable/aitable.go:1509
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --view-id <String>: View ID
- --count <Int>: 冻结列数，须 >= 0

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
