# dws agoal report submit-detail

kind: command
completeness: full
usage: dws agoal report submit-detail
description: 获取周月报规则提交详情
example: dws agoal report submit-detail --template-id TPL_ID --submit-state ON_TIME
source: internal/helpers/agoal.go:470
visible_flags: 7

## Flags
- --template-id <String>: 规则模板 id (必填)
- --submit-state <String>: 提交状态: ON_TIME(按时提交)/LATE(迟交)/NOT_SUBMITTED(未提交) (必填)
- --request-id <String>: requestId (可选)
- --query-date <String>: 查询日期，ISO-8601 格式（如 \"2026-06-18T00:00:00+08:00\"），默认为当天 (可选)
- --page <Int>: 分页参数，默认为 1 (可选)
- --page-size <Int>: 分页参数，默认为 10 (可选)
- --keyword <String>: 搜索员工名称 (可选)

## Related
- dws agoal report list-statistics
