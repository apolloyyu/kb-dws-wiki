# dws chat message list-unread-conversations

kind: command
completeness: full
usage: dws chat message list-unread-conversations
description: Fetch the list of conversations that currently have unread messages for the user.
example: dws chat message list-unread-conversations
use_when: When the agent builds a "catch me up" triage view of what still needs reading.
source: internal/helpers/chat.go:4734
visible_flags: 2

## Flags
- --count <Int>: 返回未读会话条数（可选，不传则使用服务端默认值）
- --exclude-muted <Bool>: 是否排除已设置免打扰的会话（默认 false）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
