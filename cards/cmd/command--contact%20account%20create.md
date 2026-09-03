# dws contact account create

kind: command
completeness: full
usage: dws contact account create
description: Create a dedicated login account in the current enterprise.
example: dws contact account create --org-user-name "张三" --login-id "zhangsan001" --org-user-mobile "13800138000" --email "zhangsan@example.com" --dept-ids "1,2,3" --send-pwd-via-sms
use_when: When the user explicitly asks for an enterprise account or login account, rather than a new enterprise organization.
source: internal/helpers/contact.go:2389
visible_flags: 6

## Flags
- --org-user-name <String>: 员工在企业内的名称 (必填)
- --login-id <String>: 登录号 (必填)，请勿包含手机号
- --org-user-mobile <String>: 员工手机号（可选）
- --email <String>: 邮箱（可选）
- --dept-ids <String>: 要加入的部门 ID 列表，逗号分隔（可选）
- --send-pwd-via-sms <Bool>: 是否通过手机短信/邮件发送登录邀请（可选）

## Related
- dws contact account update
