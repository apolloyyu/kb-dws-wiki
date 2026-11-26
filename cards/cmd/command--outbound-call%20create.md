# dws outbound-call create

kind: command
completeness: partial
usage: dws outbound-call create
description: —
source: internal/helpers/outbound_call.go:89
visible_flags: 3
partial_reason: missing_description

## Flags
- --callee <String> required: 被呼叫人的钉钉 userId，原样发送给服务端
- --task <String> required: 完整外呼任务说明，必须按顺序填写【角色】、【任务流程】、【话术示例】、【重要注意事项】，标签独立成行、段落间留空行，保留实际换行并作为一个参数值传入，不能仅传一句任务目标。角色说明 AI 助手身份、目标和语气；任务流程先写总览，再写节点与异常处理；话术示例按场景填写；无额外注意事项时保留标签、正文留空
- --opening <String> required: 外呼开场白，包含问好、明确的 AI 助手身份和来电目的，以任务相关问句结尾；须与 --task 的任务流程节点一、话术示例中的两处开场白逐字一致，不得冒充真人

## Related
- dws outbound-call detail
