# dws dev mcp member list

kind: command
completeness: partial
usage: dws dev mcp member list
description: 查询 MCP 开发协作者列表
example: dws dev mcp member list --mcp-id 10520 --format json
source: internal/helpers/dev_mcp.go:869
visible_flags: 18
partial_reason: too_many_flags:18

## Flags
- --user-ids <String>: 成员 staffId 列表，多个用逗号或分号分隔
- --credential-id <Int>: 凭证账号 ID
- --mcp-id <Int>: MCP 服务 ID
- --tool-id <String>: MCP 工具 ID，G-ACT- 开头
- --cursor <Int>: 分页游标，从 1 开始
- --page-size <Int>: 每页条数，最大 100
- --name <String>: 工具唯一标识，snake_case
- --title <String>: 必填。工具中文标题：中文自然语言、≤30 字、与功能一致
- … 10 more; use dwsdoc cmd/short for full flags

## Related
- none
