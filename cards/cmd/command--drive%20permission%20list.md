# dws drive permission list

kind: command
completeness: full
usage: dws drive permission list
description: 查询协作者列表
example: dws drive permission list --node DOC_ID
source: internal/helpers/drive.go:2748
visible_flags: 5

## Flags
- --node <String>: 目标节点 ID 或 URL (必填)
- --limit <Int>: 返回成员数上限，默认 30，最大 50
- --filter-role <String>: 按角色过滤: OWNER / MANAGER / EDITOR / DOWNLOADER / READER
- --next-token <String>: 分页游标，首次不传，后续传入上一次返回的 nextToken
- --workspace <String>: 知识库 ID (选填)

## Related
- dws drive permission add
- dws drive permission apply
- dws drive permission apply-info
- dws drive permission get-setting
- dws drive permission remove
- dws drive permission transfer-owner
