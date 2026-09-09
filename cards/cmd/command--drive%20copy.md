# dws drive copy

kind: command
completeness: full
usage: dws drive copy
description: 复制文件/文档到指定位置
example: dws drive copy --node DOC_ID --folder TARGET_FOLDER_ID
source: internal/helpers/drive.go:1880
visible_flags: 3

## Flags
- --node <String>: 文档/文件 ID 或 URL (必填)
- --folder <String>: 目标文件夹 nodeId
- --workspace <String>: 目标知识库 ID

## Related
- dws drive comment
- dws drive commit
- dws drive cover
- dws drive delete
- dws drive download
- dws drive download-version
