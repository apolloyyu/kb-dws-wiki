# dws aitable +view-update

kind: shortcut
completeness: full
usage: dws aitable +view-update
description: 更新视图名称 / 描述 / 配置（visibleFieldIds、filter、sort、group 等）
source: internal/shortcut/aitable/aitable.go:1289
visible_flags: 6

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --view-id <String>: View ID
- --name <String>: 新视图名（可选）
- --desc <String>: 视图描述 JSON（可选）
- --config <String>: 视图配置更新项 JSON（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
