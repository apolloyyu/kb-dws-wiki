# dws contact user profile get

kind: command
completeness: full
usage: dws contact user profile get
description: 查询员工花名册字段信息（个人档案）
example: dws contact user profile get --staff-id STAFF_ID
source: internal/helpers/contact.go:1790
visible_flags: 2

## Flags
- --staff-id <String>: 查询员工 ID（可选）
- --fields <String>: 指定字段集合, 逗号分隔, 可通过 profile fields 获取（可选）

## Related
- dws contact user profile fields
