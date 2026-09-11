# dws aitable field run-ai

kind: command
completeness: full
usage: dws aitable field run-ai
description: 触发 AI 字段运行
example: dws aitable field run-ai --base-id BASE_ID --table-id TABLE_ID --field-ids fldAI1,fldAI2
source: internal/helpers/aitable.go:3170
visible_flags: 4

## Flags
- --base-id <String>: Base ID（通过 base list 获取）(必填)
- --table-id <String>: Table ID（通过 base get 获取）(必填)
- --field-ids <String>: AI 字段 ID 列表，逗号分隔，单次 1～10 个 (必填)
- --record-ids <String>: 可选记录 ID 列表，逗号分隔，单次最多 500 条；省略时整列运行

## Related
- dws aitable field create
- dws aitable field delete
- dws aitable field get
- dws aitable field list
- dws aitable field search-options
- dws aitable field update
