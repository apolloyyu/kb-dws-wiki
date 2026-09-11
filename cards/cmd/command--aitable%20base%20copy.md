# dws aitable base copy

kind: command
completeness: full
usage: dws aitable base copy
description: 复制 AI 表格
example: dws aitable base copy --base-id BASE_ID
source: internal/helpers/aitable.go:2462
visible_flags: 3

## Flags
- --base-id <String>: 源 Base ID 或标准 Base 节点 URL (必填)
- --target-folder-id <String>: 可选目标文件夹 dentryUuid、标准节点 URL 或 Drive 文件夹 URL；不传时使用源 Base 工作区根目录
- --only-struct <Bool>: 是否仅复制结构（不含数据），默认 false 表示完整复制

## Related
- dws aitable base create
- dws aitable base delete
- dws aitable base get
- dws aitable base get-primary-doc-id
- dws aitable base list
- dws aitable base search
