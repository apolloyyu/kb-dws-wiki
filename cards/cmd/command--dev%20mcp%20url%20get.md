# dws dev mcp url get

kind: command
completeness: full
usage: dws dev mcp url get
description: 获取 MCP 实例接入地址（按调用者个人身份生成，含个人 key 勿外发）
example: dws dev mcp url get --mcp-id 10487 --source MARKET --format json
source: internal/helpers/dev_mcp.go:175
visible_flags: 2

## Flags
- --mcp-id <Int>: MCP 服务 ID
- --source <String>: 服务来源：MARKET 或 PUBLISHED

## Related
- none
