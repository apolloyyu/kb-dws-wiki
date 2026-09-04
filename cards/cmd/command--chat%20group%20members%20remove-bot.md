# dws chat group members remove-bot

kind: command
completeness: full
usage: dws chat group members remove-bot
description: 从群内移除机器人
example: dws chat group members remove-bot --id <openConversationId> --bot-id <openBotId>
source: internal/helpers/chat.go:8844
visible_flags: 2

## Flags
- --id <String> required: 群聊 openConversationId (必填)
- --bot-id <String> required: 机器人 openBotId (必填)

## Related
- dws chat group members add
- dws chat group members add-bot
- dws chat group members list-by-ids
- dws chat group members remove
