---
title: AI 语音外呼回执与后续查询
source_refs: internal/helpers/outbound_call.go, internal/helpers/outbound_call_result.go, skills/mono/references/products/outbound-call.md, skills/multi/dingtalk-misc/references/outbound-call.md
---

# AI 语音外呼回执与后续查询

## 创建与查询的命令入口

发起新的钉钉语音外呼时，使用 `dws outbound-call create`，执行前说明将由 AI 助手代为通话。查询已有任务的进展或听记时，用 `dws outbound-call detail` 并传入原任务 ID。电话 DING 使用 `dws ding`。

发起前按[产品指南](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli/blob/0d2f0ffecc56f3f9f2a31e70612ef9d11d70e98e/skills/mono/references/products/outbound-call.md)准备四栏任务正文，将完整文本作为 `--task` 的一个参数。`--opening` 先问好，再说明 AI 助手身份和来电目的，以问题结尾，并与任务流程、话术示例里的开场逐字一致。用 `--dry-run` 预览，用户确认后用 `--yes` 发起。

## 按任务回执查询

`outbound_call_result.go` 在创建回执含有可识别的单一任务 ID 时，返回 `outcome=pending`，并将原始 ID 放入 `meta.operation.id`。操作状态 `accepted` 表示服务端已接受任务。通话进展要查详情，服务端返回的 `callStatus` 等字段是判断依据。

从 `meta.operation.next_command` 取得详情命令并沿用其中的 profile。如果命令里有 `TASK_ID`，使用 `meta.operation.id` 的原始值作为 `dws outbound-call detail --task-id` 的一个参数。命令的引号由生成回执的 CLI 按运行平台处理，跨平台传递时用原始值按目标环境传参。查询详情可附加 `--format json`。

{{code: internal/helpers/outbound_call_result.go | taskIDArg = "TASK_ID"}}

## 创建回执不确定时核对任务

创建返回 `submission_unknown` 时，先核对任务记录。找到原任务 ID 后再查详情。创建会真实发起外呼，自动重复提交可能给同一人拨打多次。缺少单一 ID 的业务回执也应保留供核对。

{{quote: docs/products/outbound-call.md | 已有 taskId 时使用 `detail` 查询}}
