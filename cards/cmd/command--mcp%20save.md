# dws mcp save

kind: command
completeness: full
description: 新增或修改 MCP 凭证账号（TOKEN 型会现场调换 token 接口验密钥，密钥无效则保存失败）
source: internal/helpers/dev_mcp.go:674
visible_flags: 4

## Flags
- --auth-type <String>: 鉴权类型：NO_AUTH、BASIC、TOKEN 或 SIGNATURE；静态 API key 场景用 SIGNATURE 自定义字段+直引
- --basic-auth-config <String>: BASIC 鉴权配置 JSON 对象
- --token-auth-config <String>: TOKEN 换取及注入配置 JSON 对象：{authFields, fetchTokenRequest, 注入位, tokenExpireRules, refreshToken, testRequest}；注入位按下游要求三选一：authHeaders（token 放请求头）/ authQuery（token 放 q
- --signature-auth-config <String>: SIGNATURE 自定义鉴权配置 JSON 对象（静态 API key 直引 / 自定义签名表达式两类场景）。直引写法见上方 Examples 与 skill mcp.md：value 用 #(\"<authFields 的 dataId>\") 函数语法

## Related
- dws mcp create
- dws mcp create-hsf
- dws mcp debug
- dws mcp delete
- dws mcp get
- dws mcp list
