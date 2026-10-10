# dws recruit job list

kind: command
completeness: partial
usage: dws recruit job list
description: —
source: internal/helpers/recruit.go:91
visible_flags: 12
partial_reason: missing_description

## Flags
- --job-ids <StringSlice>: 职位 ID，多个值用逗号分隔
- --required-edu <Int>: 学历要求枚举值
- --status <String>: 职位状态：draft/open/invalid/closed，多个值用逗号分隔
- --job-nature <String>: 职位性质
- --campus <Bool>: 是否为校园招聘
- --start-modified-time <String>: 修改时间范围起点
- --end-modified-time <String>: 修改时间范围终点
- --creator-user-ids <StringSlice>: 创建人 userId，多个值用逗号分隔
- … 4 more; use dwsdoc cmd/short for full flags

## Related
- dws recruit job create
- dws recruit job get
