# dws chat message list-direct

kind: command
completeness: full
usage: dws chat message list-direct
description: 拉取单聊会话消息
example: dws chat message list-direct --user <对方userId> --time "2026-04-01 00:00:00" --forward true --limit 50
source: internal/helpers/chat.go:3433
visible_flags: 5

## Flags
- --user <String>: 对方 userId（同组织内同事，与 --open-dingtalk-id 二选一）
- --open-dingtalk-id <String>: 对方 openDingTalkId（非同组织普通好友场景，与 --user 二选一）
- --time <String>: 开始时间，格式 yyyy-MM-dd HH:mm:ss (必填)
- --direction <String>: 时间方向: newer=从给定时间往现在拉，older=从给定时间往以前拉
- --limit <Int>: 每页返回数量（默认 50）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
