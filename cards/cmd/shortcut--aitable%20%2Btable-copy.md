# dws aitable +table-copy

kind: shortcut
completeness: full
usage: dws aitable +table-copy
description: 跨 Base 同步复制一张表的可创建字段结构，并可同步复制全部记录
source: internal/shortcut/aitable/table_copy.go:36
visible_flags: 7

## Flags
- --source-base-id <String>: 源 Base ID
- --source-table-id <String>: 源 Table ID
- --target-base-id <String>: 目标 Base ID
- --new-name <String>: 目标表名
- --strict-fields <Bool>: 发现公式/关联/查找/系统等无法重建字段时在写入前失败；不代表复制所有视图
- --include-records <Bool>: 复制全部记录；默认只复制可安全重建的字段结构
- --max-records <Int>: —

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
