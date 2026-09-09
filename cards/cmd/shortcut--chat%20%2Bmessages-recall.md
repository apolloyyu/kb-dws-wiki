# dws chat +messages-recall

kind: shortcut
completeness: full
usage: dws chat +messages-recall
description: 撤回当前用户发送的消息
source: internal/shortcut/chat/chat_message.go:189
visible_flags: 7

## Flags
- --conversation-id <String>: 会话 openConversationId；省略时从消息详情解析
- --group <String>: --conversation-id 的兼容别名
- --id <String>: --conversation-id 的兼容别名
- --chat <String>: --conversation-id 的兼容别名
- --msg-id <String>: 消息 openMessageId；一次只能撤回一个消息 ID；--message-ids 仅接受单值
- --message-id <String>: --msg-id 的兼容别名
- --message-ids <StringSlice>: --msg-id 的兼容单值别名；不支持批量撤回

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
