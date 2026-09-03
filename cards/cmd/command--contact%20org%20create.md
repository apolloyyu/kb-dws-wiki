# dws contact org create

kind: command
completeness: full
usage: dws contact org create
description: Create a new DingTalk enterprise organization.
example: dws contact org create --org-name "我的企业" --creator-username "张三"
use_when: When the user explicitly asks to create or initialize an enterprise and provides its name and creator display name.
source: internal/helpers/contact.go:2323
visible_flags: 2

## Flags
- --org-name <String>: 企业名称 (必填)
- --creator-username <String>: 创建者在企业内的名称，对应 creatorUsername (必填)

## Related
- none
