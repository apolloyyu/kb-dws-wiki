# dws aitable record batch-update

kind: command
completeness: full
usage: dws aitable record batch-update
description: 批量更新记录（同一 cells 应用到多条 recordId）
example: dws aitable record batch-update --base-id BASE_ID --table-id TABLE_ID
source: internal/helpers/aitable.go:3231
visible_flags: 4

## Flags
- --base-id <String>: Base ID，可通过 base list 或 base search 获取 (必填)
- --table-id <String>: Table ID，可通过 base get 获取 (必填)
- --record-ids <String>: 待更新的记录 ID 列表，逗号分隔，单次最多 100 条 (必填)
- --cells <String>: 要应用到所有记录的 cells JSON 对象（共享 patch），如 '{\"fldStatusId\":\"已完成\"}' (必填)

## Related
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
- dws aitable record list
