# dws aitable +import-file

kind: shortcut
completeness: full
usage: dws aitable +import-file
description: 申请上传、PUT 本地 CSV/XLS/XLSX，并用同一 importId 触发导入；也可只续等已有任务
source: internal/shortcut/aitable/import_file.go:66
visible_flags: 8

## Flags
- --base-id <String>: Base ID；首次导入模式使用，值不能为空
- --file <String>: 本地非空普通 CSV/XLS/XLSX 文件；首次导入模式使用，值不能为空
- --resume-import-id <String>: 只续等已有 importId；与首次导入参数互斥
- --table-id <String>: 追加导入的目标 Table ID（可选）
- --timeout <Int>: 服务端等待超时（可选，必须大于 0）
- --header-row <Int>: XLS/XLSX 表头行号（可选，必须大于 0；CSV 不支持）
- --src-sheet-name <String>: XLS/XLSX 源 Sheet 名（可选；CSV 不支持）
- --field-mapping <String>: 字段映射 JSON 对象，目标字段名和源列名不能为空（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
