# dws drive quota

kind: command
completeness: full
usage: dws drive quota
description: Query enterprise storage quota at the enterprise (default), app (`--app`), or space (`--space`) level.
example: dws drive quota
use_when: When the agent checks DingTalk Drive storage usage or remaining space.
source: internal/helpers/drive.go:2156
visible_flags: 2

## Flags
- --app <String>: 应用 ID (可选，与 --space 互斥)
- --space <String>: 空间 ID (可选，与 --app 互斥)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
