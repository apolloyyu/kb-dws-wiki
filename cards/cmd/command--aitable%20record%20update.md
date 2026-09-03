# dws aitable record update

kind: command
completeness: full
usage: dws aitable record update
description: Update field values on one or more existing records by record ID.
example: dws aitable record update --base-id BASE_ID --table-id TABLE_ID --records '[{"recordId":"recXXX","cells":{"fldStatusId":"已完成"}}]'
use_when: When the agent modifies specific row values after reading or computing new data.
source: internal/helpers/aitable.go:3095
visible_flags: 4

## Flags
- --base-id <String>: Base ID，可通过 base list 或 base search 获取 (必填)
- --table-id <String>: Table ID，可通过 base get 获取 (必填)
- --records <String>: 待更新的记录内容列表 JSON 数组，单次最多 100 条 (必填)
- --records-file <String>: 从文件读取 records JSON（替代 --records，适合 Windows 或超长数据）

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
