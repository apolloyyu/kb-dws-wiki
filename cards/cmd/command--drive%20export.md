# dws drive export

kind: command
completeness: partial
description: Export an online doc from DingTalk Drive to a local file in docx/xlsx/markdown/pdf/pptx; submits the export task, polls it, and downloads the result in one step.
use_when: When the agent needs the general export entry: exporting to xlsx/pptx or exporting a doc whose type is uncertain.
source: internal/helpers/drive_export.go:388
visible_flags: 4
partial_reason: empty_flag_name

## Flags
- --node <String>: 要导出的文档标识，支持 URL 或 dentryUuid (必填)
- --export-format <String>: 导出格式：docx (默认) / xlsx / markdown (或 md) / pdf / pptx
- --output <String>: 本地保存路径，文件路径或目录 (可选)
- --async <Bool>: 异步模式：提交导出任务后立即返回 taskId，不等待完成

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
