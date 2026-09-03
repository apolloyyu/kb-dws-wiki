# dws aitable workflow create

kind: command
completeness: full
usage: dws aitable workflow create
description: 创建并发布自动化工作流
example: dws aitable workflow create --base-id BASE_ID --dsl @workflow.json --locale zh-CN
source: internal/helpers/aitable.go:5701
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --dsl <String>: workflow-dsl/v1 JSON 对象；支持内联 JSON、@文件路径或 - 从 stdin 读取 (必填)
- --locale <String>: 请求语言，例如 zh-CN 或 zh_CN (可选)

## Related
- dws aitable workflow disable
- dws aitable workflow edit-example
- dws aitable workflow enable
- dws aitable workflow get
- dws aitable workflow history
- dws aitable workflow list
