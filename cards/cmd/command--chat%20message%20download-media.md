# dws chat message download-media

kind: command
completeness: full
usage: dws chat message download-media
description: 下载消息中的资源（图片/视频/语音等）到本地
example: dws chat message download-media --type mediaId --resource-id <mediaId> --message-id <openMessageId> --open-conversation-id <openConversationId> --output ./download.bin
source: internal/helpers/chat.go:7020
visible_flags: 5

## Flags
- --type <String> required: 资源类型: mediaId（必填；仅支持聊天消息 mediaId，不支持钉盘 fileId）
- --resource-id <String> required: 资源 ID，mediaId 类型时为消息中的 mediaId 值（必填；不是钉盘 fileId）
- --open-conversation-id <String> required: 会话 openConversationId (必填)
- --message-id <String> required: 消息 openMessageId (必填)
- --output <String> required: 本地保存路径，文件或目录 (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message edit
