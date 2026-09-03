# dws doc folder create

kind: command
completeness: full
usage: dws doc folder create
description: Create a new folder inside a DingTalk Docs knowledge base or drive location.
example: dws doc folder create --name "项目资料"
use_when: When the agent organizes output into a fresh folder before writing files into it.
source: internal/helpers/doc.go:1936
visible_flags: 3

## Flags
- --name <String>: 文件夹名称 (必填)
- --folder <String>: 父文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 目标知识库 ID

## Related
- none
