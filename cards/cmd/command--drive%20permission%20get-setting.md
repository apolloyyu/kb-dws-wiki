# dws drive permission get-setting

kind: command
completeness: full
usage: dws drive permission get-setting
description: 查询节点权限设置
example: dws drive permission get-setting --node DOC_ID
source: internal/helpers/drive.go:2824
visible_flags: 1

## Flags
- --node <String>: 目标节点 ID 或 URL (必填)

## Related
- dws drive permission add
- dws drive permission apply
- dws drive permission apply-info
- dws drive permission list
- dws drive permission remove
- dws drive permission transfer-owner
