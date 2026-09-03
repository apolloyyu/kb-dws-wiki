# dws agoal contract update

kind: command
completeness: full
usage: dws agoal contract update
description: 更新经营合约
example: dws agoal contract update --contract-id CONTRACT_ID
source: internal/helpers/agoal.go:209
visible_flags: 5

## Flags
- --contract-id <String>: 经营合约 id (必填)
- --request-id <String>: requestId (可选)
- --audit-config <String>: 审批配置 JSON (可选)
- --objective-template <String>: 合约模板 JSON (可选)
- --dimensions <String>: 维度内容列表 JSON 数组 (必填)

## Related
- dws agoal contract detail
- dws agoal contract fields
- dws agoal contract list
