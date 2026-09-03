# dws chat category create-smart

kind: command
completeness: full
description: 创建智能会话分组
source: internal/helpers/chat.go:10821
visible_flags: 3

## Flags
- --name <String> required: 分组名称 (必填)
- --keywords <String>: 群名称关键词列表，逗号分隔（可选）
- --members <String>: 群内成员 openDingTalkId 列表，逗号分隔（可选）

## Related
- dws chat category add-conv
- dws chat category batch-info
- dws chat category create
- dws chat category delete
- dws chat category list
- dws chat category list-by-conv
