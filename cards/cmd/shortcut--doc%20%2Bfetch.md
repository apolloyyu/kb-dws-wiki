# dws doc +fetch

kind: shortcut
completeness: full
description: 读取完整或局部文档内容，并按 detail 控制保真度
source: internal/shortcut/doc/content_shortcuts.go:202
visible_flags: 14

## Flags
- --node <String>: 文档 ID 或 URL；
- --query <String>: 文档标题或关键词；跨页唯一解析后读取；
- --detail <String>: —
- --scope <String>: —
- --start-block-id <String>: range/section 起始块 ID
- --end-block-id <String>: range 结束块 ID
- --keyword <String>: keyword 范围搜索词，不能为空，支持 foo|bar
- --tags <StringSlice>: tags 范围的 JSONML tag
- --context-before <Int>: 关键词命中前的上下文字符数
- --context-after <Int>: 关键词命中后的上下文字符数
- --max-depth <Int>: outline/section 最大深度
- --password <String>: 互联网公开文档开启密码保护时的访问密码；普通文档无需传入
- --revision <Int>: 不支持；revision 是文档编辑版本号（JSONML 读取响应返回、供 +update --expected-revision 条件写使用），不是历史版本号
- --version <Int>: 读取指定历史版本(版本号从 doc +version-list 获取, 0 表示初始版本, 需要文档编辑权限)；缺省读最新版

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
