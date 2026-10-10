# dws aitable api-key revoke

kind: command
completeness: partial
usage: dws aitable api-key revoke
description: —
source: internal/helpers/aitable_api_key.go:156
visible_flags: 2
partial_reason: missing_description

## Flags
- --base-id <String> required: AI 表格 Base ID
- --key-id <String> required: 要撤销的 Key 标识，小写规范 UUID

## Related
- dws aitable api-key create
- dws aitable api-key list
