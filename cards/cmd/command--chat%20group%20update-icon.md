# dws chat group update-icon

kind: command
completeness: full
usage: dws chat group update-icon
description: 更新群头像
example: dws chat group update-icon --conversation-id <openConversationId> --icon-media-id <mediaId>
source: internal/helpers/chat.go:7440
visible_flags: 2

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --icon-media-id <String> required: 群头像 mediaId (必填)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
