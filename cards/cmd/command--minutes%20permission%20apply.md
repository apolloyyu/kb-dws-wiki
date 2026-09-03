# dws minutes permission apply

kind: command
completeness: full
usage: dws minutes permission apply
description: 为当前用户申请听记权限
example: dws minutes permission apply --id <taskUuid> --policy 4
source: internal/helpers/minutes.go:1879
visible_flags: 2

## Flags
- --id <String>: 听记 taskUuid (必填)
- --policy <Int>: 权限类型: 2=可编辑, 3=可查看/下载, 4=仅查看 (必填)

## Related
- dws minutes permission add
- dws minutes permission remove
