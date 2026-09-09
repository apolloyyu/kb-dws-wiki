# dws contract project import

kind: command
completeness: full
usage: dws contract project import
description: 批量导入项目
example: dws contract project import --file-id "abc123" --space-id 7890 --format json
source: internal/helpers/contract.go:1061
visible_flags: 5

## Flags
- --file-id <String>: 钉盘文件 ID（必填）
- --space-id <Int64>: 钉盘空间 ID
- --file-name <String>: 文件名称
- --file-type <String>: 文件类型
- --file-size <Int64>: 文件大小（字节）

## Related
- dws contract project add
- dws contract project delete
- dws contract project detail
- dws contract project digests
- dws contract project export
- dws contract project import-result
