# dws contract draft

kind: command
completeness: full
usage: dws contract draft
description: 根据听记和模版起草合同
example: dws contract draft --task-uuids uuid1,uuid2 --template-url "https://..." --format json
source: internal/helpers/contract.go:268
visible_flags: 3

## Flags
- --task-uuids <String>: 听记任务 id 列表，逗号分隔 (必填)
- --template-url <String>: 合同模版 URL（与 --template-content 至少填一项；对应 MCP templateUrl）
- --template-content <String>: 合同模版全文（与 --template-url 至少填一项；对应 MCP templateContent）

## Related
- dws contract account
- dws contract archive
- dws contract file-directories
- dws contract import
- dws contract process-templates
- dws contract project
