# dws chat +messages-send-card

kind: shortcut
completeness: full
usage: dws chat +messages-send-card
description: 创建流式卡片，可在同一次调用中写入内容并结束；群聊创建时可 @成员或 @所有人
source: internal/shortcut/chat/chat_message.go:1463
visible_flags: 7

## Flags
- --group <String>: 群 openConversationId（与两个单聊接收者参数互斥）；艾特参数仅支持群聊 --group
- --receiver <String>: 单聊接收者 userId（与 --group/--receiver-open-dingtalk-id 互斥）；始终通过通讯录搜索精确匹配 openDingTalkId，包括 --dry-run 和 D/d 开头的 userId
- --receiver-open-dingtalk-id <String>: 单聊接收者 openDingTalkId（与 --group/--receiver 互斥）；显式直传且不做通讯录解析
- --at-open-dingtalk-ids <StringSlice>: 群聊创建卡片时 @ 的 openDingTalkId 列表；仅随 create_and_send_card 发送；艾特参数仅支持群聊 --group
- --at-all <Bool>: 群聊创建卡片时 @ 所有人；仅随 create_and_send_card 发送；艾特参数仅支持群聊 --group
- --content <String>: 创建后立即写入的卡片正文；群聊 @ 时 Runtime 自动前置 create 返回的 atTag；省略时仅创建并返回 bizId
- --flow-status <Int>: —

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
