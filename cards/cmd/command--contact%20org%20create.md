# dws contact org create

kind: command
completeness: full
description: Create a new DingTalk enterprise organization.
use_when: When the user explicitly asks to create or initialize an enterprise and provides its name and creator display name.
source: internal/helpers/contact.go:180
visible_flags: 3

## Flags
- --name <String>: 部门名称 (必填)
- --parent <String>: 父部门 ID（可选，不传默认根部门）
- --create-dept-group <Bool>: 是否创建部门群 (必填，需显式传 true 或 false)

## Related
- none
