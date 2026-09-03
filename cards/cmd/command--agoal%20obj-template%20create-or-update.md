# dws agoal obj-template create-or-update

kind: command
completeness: full
description: 新增或更新目标模板
source: internal/helpers/agoal.go:553
visible_flags: 7

## Flags
- --request-id <String>: requestId (可选)
- --template-id <String>: 模板 id (更新时必填)
- --title <String>: 模板标题 (新增时必填)
- --objective-weight <Bool>: 是否启用目标权重
- --dimension-weight <Bool>: 是否启用维度权重
- --compute-by-weight <Bool>: 维度是否参与计算
- --dimensions <String>: 模板关联的维度 JSON 字符串 (必填，更新时基于老数据修改，新增时建议参考已有模板)

## Related
- dws agoal obj-template list
