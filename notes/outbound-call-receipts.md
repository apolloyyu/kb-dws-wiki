---
title: AI 语音外呼回执与后续查询
source_refs: internal/helpers/outbound_call_result.go, skills/mono/references/products/outbound-call.md
---

# AI 语音外呼回执与后续查询

## 按任务回执查询

`outbound_call_result.go` 在创建回执含有可识别的单一任务 ID 时，返回 `outcome=pending`，并将原始 ID 放入 `meta.operation.id`。操作状态 `accepted` 表示服务端已接受任务。通话进展要查详情，服务端返回的 `callStatus` 等字段是判断依据。

从 `meta.operation.next_command` 取得详情命令并沿用其中的 profile。如果命令里有 `TASK_ID`，使用 `meta.operation.id` 的原始值作为 `dws outbound-call detail --task-id` 的一个参数。命令的引号由生成回执的 CLI 按运行平台处理，跨平台传递时用原始值按目标环境传参。查询详情可附加 `--format json`。

{{code: internal/helpers/outbound_call_result.go | taskIDArg = "TASK_ID"}}

## 创建回执不确定时核对任务

创建返回 `submission_unknown` 时，先核对任务记录。找到原任务 ID 后再查详情。创建会真实发起外呼，自动重复提交可能给同一人拨打多次。缺少单一 ID 的业务回执也应保留供核对。

{{quote: docs/products/outbound-call.md | 已有 taskId 时使用 `detail` 查询}}
