# dws aitable +dashboard-delete

kind: shortcut
completeness: full
usage: dws aitable +dashboard-delete
description: 删除指定 dashboard（级联删除其 chart，不可逆）
source: internal/shortcut/aitable/aitable.go:2264
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --dashboard-id <String>: Dashboard ID
- --reason <String>: 删除原因（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
