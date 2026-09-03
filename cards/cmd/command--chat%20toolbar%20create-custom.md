# dws chat toolbar create-custom

kind: command
completeness: partial
usage: dws chat toolbar create-custom
description: 创建自定义快捷栏入口
example: dws chat toolbar create-custom --conversation-id <cid> --title "周报" --url "https://example.com" --icon-url "https://example.com/icon.png" --pc-url "https://example.com"
source: internal/helpers/chat/toolbar_create_custom.go:23
visible_flags: 9
partial_reason: unverified_flags

## Flags
- --conversation-id <String> required: 会话 openConversationId
- --title <String> required: 入口标题
- --url <String> required: 入口跳转链接
- --icon-url <String> required: 入口图标 URL
- --pc-url <String> required: PC 端跳转链接
- --extension <StringArray>: 扩展信息，格式 key=value，可重复使用
- --desc <String>: 入口描述（为空时使用 --title）
- --tag <String>: 入口标签
- --sort-index <Int>: 排序权重

## Related
- dws chat toolbar add
- dws chat toolbar hide
- dws chat toolbar list
- dws chat toolbar remove-custom
- dws chat toolbar sort
- dws chat toolbar update-custom
