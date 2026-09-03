# dws wiki member list

kind: command
completeness: full
usage: dws wiki member list
description: 查询知识库成员列表
example: dws wiki member list --workspace <workspaceId>
source: internal/helpers/wiki.go:772
visible_flags: 4

## Flags
- --workspace <String>: 知识库 ID 或 URL (必填)
- --limit <Int>: 返回成员数上限，默认 30，最大 50
- --filter-role <String>: 按角色过滤（逗号分隔）：OWNER / MANAGER / EDITOR / DOWNLOADER / READER
- --next-token <String>: 分页游标，首次不传，后续传入上一次返回的 nextToken

## Related
- dws wiki member add
- dws wiki member remove
- dws wiki member update
