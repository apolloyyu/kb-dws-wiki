# dws oa approval list-by-admin

kind: command
completeness: full
usage: dws oa approval list-by-admin
description: 以管理员身份查询审批模板的实例列表
example: dws oa approval list-by-admin --process-code <code> --start "2026-03-10T00:00:00+08:00" --cursor 0 --limit 20
source: internal/helpers/oa.go:1950
visible_flags: 8

## Flags
- --process-code <String>: 审批模板 processCode（简单模式使用；与 --request 互斥）
- --start <String>: 开始时间 ISO-8601 (如 2026-03-10T00:00:00+08:00)（简单模式使用；与 --request 互斥）
- --end <String>: 结束时间 ISO-8601 (如 2026-03-10T23:59:59+08:00)（可选）
- --cursor <String>: 分页游标，首次传 0
- --limit <String>: 每页大小，最大 20
- --user-ids <String>: 按发起人 userId 过滤，多个用逗号分隔（可选）
- --statuses <String>: 按审批状态过滤，多个用逗号分隔（可选，如 RUNNING、TERMINATED、COMPLETED）
- --request <String>: 完整请求 JSON（高级模式；与简单模式参数互斥）

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
