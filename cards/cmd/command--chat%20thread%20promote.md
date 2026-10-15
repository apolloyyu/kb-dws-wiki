# dws chat thread promote

kind: command
completeness: partial
usage: dws chat thread promote
description: 已下线：消息转话题历史兼容入口
example: dws chat thread promote --conversation-id <openConversationId> --message-id <openMessageId>
source: internal/helpers/chat_thread.go:93
visible_flags: 12
partial_reason: unverified_flags,empty_flag_name

## Flags
- --message-id <String>: 旧版兼容参数，已忽略
- --title <String>: 消息标题
- --at-all <Bool>: @所有人（仅群聊时生效，可选）,设置时，消息内容中一定要包含对应的占位符<@all>
- --at-open-dingtalk-ids <String>: @指定成员的 openDingTalkId 列表，逗号分隔（仅群聊时生效，可选）,设置--at-open-dingtalk-ids openDingTalkId1,openDingTalkId2时，消息内容中一定要包含对应格式的占位符<@openDingTalkId1> <@openDingTalkId2>
- --media-id <String>: 已有图片 mediaId
- --msg-type <String>: 内容类型: image/file/audio/video
- --dentry-id <Int64>: 文件 dentryId（与 --space-id 成对传入时跳过自动上传）
- --space-id <Int64>: 空间 ID（与 --dentry-id 成对传入时跳过自动上传）
- … 4 more; use dwsdoc cmd/short for full flags

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
