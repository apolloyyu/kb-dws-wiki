# dws aitable +workflow-deploy

kind: shortcut
completeness: full
usage: dws aitable +workflow-deploy
description: 创建或更新完整 workflow-dsl/v1，检查 valid/flowId；新建默认验证 STOP，--enable 验证 RUNNING
source: internal/shortcut/aitable/workflow_deploy.go:17
visible_flags: 5

## Flags
- --base-id <String>: Base ID
- --workflow-id <String>: 已有 Workflow ID；为空表示创建
- --dsl <String>: 完整 workflow-dsl/v1 JSON 对象
- --locale <String>: —
- --enable <Bool>: 发布后启用并从 workflow list 验证 RUNNING

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
