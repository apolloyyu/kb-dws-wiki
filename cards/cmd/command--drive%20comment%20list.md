# dws drive comment list

kind: command
completeness: partial
description: 获取文件/文件夹列表（统一入口）
source: internal/helpers/drive.go:490
visible_flags: 17
partial_reason: too_many_flags:17

## Flags
- --limit <Int>: 每页返回数量，默认 20，最大 50
- --space-id <String>: 钉盘空间 ID (纯数字)，不传则使用「我的文件」(可选)
- --workspace <String>: 文档空间/知识库 ID (加密 string 或 URL)，传入则路由到文档空间 (可选)
- --folder <String>: 父节点 ID (dentryUuid)，不传则列出空间根目录 (可选)
- --cursor <String>: 分页游标，首次不传 (可选)
- --order-by <String>: 排序字段: createTime|modifyTime|name (可选，仅钉盘)
- --order <String>: 排序方向: asc|desc，默认 desc (可选，仅钉盘)
- --thumbnail <Bool>: 是否返回缩略图信息 (可选，仅钉盘)
- … 9 more; use dwsdoc cmd/short for full flags

## Related
- dws drive comment create
