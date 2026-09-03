# dws contact user update-self

kind: command
completeness: full
usage: dws contact user update-self
description: 更新当前用户自己的 profile 信息
example: dws contact user update-self --nick "新昵称"
source: internal/helpers/contact.go:776
visible_flags: 2

## Flags
- --nick <String>: 新昵称（可选）
- --avatar-file-id <String>: 新头像在钉盘的 fileId（可选）

## Related
- dws contact user dismission
- dws contact user get
- dws contact user get-self
- dws contact user invite
- dws contact user profile
- dws contact user search
