# dws aitable +read-batch

kind: shortcut
completeness: full
usage: dws aitable +read-batch
description: 集中执行 1～20 个独立只读查询，可显式启用最多 4 路并发
source: internal/shortcut/aitable/read_batch.go:21
visible_flags: 3

## Flags
- --base-id <String>: 固定 Base ID
- --requests <String>: 1～20 项只读请求 JSON，tool 和 arguments 必填
- --concurrency <String>: —

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
