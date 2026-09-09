# dws chat +messages-reply

kind: shortcut
completeness: partial
usage: dws chat +messages-reply
description: 统一回复已有消息：个人群/单聊引用、个人 Thread 追加、Bot 群引用
source: internal/shortcut/chat/lark_alignment.go:217
visible_flags: 15
partial_reason: too_many_flags:15

## Flags
- --as <String>: —
- --robot-code <String>: Bot 回复所用 robotCode
- --open-dingtalk-id <String>: 个人单聊接收者；可省略 --group，自动读取源消息会话核实
- --create-thread <Bool>: 与reply-in-thread一起：仅源消息尚无Thread时先转换，再追加；转换后失败保留恢复ID
- --reply-in-thread <Bool>: 直接追加到源消息所属 Thread，不生成引用消息；仅 user
- --thread-id <String>: 可选 openConvThreadId，必须与源消息返回值一致；仅 reply-in-thread
- --group <String>: 可选会话 openConversationId；
- --ref-msg-id <String>: 被引用消息 openMessageId
- … 7 more; use dwsdoc cmd/short for full flags

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
