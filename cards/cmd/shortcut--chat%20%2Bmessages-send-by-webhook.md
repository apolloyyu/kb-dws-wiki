# dws chat +messages-send-by-webhook

kind: shortcut
completeness: full
description: 兼容旧入口的自定义机器人 Webhook 群消息发送
source: internal/shortcut/chat/chat_message.go:124
visible_flags: 6

## Flags
- --token <String>: Webhook token
- --title <String>: 消息标题
- --content <String>: 消息正文
- --at-all <Bool>: @ 所有人
- --at-mobiles <StringSlice>: @ 的手机号列表
- --at-users <StringSlice>: @ 的 userId 列表

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
