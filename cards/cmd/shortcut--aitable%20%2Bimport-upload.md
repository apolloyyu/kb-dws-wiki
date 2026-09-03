# dws aitable +import-upload

kind: shortcut
completeness: full
usage: dws aitable +import-upload
description: 为导入任务申请 OSS 直传地址（uploadUrl / importId）
source: internal/shortcut/aitable/aitable.go:2626
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --file-name <String>: 文件名（含扩展名）
- --file-size <Int>: 文件大小（字节，必须大于 0）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
