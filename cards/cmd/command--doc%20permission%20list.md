# dws doc permission list

kind: command
completeness: full
usage: dws doc permission list
description: 查询文档协作者列表
example: dws doc permission list --node DOC_ID
source: internal/helpers/doc.go:3821
visible_flags: 5

## Flags
- --node <String>: 目标节点的标识（文档/文件夹/文件），支持传入 URL 或 ID (必填)
- --limit <Int>: 返回成员数上限，默认 30，最大 50
- --filter-role <String>: 按角色过滤（逗号分隔）：OWNER / MANAGER / EDITOR / DOWNLOADER / READER
- --next-token <String>: 分页游标，首次不传，后续传入上一次返回的 nextToken
- --workspace <String>: 目标知识库 ID 或 URL（选填，仅用于辅助构造返回的 docUrl）

## Related
- dws doc permission add
- dws doc permission remove
- dws doc permission update
