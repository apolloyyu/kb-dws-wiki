# dws drive permission set-share-scope

kind: command
completeness: partial
usage: dws drive permission set-share-scope
description: —
source: internal/helpers/drive.go:3076
visible_flags: 8
partial_reason: missing_description

## Flags
- --node <String> required: 目标节点 ID 或 URL (必填)
- --visibility <String> required: 目标可见性: PRIVATE / ORGANIZATION / PUBLIC (必填)(可选: PRIVATE|ORGANIZATION|PUBLIC)
- --role <String>: 链接访问者默认角色: READER / DOWNLOADER / EDITOR (选填)(可选: READER|DOWNLOADER|EDITOR)
- --partner <Bool>: 企业内公开是否包含合作伙伴（外包）(选填，仅 ORGANIZATION)
- --can-search <Bool>: 是否可被组织内搜索 (选填，仅 ORGANIZATION)
- --can-recommend <Bool>: 是否可被组织内推荐 (选填，仅 ORGANIZATION)
- --password <String>: 互联网公开访问密码：非空=设置，空串=清除，不传=不改变 (选填，仅 PUBLIC)
- --expire-days <Int>: 互联网公开有效期天数：0=永久，正整数=N天 (选填，仅 PUBLIC)

## Related
- dws drive permission add
- dws drive permission apply
- dws drive permission apply-info
- dws drive permission get-setting
- dws drive permission list
- dws drive permission remove
