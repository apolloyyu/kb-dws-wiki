# dws doc export

kind: command
completeness: full
usage: dws doc export
description: 导出在线文档 (支持 docx / markdown / pdf)
example: dws doc export get --job-id <jobId>
source: internal/helpers/doc.go:4024
visible_flags: 3

## Flags
- --node <String>: 要导出的文档标识，支持文档 URL 或 dentryUuid (必填)
- --export-format <String>: 导出格式：docx (默认) / markdown (或 md) / pdf
- --output <String>: 本地保存路径，文件路径或目录 (必填)

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
