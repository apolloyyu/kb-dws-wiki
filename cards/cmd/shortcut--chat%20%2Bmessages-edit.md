# dws chat +messages-edit

kind: shortcut
completeness: full
usage: dws chat +messages-edit
description: 编辑当前用户自己的 Markdown 消息（不支持 Bot 普通消息编辑）
source: internal/shortcut/chat/messages_edit.go:20
visible_flags: 8

## Flags
- --group <String>: 消息所在会话 openConversationId
- --message-id <String>: —
- --as <String>: —
- --text <String>: 新的 Markdown 正文
- --title <String>: 新标题；仅 --text 模式，省略则从正文生成
- --content <String>: 完整 Markdown JSON，包含 text，可选 title
- --at-open-dingtalk-ids <StringSlice>: @成员 openDingTalkId
- --at-all <Bool>: @所有人

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
