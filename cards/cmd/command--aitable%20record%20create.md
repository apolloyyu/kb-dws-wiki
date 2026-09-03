# dws aitable record create

kind: command
completeness: full
usage: dws aitable record create
description: Insert one or more records into a datasheet with given field values.
example: dws aitable record create --base-id BASE_ID --table-id TABLE_ID --records '[{"cells":{"fldTextId":"文本内容","fldNumId":123}}]'
use_when: When the agent needs to add new rows to a datasheet, individually or in batches.
source: internal/helpers/aitable.go:2997
visible_flags: 4

## Flags
- --base-id <String>: Base ID，可通过 base list 或 base search 获取 (必填)
- --table-id <String>: Table ID，可通过 base get 获取 (必填)
- --records <String>: 待创建的记录列表 JSON 数组，单次最多 100 条 (必填)
- --records-file <String>: 从文件读取 records JSON（替代 --records，适合 Windows 或超长数据）

## Related
- dws aitable record batch-update
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
- dws aitable record list
