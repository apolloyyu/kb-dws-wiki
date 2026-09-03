# dws aitable +section-create

kind: shortcut
completeness: full
usage: dws aitable +section-create
description: 在指定 Base 下创建文件夹（组织 table / dashboard）
source: internal/shortcut/aitable/aitable.go:2917
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --name <String>: 文件夹名称
- --parent-section-id <String>: 父文件夹 ID，空表示根目录（可选）
- --index <Int>: —

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
