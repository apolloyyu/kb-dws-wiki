# dws aitable +workflow-enable

kind: shortcut
completeness: full
usage: dws aitable +workflow-enable
description: 启用指定 Base 中的自动化工作流
source: internal/shortcut/aitable/aitable.go:1988
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
