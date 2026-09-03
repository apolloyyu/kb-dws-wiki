# dws chat conversation-file upload

kind: command
completeness: full
description: Upload a local file to a conversation file space without sending a message, returning reusable file identifiers.
use_when: When the agent explicitly needs conversation-file identifiers without posting a chat message.
source: internal/helpers/chat_media_upload.go:41
visible_flags: 2

## Flags
- --file <String>: 旧版兼容参数；本地文件请改用 chat message send --file
- --type <String>: 旧版兼容参数；不再执行媒体上传

## Related
- none
