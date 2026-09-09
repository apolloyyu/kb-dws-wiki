# dws chat +messages-batch-send-by-bot

kind: shortcut
completeness: full
usage: dws chat +messages-batch-send-by-bot
description: 机器人批量向用户发送单聊 Markdown 消息
source: internal/shortcut/chat/chat_message.go:89
visible_flags: 6

## Flags
- --robot-code <String>: 机器人 Code
- --title <String>: 消息标题
- --content <String>: Markdown 正文
- --users <StringSlice>: 接收人 userId 列表
- --open-dingtalk-ids <StringSlice>: 接收人 openDingTalkId 列表
- --at-all <Bool>: @ 所有人

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
