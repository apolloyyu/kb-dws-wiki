# dws minutes upload create

kind: command
completeness: full
usage: dws minutes upload create
description: Create a file upload session for producing a meeting note from a local audio/video file.
example: dws minutes upload create --file-name "meeting.mp4" --file-size 102400
use_when: When the agent begins uploading a recording to be turned into a meeting note.
source: internal/helpers/minutes.go:1478
visible_flags: 6

## Flags
- --file-name <String>: 文件名（含后缀），如 meeting.mp4 (必填)
- --file-size <Int64>: 文件大小（字节）(必填)
- --title <String>: 听记标题，不传时默认使用文件名去掉后缀 (可选)
- --template-id <String>: 纪要生成使用的模板 ID (可选)
- --input-language <String>: ASR 识别的源语言 (可选)
- --enable-message-card <Bool>: [兼容提示] 已迁移，请使用 upload create-and-notify

## Related
- dws minutes upload cancel
- dws minutes upload complete
- dws minutes upload create-and-notify
