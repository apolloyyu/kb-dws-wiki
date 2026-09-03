# dws sheet formula-verify

kind: command
completeness: partial
usage: dws sheet formula-verify
description: 校验表格公式错误
example: dws sheet formula-verify --node NODE_ID
source: internal/helpers/sheet_formula_verify.go:18
visible_flags: 7
partial_reason: unverified_flags

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称；与 --range 组成单个扫描目标
- --range <String>: A1 范围；需与 --sheet-id 配合使用
- --targets <String>: A1:D100
- --max-locations-per-error <Int>: 每种错误类型最多返回的位置数
- --max-cells <Int>: 最多扫描的单元格数
- --exit-on-error <Bool>: 发现公式错误时返回非 0 退出码，便于 CI/自动化使用

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
