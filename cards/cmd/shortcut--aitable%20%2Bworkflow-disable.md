# dws aitable +workflow-disable

kind: shortcut
completeness: full
description: 禁用指定 Base 中的自动化工作流（影响业务自动化）
source: internal/shortcut/aitable/aitable.go:2009
visible_flags: 2

## Flags
- --base-id <String>: Base ID
- --workflow-id <String>: Workflow ID

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
