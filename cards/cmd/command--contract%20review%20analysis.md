# dws contract review analysis

kind: command
completeness: full
usage: dws contract review analysis
description: 解析合同文件
example: dws contract review analysis --file ./analysis_request.json --format json
source: internal/helpers/contract.go:395
visible_flags: 1

## Flags
- --file <String>: contractAnalysis 请求 JSON 文件路径，\"-\" 表示 stdin（必填）

## Related
- dws contract review benefit
- dws contract review create
- dws contract review result
