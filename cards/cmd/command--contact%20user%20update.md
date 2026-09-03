# dws contact user update

kind: command
completeness: partial
usage: dws contact user update
description: 修改员工信息
example: dws contact user update --user-id user001 --org-user-name "张三三"
source: internal/helpers/contact.go:721
visible_flags: 4
partial_reason: unverified_flags

## Flags
- --user-id <String>: 要修改的员工 userId (必填)
- --org-user-name <String>: 员工在企业内的名称（可选）
- --depts <String>: 员工所属部门列表 JSON 数组（可选），格式: [{\"deptId\":1}]
- --master-user-id <String>: 直属主管 userId（可选）

## Related
- dws contact user dismission
- dws contact user get
- dws contact user get-self
- dws contact user invite
- dws contact user profile
- dws contact user search
