# dws dev mcp credential save

kind: command
completeness: partial
usage: dws dev mcp credential save
description: 新增或修改 MCP 凭证账号（TOKEN 型会现场调换 token 接口验密钥，密钥无效则保存失败）
example: dws dev mcp credential save --mcp-id 10520 --name 示例账号 --content '{"apiKey":"example"}' --dry-run --format json
source: internal/helpers/dev_mcp.go:825
visible_flags: 5
partial_reason: unverified_flags

## Flags
- --credential-id <Int>: 已有凭证账号 ID；不传表示新增
- --name <String>: 凭证账号名称
- --content <String>: 密钥键值 JSON 对象；推荐改用 --content-file
- --content-file <String>: 密钥键值 JSON 文件路径，传 - 从 stdin 读取
- --mcp-id <Int>: MCP 服务 ID

## Related
- dws dev mcp credential list
- dws dev mcp credential unbind
