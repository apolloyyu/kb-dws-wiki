# dws aitable form share notify

kind: command
completeness: full
usage: dws aitable form share notify
description: 通知表单填写人
example: dws aitable form share notify --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --recipients USER_ID_1,USER_ID_2 --send-chat true
source: internal/helpers/aitable.go:6685
visible_flags: 8

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID (必填)
- --recipients <String>: 接收通知的用户 ID，逗号分隔 (必填)
- --send-chat <String>: 是否发送聊天消息 (true/false)
- --send-card <String>: 是否通过钉钉文档发送卡片 (true/false)
- --send-todo <String>: 是否创建待办 (true/false)
- --send-work-notice <String>: 是否发送工作通知 (true/false)

## Related
- dws aitable form share get
- dws aitable form share update
