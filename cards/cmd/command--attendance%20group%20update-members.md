# dws attendance group update-members

kind: command
completeness: full
description: 更新考勤组成员（添加/删除考勤人员、部门、无需考勤人员）
source: internal/helpers/attendance.go:2328
visible_flags: 8

## Flags
- --group-id <Int64>: 考勤组 ID（必填）
- --add-users <String>: 添加考勤人员 userId 列表，逗号分隔，最多 20 个（可选）
- --remove-users <String>: 删除考勤人员 userId 列表，逗号分隔，最多 20 个（可选）
- --add-extra-users <String>: 添加无需考勤的人员 userId 列表，逗号分隔，最多 20 个（可选）
- --remove-extra-users <String>: 删除无需考勤的成员 userId 列表，逗号分隔，最多 20 个（可选）
- --add-depts <String>: 添加考勤部门 ID 列表，逗号分隔，最多 20 个（可选）
- --remove-depts <String>: 删除考勤部门 ID 列表，逗号分隔，最多 20 个（可选）
- --yes <Bool>: 跳过确认提示

## Related
- dws attendance group create
- dws attendance group filtered-get
- dws attendance group get
- dws attendance group search
- dws attendance group update
