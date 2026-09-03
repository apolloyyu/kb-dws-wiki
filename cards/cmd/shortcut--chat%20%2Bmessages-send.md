# dws chat +messages-send

kind: shortcut
completeness: partial
description: 按身份和目标统一发送消息，Bot 多群返回逐目标 ledger
source: internal/shortcut/chat/unified_send.go:43
visible_flags: 27
partial_reason: too_many_flags:27

## Flags
- --identity <String>: —
- --as <String>: —
- --group <String>: 群 openConversationId（user/bot 群聊）；受发送身份能力矩阵约束
- --chat-id <String>: --group 的 lark-cli 对齐别名；受发送身份能力矩阵约束
- --groups <StringSlice>: 多个群 openConversationId（仅 bot；受发送身份能力矩阵约束，逐群返回 typed ledger，最多 100 个）
- --groups-file <String>: 工作目录内相对文本文件（仅 bot；受发送身份能力矩阵约束），每行或逗号分隔一个群 openConversationId
- --chat-query <String>: 按群名解析唯一群聊（仅 user 的高级发送场景）；受发送身份能力矩阵约束
- --user <String>: 单聊接收者 userId（user；包括 --dry-run 也会先通过通讯录搜索精确匹配 openDingTalkId）；受发送身份能力矩阵约束
- … 19 more; use dwsdoc cmd/short for full flags

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
