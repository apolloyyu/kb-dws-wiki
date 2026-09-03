# dws agoal strategy detail

kind: command
completeness: full
usage: dws agoal strategy detail
description: 获取战略解码详情
example: dws agoal strategy detail --profile-id PROFILE_ID
source: internal/helpers/agoal.go:77
visible_flags: 2

## Flags
- --profile-id <String>: 战略解码 id (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal strategy list
- dws agoal strategy update
