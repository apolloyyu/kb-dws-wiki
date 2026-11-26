# dws aitable +record-write-result

kind: shortcut
completeness: full
usage: dws aitable +record-write-result
description: 按原 clientToken 只读核对创建分组；未知结果不能作为重新创建依据
source: internal/shortcut/aitable/record_write_reconcile.go:180
visible_flags: 4

## Flags
- --base-id <String>: 原写入 Base ID
- --table-id <String>: 原写入 Table ID
- --client-token <String>: 原写入使用的 UUID v4
- --write-intent <String>: 原 upsert 写前保存的恢复文件，查询前校验原账号、端点与目标；checkpoint 已提供文件时首次查询必须带上，不得省略或查询后再补；没有原文件时才可省略

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
