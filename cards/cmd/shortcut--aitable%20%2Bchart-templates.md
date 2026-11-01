# dws aitable +chart-templates

kind: shortcut
completeness: full
usage: dws aitable +chart-templates
description: 解析 JSONC 模板，只输出指定图表类型的结构化配置
source: internal/shortcut/aitable/chart_templates.go:18
visible_flags: 2

## Flags
- --chart-types <StringSlice>: 需要的图表类型，使用大写 chartType，多个用逗号分隔
- --server-filter <Bool>: 默认发现能力后优先按类型读取；false 强制全量 JSONC 客户端投影，true 显式选择新接口

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
