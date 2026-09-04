# dws chat message update-a2ui-card

kind: command
completeness: full
usage: dws chat message update-a2ui-card
description: 更新 A2UI 卡片内容和状态
example: dws chat message update-a2ui-card --biz-id <bizId> --content '["{\"version\":\"v1.0\",\"updateDataModel\":{\"surfaceId\":\"surface\",\"path\":\"/status\",\"value\":\"finished\"}}"]' --flow-status FINISH
source: internal/helpers/chat.go:7150
visible_flags: 3

## Flags
- --biz-id <String> required: 卡片业务 ID (必填)
- --content <String> required: A2UI 卡片消息 JSON 字符串数组 (必填)
- --flow-status <String> required: A2UI 状态枚举或兼容数字 1-9 (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
