# dws contact user invite

kind: command
completeness: full
description: Invite one employee by mobile number into the current enterprise.
use_when: When the user explicitly asks to add an employee and has supplied the employee name and mobile number.
source: internal/helpers/contact.go:1999
visible_flags: 3

## Flags
- --org-user-name <String>: 员工在企业内的名称 (必填)
- --org-user-mobile <String>: 员工手机号 (必填)
- --depts <String>: 员工所属部门列表 JSON 数组（可选），格式: [{\"deptId\":1}]

## Related
- dws contact user get
- dws contact user get-self
- dws contact user search
- dws contact user search-mobile
- dws contact user update
- dws contact user update-ownness
