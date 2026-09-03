# dws aitable +table-bootstrap

kind: shortcut
completeness: full
description: 在已有 Base 中一次创建数据表和字段，自动分片并读回验证
source: internal/shortcut/aitable/table_bootstrap.go:19
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID
- --name <String>: 新数据表名称
- --fields <String>: 字段结构 JSON 数组；字段对象使用 fieldName/type/config

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
