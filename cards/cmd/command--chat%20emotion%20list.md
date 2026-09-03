# dws chat emotion list

kind: command
completeness: full
usage: dws chat emotion list
description: List the current user's personal favorite emotions.
use_when: When the agent needs to inspect available personal emotions or resolve an emotionId/mediaId before sending.
source: internal/helpers/chat_personal_emotion.go:54
visible_flags: 0

## Flags
- none

## Related
- dws chat emotion favorite
- dws chat emotion send
