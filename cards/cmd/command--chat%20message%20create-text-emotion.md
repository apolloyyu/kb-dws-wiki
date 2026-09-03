# dws chat message create-text-emotion

kind: command
completeness: full
description: 创建文字表情（获取 emotionId）
source: internal/helpers/chat.go:6618
visible_flags: 3

## Flags
- --emotion-name <String> required: 表情名称 (必填)
- --text <String> required: 文字内容 (必填)
- --background-id <String>: 背景 ID（可选，不传则由服务端默认分配）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message download-media
- dws chat message edit
