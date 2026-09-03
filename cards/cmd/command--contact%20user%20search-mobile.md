# dws contact user search-mobile

kind: command
completeness: full
usage: dws contact user search-mobile
description: Look up a user by mobile phone number.
example: dws contact user search-mobile --mobile 13800138000
use_when: When the agent has only a phone number and needs to find the corresponding DingTalk user.
source: internal/helpers/contact.go:1093
visible_flags: 1

## Flags
- --mobile <String>: 手机号 (必填)

## Related
- dws contact user dismission
- dws contact user get
- dws contact user get-self
- dws contact user invite
- dws contact user profile
- dws contact user search
