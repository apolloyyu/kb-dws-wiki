# dws contact user update-ownness

kind: command
completeness: partial
usage: dws contact user update-ownness
description: 更新用户个人状态
example: dws contact user update-ownness --user-id user001 --ownness-text "居家办公中"
source: internal/helpers/contact.go:806
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --user-id <String>: 要更新个人状态的用户 userId (必填)
- --ownness-text <String>: 个人状态文本 (必填)，如 \"居家办公中\"

## Related
- dws contact user dismission
- dws contact user get
- dws contact user get-self
- dws contact user invite
- dws contact user profile
- dws contact user search
