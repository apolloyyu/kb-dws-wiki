# dws chat conversation-file upload

kind: command
completeness: full
usage: dws chat conversation-file upload
description: Upload a local file to a conversation file space without sending a message, returning reusable file identifiers.
use_when: When the agent explicitly needs conversation-file identifiers without posting a chat message.
source: internal/helpers/chat.go:6192
visible_flags: 7

## Flags
- --conversation-id <String>: 群聊 openConversationId
- --user <String>: 单聊对方 userId
- --open-dingtalk-id <String>: 单聊对方 openDingTalkId
- --file <String> required: 工作目录内的本地文件路径（必填）
- --file-name <String>: 上传后的文件名；省略时使用本地文件名
- --md5 <String>: 文件 MD5；省略时由 CLI 计算
- --idempotency-key <String>: 幂等键

## Related
- none
