# dws aitable import upload

kind: command
completeness: full
description: Request an upload ticket for an import file (Excel/CSV) to be staged before calling import data.
use_when: When the agent needs to push a local dataset into a Base and must first stage the file.
source: internal/helpers/aitable.go:3701
visible_flags: 4

## Flags
- --base-id <String>: Base ID，可通过 base list 或 base search 获取 (必填)
- --file-name <String>: 待上传的文件名，必须包含扩展名（如 report.xlsx、photo.png）(必填)
- --size <Int64>: 文件大小（字节），必须大于 0 (必填)
- --mime-type <String>: 文件 MIME type（如 image/png），不传时根据扩展名推断

## Related
- dws aitable import data
