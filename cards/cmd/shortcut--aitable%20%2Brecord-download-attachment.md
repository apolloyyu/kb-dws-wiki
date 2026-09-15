# dws aitable +record-download-attachment

kind: shortcut
completeness: full
usage: dws aitable +record-download-attachment
description: 按记录单元格中的准确 resourceId 下载附件，校验字节数并返回 SHA256
source: internal/shortcut/aitable/parity_attachment_download.go:13
visible_flags: 6

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-id <String>: 准确记录 ID
- --field-id <String>: 附件字段 ID
- --resource-id <String>: 同一附件单元格中的准确 resourceId
- --output <String>: 工作目录内相对路径，不覆盖已有文件

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
