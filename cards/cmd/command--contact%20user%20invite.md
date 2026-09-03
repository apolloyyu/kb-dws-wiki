# dws contact user invite

kind: command
completeness: full
usage: dws contact user invite
description: Invite one employee by mobile number into the current enterprise.
example: dws contact user invite --org-user-name "张三" --org-user-mobile "13800138000" --depts '[{"deptId":1}]'
use_when: When the user explicitly asks to add an employee and has supplied the employee name and mobile number.
source: internal/helpers/contact.go:1999
visible_flags: 3

## Flags
- --org-user-name <String>: 员工在企业内的名称 (必填)
- --org-user-mobile <String>: 员工手机号 (必填)
- --depts <String>: 员工所属部门列表 JSON 数组（可选），格式: [{\"deptId\":1}]

## Related
- dws contact user dismission
- dws contact user get
- dws contact user get-self
- dws contact user profile
- dws contact user search
- dws contact user search-mobile
