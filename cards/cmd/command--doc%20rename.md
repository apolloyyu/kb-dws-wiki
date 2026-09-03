# dws doc rename

kind: command
completeness: full
usage: dws doc rename
description: Rename a DingTalk Doc or file.
example: dws doc rename --node DOC_ID --name "新名称"
use_when: When the agent needs to change a document's title without altering its contents or location.
source: internal/helpers/doc.go:2561
visible_flags: 2

## Flags
- --node <String>: 文档/文件 ID 或 URL (必填)
- --name <String>: 新名称 (必填；原样传给服务端，不做扩展名规范化；如需根据节点类型和当前后缀规范化，请使用 drive rename)

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
