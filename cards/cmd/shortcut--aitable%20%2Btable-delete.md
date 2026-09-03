# dws aitable +table-delete

kind: shortcut
completeness: full
usage: dws aitable +table-delete
description: 删除指定数据表（不可逆）
source: internal/shortcut/aitable/aitable.go:526
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --table-id <String>: 待删除 Table ID
- --reason <String>: 删除原因（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
