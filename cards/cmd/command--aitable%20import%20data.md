# dws aitable import data

kind: command
completeness: full
usage: dws aitable import data
description: Import previously-uploaded data (e.g. Excel) into a datasheet as records, optionally creating fields.
example: dws aitable import data --import-id IMPORT_ID
use_when: When the agent is bulk-loading external data into a Base after a successful import upload.
source: internal/helpers/aitable.go:7407
visible_flags: 6

## Flags
- --import-id <String>: prepare_import_upload 返回的 importId (必填)
- --table-id <String>: 目标数据表 ID。传入后数据将作为新行追加到该表中；不传则默认新建表导入
- --timeout <Int>: 最长等待时间（秒），默认且推荐使用最大值 30
- --header-row <Int>: 表头所在行号（从 1 开始），数据从 headerRow 的下一行开始读取。不传则自动识别表头行
- --src-sheet-name <String>: 源文件中的 Sheet 名称。多 Sheet 文件时指定从哪个 Sheet 导入数据。不传则默认使用第一个 Sheet
- --field-mapping <String>: 字段映射关系 JSON 对象。key 为目标表的字段名，value 为源文件中的列名。不传则按列名自动匹配

## Related
- dws aitable import upload
