# dws chat thread send

kind: command
completeness: partial
usage: dws chat thread send
description: Publish a new topic.
use_when: When the agent needs to create a new top-level discussion.
source: internal/helpers/chat.go:4040
visible_flags: 14
partial_reason: unverified_flags,empty_flag_name

## Flags
- --conversation-id <String>: 群聊 openconversation_id（群聊时必填）
- --user <String>: 单聊接收人 userId（单聊时与 --open-dingtalk-id 二选一）
- --open-dingtalk-id <String>: 单聊接收人 openDingTalkId（单聊时与 --user 二选一）
- --title <String>: 消息标题，显示在消息列表（可选，未指定时使用消息内容）
- --at-all <Bool>: @所有人（仅群聊时生效，可选）,设置时，消息内容中一定要包含对应的占位符<@all>
- --at-open-dingtalk-ids <String>: @指定成员的 openDingTalkId 列表，逗号分隔（仅群聊时生效，可选）,设置--at-open-dingtalk-ids openDingTalkId1,openDingTalkId2时，消息内容中一定要包含对应格式的占位符<@openDingTalkId1> <@openDingTalkId2>
- --media-id <String>: 上游已提供的图片 mediaId（仅独立 msgType=image；Markdown 内联本地图片请写在 --content 中）
- --msg-type <String>: 独立富媒体消息类型: image/file/audio/video/location/profile（内联本地图文无需此 flag；附件用 file --file）
- … 6 more; use dwsdoc cmd/short for full flags

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
