# dws aitable +record-upsert-by-key

kind: shortcut
completeness: full
usage: dws aitable +record-upsert-by-key
description: 按唯一字段值有则更新、无则创建记录，并读回验证
source: internal/shortcut/aitable/record_upsert_by_key.go:25
visible_flags: 6

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --key-field-id <String>: 具有唯一语义的字段 ID
- --key-value <String>: 字符串键值；与 --key-value-json 二选一
- --key-value-json <String>: JSON 类型键值；与 --key-value 二选一
- --cells <String>: 要写入的 cells JSON 对象

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
