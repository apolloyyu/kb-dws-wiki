# dws contact org invite-audit

kind: command
completeness: partial
usage: dws contact org invite-audit
description: Set whether joining the enterprise requires admin review (enterprise-level auto-approval).
example: dws contact org invite-audit --no-audit
use_when: When the user explicitly asks to enable or disable join-request auditing for the whole enterprise.
source: internal/helpers/contact.go:1105
visible_flags: 1
partial_reason: unverified_flags

## Flags
- --no-audit <Bool>: 裸传 --no-audit 即开启免审核（auditType=0，申请自动通过），--no-audit=false 恢复需管理员审核（auditType=1）(必填)

## Related
- dws contact org apply-approve
- dws contact org apply-block
- dws contact org apply-list
- dws contact org apply-reject
- dws contact org apply-remove
- dws contact org create
