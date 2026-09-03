# dws contact user update-self

kind: command
completeness: full
description: 更新当前用户自己的 profile 信息
source: internal/helpers/contact.go:776
visible_flags: 2

## Flags
- --nick <String>: 新昵称（可选）
- --avatar-file-id <String>: 新头像在钉盘的 fileId（可选）

## Related
- dws contact user get
- dws contact user get-self
- dws contact user invite
- dws contact user search
- dws contact user search-mobile
- dws contact user update
