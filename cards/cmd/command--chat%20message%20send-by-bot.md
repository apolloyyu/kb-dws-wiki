# dws chat message send-by-bot

kind: command
completeness: full
description: Send a group message as a specific robot (bot) the user owns.
use_when: When the agent posts automated notifications under a bot identity rather than as the user.
source: internal/helpers/chat.go:3860
visible_flags: 14

## Flags
- --robot-code <String> required: 机器人 Code (必填)
- --conversation-id <String>: 群聊 openConversationId（群聊时必填）
- --users <String>: 用户 userId 列表，逗号分隔，最多20个（单聊时必填）
- --msg-type <String>: 消息类型: markdown/image/file（省略时为 markdown；图片使用 image --image-url；本地文件使用 file --file-path）
- --title <String>: Markdown 消息标题（发送普通 Markdown 时必填；引用回复省略时从正文生成）
- --text <String>: Markdown 消息内容（发送 Markdown 时必填；稳定换行用空行，转义形式写 \\n\\n，不要只写 \\n）
- --image-url <String>: 公网图片 URL（msgType=image 时必填）
- --file-path <String>: 本地文件路径（msgType=file 时直接上传并按 file 消息发送）
- --at-user-ids <String>: @指定成员的 userId 列表，逗号分隔（仅群聊时生效，可选），--text 中需包含 @userId 对应文本
- --open-dingtalk-ids <String>: 用户 openDingtalkId 列表，逗号分隔（单聊时可替代 --users，可选）
- --at-open-dingtalk-ids <String>: @指定成员的 openDingtalkId 列表，逗号分隔（仅群聊时生效，可选）
- --at-all <Bool>: @所有人（可选），服务端接收字符串 true/false
- --reply <String>: 被引用消息的 openMessageId（仅群聊 Markdown；必须与 --ref-sender 同时使用）
- --ref-sender <String>: 被引用消息发送者的 openDingTalkId（仅群聊 Markdown；必须与 --reply 同时使用）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
