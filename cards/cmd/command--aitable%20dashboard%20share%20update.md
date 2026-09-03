# dws aitable dashboard share update

kind: command
completeness: full
description: Enable, disable, or update the public-sharing configuration of a dashboard.
use_when: When the agent needs to generate or revoke an external share link for a dashboard.
source: internal/helpers/aitable.go:1897
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --name <String>: 新名称，1-50 字符 (必填)
- --desc <String>: 备注文本

## Related
- dws aitable dashboard share get
