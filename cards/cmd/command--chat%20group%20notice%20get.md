# dws chat group notice get

kind: command
completeness: full
usage: dws chat group notice get
description: 查看群公告详情
example: dws chat group notice get --conversation-id <openConversationId> --notice-id <dataId>
source: internal/helpers/chat.go:10569
visible_flags: 2

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --notice-id <String> required: 群公告 dataId (必填)

## Related
- dws chat group notice create
- dws chat group notice edit
- dws chat group notice list
