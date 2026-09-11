# dws chat +chat-create

kind: shortcut
completeness: full
usage: dws chat +chat-create
description: 按成员和可选群主全量预检后创建一个钉钉群聊
source: internal/shortcut/chat/lark_alignment.go:32
visible_flags: 8

## Flags
- --name <String>: 群名称；省略或空白时不传 groupName，由服务端生成默认群名
- --users <StringSlice>: 初始成员 userId 或 openDingTalkId 列表
- --member-query <StringSlice>: 按姓名/花名唯一解析的初始成员，可逗号分隔或重复传入
- --owner-open-dingtalk-id <String>: 明确指定群主 openDingTalkId（与 --owner-query 互斥；省略时群主为当前用户）
- --owner-query <String>: 按姓名唯一解析群主 openDingTalkId（与 --owner-open-dingtalk-id 互斥）
- --type <String>: —
- --bots <StringSlice>: 初始机器人 robotCode 去重后最多10个；创建后逐个添加，权限失败保留已建群
- --thread <Bool>: 创建为话题群

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
