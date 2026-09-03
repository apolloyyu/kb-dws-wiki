# dws aitable +field-update

kind: shortcut
completeness: full
usage: dws aitable +field-update
description: 更新字段名称 / 配置 / AI 配置（类型不可改）
source: internal/shortcut/aitable/aitable.go:608
visible_flags: 6

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --field-id <String>: Field ID
- --name <String>: 新字段名（可选）
- --config <String>: 字段配置 JSON（可选）
- --ai-config <String>: AI 配置 JSON（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
