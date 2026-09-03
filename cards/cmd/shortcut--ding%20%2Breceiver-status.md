# dws ding +receiver-status

kind: shortcut
completeness: full
usage: dws ding +receiver-status
description: 查询 DING 消息接收人已读状态
source: internal/shortcut/ding/ding.go:68
visible_flags: 10

## Flags
- --ding-id <String>: openDingId
- --users <StringSlice>: 接收人 openDingTalkId 列表 (CSV)
- --content <String>: 消息内容
- --type <String>: —
- --uuid <String>: 幂等键
- --group <String>: openConversationId
- --message-id <String>: openMessageId

## Related
- dws ding +list
