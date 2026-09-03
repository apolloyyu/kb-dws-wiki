# dws chat emotion favorite

kind: command
completeness: full
usage: dws chat emotion favorite
description: Add a media ID or a local image (jpg/jpeg/png/gif/webp/bmp, ≤10MB) to the current user's personal favorite emotions.
example: dws chat emotion favorite --media-id <mediaId> --name "赞"
use_when: When the agent needs to save an available mediaId or a local image file as a reusable personal emotion; local images are uploaded through dingtalk-file/upload_media (bizType=chat_emoticon) first, optionally preserving source message context.
source: internal/helpers/chat_personal_emotion.go:141
visible_flags: 5

## Flags
- --media-id <String>: 待收藏 mediaId；与 --file-path 二选一必填
- --file-path <String>: 本地图片路径 (jpg/jpeg/png/gif/webp/bmp，≤10MB；超过2MB会先自动压缩)；与 --media-id 二选一必填
- --name <String>: 表情名称
- --source-conversation-id <String>: 来源会话 ID；需与 --source-message-id 成对指定
- --source-message-id <String>: 来源消息 ID；需与 --source-conversation-id 成对指定

## Related
- dws chat emotion list
- dws chat emotion send
