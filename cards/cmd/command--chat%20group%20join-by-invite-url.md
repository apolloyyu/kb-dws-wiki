# dws chat group join-by-invite-url

kind: command
completeness: full
usage: dws chat group join-by-invite-url
description: 通过群邀请链接申请加入群聊
example: dws chat group join-by-invite-url --invite-url "https://qr.dingtalk.com/action/joingroup?code=xxx"
source: internal/helpers/chat.go:10553
visible_flags: 1

## Flags
- --invite-url <String> required: 群邀请链接 (必填，原样透传服务端)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-info-by-invite-url
