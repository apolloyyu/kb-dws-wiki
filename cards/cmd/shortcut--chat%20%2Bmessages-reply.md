# dws chat +messages-reply

kind: shortcut
completeness: full
usage: dws chat +messages-reply
description: 引用回复一条已有消息，并返回可继续查询或撤回的发送上下文
source: internal/shortcut/chat/lark_alignment.go:197
visible_flags: 7

## Flags
- --group <String>: 会话 openConversationId
- --ref-msg-id <String>: 被引用消息 openMessageId
- --message-id <String>: --ref-msg-id 的 lark-cli 对齐别名
- --ref-sender <String>: 原消息发送者 openDingTalkId/userId（userId 通过通讯录搜索精确匹配；不传则自动读取）
- --content <String>: 纯文本回复内容
- --uuid <String>: 幂等键（可选）
- --idempotency-key <String>: --uuid 的 lark-cli 对齐别名

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
