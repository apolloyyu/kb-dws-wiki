# dws contact +get-roster

kind: shortcut
completeness: full
usage: dws contact +get-roster
description: 查询员工花名册字段信息（学历、家庭、银行卡、合同等）
source: internal/shortcut/contact/contact.go:763
visible_flags: 2

## Flags
- --staff-id <String>: 查询员工 ID（可选）
- --fields <StringSlice>: 指定字段集合，逗号分隔，可通过 +list-roster-fields 获取（可选）

## Related
- dws contact +list-dept-members
- dws contact +list-followings
- dws contact +list-role-members
- dws contact +list-roles
- dws contact +list-roster-fields
- dws contact +list-sub-depts
