# dws aitable +attachment-upload

kind: shortcut
completeness: full
description: 为 attachment 字段申请 OSS 直传地址（uploadUrl / fileToken）
source: internal/shortcut/aitable/aitable.go:1145
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --file-name <String>: 文件名（含扩展名）
- --size <Int>: 文件大小（字节），须 > 0
- --mime-type <String>: MIME type，如 image/png（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +base-bootstrap
- dws aitable +base-copy
