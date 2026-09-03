# dws aitable form share update

kind: command
completeness: full
usage: dws aitable form share update
description: 开启/关闭分享表单
example: dws aitable form share update --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --enabled true
source: internal/helpers/aitable.go:5649
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID (必填)
- --enabled <String>: 分享开关：true 开启，false 关闭 (必填)

## Related
- dws aitable form share get
