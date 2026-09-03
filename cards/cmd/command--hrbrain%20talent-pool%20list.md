# dws hrbrain talent-pool list

kind: command
completeness: full
description: 人才池列表
source: internal/helpers/hrbrain.go:64
visible_flags: 6

## Flags
- --keyword <String>: 人才池名称关键词 (可选)
- --pool-type <String>: 人才池类型 (可选)
- --creator <String>: 创建人 (可选)
- --labels <String>: 标签列表，逗号分隔 (可选)
- --page <Int>: 当前页码 (默认 1)
- --page-size <Int>: 每页条数 (默认 20)

## Related
- dws hrbrain talent-pool detail
- dws hrbrain talent-pool employees
- dws hrbrain talent-pool move-members
- dws hrbrain talent-pool save
