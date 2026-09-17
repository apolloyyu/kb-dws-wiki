# dws aitable import upload

kind: command
completeness: full
usage: dws aitable import upload
description: Request an upload ticket for an import file (Excel/CSV) to be staged before calling import data.
example: dws aitable import upload --base-id BASE_ID --file-name data.xlsx --file-size 204800
use_when: When the agent needs to push a local dataset into a Base and must first stage the file.
source: internal/helpers/aitable.go:8885
visible_flags: 4

## Flags
- --base-id <String>: Base ID (必填)
- --file-name <String>: 文件名，须带扩展名，如 data.xlsx (必填)
- --file-size <Int64>: 文件大小（字节数）(必填)
- --table-names <StringSlice>: 可选，指定要导入的 Sheet 名称列表（逗号分隔）；不传则导入文件内所有 Sheet

## Related
- dws aitable import data
