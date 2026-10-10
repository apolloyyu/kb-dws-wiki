# dws oa approval template update

kind: command
completeness: partial
usage: dws oa approval template update
description: —
source: internal/helpers/oa.go:2431
visible_flags: 8
partial_reason: unverified_flags,missing_description

## Flags
- --from-document <String>: 完整模板配置 JSON 文档的绝对路径；与逐项配置互斥（更新可额外指定 process-code）
- --name <String>: 模板名称（未提供 --from-document 时必填）
- --description <String>: 模板描述；不传则创建使用默认值/更新沿用已有；显式空字符串提交清空
- --icon-url <String>: 图标链接或内置标识，如 collection；不传则沿用默认或已有值
- --static-workflow <String>: 流程类型：1 静态，0 动态；更新不传沿用已有(可选: 0|1)
- --append-enable <String>: 是否支持加签：y 支持，n 不支持；更新不传沿用已有(可选: y|n)
- --duplicate-removal <String>: 审批人去重：true 去重，false 不去重；更新不传沿用已有(可选: true|false)
- --process-code <String>: 要更新的审批模板 code（从 template detail 获取）

## Related
- dws oa approval template create
- dws oa approval template detail
- dws oa approval template list
