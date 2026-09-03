# dws aitable record upsert

kind: command
completeness: full
description: 批量创建或更新记录（Upsert）
source: internal/helpers/aitable.go:3486
visible_flags: 4

## Flags
- --base-id <String>: Base ID，可通过 base list 或 base search 获取 (必填)
- --table-id <String>: Table ID，可通过 base get 获取 (必填)
- --records <String>: 待 upsert 的记录内容列表 JSON 数组，单次最多 100 条；带 recordId 的走更新，不带的走创建 (必填，可改用 --records-file)
- --records-file <String>: 从文件读取 records JSON（避免命令行长度限制）；与 --records 互斥，优先级更高

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
