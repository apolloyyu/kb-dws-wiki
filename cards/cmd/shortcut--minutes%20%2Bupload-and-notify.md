# dws minutes +upload-and-notify

kind: shortcut
completeness: full
description: 上传本地音视频创建听记，并在生成后推送闪记卡片
source: internal/shortcut/minutes/alignment.go:129
visible_flags: 7

## Flags
- --file <String>: 本地音视频文件
- --title <String>: 听记标题
- --template-id <String>: 纪要模板 ID
- --input-language <String>: ASR 输入语言
- --complete-timeout <Int>: —
- --poll-interval <Int>: —
- --enable-message-card <Bool>: 兼容入口：上传后推送闪记卡片；新调用推荐 +upload-and-notify

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
