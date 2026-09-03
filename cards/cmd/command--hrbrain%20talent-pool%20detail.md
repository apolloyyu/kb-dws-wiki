# dws hrbrain talent-pool detail

kind: command
completeness: full
usage: dws hrbrain talent-pool detail
description: 获取人才池详情
example: dws hrbrain talent-pool detail --pool-code POOL_CODE
source: internal/helpers/hrbrain.go:140
visible_flags: 1

## Flags
- --pool-code <String>: 人才池编码 (必填)

## Related
- dws hrbrain talent-pool employees
- dws hrbrain talent-pool list
- dws hrbrain talent-pool move-members
- dws hrbrain talent-pool save
