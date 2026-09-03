# dws drive info

kind: command
completeness: full
description: Retrieve metadata for a file or folder in DingTalk Drive.
use_when: When the agent inspects a Drive node before downloading, moving, or listing around it.
source: internal/helpers/drive.go:730
visible_flags: 2

## Flags
- --node <String>: 节点 ID (dentryUuid) (必填)
- --space-id <String>: 节点所属空间 ID (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
