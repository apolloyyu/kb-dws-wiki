# dws sheet batch-set-style

kind: command
completeness: full
description: 批量设置样式（服务端原子事务）
source: internal/helpers/sheet_style.go:594
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --ranges <String>: Sheet2!D1:D10
- --batch <String>: 批次配置 JSON 文件路径（与 --ranges 二选一，每项可用不同样式）
- --continue-on-error <Bool>: 遇到失败时继续执行其余项（默认严格事务，整批回滚）

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
- dws sheet copy
