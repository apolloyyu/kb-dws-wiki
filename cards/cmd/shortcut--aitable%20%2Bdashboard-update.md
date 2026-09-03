# dws aitable +dashboard-update

kind: shortcut
completeness: full
description: 更新指定 dashboard 的配置
source: internal/shortcut/aitable/aitable.go:2226
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --dashboard-id <String>: Dashboard ID
- --config <String>: dashboard 配置 JSON（可选，与 --name 二选一）
- --name <String>: dashboard 名称（可选，与 --config 二选一）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
