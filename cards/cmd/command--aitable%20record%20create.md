# dws aitable record create

kind: command
completeness: full
description: Insert one or more records into a datasheet with given field values.
use_when: When the agent needs to add new rows to a datasheet, individually or in batches.
source: internal/helpers/aitable.go:1849
visible_flags: 3

## Flags
- --name <String>: Base 名称，1-50 字符；会去除首尾空格后校验 (必填)
- --folder-id <String>: 目标父节点的 dentryUuid (知识库节点 ID)，也可传入标准节点 URL，MCP 会在创建前解析出实际生效的节点 ID
- --template-id <String>: 创建 Base 模板 ID，默认创建一个空 Base。可通过 template search 获取模板

## Related
- dws aitable record batch-update
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
- dws aitable record list
