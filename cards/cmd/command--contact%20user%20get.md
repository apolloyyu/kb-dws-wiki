# dws contact user get

kind: command
completeness: full
description: Batch-fetch detailed profile information for one or more users by user ID.
use_when: When the agent needs names, titles, emails, or departments for a known set of user IDs.
source: internal/helpers/contact.go:1134
visible_flags: 1

## Flags
- --ids <String>: 用户 ID 列表 (必填)

## Related
- dws contact user get-self
- dws contact user invite
- dws contact user search
- dws contact user search-mobile
- dws contact user update
- dws contact user update-ownness
