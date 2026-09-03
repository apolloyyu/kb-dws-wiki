# dws aitable +import-data

kind: shortcut
completeness: full
description: 将已上传文件导入 AI 表格（新建表或追加到已有表）
source: internal/shortcut/aitable/aitable.go:2663
visible_flags: 6

## Flags
- --import-id <String>: import upload 返回的 importId
- --table-id <String>: 追加导入的目标 Table ID（可选）
- --timeout <Int>: 等待超时（可选）
- --header-row <Int>: 表头行号（可选）
- --src-sheet-name <String>: 源 Sheet 名（可选）
- --field-mapping <String>: 字段映射 JSON 对象，key=目标字段名 value=源列名（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
