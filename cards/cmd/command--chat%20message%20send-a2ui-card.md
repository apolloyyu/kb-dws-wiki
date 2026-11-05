# dws chat message send-a2ui-card

kind: command
completeness: full
usage: dws chat message send-a2ui-card
description: 创建并推送 A2UI 卡片
example: dws chat message send-a2ui-card --conversation-id <openConversationId> --content '["{\"version\":\"v1.0\"}"]'
source: internal/helpers/chat.go:7519
visible_flags: 9

## Flags
- --conversation-id <String>: 群聊 openConversationId（群聊时必填，与 --open-dingtalk-id 互斥）
- --open-dingtalk-id <String>: 单聊接收者 openDingTalkId（单聊时必填，与 --conversation-id 互斥）
- --a2ui-annotations <String>: A2UI 组件注解 JSON 对象数组（可选，支持空数组 []）
- --extension <String>: AICard 消息扩展 JSON 对象，key 非空白且 value 必须为字符串；业务 key 由服务端白名单控制（可选，支持 {}）
- --support-forward <Bool>: 允许转发 A2UI 卡片（默认不允许）
- --at-open-dingtalk-ids <StringSlice>: @ 的成员 openDingTalkId（仅群聊；检查静态 Markdown 与同批绑定值，合法绑定可延后填充；透传 atOpenDingTalkIds，声明总数含重复不超过 100）
- --at-all <Bool>: @所有人（仅群聊；静态正文须含 <a atId=\"all\">，合法绑定可延后填充；线上传 atAll 并改写已知标签为高亮别名）
- --summary <String>: 卡片无法渲染时的降级文案；省略时为“互动卡片”，显式传入时不能为空
- --content <String> required: A2UI 卡片消息 JSON 字符串数组，或 - 从 stdin 读取 (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
