# dws aitable +template-search

kind: shortcut
completeness: full
usage: dws aitable +template-search
description: 按名称关键词搜索 AI 表格模板
source: internal/shortcut/aitable/aitable.go:1034
visible_flags: 3

## Flags
- --query <String>: 模板名称关键词（可选，不传返回热门）
- --limit <Int>: 每页数量，默认 10，最大 30（可选）
- --cursor <String>: 分页游标（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
