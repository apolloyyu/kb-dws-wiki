# dws sheet update

kind: command
completeness: full
description: 更新工作表属性
source: internal/helpers/sheet_workbook.go:241
visible_flags: 9

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --name <String>: 工作表新名称，最长 100 字符
- --title <String>: --name 的别名（兼容）
- --index <Int>: 工作表新位置索引，0-based
- --hidden <Bool>: 是否隐藏工作表 (true=隐藏, false=显示)
- --frozen-row-count <Int>: 冻结行数，0 表示取消冻结
- --frozen-column-count <Int>: 冻结列数，0 表示取消冻结
- --tab-color <String>: 工作表标签颜色，Hex 格式如 #FF0000；传空字符串清除颜色

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
