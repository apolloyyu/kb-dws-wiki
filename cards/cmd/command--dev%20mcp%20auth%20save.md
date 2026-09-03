# dws dev mcp auth save

kind: command
completeness: partial
usage: dws dev mcp auth save
description: 保存 MCP 下游鉴权配置
example: dws dev mcp auth save --mcp-id 10520 --auth-type NO_AUTH --dry-run --format json
source: internal/helpers/dev_mcp.go:674
visible_flags: 5
partial_reason: unverified_flags

## Flags
- --auth-type <String>: 鉴权类型：NO_AUTH、BASIC、TOKEN 或 SIGNATURE；静态 API key 场景用 SIGNATURE 自定义字段+直引
- --basic-auth-config <String>: BASIC 鉴权配置 JSON 对象
- --token-auth-config <String>: TOKEN 换取及注入配置 JSON 对象：{authFields, fetchTokenRequest, 注入位, tokenExpireRules, refreshToken, testRequest}；注入位按下游要求三选一：authHeaders（token 放请求头）/ authQuery（token 放 q
- --signature-auth-config <String>: SIGNATURE 自定义鉴权配置 JSON 对象（静态 API key 直引 / 自定义签名表达式两类场景）。直引写法见上方 Examples 与 skill mcp.md：value 用 #(\"<authFields 的 dataId>\") 函数语法
- --mcp-id <Int>: MCP 服务 ID

## Related
- dws dev mcp auth get
