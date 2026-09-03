# dws attendance +update-group-members

kind: shortcut
completeness: full
usage: dws attendance +update-group-members
description: 更新考勤组成员（增删考勤人员/部门/无需考勤人员）
source: internal/shortcut/attendance/attendance.go:1442
visible_flags: 7

## Flags
- --group-id <Int>: 考勤组 ID
- --add-users <StringSlice>: 添加考勤人员 userId 列表，逗号分隔，最多 20 个
- --remove-users <StringSlice>: 删除考勤人员 userId 列表，逗号分隔，最多 20 个
- --add-extra-users <StringSlice>: 添加无需考勤人员 userId 列表，逗号分隔，最多 20 个
- --remove-extra-users <StringSlice>: 删除无需考勤成员 userId 列表，逗号分隔，最多 20 个
- --add-depts <StringSlice>: 添加考勤部门 ID 列表，逗号分隔（全公司根部门 id 为 -1）
- --remove-depts <StringSlice>: 删除考勤部门 ID 列表，逗号分隔（全公司根部门 id 为 -1）

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
