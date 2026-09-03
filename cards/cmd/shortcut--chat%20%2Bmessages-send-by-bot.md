# dws chat +messages-send-by-bot

kind: shortcut
completeness: full
description: 机器人向群聊发送 Markdown 消息
source: internal/shortcut/chat/chat_message.go:43
visible_flags: 7

## Flags
- --robot-code <String>: 机器人 Code
- --group <String>: 群 openConversationId
- --title <String>: 消息标题
- --content <String>: Markdown 正文
- --at-user-ids <StringSlice>: @ 的 userId 列表
- --at-open-dingtalk-ids <StringSlice>: @ 的 openDingTalkId 列表
- --at-all <Bool>: @ 所有人

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
