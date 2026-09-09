# dws contract import batch

kind: command
completeness: full
usage: dws contract import batch
description: 从钉盘模版文件创建批量导入任务
example: dws contract import batch --file-id "123456" --space-id "7890" --format json
source: internal/helpers/contract.go:200
visible_flags: 2

## Flags
- --file-id <String>: 钉盘批量导入模版文件的 fileId（必填）；勿使用 -f 简写，与全局 --format/-f 冲突
- --space-id (-s) <String>: 模版文件所在钉盘空间的 spaceId（必填）

## Related
- dws contract import batch-result
