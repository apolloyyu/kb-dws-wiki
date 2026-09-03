# dws hrbrain talent-pool move-members

kind: command
completeness: full
description: 人才池人员出入池
source: internal/helpers/hrbrain.go:331
visible_flags: 4

## Flags
- --pool-code <String>: 人才池编码 (必填)
- --opt-type <String>: 操作类型：ENTERING 入池 / LEAVING 出池 (必填)
- --staff-ids <String>: 出入池人员工号列表，逗号分隔 (必填)
- --remark <String>: 操作备注 (可选)

## Related
- dws hrbrain talent-pool detail
- dws hrbrain talent-pool employees
- dws hrbrain talent-pool list
- dws hrbrain talent-pool save
