# dws hrbrain search employees

kind: command
completeness: full
usage: dws hrbrain search employees
description: 人才搜索
example: dws hrbrain search employees --keyword "张三" --page 1 --page-size 20
source: internal/helpers/hrbrain.go:672
visible_flags: 7

## Flags
- --keyword <String>: 全文搜索关键词（姓名/工号等）(可选)
- --dept-name <String>: 部门名称 (可选)
- --position-name <String>: 职务名称 (可选)
- --job-level <String>: 职级 (可选)
- --pool-code <String>: 限定人才池编码 (可选)
- --page <Int>: 当前页码 (默认 1)
- --page-size <Int>: 每页条数 (默认 20)

## Related
- dws hrbrain search employees-structured
- dws hrbrain search fields
