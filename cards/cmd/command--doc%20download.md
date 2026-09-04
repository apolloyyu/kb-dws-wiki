# dws doc download

kind: command
completeness: full
usage: dws doc download
description: Download a DingTalk Doc or file to a local path.
example: dws doc download --node NODE_ID --output ./download.bin
use_when: When the agent needs the raw file locally for processing or attachment.
source: internal/helpers/doc.go:2047
visible_flags: 2

## Flags
- --node <String> required: 文件节点 ID 或 URL (必填)
- --output <String> required: 本地保存路径 (文件路径或目录)

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc create
- dws doc delete
- dws doc export
