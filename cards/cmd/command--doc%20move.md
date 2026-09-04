# dws doc move

kind: command
completeness: full
usage: dws doc move
description: Move a DingTalk Doc or file to a different folder location.
example: dws doc move --node DOC_ID --folder TARGET_DOC_FOLDER_NODE_ID
use_when: When the agent reorganizes document structure.
source: internal/helpers/doc.go:2525
visible_flags: 3

## Flags
- --node <String>: 文档/文件 ID 或 URL (必填)
- --folder <String>: 目标文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 目标知识库 ID 或 URL (不传 --folder 时移动到该知识库根目录)

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
