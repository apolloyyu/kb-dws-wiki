# dws mind create

kind: command
completeness: partial
usage: dws mind create
description: —
source: internal/helpers/mind.go:53
visible_flags: 5
partial_reason: missing_description

## Flags
- --name <String> required: 脑图名称，最多 128 个 UTF-16 单元（必填）
- --source <String> required: OpenNodes mind-v1 JSON 或 JSON 文件路径；远端调用前完成格式和树结构校验（必填）
- --request-id <String> required: 稳定幂等键；恢复必须复用（必填）
- --folder <String>: 目标文件夹节点 ID/URL
- --workspace <String>: 目标知识库 ID/URL

## Related
- dws mind node
