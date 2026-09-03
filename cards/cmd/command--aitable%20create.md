# dws aitable create

kind: command
completeness: full
usage: dws aitable create
description: 创建 AI 表格（dws aitable base create 的别名）
example: dws aitable create --name "项目跟踪"
source: internal/helpers/aitable.go:9020
visible_flags: 3

## Flags
- --name <String>: Base 名称，1-50 字符；会去除首尾空格后校验 (必填)
- --folder-id <String>: 目标父节点的 dentryUuid (知识库节点 ID)，也可传入标准节点 URL，MCP 会在创建前解析出实际生效的节点 ID
- --template-id <String>: 创建 Base 模板 ID，默认创建一个空 Base。可通过 template search 获取模板

## Related
- dws aitable advperm
- dws aitable attachment
- dws aitable base
- dws aitable chart
- dws aitable dashboard
- dws aitable datasource
