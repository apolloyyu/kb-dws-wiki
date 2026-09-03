# dws dev mcp tool update-hsf

kind: command
completeness: partial
usage: dws dev mcp tool update-hsf
description: 编辑 HSF 型工具（⚠️部分更新语义：只传要改的字段，未传保持原值——与 http 版全量提交完全相反）
example: dws dev mcp tool update-hsf --mcp-id 10520 --tool-id G-ACT-xxx --description 更准确的新描述 --dry-run --format json
source: internal/helpers/dev_mcp_hsf.go:95
visible_flags: 8
partial_reason: unverified_flags

## Flags
- --name <String>: 可选。改工具标识名（snake_case）；不传=保持原值
- --title <String>: 可选。改标题；不传=保持原值
- --description <String>: 可选。改工具描述；不传=保持原值
- --hsf-info <String>: 可选。改 HSF 三元组 JSON 对象；⚠️interfaceName 与 methodName 必须同时给才会切换方法，只给其一会被静默忽略（照样返回 success 但方法没换）；不传=保持原值
- --tool-inputs <String>: 可选。改入参字段树；不传=保持原值，传了=整块替换
- --input-mappings <String>: 可选。改入参映射；不传=保持原值，传了=整块替换（target=$.<DTO简名>.<字段>，字段名以 hsf method-list 为准）
- --tool-outputs <String>: 可选。改出参字段树；不传=保持原值，传了=整块替换
- --output-mappings <String>: 可选。改出参映射；不传=保持原值，传数组=整块替换；⚠️传 []=清空既有映射导致工具出参失效，勿用 [] 表达「不改」

## Related
- dws dev mcp tool create
- dws dev mcp tool create-hsf
- dws dev mcp tool debug
- dws dev mcp tool delete
- dws dev mcp tool get
- dws dev mcp tool list
