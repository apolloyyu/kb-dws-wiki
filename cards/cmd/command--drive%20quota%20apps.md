# dws drive quota apps

kind: command
completeness: full
usage: dws drive quota apps
description: List app-level storage usage across the enterprise with paging and sorting.
example: dws drive quota apps
use_when: When the agent inventories which apps consume Drive storage or walks the full app list page by page.
source: internal/helpers/drive.go:2220
visible_flags: 4

## Flags
- --limit <Int>: 每页返回数量，默认 20，最大 50
- --cursor <String>: 分页游标，从上次返回的 nextToken 获取 (可选)
- --order-by <String>: 排序字段：used-quota(总用量)/standard-used-quota(标准存储)/exclusive-used-quota(专属存储) (可选)
- --order <String>: 排序方向：asc/desc (可选，默认 desc)

## Related
- none
