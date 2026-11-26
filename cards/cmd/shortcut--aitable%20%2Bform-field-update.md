# dws aitable +form-field-update

kind: shortcut
completeness: full
usage: dws aitable +form-field-update
description: 更新表单字段必填、描述或条件显隐
source: internal/shortcut/aitable/aitable.go:1958
visible_flags: 8

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --view-id <String>: 表单 View ID
- --field-id <String>: Field ID
- --required <Bool>: 是否必填（可选）；
- --field-description <String>: 字段描述（可选）；空字符串省略，纯空白报错；
- --display-condition <String>: 整体替换显示条件 JSON：单层and/or与1至20个eq [字段ID,选项ID]；
- --clear-display-condition <Bool>: 仅true清除条件，保留必填和固定隐藏；

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
