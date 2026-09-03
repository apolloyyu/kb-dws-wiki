# dws mcp create-hsf

kind: command
completeness: full
description: 新建 HSF 型 MCP 工具草稿（apiInputs/apiOutputs 由服务端按方法 schema 自动生成）
source: internal/helpers/dev_mcp_hsf.go:59
visible_flags: 8

## Flags
- --name <String>: 必填。工具唯一标识，snake_case、动词开头、语义明确
- --title <String>: 必填。工具中文标题
- --description <String>: 必填。工具功能完整描述（何时用+返回什么）
- --hsf-info <String>: 必填。HSF 三元组 JSON 对象 {interfaceName,methodName,version(可省，缺省1.0.0)}——先用 hsf method-list 发现方法；与 http 版的 --http-info 对仗
- --tool-inputs <String>: 必填。暴露给 LLM 的入参字段树 JSON 数组（与 http 版同构）
- --input-mappings <String>: 必填。toolInputs→DTO 映射 JSON 数组；target=$.<DTO简名>.<字段>（DTO 字段名以 hsf method-list 的 inputSchema 为准，写错=静默忽略）；⚠️DTO 含 corpId/userId 时必须显式加两条系统注入映射（$.system_node.ddDataC
- --tool-outputs <String>: 必填。对外出参字段树 JSON 数组；不做精修显式传 '[]'
- --output-mappings <String>: 必填。出参映射 JSON 数组；⚠️HSF 侧 source 无 .Body. 前缀：$.node_service_activator.result…（写操作类最简=只透 success/errorCode/errorMsg 三条）

## Related
- dws mcp create
- dws mcp debug
- dws mcp delete
- dws mcp get
- dws mcp list
- dws mcp method-list
