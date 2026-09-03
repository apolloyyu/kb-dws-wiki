# dws agoal contract detail

kind: command
completeness: full
usage: dws agoal contract detail
description: 获取经营合约详情
example: dws agoal contract detail --contract-id CONTRACT_ID
source: internal/helpers/agoal.go:188
visible_flags: 2

## Flags
- --contract-id <String>: 经营合约 id (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal contract fields
- dws agoal contract list
- dws agoal contract update
