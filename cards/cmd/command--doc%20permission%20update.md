# dws doc permission update

kind: command
completeness: full
usage: dws doc permission update
description: 更新文档协作者权限
example: dws doc permission update --node DOC_ID --users uid1 --role EDITOR
source: internal/helpers/doc.go:3723
visible_flags: 6

## Flags
- --node <String>: 目标节点的标识（文档/文件夹/文件），支持传入 URL 或 ID (必填)
- --users <String>: 被更新的用户 userId 列表，逗号分隔 (旧格式，单次最多 30 个)
- --role <String>: 新权限角色: MANAGER / EDITOR / DOWNLOADER / READER (旧格式必填，大小写不敏感)
- --workspace <String>: 目标知识库 ID 或 URL（选填，仅用于辅助构造返回的 docUrl）
- --members <String>: 成员列表 JSON 数组（新格式），支持 USER/DEPT/CONVERSATION/TAG 类型（TAG=角色组），与 --users 互斥
- --notify <Bool>: 是否通知被变更的成员（仅 --members 新格式时生效）

## Related
- dws doc permission add
- dws doc permission list
- dws doc permission remove
