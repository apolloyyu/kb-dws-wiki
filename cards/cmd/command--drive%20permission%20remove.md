# dws drive permission remove

kind: command
completeness: full
usage: dws drive permission remove
description: 移除协作者权限
example: dws drive permission remove --node DOC_ID --users uid1
source: internal/helpers/drive.go:2945
visible_flags: 4

## Flags
- --node <String>: 目标节点 ID 或 URL (必填)
- --users <String>: 用户 userId 列表，逗号分隔 (旧格式)
- --members <String>: 成员列表 JSON 数组（新格式），只需 type 和 id（USER/DEPT/TAG 还需 corpId），与 --users 互斥
- --workspace <String>: 知识库 ID (选填)

## Related
- dws drive permission add
- dws drive permission apply
- dws drive permission apply-info
- dws drive permission get-setting
- dws drive permission list
- dws drive permission transfer-owner
