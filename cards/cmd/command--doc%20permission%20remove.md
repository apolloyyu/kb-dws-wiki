# dws doc permission remove

kind: command
completeness: full
description: 移除文档协作者权限
source: internal/helpers/doc.go:3906
visible_flags: 4

## Flags
- --node <String>: 目标节点的标识（文档/文件夹/文件），支持传入 URL 或 ID (必填)
- --users <String>: 被移除权限的用户 userId 列表，逗号分隔 (旧格式，单次最多 30 个)
- --members <String>: 成员列表 JSON 数组（新格式），只需 type 和 id（USER/DEPT/TAG 还需 corpId），与 --users 互斥
- --workspace <String>: 目标知识库 ID 或 URL（选填，仅用于辅助构造返回的 docUrl）

## Related
- dws doc permission add
- dws doc permission list
- dws doc permission update
