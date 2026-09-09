# dws contact org apply-list

kind: command
completeness: partial
usage: dws contact org apply-list
description: List user-submitted applications to join the enterprise, filterable by status.
example: dws contact org apply-list
use_when: When the user asks to review pending or processed join requests, or needs application IDs for approval commands.
source: internal/helpers/contact.go:1335
visible_flags: 7
partial_reason: unverified_flags,empty_flag_name

## Flags
- --status <String>: 申请状态：0=全部，1=未处理，2=已通过，3=已拒绝，4=已屏蔽（默认 1）
- --size <String>: 每页条数，1-100（默认 20）
- --cursor <String>: 分页游标；首页不传，翻页时传上一页返回的 nextCursor（可选）
- --reason <String>: 原因 (必填)
- --ids <String>: 用户 ID 列表
- --names <String>: 角色名称，逗号分隔
- --dept <String>: 部门 ID

## Related
- dws contact org apply-approve
- dws contact org apply-block
- dws contact org apply-reject
- dws contact org apply-remove
- dws contact org create
- dws contact org invite-audit
