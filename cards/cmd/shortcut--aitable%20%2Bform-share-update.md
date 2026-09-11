# dws aitable +form-share-update

kind: shortcut
completeness: partial
usage: dws aitable +form-share-update
description: 部分更新分享表单的开关、访问范围、有效期和通知等配置
source: internal/shortcut/aitable/aitable.go:1994
visible_flags: 16
partial_reason: too_many_flags:16

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --view-id <String>: View ID
- --enabled <String>: 分享开关
- --auth-type-code <Int>: 授权类型 code：0 企业内成员，1 钉钉用户，2 指定成员，3/4/5 为教育业务
- --auth-data <String>: 授权内容；auth-type-code=2 时为逗号分隔的成员 ID
- --submit-times-limit <Int>: 所有人合计提交次数上限
- --submit-times-user-limit <Int>: 单用户提交限制 code：0 不限制，1 仅一次，2 每天一次，3 每周期一次
- … 8 more; use dwsdoc cmd/short for full flags

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
