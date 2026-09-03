# dws chat group members remove-bot

kind: command
completeness: full
description: 从群内移除机器人
source: internal/helpers/chat.go:8642
visible_flags: 2

## Flags
- --id <String> required: 群聊 openConversationId (必填)
- --bot-id <String> required: 机器人 openBotId (必填)

## Related
- dws chat group members add
- dws chat group members add-bot
- dws chat group members list-by-ids
- dws chat group members remove
