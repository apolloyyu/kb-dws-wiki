# dws chat message update-card

kind: command
completeness: full
usage: dws chat message update-card
description: 流式更新卡片内容
example: dws chat message update-card --biz-id <bizId> --content "更新的卡片内容" --flow-status 2
source: internal/helpers/chat.go:7050
visible_flags: 3

## Flags
- --biz-id <String> required: 卡片业务 ID (必填)
- --content <String> required: 卡片消息内容 (必填)
- --flow-status <String>: 流式状态 (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
