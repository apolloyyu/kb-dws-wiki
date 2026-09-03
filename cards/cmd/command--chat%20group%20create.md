# dws chat group create

kind: command
completeness: full
description: Create a new internal group chat with a set of initial members.
use_when: When the agent needs to spin up a dedicated group for a new project, incident, or discussion thread.
source: internal/helpers/chat.go:2905
visible_flags: 3

## Flags
- --name <String> required: 群名称 (必填)
- --users <String> required: 成员 userId 或 openDingTalkId（可混传），逗号分隔 (必填)
- --type <String>: 群类型: INTERNAL(内部群,默认)/EXTERNAL(外部群)/NORMAL(普通群)

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
- dws chat group invite-url
