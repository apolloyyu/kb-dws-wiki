# dws aitable entity search

kind: command
completeness: full
usage: dws aitable entity search
description: 搜索实体候选，不自动选择重名或模糊结果
example: dws aitable entity search --entity-type DEPARTMENT --keyword "客户成功部"
source: internal/helpers/aitable_entity_filter.go:54
visible_flags: 2

## Flags
- --entity-type <String> required: 实体类型：PERSON、DEPARTMENT 或 GROUP (必填)
- --keyword <String> required: 人员、部门或群组显示名称关键词，最长 100 个字符 (必填)

## Related
- none
