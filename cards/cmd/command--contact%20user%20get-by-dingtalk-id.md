# dws contact user get-by-dingtalk-id

kind: command
completeness: full
usage: dws contact user get-by-dingtalk-id
description: 按钉钉号获取用户ID
example: dws contact user get-by-dingtalk-id --id zhangsan
source: internal/helpers/contact.go:1676
visible_flags: 1

## Flags
- --id <String>: 钉钉号 dingtalkId (必填)

## Related
- dws contact user dismission
- dws contact user get
- dws contact user get-by-open-dingtalk-id
- dws contact user get-self
- dws contact user invite
- dws contact user profile
