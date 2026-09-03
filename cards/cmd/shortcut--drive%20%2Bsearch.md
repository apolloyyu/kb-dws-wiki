# dws drive +search

kind: shortcut
completeness: full
description: 搜索钉盘文件
source: internal/shortcut/drive/drive.go:239
visible_flags: 14

## Flags
- --query <String>: 搜索关键词
- --target <String>: 搜索范围: file(钉盘文件) / space(钉盘团队空间)
- --file-types <StringSlice>: 按文件内容类型过滤: alidoc,document,image,video,audio,archive
- --extensions <StringSlice>: 按文件扩展名过滤，不含点号 (如 pdf,docx)
- --creator-uids <StringSlice>: 按创建者用户 ID 过滤
- --created-from <Int>: 创建时间起始 (毫秒时间戳，含)
- --created-to <Int>: 创建时间截止 (毫秒时间戳，含)
- --modified-from <Int>: 修改时间起始 (毫秒时间戳，含)
- --modified-to <Int>: 修改时间截止 (毫秒时间戳，含)
- --limit <Int>: 每页返回数量 (默认 10，最大 30)
- --cursor <String>: 分页游标，从上次返回的 nextCursor 获取
- --page-all <Bool>: 有界读取全部后续页；--max-pages/--max-items 仅在 --page-all 时生效且必须大于 0
- --max-pages <Int>: —
- --max-items <Int>: —

## Related
- dws drive +copy
- dws drive +create-folder
- dws drive +create-shortcut
- dws drive +delete
- dws drive +download
- dws drive +info
