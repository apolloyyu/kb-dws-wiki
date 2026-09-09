# dws contact account update

kind: command
completeness: partial
usage: dws contact account update
description: 更新企业账号用户信息
example: dws contact account update --user-id user001 --org-user-name "张三"
source: internal/helpers/contact.go:846
visible_flags: 6
partial_reason: unverified_flags

## Flags
- --org-user-name <String>: 企业账号在企业内的员工姓名（可选）
- --depts <String>: 部门列表 JSON 数组（可选），格式: [{\"deptId\":1}]
- --master-user-id <String>: 直属主管 userId（可选）
- --nick <String>: 企业账号自身昵称（可选）
- --avatar-file-id <String>: 企业账号头像在钉盘的 fileId（可选）
- --staff-id <String>: 企业账号的员工 userid (必填)

## Related
- dws contact account create
