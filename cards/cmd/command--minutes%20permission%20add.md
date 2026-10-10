# dws minutes permission add

kind: command
completeness: partial
usage: dws minutes permission add
description: —
source: internal/helpers/minutes.go:1708
visible_flags: 6
partial_reason: missing_description

## Flags
- --ids <String>: 听记 taskUuid 列表，逗号分隔 (必填)
- --member-uids <String>: 真实成员钉钉 UID 列表，逗号分隔；与 --member-staff-ids 二选一
- --member-staff-ids <String>: 组织内成员 staffId 列表，逗号分隔并保留前导零；与 --member-uids 二选一
- --policy <String>: 权限类型: 0=管理员, 1=所有者, 2=可编辑, 3=可查看/下载, 4=仅查看 (必填)
- --cover <Bool>: 是否覆盖已有权限 (可选，默认 false)
- --sub-resources <String>: 权限子模块，逗号分隔: OrigContent/Summary/Analysis/Note (可选)

## Related
- dws minutes permission apply
- dws minutes permission remove
