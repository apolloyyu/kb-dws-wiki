# dws contract subject import

kind: command
completeness: full
usage: dws contract subject import
description: 批量导入相对方
example: dws contract subject import --file-id "abc123" --space-id 7890 --format json
source: internal/helpers/contract.go:1474
visible_flags: 5

## Flags
- --file-id <String>: 钉盘文件 ID（必填）
- --space-id <Int64>: 钉盘空间 ID
- --file-name <String>: 文件名称
- --file-type <String>: 文件类型
- --file-size <Int64>: 文件大小（字节）

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject batch-delete
- dws contract subject delete
- dws contract subject detail
