# dws wiki permission set-share-scope

kind: command
completeness: partial
usage: dws wiki permission set-share-scope
description: —
source: internal/helpers/wiki.go:1021
visible_flags: 6
partial_reason: missing_description

## Flags
- --workspace <String> required: 目标知识库 ID 或 URL (必填)
- --visibility <String> required: 目标可见性: PRIVATE / ORGANIZATION / PUBLIC (必填)(可选: PRIVATE|ORGANIZATION|PUBLIC)
- --role <String>: 链接访问者默认角色: READER / DOWNLOADER / EDITOR（PUBLIC 仅 READER/DOWNLOADER）(选填)(可选: READER|DOWNLOADER|EDITOR)
- --partner <Bool>: 企业内公开是否包含合作伙伴（外包）(选填，仅 ORGANIZATION)
- --can-search <Bool>: 是否可被组织内搜索 (选填，仅 ORGANIZATION)
- --can-recommend <Bool>: 是否可被组织内推荐 (选填，仅 ORGANIZATION)

## Related
- none
