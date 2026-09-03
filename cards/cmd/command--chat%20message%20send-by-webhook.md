# dws chat message send-by-webhook

kind: command
completeness: full
description: Send a group message via a custom-robot incoming webhook URL.
use_when: When the agent needs to post to a group using a webhook without requiring full bot-permission setup.
source: internal/helpers/chat.go:4166
visible_flags: 5

## Flags
- --token <String> required: Webhook Token (必填)
- --title <String> required: 消息标题 (必填)
- --at-all <Bool>: @ 所有人
- --at-mobiles <String>: @ 指定手机号，逗号分隔
- --at-users <String>: @ 指定用户，逗号分隔

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
