# dws aitable +charts-create

kind: shortcut
completeness: full
usage: dws aitable +charts-create
description: 一次编排 1～20 张图表并按真实 ID 验证完整配置与显式布局
source: internal/shortcut/aitable/chart_batch.go:20
visible_flags: 5

## Flags
- --base-id <String>: Base ID
- --dashboard-id <String>: Dashboard ID
- --charts <String>: 1～20 个完整 config/layout 的 JSON 数组；chartType 大写，布局显式声明
- --server-batch <Bool>: 默认发现能力后优先一次批建；false 强制串行，true 显式选择新接口；均不保证整批原子性
- --is-app-mode <Bool>: 已确认目标为应用模式时开启，用于核准根网格列数

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
