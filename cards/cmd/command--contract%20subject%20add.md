# dws contract subject add

kind: command
completeness: full
usage: dws contract subject add
description: 添加相对方
example: dws contract subject add --file ./subject.json --format json
source: internal/helpers/contract.go:1188
visible_flags: 1

## Flags
- --file <String>: AddSubjectOpenRequest JSON 文件路径，\"-\" 表示 stdin（必填）

## Related
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject batch-delete
- dws contract subject delete
- dws contract subject detail
- dws contract subject detect-risk
