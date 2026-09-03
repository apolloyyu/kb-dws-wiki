# dws doc whiteboard insert

kind: command
completeness: partial
description: 插入白板卡片
source: internal/helpers/doc_whiteboard.go:217
visible_flags: 6
partial_reason: empty_flag_name

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --ref-block <String>: 参照块 UUID（同级插入，配合 --where）
- --where <String>: 插入方向: before / after (默认 after，配合 --ref-block)
- --parent-block <String>: 父容器 UUID（容器内插入，与 --index 配合）
- --index <Int>: 位置索引 (从 0 开始)
- --yes <Bool>: 确认插入白板卡片

## Related
- none
