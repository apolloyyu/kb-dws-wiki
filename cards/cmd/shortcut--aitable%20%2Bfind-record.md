# dws aitable +find-record

kind: shortcut
completeness: full
usage: dws aitable +find-record
description: 在指定多维表里按关键词查记录（只读）
source: internal/shortcut/smart/find_record.go:40
visible_flags: 3

## Flags
- --base <String>: Base ID（多维表所属 base）
- --table <String>: Table ID（要检索的数据表）
- --query <String>: 全文关键词（可选，不填则取前若干条）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
