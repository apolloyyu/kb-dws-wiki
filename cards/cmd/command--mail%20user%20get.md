# dws mail user get

kind: command
completeness: partial
usage: dws mail user get
description: —
source: internal/helpers/mail_user.go:16
visible_flags: 1
partial_reason: missing_description

## Flags
- --org-email <String> required: 待查询员工的完整企业邮箱 (必填)，不自动补全域名或转换别名

## Related
- dws mail user batch-get
- dws mail user search
