# dws agoal user objectives

kind: command
completeness: full
usage: dws agoal user objectives
description: 查询用户目标列表
example: dws agoal user objectives --user-id USER_ID --rule-id RULE_ID --period-ids "period1,period2"
source: internal/helpers/agoal.go:419
visible_flags: 4

## Flags
- --user-id <String>: 要查询的人员钉钉 id (必填)
- --rule-id <String>: 规则 id (必填)
- --period-ids <String>: 周期 id 列表，逗号分隔 (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal user rules
