# dws oa approval append-task

kind: command
completeness: full
usage: dws oa approval append-task
description: 对审批任务进行加签
example: dws oa approval append-task --instance-id <processInstanceId> --task-id <taskId> --type before --appender-user-ids "userId1,userId2" --activate-type ALL --agree-all true
source: internal/helpers/oa.go:1755
visible_flags: 6

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --task-id <String>: 审批任务 ID (必填)
- --type <String>: 加签类型：before（前加签），after（后加签），Parallel（并加签）(必填)
- --appender-user-ids <String>: 被加签用户 ID 列表，多个用逗号分隔 (必填)
- --activate-type <String>: 任务激活类型：ALL（或签），ONE_BY_ONE（依次审批）(必填)
- --agree-all <String>: 是否需要全部同意，true 或 false (必填)

## Related
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
- dws oa approval forecast-process
