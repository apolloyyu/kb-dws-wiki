# dws contact +team

kind: shortcut
completeness: full
usage: dws contact +team
description: 按姓名列出某人所在部门的成员（自动解析 userId 与 deptId）
source: internal/shortcut/smart/team.go:40
visible_flags: 1

## Flags
- --name <String>: 同事姓名/花名

## Related
- dws contact +by-mobile
- dws contact +dept-members
- dws contact +friend-list
- dws contact +friend-remove
- dws contact +friend-request-accept
- dws contact +friend-request-list
