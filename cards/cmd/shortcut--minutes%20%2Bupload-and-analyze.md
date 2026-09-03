# dws minutes +upload-and-analyze

kind: shortcut
completeness: full
description: 本地音视频直传听记并等待分析产物，可选思维导图和发言人洞察
source: internal/shortcut/minutes/workflows.go:63
visible_flags: 13

## Flags
- --file <String>: 本地音视频文件；与 --resume-id 二选一
- --resume-id <String>: 先前已成功上传的 taskUuid；只恢复分析、不重复上传
- --title <String>: 听记标题
- --template-id <String>: 纪要模板 ID
- --input-language <String>: ASR 输入语言
- --enable-message-card <Bool>: 兼容入口：上传后推送闪记卡片；新调用推荐先使用 +upload-and-notify
- --complete-timeout <Int>: —
- --poll-interval <Int>: —
- --wait-timeout <Int>: —
- --artifacts <StringSlice>: 等待的分析产物
- --page-limit <Int>: —
- --mindmap <Bool>: 继续创建并等待思维导图
- --speaker-insights <Bool>: 继续创建并等待发言人总结

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
