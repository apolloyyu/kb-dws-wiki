# dws chat message recall-by-bot

kind: command
completeness: full
usage: dws chat message recall-by-bot
description: Recall (retract) a message previously sent by a robot in a group chat.
example: dws chat message recall-by-bot --robot-code <robot-code> --conversation-id <openconversation_id> --keys <process-query-key>
use_when: When the agent sent a bot message in error or with incorrect content and needs to withdraw it.
source: internal/helpers/chat.go:4105
visible_flags: 3

## Flags
- --robot-code <String> required: 机器人 Code (必填)
- --conversation-id <String>: 群聊 openConversationId（群聊撤回时必填）
- --keys <String> required: 消息 processQueryKey 列表，逗号分隔 (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
