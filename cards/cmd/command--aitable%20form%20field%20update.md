# dws aitable form field update

kind: command
completeness: full
description: 更新 AI 表格
source: internal/helpers/aitable.go:1897
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --name <String>: 新名称，1-50 字符 (必填)
- --desc <String>: 备注文本

## Related
- dws aitable form field hide
- dws aitable form field list
