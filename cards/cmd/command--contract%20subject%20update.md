# dws contract subject update

kind: command
completeness: full
usage: dws contract subject update
description: 修改相对方
example: dws contract subject update --file ./subject_update.json --format json
source: internal/helpers/contract.go:1275
visible_flags: 1

## Flags
- --file <String>: UpdateSubjectOpenRequest JSON 文件路径，\"-\" 表示 stdin（必填）

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject batch-delete
- dws contract subject delete
- dws contract subject detail
