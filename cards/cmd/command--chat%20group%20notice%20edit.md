# dws chat group notice edit

kind: command
completeness: full
usage: dws chat group notice edit
description: 修改群公告
example: dws chat group notice edit --conversation-id <openConversationId> --notice-id <dataId> --content "更新后的公告内容"
source: internal/helpers/chat.go:10501
visible_flags: 5

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --notice-id <String> required: 群公告 dataId (必填)
- --content <String> required: 公告新正文，Markdown 格式 (必填)
- --sticky <Bool>: 是否吊顶置顶（不传按 false 处理）
- --send-ding <Bool>: 是否发 DING 提醒（默认 false）

## Related
- dws chat group notice create
- dws chat group notice get
- dws chat group notice list
