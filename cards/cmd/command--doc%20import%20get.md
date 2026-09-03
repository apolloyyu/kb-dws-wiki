# dws doc import get

kind: command
completeness: full
usage: dws doc import get
description: 查询导入任务结果（手动兜底）
example: dws doc import get --task-id <TASK_ID> --workspace <WORKSPACE_ID>
source: internal/helpers/doc.go:4346
visible_flags: 3

## Flags
- --task-id <String>: 导入任务 ID (必填)
- --folder <String>: 原导入目标文件夹 ID 或 URL（completed 后落点验证需要）
- --workspace <String>: 原导入目标知识库 ID 或 URL（completed 后落点验证需要）

## Related
- none
