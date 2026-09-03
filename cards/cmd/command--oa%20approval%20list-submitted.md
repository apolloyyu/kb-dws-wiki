# dws oa approval list-submitted

kind: command
completeness: partial
usage: dws oa approval list-submitted
description: 获取当前用户已发起的审批单列表
example: dws oa approval list-submitted --limit 20 --page 1 --query 关键词
source: internal/helpers/oa.go:1489
visible_flags: 0
partial_reason: unverified_flags

## Flags
- none

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
