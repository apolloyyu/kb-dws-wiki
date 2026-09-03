# dws skill search

kind: command
completeness: full
description: 从钉钉技能市场搜索技能
source: internal/app/skill_command.go:322
visible_flags: 3

## Flags
- --query <String> required: 搜索关键词（必填）
- --source <String>: 查询范围，空格分隔。备选值：DingtalkMarket（钉钉市场）、OrgInternal（企业内部）
- --scopes <String>: 查询范围（已废弃，请使用 --source）

## Related
- dws skill add
- dws skill find
- dws skill get
- dws skill install
- dws skill setup
