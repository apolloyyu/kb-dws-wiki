# dws aitable +form-share-update

kind: shortcut
completeness: partial
usage: dws aitable +form-share-update
description: 部分更新分享表单配置，并返回经服务端回读和 CP 投影校验的真实终态
source: internal/shortcut/aitable/aitable.go:2025
visible_flags: 22
partial_reason: too_many_flags:22

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --view-id <String>: View ID
- --enabled <String>: 分享开关
- --auth-type-code <Int>: 授权类型 code：0 企业内成员，1 钉钉用户，2 指定成员，6 免登录，3/4/5 为教育业务
- --auth-data <String>: 指定成员：当前组织 userId，逗号分隔，1-100 人；不接受内部 uid；非指定成员模式可显式传空字符串清除残留授权，未传保持原值
- --submit-times-limit <Int>: 所有人合计提交次数上限
- --submit-times-user-limit <Int>: 单用户提交限制 code：0 不限制，1 仅一次，2 每天一次，3 每周期一次
- … 14 more; use dwsdoc cmd/short for full flags

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
