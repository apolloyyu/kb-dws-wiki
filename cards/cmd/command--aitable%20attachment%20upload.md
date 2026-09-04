# dws aitable attachment upload

kind: command
completeness: full
usage: dws aitable attachment upload
description: Request an upload ticket for attaching a file to an AI table attachment-type field. Returns an upload URL and token the caller uses to stream the file.
example: dws aitable attachment upload --base-id BASE_ID --file-name report.xlsx --size 204800
use_when: When the agent needs to attach binary assets (images, PDFs, etc.) to records before creating or updating an attachment field value.
source: internal/helpers/aitable.go:3713
visible_flags: 4

## Flags
- --base-id <String>: Base ID，可通过 base list 或 base search 获取 (必填)
- --file-name <String>: 待上传的文件名，必须包含扩展名（如 report.xlsx、photo.png）(必填)
- --size <Int64>: 文件大小（字节），必须大于 0 (必填)
- --mime-type <String>: 文件 MIME type（如 image/png），不传时根据扩展名推断

## Related
- none
