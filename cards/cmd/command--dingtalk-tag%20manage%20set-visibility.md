# dws dingtalk-tag manage set-visibility

kind: command
completeness: partial
usage: dws dingtalk-tag manage set-visibility
description: —
source: internal/helpers/deap_agent.go:457
visible_flags: 4
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 数字员工 ID
- --visibility <String> required: 可见范围：ALL 表示本企业全员可见；PARTIAL 表示仅指定成员/部门可见（配合 --user-ids/--dept-ids）
- --user-ids <StringSlice>: 指定可见成员 userId，可重复或用英文逗号分隔；全量替换，未提供则清空成员维度
- --dept-ids <StringSlice>: 指定可见部门 ID，可重复或用英文逗号分隔；全量替换，未提供则清空部门维度

## Related
- dws dingtalk-tag manage create
- dws dingtalk-tag manage delete
- dws dingtalk-tag manage detail
- dws dingtalk-tag manage list
- dws dingtalk-tag manage login
- dws dingtalk-tag manage publish
