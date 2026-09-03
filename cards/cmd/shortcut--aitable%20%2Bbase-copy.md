# dws aitable +base-copy

kind: shortcut
completeness: full
description: 复制 AI 表格到指定目录（可仅复制结构）
source: internal/shortcut/aitable/aitable.go:417
visible_flags: 4

## Flags
- --base-id <String>: 源 Base ID
- --target-folder-id <String>: 目标文件夹 nodeId
- --only-struct <Bool>: 仅复制结构（不含数据），默认 false
- --new-name <String>: 复制后设置的新 Base 名称（1-50 个字符）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
