# dws smart +group-members

kind: shortcut
completeness: full
usage: dws smart +group-members
description: 按群名唯一解析后全量列出用户成员并公开分页完整性
source: internal/shortcut/smart/group_members.go:50
visible_flags: 5

## Flags
- --group <String>: 群名称（搜群关键词，用群名里连续的核心词）
- --cursor <String>: —
- --single-page <Bool>: 只读取一页用户成员，保留实际续页信息
- --page-delay <Int>: —
- --page-limit <Int>: —

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
