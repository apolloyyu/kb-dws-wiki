# dws dev mcp tool debug

kind: command
completeness: partial
usage: dws dev mcp tool debug
description: 调试 MCP 工具
example: dws dev mcp tool debug --mcp-id 10487 --tool-id G-ACT-xxx --value '{"city":"杭州"}' --credential-id 10518 --dry-run --format json
source: internal/helpers/dev_mcp.go:512
visible_flags: 6
partial_reason: unverified_flags

## Flags
- --value <String>: 调试入参 JSON 对象，结构须符合工具 toolInputs 定义；不要传空 {} 走过场
- --version-id <String>: 指定调试的版本 ID
- --credential-id <Int>: 凭证账号 ID（credential list 可查）；服务已配置鉴权时必须指定，作为本次调试的实际运行时鉴权（debug 不吃 bind 绑定的凭证；缺省不传不会被直接拦，会降级空跑、下游返回 40014 等误导报错）
- --no-credential <Bool>: 无鉴权工具的正常走法——声明本次调试不使用凭证（与 --credential-id 二选一必填其一）
- --mcp-id <Int>: MCP 服务 ID
- --tool-id <String>: MCP 工具 ID，G-ACT- 开头

## Related
- dws dev mcp tool create
- dws dev mcp tool create-hsf
- dws dev mcp tool delete
- dws dev mcp tool get
- dws dev mcp tool list
- dws dev mcp tool publish
