# dws chat +messages-list-direct

kind: shortcut
completeness: full
usage: dws chat +messages-list-direct
description: 拉取单聊会话消息
source: internal/shortcut/chat/chat_message.go:687
visible_flags: 9

## Flags
- --user <String>: 对方 userId（与 --open-dingtalk-id 二选一）
- --open-dingtalk-id <String>: 对方 openDingTalkId（与 --user 二选一）
- --time <String>: 起始时间，如 \"2025-03-01 00:00:00\"
- --forward <Bool>: —
- --limit <Int>: 每页返回数量；显式页大小必须大于 0
- --size <Int>: --limit 的旧版别名；显式页大小必须大于 0
- --page-all <Bool>: 沿毫秒级 nextCursor 自动读取全部单聊消息；--page-limit 仅与 --page-all 一起使用且范围 1-500
- --page-limit <Int>: —
- --no-reactions <Bool>: 不输出消息 reaction（默认输出）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
