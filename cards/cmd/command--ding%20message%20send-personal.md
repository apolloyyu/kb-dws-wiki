# dws ding message send-personal

kind: command
completeness: full
usage: dws ding message send-personal
description: 以用户身份发送 DING
example: dws ding message send-personal --users openDingTalkId1,openDingTalkId2 --content "请查看"
source: internal/helpers/ding.go:336
visible_flags: 4

## Flags
- --users <String> required: 接收者 openDingTalkId 列表，逗号分隔 (必填)
- --content <String> required: DING 内容 (必填)
- --type <String>: 提醒类型: app/sms/call (默认 app)
- --uuid <String>: 幂等唯一标识（可选，不传由服务端生成）

## Related
- dws ding message list
- dws ding message recall
- dws ding message recall-personal
- dws ding message receiver-status
- dws ding message send
- dws ding message send-by-message
