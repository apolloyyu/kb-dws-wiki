# dws aitable +base-list

kind: shortcut
completeness: full
usage: dws aitable +base-list
description: 获取当前用户可访问的 AI 表格 Base 列表（最近访问，支持游标分页）
source: internal/shortcut/aitable/aitable.go:129
visible_flags: 2

## Flags
- --limit <Int>: 每页数量，默认 10，最大 10
- --cursor <String>: 分页游标，首次不传

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
