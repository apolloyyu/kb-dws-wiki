# dws aitable +table-update

kind: shortcut
completeness: full
usage: dws aitable +table-update
description: 更新数据表名称 / 备注 / 行命名规则
source: internal/shortcut/aitable/aitable.go:492
visible_flags: 5

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --name <String>: 新表名（可选）
- --description <String>: 备注说明（可选）
- --record-name-key <String>: 行命名规则枚举键，如 task/project（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
