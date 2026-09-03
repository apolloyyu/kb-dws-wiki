# dws chat category create

kind: command
completeness: full
description: 创建群（支持内部群/外部群/普通群）
source: internal/helpers/chat.go:2905
visible_flags: 3

## Flags
- --name <String> required: 群名称 (必填)
- --users <String> required: 成员 userId 或 openDingTalkId（可混传），逗号分隔 (必填)
- --type <String>: 群类型: INTERNAL(内部群,默认)/EXTERNAL(外部群)/NORMAL(普通群)

## Related
- dws chat category add-conv
- dws chat category batch-info
- dws chat category create-smart
- dws chat category delete
- dws chat category list
- dws chat category list-by-conv
