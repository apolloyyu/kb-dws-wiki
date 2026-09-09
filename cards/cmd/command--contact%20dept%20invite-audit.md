# dws contact dept invite-audit

kind: command
completeness: partial
usage: dws contact dept invite-audit
description: Set whether joining a specific department requires admin review (department-level auto-approval).
example: dws contact dept invite-audit --dept 12345 --no-audit
use_when: When the user explicitly asks to enable or disable per-department join-request auditing.
source: internal/helpers/contact.go:1132
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --dept <String>: 部门 ID (必填)；根部门传 1
- --no-audit <Bool>: 裸传 --no-audit 即开启免审核（auditType=0，申请自动通过），--no-audit=false 恢复需管理员审核（auditType=1）(必填)
- --emp-apply-join-dept <String>: 免审核开启时是否允许组织内成员申请加入该部门：true/false（可选，默认 false）

## Related
- dws contact dept create
- dws contact dept get-info
- dws contact dept list-children
- dws contact dept list-members
- dws contact dept search
- dws contact dept update
