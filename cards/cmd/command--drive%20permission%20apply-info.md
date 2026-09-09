# dws drive permission apply-info

kind: command
completeness: full
usage: dws drive permission apply-info
description: 查询节点可申请的角色与审批人
example: dws drive permission apply-info --node DOC_ID
source: internal/helpers/drive.go:3167
visible_flags: 1

## Flags
- --node <String>: 目标节点 ID 或 URL (必填)

## Related
- dws drive permission add
- dws drive permission apply
- dws drive permission get-setting
- dws drive permission list
- dws drive permission remove
- dws drive permission transfer-owner
