# dws aitable +workflow-list

kind: shortcut
completeness: full
description: 列出指定 Base 中的自动化工作流（分页）
source: internal/shortcut/aitable/aitable.go:2051
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --limit <Int>: 每页数量，默认 20，最大 100（可选）
- --offset <Int>: 分页偏移量，默认 0（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
