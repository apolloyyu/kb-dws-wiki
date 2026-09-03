# dws chat +messages-update-card

kind: shortcut
completeness: full
usage: dws chat +messages-update-card
description: 流式更新卡片内容（最后一次 --flow-status 应为 3）
source: internal/shortcut/chat/chat_message.go:1730
visible_flags: 3

## Flags
- --biz-id <String>: send-card 返回的卡片业务 ID
- --content <String>: 卡片消息内容
- --flow-status <Int>: 流式状态 1处理中/2输入中/3完成/4执行中/5错误；--flow-status 必须在 1-5 之间

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
