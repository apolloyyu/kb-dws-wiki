# dws doc import

kind: command
completeness: full
description: 导入本地文件为在线文档 (支持 docx / xlsx / md 等)
source: internal/helpers/doc.go:4297
visible_flags: 4

## Flags
- --file <String>: 本地文件路径 (必填)
- --folder <String>: 目标文件夹 ID 或 URL (可选；与 workspace 互斥；在线转换格式都不传时解析当前组织唯一 orgSpace 根目录)
- --workspace <String>: 目标知识库 ID 或 URL (可选；与 folder 互斥；在线转换格式都不传时解析当前组织唯一 orgSpace 根目录)
- --name (-n) <String>: 导入后文档名称 (可选，默认取文件名)

## Related
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
- dws doc export
- dws doc info
