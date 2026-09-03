# dws aisearch person

kind: command
completeness: partial
usage: dws aisearch person
description: 搜索企业人员
example: dws aisearch person --query "张三" --dimension department
source: internal/helpers/aisearch.go:229
visible_flags: 1
partial_reason: unverified_flags,empty_flag_name

## Flags
- --dimension (-d) <String>: 查询维度: all/name/department/position/duty/supervisor/subordinate/phone/jobNumber，多个用逗号分隔

## Related
- dws aisearch behavior
- dws aisearch enterprise
