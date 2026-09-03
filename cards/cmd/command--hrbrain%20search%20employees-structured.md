# dws hrbrain search employees-structured

kind: command
completeness: full
usage: dws hrbrain search employees-structured
description: 使用高级条件搜索人员
example: dws hrbrain search employees-structured --origin-json '{"rules":[{"field":"name","operator":"contains","value":"张"}],"combinator":"and"}' --fields '[{"label":"姓名","value":"name"}]' --page 1 --page-size 20
source: internal/helpers/hrbrain.go:753
visible_flags: 5

## Flags
- --origin-json <String>: 搜索条件 JSON 表达式 (必填)
- --page <Int>: 当前页码 (默认 1)
- --page-size <Int>: 每页条数 (默认 20)
- --order-by <String>: 排序字段列表，逗号分隔 (可选)
- --fields <String>: 返回列定义 JSON 数组 (必填)

## Related
- dws hrbrain search employees
- dws hrbrain search fields
