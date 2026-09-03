# dws chat group notice edit

kind: command
completeness: full
description: 编辑消息
source: internal/helpers/chat.go:4833
visible_flags: 7

## Flags
- --conversation-id <String>: 会话 openConversationId (必填)
- --message-id <String> required: 消息 openMessageId (必填)
- --text <String>: 编辑后的 Markdown 正文；与 --content 二选一
- --title <String>: 消息标题；配合 --text 使用，未传时从正文自动生成
- --content <String>: 完整 Markdown content JSON；与 --text 二选一
- --at-all <Bool>: 是否 @所有人；正文未包含 <@all> 时自动补到开头
- --at-open-dingtalk-ids <String>: @指定成员的 openDingTalkId 列表，逗号分隔

## Related
- dws chat group notice create
- dws chat group notice get
- dws chat group notice list
