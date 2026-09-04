# dws aitable info

kind: command
completeness: full
usage: dws aitable info
description: 获取 AI 表格信息（dws aitable base get 的别名）
example: dws aitable info --base-id BASE_ID
source: internal/helpers/aitable.go:9071
visible_flags: 1

## Flags
- --base-id <String>: Base 唯一标识。优先使用 base search / base list 返回值 (必填)

## Related
- dws aitable advperm
- dws aitable app
- dws aitable attachment
- dws aitable base
- dws aitable chart
- dws aitable create
