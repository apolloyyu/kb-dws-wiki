# dws contact org invite-list

kind: command
completeness: full
usage: dws contact org invite-list
description: List join-enterprise invitations the administrators have sent, filterable by status.
example: dws contact org invite-list
use_when: When the user asks which invited members have not yet accepted.
source: internal/helpers/contact.go:1291
visible_flags: 3

## Flags
- --status <String>: 邀请状态：1=未处理，2=已同意，3=已忽略或失效（默认 1）
- --size <String>: 每页条数，1-100（默认 20）
- --cursor <String>: 分页游标；首页不传，翻页时传上一页返回的 nextCursor（可选）

## Related
- dws contact org apply-approve
- dws contact org apply-block
- dws contact org apply-list
- dws contact org apply-reject
- dws contact org apply-remove
- dws contact org create
