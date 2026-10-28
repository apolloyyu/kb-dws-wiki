# dws aitable +field-wait-ai

kind: shortcut
completeness: full
usage: dws aitable +field-wait-ai
description: 按本轮 taskId 和固定记录集合只读等待终态，结果可读尚未核实
source: internal/shortcut/aitable/ai_task_wait.go:23
visible_flags: 6

## Flags
- --base-id <String>: 本轮任务所属 Base ID
- --table-id <String>: 本轮任务所属 Table ID
- --tasks <String>: 本轮已受理的 1～10 项 JSON 数组；真实非空 taskId/fieldId 必填且字段不同，每项 recordIds 为 1～500 个不同非空 ID
- --checkpoint <String>: 可选私有持久检查点文件；绑定原始全部 tasks、账号组织、网关及目标，禁止覆盖
- --resume <Bool>: 从 checkpoint 恢复同一固定任务证据，只读续查未确认行
- --timeout <String>: —

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
