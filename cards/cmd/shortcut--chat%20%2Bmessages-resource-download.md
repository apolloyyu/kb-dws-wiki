# dws chat +messages-resource-download

kind: shortcut
completeness: full
usage: dws chat +messages-resource-download
description: 安全下载消息资源（图片/视频/语音/文件）到本地
source: internal/shortcut/chat/resource_download.go:55
visible_flags: 9

## Flags
- --type <String>: —
- --resource-id <String>: —
- --message-id <String>: mediaId 所属消息的 openMessageId；媒体需message-id，可自动补会话；image/file从消息资源元数据解析ID类型；fileId可独立下载
- --open-conversation-id <String>: mediaId 所属会话的 openConversationId；媒体需message-id，可自动补会话；image/file从消息资源元数据解析ID类型；fileId可独立下载
- --output <String>: —
- --part-size <Int>: —
- --retries <Int>: —
- --retry-delay <Int>: —
- --overwrite <Bool>: 允许覆盖工作目录内已存在的目标文件（默认拒绝）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
