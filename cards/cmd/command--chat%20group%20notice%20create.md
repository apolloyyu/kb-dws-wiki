# dws chat group notice create

kind: command
completeness: full
usage: dws chat group notice create
description: 发布群公告
example: dws chat group notice create --conversation-id <openConversationId> --content "今晚 22 点系统维护，请提前保存工作内容"
source: internal/helpers/chat.go:10630
visible_flags: 5

## Flags
- --conversation-id <String> required: 群聊 openConversationId (必填)
- --content <String> required: 公告正文，Markdown 格式 (必填)
- --sticky <Bool>: 是否吊顶置顶（默认 false）
- --send-ding <Bool>: 是否发 DING 提醒（默认 false）
- --run-at <String>: 定时发布时间 ISO-8601（如 2026-07-03T09:00:00+08:00，传入则定时发布）

## Related
- dws chat group notice edit
- dws chat group notice get
- dws chat group notice list
