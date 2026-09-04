# dws contract review result

kind: command
completeness: full
usage: dws contract review result
description: 查询合同审查结果
example: dws contract review result --task-id "MjIzODAwMkFJX1JFVklFVw==" --review-type AI_REVIEW --format json
source: internal/helpers/contract.go:452
visible_flags: 2

## Flags
- --task-id <String>: 审查任务 ID（必填）
- --review-type <String>: 审查类型，如 AI_REVIEW（必填）

## Related
- dws contract review analysis
- dws contract review benefit
- dws contract review create
