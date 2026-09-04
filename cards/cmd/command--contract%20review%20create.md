# dws contract review create

kind: command
completeness: full
usage: dws contract review create
description: 创建合同审查任务
example: dws contract review create --file ./review_request.json --format json
source: internal/helpers/contract.go:327
visible_flags: 1

## Flags
- --file <String>: IntelligentContractReviewClientRequest JSON 文件路径，\"-\" 表示 stdin（必填）

## Related
- dws contract review analysis
- dws contract review benefit
- dws contract review result
