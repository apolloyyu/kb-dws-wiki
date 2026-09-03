# dws contact ext-field update

kind: command
completeness: partial
usage: dws contact ext-field update
description: 更新自定义字段设置
example: dws contact ext-field update --code "rank" --client-display true --is-search false
source: internal/helpers/contact.go:566
visible_flags: 4
partial_reason: unverified_flags

## Flags
- --code <String>: 自定义字段编码 (必填)
- --org-self-tag <String>: 字段类型：1 企业个性化字段，0 默认扩展字段
- --client-display <String>: 是否在客户端展示：true / false (必填)
- --is-search <String>: 是否支持搜索：true / false (必填)

## Related
- dws contact ext-field create
- dws contact ext-field delete
- dws contact ext-field list
