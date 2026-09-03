# dws aitable +view-preset-apply

kind: shortcut
completeness: full
usage: dws aitable +view-preset-apply
description: 按视图精确名称幂等创建或更新预设，并读回校验类型和 config
source: internal/shortcut/aitable/view_preset.go:23
visible_flags: 5

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --name <String>: 预设视图精确名称
- --view-type <String>: 视图类型
- --config <String>: 目标 config JSON 对象

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
