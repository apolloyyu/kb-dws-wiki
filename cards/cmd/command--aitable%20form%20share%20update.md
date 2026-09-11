# dws aitable form share update

kind: command
completeness: partial
usage: dws aitable form share update
description: 更新分享表单配置
example: dws aitable form share update --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --enabled true
source: internal/helpers/aitable.go:6568
visible_flags: 16
partial_reason: too_many_flags:16

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID (必填)
- --enabled <String>: 分享开关：true 开启，false 关闭
- --auth-type-code <Int>: 授权类型 code：0 企业内成员，1 钉钉用户，2 指定成员，3/4/5 为教育业务
- --auth-data <String>: 授权内容；auth-type-code=2 时为逗号分隔的成员 ID
- --submit-times-limit <Int>: 所有人合计提交次数上限，0 通常表示不限制
- --submit-times-user-limit <Int>: 单用户提交限制 code：0 不限制，1 仅一次，2 每天一次，3 每周期一次
- … 8 more; use dwsdoc cmd/short for full flags

## Related
- dws aitable form share get
- dws aitable form share notify
