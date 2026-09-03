# dws chat conversation-file upload

kind: command
completeness: full
usage: dws chat conversation-file upload
description: Upload a local file to a conversation file space without sending a message, returning reusable file identifiers.
use_when: When the agent explicitly needs conversation-file identifiers without posting a chat message.
source: internal/helpers/chat.go:5592
visible_flags: 8

## Flags
- --conversation-id <String>: 群聊 openConversationId（群聊时使用）
- --user <String>: 单聊对方 userId（单聊时使用）
- --open-dingtalk-id <String>: 单聊对方 openDingTalkId（单聊时使用）
- --file <String>: 本地文件路径（与 --url 二选一）
- --url <String>: 远程文件 URL（与 --file 二选一，服务端代传）
- --file-name <String>: 文件名（可选，本地文件默认取文件名，URL 默认从 URL 推断）
- --md5 <String>: 文件 MD5（可选，本地文件不传时自动计算）
- --uuid <String>: 幂等 UUID（可选）

## Related
- none
