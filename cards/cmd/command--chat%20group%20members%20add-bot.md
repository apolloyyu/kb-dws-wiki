# dws chat group members add-bot

kind: command
completeness: full
usage: dws chat group members add-bot
description: Add a robot (bot) to an existing group chat so the bot can post messages there.
example: dws chat group members add-bot --robot-code <robot-code> --id <openconversation_id>
use_when: When the agent needs to enable bot-driven notifications in a group that does not yet contain the bot.
source: internal/helpers/chat.go:3087
visible_flags: 2

## Flags
- --robot-code <String> required: 机器人 Code (必填)
- --id <String> required: 群聊 openConversationId (必填)

## Related
- dws chat group members add
- dws chat group members list-by-ids
- dws chat group members remove
- dws chat group members remove-bot
