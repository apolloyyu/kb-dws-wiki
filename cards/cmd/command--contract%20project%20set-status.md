# dws contract project set-status

kind: command
completeness: full
usage: dws contract project set-status
description: 更新项目状态
example: dws contract project set-status --project-id 1001 --status "active" --format json
source: internal/helpers/contract.go:872
visible_flags: 2

## Flags
- --project-id <Int64>: 项目 ID（必填）
- --status <String>: 项目状态（必填）

## Related
- dws contract project add
- dws contract project delete
- dws contract project detail
- dws contract project digests
- dws contract project export
- dws contract project import
