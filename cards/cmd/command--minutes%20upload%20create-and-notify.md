# dws minutes upload create-and-notify

kind: command
completeness: full
description: 创建上传会话并在生成后推送闪记卡片
source: internal/helpers/minutes.go:1535
visible_flags: 5

## Flags
- --file-name <String>: 文件名（含后缀），如 meeting.mp4 (必填)
- --file-size <Int64>: 文件大小（字节）(必填)
- --title <String>: 听记标题，不传时默认使用文件名去掉后缀 (可选)
- --template-id <String>: 纪要生成使用的模板 ID (可选)
- --input-language <String>: ASR 识别的源语言 (可选)

## Related
- dws minutes upload cancel
- dws minutes upload complete
- dws minutes upload create
