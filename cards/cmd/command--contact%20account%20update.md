# dws contact account update

kind: command
completeness: partial
usage: dws contact account update
description: 更新企业账号用户信息
example: dws contact account update --user-id user001 --org-user-name "张三"
source: internal/helpers/contact.go:844
visible_flags: 8
partial_reason: unverified_flags,empty_flag_name

## Flags
- --org-user-name <String>: 企业账号在企业内的员工姓名（可选）
- --depts <String>: 部门列表 JSON 数组（可选），格式: [{\"deptId\":1}]
- --master-user-id <String>: 直属主管 userId（可选）
- --nick <String>: 企业账号自身昵称（可选）
- --avatar-file-id <String>: 企业账号头像在钉盘的 fileId（可选）
- --ids <String>: 用户 ID 列表
- --names <String>: 角色名称，逗号分隔
- --dept <String>: 部门 ID

## Related
- dws contact account create
