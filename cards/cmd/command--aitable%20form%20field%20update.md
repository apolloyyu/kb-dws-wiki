# dws aitable form field update

kind: command
completeness: partial
usage: dws aitable form field update
description: —
source: internal/helpers/aitable.go:6913
visible_flags: 8
partial_reason: missing_description

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID (必填)
- --field-id <String>: 目标字段 ID（通过 form field list 获取）(必填)
- --required <String>: 设置字段在表单中的必填状态 (true/false，可选)；
- --field-description <String>: 设置字段在表单中的描述文案（可选）；空字符串省略，纯空白报错；
- --display-condition <String>: 整体替换条件 JSON：单层 and/or、1至20个 eq [字段ID,选项ID]；
- --clear-display-condition <Bool>: 显式清除条件（保留必填与固定隐藏）；

## Related
- dws aitable form field hide
- dws aitable form field list
