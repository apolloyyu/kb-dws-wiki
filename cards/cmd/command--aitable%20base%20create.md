# dws aitable base create

kind: command
completeness: full
usage: dws aitable base create
description: Create a new AI table (Base) under the current user's workspace. Returns the newly-created Base ID.
example: dws aitable base create --name "项目跟踪"
use_when: When an agent needs to provision a fresh Base before populating datasheets, fields, and records.
source: internal/helpers/aitable.go:1861
visible_flags: 3

## Flags
- --name <String>: Base 名称，1-50 字符；会去除首尾空格后校验 (必填)
- --folder-id <String>: 目标父节点的 dentryUuid (知识库节点 ID)，也可传入标准节点 URL，MCP 会在创建前解析出实际生效的节点 ID
- --template-id <String>: 创建 Base 模板 ID，默认创建一个空 Base。可通过 template search 获取模板

## Related
- dws aitable base copy
- dws aitable base delete
- dws aitable base get
- dws aitable base get-primary-doc-id
- dws aitable base list
- dws aitable base search
