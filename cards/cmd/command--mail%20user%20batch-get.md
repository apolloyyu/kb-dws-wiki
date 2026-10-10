# dws mail user batch-get

kind: command
completeness: partial
usage: dws mail user batch-get
description: —
source: internal/helpers/mail_user.go:83
visible_flags: 1
partial_reason: missing_description

## Flags
- --org-emails <StringSlice> required: 1 至 100 个完整企业邮箱，逗号分隔或重复传入 (必填)；上限按去重前数量计算，单项错误不丢弃其他结果

## Related
- dws mail user get
- dws mail user search
