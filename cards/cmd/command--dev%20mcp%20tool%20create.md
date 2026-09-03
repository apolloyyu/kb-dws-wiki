# dws dev mcp tool create

kind: command
completeness: partial
usage: dws dev mcp tool create
description: 新建 MCP 工具草稿
example: dws dev mcp tool create --mcp-id 10487 --name get_weather --title 查询天气 --description 按经纬度查询实时天气 --http-info '{"method":"GET","url":"https://example.com","auth":{"type":"NO_AUTH"}}' --api-inputs '{"query":[{"key":"lat","type":"number","description":"纬度"}]}' --tool-inputs '[{"key":"lat","type":"number","required":true,"description":"纬度，示例：39.9"}]' --input-mappings '[{"target":"$.Query.lat","type":"reference","source":"$.node_start.lat"}]' --api-outputs '{"body":[{"key":"temperature","type":"number","description":"温度"}]}' --tool-outputs '[]' --output-mappings '[{"target":"$","type":"reference","source":"$.node_service_activator.Body"}]' --dry-run --format json
source: internal/helpers/dev_mcp.go:458
visible_flags: 0
partial_reason: unverified_flags

## Flags
- none

## Related
- dws dev mcp tool create-hsf
- dws dev mcp tool debug
- dws dev mcp tool delete
- dws dev mcp tool get
- dws dev mcp tool list
- dws dev mcp tool publish
