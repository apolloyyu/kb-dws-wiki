# dws aitable +task-report

kind: shortcut
completeness: full
usage: dws aitable +task-report
description: 离线汇总搭建或 AI 等待检查点的调用、等待和客户端模型统计
source: internal/shortcut/aitable/task_report.go:47
visible_flags: 4

## Flags
- --checkpoint <String>: —
- --baseline <String>: 可选基线检查点，只读对照，不修改文件
- --model-metrics <String>: 可选客户端指标 JSON：model/environment/inputDigest 必填，elapsedMs/outputBytes/interactions/reworkCount 可选非负整数
- --baseline-model-metrics <String>: 基线对应的客户端指标 JSON，需同时提供 baseline

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
