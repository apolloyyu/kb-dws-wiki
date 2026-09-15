# dws aitable +field-create

kind: shortcut
completeness: full
usage: dws aitable +field-create
description: 批量新增字段，15 个分片并核对新字段 ID、类型与配置
source: internal/shortcut/aitable/parity_create.go:45
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --fields <String>: 非空字段结构数组，fieldName/type/config/description/aiConfig，最多 100 个
- --resume-field-ids <StringSlice>: 提供 fields 开头已创建字段的 ID；核实名称与结构后按 fields 顺序返回，只创建剩余字段，全部提供时只核实

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
