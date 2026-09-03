# dws chat +messages-resource-download

kind: shortcut
completeness: full
description: 安全下载消息资源（图片/视频/语音/文件）到本地
source: internal/shortcut/chat/resource_download.go:55
visible_flags: 6

## Flags
- --type <String>: —
- --resource-id <String>: 消息中的 mediaId 或 fileId
- --message-id <String>: mediaId 所属消息的 openMessageId；--type mediaId 时必须同时提供 --message-id 和 --open-conversation-id；fileId 不需要消息上下文
- --open-conversation-id <String>: mediaId 所属会话的 openConversationId；--type mediaId 时必须同时提供 --message-id 和 --open-conversation-id；fileId 不需要消息上下文
- --output <String>: —
- --overwrite <Bool>: 允许覆盖工作目录内已存在的目标文件（默认拒绝）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
