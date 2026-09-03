# dws contact user search

kind: command
completeness: full
usage: dws contact user search
description: Search users in the contact directory by keyword (name, title, etc.).
example: dws contact user search --query "张三"
use_when: When the agent needs to resolve a person's display name to a user ID.
source: internal/helpers/contact.go:1043
visible_flags: 1

## Flags
- --query <String>: 搜索关键词 (必填)

## Related
- dws contact user dismission
- dws contact user get
- dws contact user get-self
- dws contact user invite
- dws contact user profile
- dws contact user search-mobile
