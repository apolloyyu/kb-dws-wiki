# dws contract account list

kind: command
completeness: full
usage: dws contract account list
description: 列举账款信息
example: dws contract account list --scope self --format json
source: internal/helpers/contract.go:604
visible_flags: 12

## Flags
- --scope <String>: 查询范围: self / department / all
- --query-status <String>: 收付款状态: all / pay / receive
- --amount-type <String>: 金额类型: payment_party_other / payment_party_our / none
- --status <String>: 账款状态
- --source <String>: 来源
- --contract-code <String>: 合同代码
- --contract-name <String>: 合同名称
- --transaction-no <String>: 单据号
- --exec-start <String>: 执行开始时间（ISO-8601 时间字符串；CLI 转换为 MCP 所需的 Unix 毫秒时间戳）
- --exec-end <String>: 执行结束时间（ISO-8601 时间字符串；CLI 转换为 MCP 所需的 Unix 毫秒时间戳）
- --page <Int>: 当前页码
- --page-size <Int>: 每页条数

## Related
- dws contract account create
- dws contract account delete
- dws contract account get
- dws contract account update
