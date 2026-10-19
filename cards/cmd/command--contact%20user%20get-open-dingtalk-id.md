# dws contact user get-open-dingtalk-id

kind: command
completeness: full
usage: dws contact user get-open-dingtalk-id
description: 按手机号或钉钉号获取 openDingTalkId
example: dws contact user get-open-dingtalk-id --keyword 13800138000
source: internal/helpers/contact.go:1802
visible_flags: 1

## Flags
- --keyword <String>: 手机号（11位数字）或钉钉号 (必填)

## Related
- dws contact user dismission
- dws contact user get
- dws contact user get-by-dingtalk-id
- dws contact user get-by-open-dingtalk-id
- dws contact user get-self
- dws contact user invite
