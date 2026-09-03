# dws conference member invite

kind: command
completeness: full
usage: dws conference member invite
description: 邀请指定人入会（已下线）
example: dws conference member invite --conference-id "xxx"
source: internal/helpers/conference.go:65
visible_flags: 3

## Flags
- --conference-id <String>: 会议ID (必填)
- --nicks <String>: 被邀请人昵称，逗号分隔 (必填)
- --open-dingtalk-ids <String>: 被邀请人 openDingTalkId，逗号分隔，通过 contact/aisearch 获取 (必填)

## Related
- none
