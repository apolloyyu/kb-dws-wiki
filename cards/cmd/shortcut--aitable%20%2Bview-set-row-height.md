# dws aitable +view-set-row-height

kind: shortcut
completeness: full
usage: dws aitable +view-set-row-height
description: 设置视图单元格行高（像素，合法档位 32/56/88/128）
source: internal/shortcut/aitable/aitable.go:1582
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --view-id <String>: View ID
- --cell-height <Int>: 单元格高度（像素），须 > 0

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
