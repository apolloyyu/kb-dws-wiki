# dws aitable base copy

kind: command
completeness: full
usage: dws aitable base copy
description: 复制 AI 表格
example: dws aitable base copy --base-id BASE_ID --target-folder-id FOLDER_NODE_ID
source: internal/helpers/aitable.go:1985
visible_flags: 3

## Flags
- --base-id <String>: 源 Base ID (必填)
- --target-folder-id <String>: 目标文件夹 nodeId (必填)
- --only-struct <Bool>: 是否仅复制结构（不含数据），默认 false 表示完整复制

## Related
- dws aitable base create
- dws aitable base delete
- dws aitable base get
- dws aitable base get-primary-doc-id
- dws aitable base list
- dws aitable base search
