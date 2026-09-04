# dws chat message edit

kind: command
completeness: partial
usage: dws chat message edit
description: 编辑消息
example: dws chat message edit --conversation-id <openConversationId> --message-id <openMessageId> --text "更新后的内容"
source: internal/helpers/chat.go:5035
visible_flags: 7
partial_reason: unverified_flags

## Flags
- --message-id <String> required: 消息 openMessageId (必填)
- --conversation-id <String>: 会话 openConversationId (必填)
- --text <String>: 编辑后的 Markdown 正文；与 --content 二选一
- --title <String>: 消息标题；配合 --text 使用，未传时从正文自动生成
- --content <String>: 完整 Markdown content JSON；与 --text 二选一
- --at-all <Bool>: 是否 @所有人；正文未包含 <@all> 时自动补到开头
- --at-open-dingtalk-ids <String>: @指定成员的 openDingTalkId 列表，逗号分隔

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
