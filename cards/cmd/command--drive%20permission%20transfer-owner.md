# dws drive permission transfer-owner

kind: command
completeness: full
description: [危险] 转交所有者
source: internal/helpers/drive.go:3051
visible_flags: 5

## Flags
- --node <String>: 目标节点 ID 或 URL（与 --workspace 二选一）
- --workspace <String>: 目标知识库 ID 或 URL（与 --node 二选一）
- --new-owner <String>: 新所有者的用户 userId (必填)
- --reserve-role <String>: 转交后原所有者保留角色: MANAGER / EDITOR / DOWNLOADER / READER / NONE
- --recursive <Bool>: 是否递归变更所有子节点的所有者

## Related
- dws drive permission add
- dws drive permission apply
- dws drive permission apply-info
- dws drive permission get-setting
- dws drive permission list
- dws drive permission remove
