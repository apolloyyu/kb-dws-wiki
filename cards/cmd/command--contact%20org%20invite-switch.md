# dws contact org invite-switch

kind: command
completeness: partial
usage: dws contact org invite-switch
description: Toggle who can apply to join the enterprise (master switch plus search/code/link channels).
example: dws contact org invite-switch --open true
use_when: When the user explicitly asks to open or close join-application channels.
source: internal/helpers/contact.go:1059
visible_flags: 4
partial_reason: unverified_flags

## Flags
- --open <String>: 申请加入企业总开关：true=允许用户申请加入企业 (必填)
- --search-invite <String>: 搜索团队名称申请加入开关：true/false（可选，不传保持不变）
- --apply-code-invite <String>: 填写团队号申请加入开关：true/false（可选，不传保持不变）
- --link-invite <String>: 链接和二维码申请加入开关：true/false（可选，不传保持不变）

## Related
- dws contact org apply-approve
- dws contact org apply-block
- dws contact org apply-list
- dws contact org apply-reject
- dws contact org apply-remove
- dws contact org create
