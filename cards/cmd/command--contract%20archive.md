# dws contract archive

kind: command
completeness: full
usage: dws contract archive
description: 合同文档归档
example: dws contract archive --file ./archive_request.json --format json
source: internal/helpers/contract.go:703
visible_flags: 1

## Flags
- --file <String>: ContractOpenArchiveRequest JSON 文件路径，\"-\" 表示 stdin（必填）

## Related
- dws contract account
- dws contract draft
- dws contract file-directories
- dws contract import
- dws contract process-templates
- dws contract project
