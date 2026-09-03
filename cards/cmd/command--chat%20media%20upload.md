# dws chat media upload

kind: command
completeness: full
description: 已下线：请通过 chat message send 直接发送本地文件
source: internal/helpers/chat_media_upload.go:41
visible_flags: 2

## Flags
- --file <String>: 旧版兼容参数；本地文件请改用 chat message send --file
- --type <String>: 旧版兼容参数；不再执行媒体上传

## Related
- none
