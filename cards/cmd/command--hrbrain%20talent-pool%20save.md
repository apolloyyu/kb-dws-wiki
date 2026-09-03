# dws hrbrain talent-pool save

kind: command
completeness: full
usage: dws hrbrain talent-pool save
description: 创建或更新人才池
example: dws hrbrain talent-pool save --pool-name "储备干部池"
source: internal/helpers/hrbrain.go:243
visible_flags: 5

## Flags
- --pool-name <String>: 人才池名称 (必填)
- --pool-code <String>: 人才池编码；更新时传入，新建时留空 (可选)
- --pool-desc <String>: 人才池描述 (可选)
- --rule-json <String>: 自动出入池规则 JSON 对象字符串 (可选)
- --pool-tags <String>: 人才池标识 JSON 数组 (可选)

## Related
- dws hrbrain talent-pool detail
- dws hrbrain talent-pool employees
- dws hrbrain talent-pool list
- dws hrbrain talent-pool move-members
