# dws aitable +attachment-put

kind: shortcut
completeness: full
usage: dws aitable +attachment-put
description: 准备凭证、实际 PUT 本地文件、写入 attachment 单元格并读回验证
source: internal/shortcut/aitable/attachment_composite.go:35
visible_flags: 7

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-id <String>: Record ID
- --field-id <String>: attachment Field ID
- --file <String>: 本地文件路径
- --mode <String>: —
- --mime-type <String>: 覆盖自动推断的 MIME type（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
- dws aitable +base-copy
