# dws aitable record create-sub

kind: command
completeness: full
usage: dws aitable record create-sub
description: 在父记录下创建子记录
example: dws aitable record create-sub --base-id BASE_ID --table-id TABLE_ID --parent-record-id recParent --records '[{"cells":{"fldTitle":"子任务"}}]'
source: internal/helpers/aitable.go:3745
visible_flags: 7

## Flags
- --base-id <String>: Base ID，可通过 base list 或 base search 获取 (必填)
- --table-id <String>: Table ID，可通过 base get 获取 (必填)
- --parent-record-id <String>: 父记录 ID，可通过 record query 获取 (必填)
- --records <String>: 待创建的子记录 JSON 数组，单次 1～100 条 (必填，可改用 --records-file)
- --records-file <String>: 从文件读取 records JSON（替代 --records）
- --view-id <String>: 可选视图 ID；指定时从该视图读取 hierarchyConfig
- --client-token <String>: 可选 UUID v4 幂等键；超时重试时必须复用同一值

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
