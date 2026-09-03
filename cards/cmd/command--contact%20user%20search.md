# dws contact user search

kind: command
completeness: full
description: Search users in the contact directory by keyword (name, title, etc.).
use_when: When the agent needs to resolve a person's display name to a user ID.
source: internal/helpers/contact.go:1043
visible_flags: 1

## Flags
- --query <String>: 搜索关键词 (必填)

## Related
- dws contact user get
- dws contact user get-self
- dws contact user invite
- dws contact user search-mobile
- dws contact user update
- dws contact user update-ownness
