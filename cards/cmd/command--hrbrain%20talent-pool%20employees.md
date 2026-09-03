# dws hrbrain talent-pool employees

kind: command
completeness: full
description: 人才池人员列表
source: internal/helpers/hrbrain.go:186
visible_flags: 3

## Flags
- --pool-code <String>: 人才池编码 (必填)
- --page <Int>: 当前页码 (默认 1)
- --page-size <Int>: 每页条数 (默认 20)

## Related
- dws hrbrain talent-pool detail
- dws hrbrain talent-pool list
- dws hrbrain talent-pool move-members
- dws hrbrain talent-pool save
