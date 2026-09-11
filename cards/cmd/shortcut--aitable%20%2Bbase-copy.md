# dws aitable +base-copy

kind: shortcut
completeness: full
usage: dws aitable +base-copy
description: 复制 AI 表格（可选目标目录，可仅复制结构）
source: internal/shortcut/aitable/aitable.go:421
visible_flags: 4

## Flags
- --base-id <String>: 源 Base ID 或标准 Base 节点 URL
- --target-folder-id <String>: 可选目标文件夹 dentryUuid、标准节点 URL 或 Drive 文件夹 URL；不传时使用源 Base 工作区根目录
- --only-struct <Bool>: 仅复制结构（不含数据），默认 false
- --new-name <String>: 复制后设置的新 Base 名称（1-50 个字符）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
