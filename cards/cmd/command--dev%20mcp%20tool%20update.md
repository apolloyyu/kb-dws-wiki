# dws dev mcp tool update

kind: command
completeness: partial
usage: dws dev mcp tool update
description: 编辑 MCP 工具并保存为草稿
example: dws dev mcp tool update --mcp-id 10487 --tool-id G-ACT-example --name get_weather --title 查询天气 --description 按城市查询天气 --http-info '{"method":"GET","url":"https://example.com/weather","auth":{"type":"NO_AUTH"}}' --api-inputs '{"query":[{"key":"city","type":"string","description":"城市名"}]}' --tool-inputs '[{"key":"city","type":"string","required":true,"description":"城市名，例如杭州"}]' --input-mappings '[{"target":"$.Query.city","type":"reference","source":"$.node_start.city"}]' --api-outputs '{"body":[{"key":"temperature","type":"number","description":"温度"}]}' --tool-outputs '[]' --output-mappings '[{"target":"$","type":"reference","source":"$.node_service_activator.Body"}]' --dry-run --format json
source: internal/helpers/dev_mcp.go:485
visible_flags: 0
partial_reason: unverified_flags

## Flags
- none

## Related
- dws dev mcp tool create
- dws dev mcp tool create-hsf
- dws dev mcp tool debug
- dws dev mcp tool delete
- dws dev mcp tool get
- dws dev mcp tool list
