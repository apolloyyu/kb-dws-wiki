# dws ding message send

kind: command
completeness: full
usage: dws ding message send
description: Send a DING message (high-priority notification) to one or more recipients via app/SMS/phone.
example: dws ding message send --robot-code <robot-code> --users userId1,userId2 --content "请查看"
use_when: When the agent needs to page recipients with urgency beyond a normal chat message.
source: internal/helpers/ding.go:162
visible_flags: 4

## Flags
- --robot-code <String>: 机器人 ID，发 DING 的机器人编码 (必填，可从 应用管理→机器人 获取，或设 DINGTALK_DING_ROBOT_CODE)
- --type <String>: 提醒类型: app/sms/call (默认 app)
- --users <String>: 接收人 userId 列表 (必填)
- --content <String>: 消息内容 (必填)

## Related
- dws ding message list
- dws ding message recall
- dws ding message recall-personal
- dws ding message receiver-status
- dws ding message send-by-message
- dws ding message send-personal
