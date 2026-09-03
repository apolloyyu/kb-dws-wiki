# dws contact user dismission search

kind: command
completeness: full
usage: dws contact user dismission search
description: 分页获取离职员工列表
example: dws contact user dismission search
source: internal/helpers/contact.go:1874
visible_flags: 8

## Flags
- --name <String>: 员工姓名，模糊搜索（可选）
- --start <String>: 离职日期查询范围开始，格式 YYYY-MM-DD（可选），与end要么都不填要么都填
- --end <String>: 离职日期查询范围结束，格式 YYYY-MM-DD（可选），与start要么都不填要么都填
- --depts <String>: 部门 ID 列表，逗号分隔（可选）
- --hide-retirement <Bool>: 是否隐藏退休，默认 true（可选）
- --hide-partner <Bool>: 是否隐藏合作伙伴，默认 false（可选）
- --page <Int>: 页码，从 1 开始（可选）
- --limit <Int>: 页大小，200 以内（可选）

## Related
- none
