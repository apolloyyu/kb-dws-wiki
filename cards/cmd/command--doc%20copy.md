# dws doc copy

kind: command
completeness: full
usage: dws doc copy
description: Copy an existing DingTalk Doc or file to a specified destination folder.
example: dws doc copy --node DOC_ID --folder TARGET_DOC_FOLDER_NODE_ID
use_when: When the agent needs to duplicate a template document into a new location for reuse.
source: internal/helpers/doc.go:2452
visible_flags: 3

## Flags
- --node <String>: 文档/文件 ID 或 URL (必填)
- --folder <String>: 目标文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 目标知识库 ID 或 URL (不传 --folder 时复制到该知识库根目录)

## Related
- dws doc block
- dws doc comment
- dws doc create
- dws doc delete
- dws doc download
- dws doc export
