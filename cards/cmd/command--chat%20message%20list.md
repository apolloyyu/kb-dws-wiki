# dws chat message list

kind: command
completeness: partial
usage: dws chat message list
description: Pull the recent message history of a specific conversation, including quoted-message context for merged forwards and images.
example: dws chat message list --conversation-id <openconversation_id> --time "2025-03-01 00:00:00"
use_when: When the agent needs to read what has recently been said in a conversation and retain the context of replies.
source: internal/helpers/chat.go:3301
visible_flags: 6
partial_reason: unverified_flags

## Flags
- --conversation-id <String>: 群聊 openconversation_id（群聊时必填）
- --user <String>: 单聊用户 userId（单聊时与 --open-dingtalk-id 二选一）
- --open-dingtalk-id <String>: 单聊用户 openDingTalkId（单聊时与 --user 二选一，适用于无法获取 userId 的场景）
- --time <String>: 开始时间，格式: yyyy-MM-dd HH:mm:ss（可选，默认上海时间当前时间）
- --direction <String>: 时间方向: newer=从给定时间往现在拉，older=从给定时间往以前拉（未传 --time 时默认 older）
- --limit <Int>: 返回数量，不传则不限制

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
