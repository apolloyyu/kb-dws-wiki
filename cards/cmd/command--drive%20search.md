# dws drive search

kind: command
completeness: full
description: 搜索文件（聚合钉盘+文档空间）
source: internal/helpers/drive.go:1622
visible_flags: 11

## Flags
- --query <String>: 搜索关键词 (必填)
- --target <String>: 搜索范围: all(默认,聚合钉盘+文档空间) | file(仅钉盘文件) | space(仅钉盘空间) (可选)
- --file-types <StringSlice>: 按文件内容类型过滤，逗号分隔: alidoc,document,image,video,audio,archive (仅 target=file/all 生效)
- --extensions <StringSlice>: 按文件扩展名过滤，不含点号，逗号分隔 (如 pdf,docx,adoc)
- --creator-uids <StringSlice>: 按创建者用户 ID 过滤，逗号分隔
- --created-from <Int64>: 创建时间起始 (毫秒时间戳，含)
- --created-to <Int64>: 创建时间截止 (毫秒时间戳，含)
- --modified-from <Int64>: 修改时间起始 (毫秒时间戳，含)
- --modified-to <Int64>: 修改时间截止 (毫秒时间戳，含)
- --limit <Int>: 每页返回数量（默认 10，最大 30）
- --cursor <String>: 分页游标，从上次返回的 nextCursor 获取 (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
