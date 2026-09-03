# dws chat +chat-audit-join

kind: shortcut
completeness: full
usage: dws chat +chat-audit-join
description: 审批入群验证（通过/拒绝/删除/忽略/拉黑）
source: internal/shortcut/chat/chat_group.go:1229
visible_flags: 6

## Flags
- --group <String>: 群 openConversationId
- --record-id <Int>: 申请记录 ID
- --applicant <String>: 申请人 userId
- --inviter <String>: 邀请人 userId
- --status <String>: 审批动作
- --description <String>: 审批说明

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
