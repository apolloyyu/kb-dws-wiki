# dws aitable +attachment-remove

kind: shortcut
completeness: full
usage: dws aitable +attachment-remove
description: 清空 attachment 字段或按文件名解析 resourceId 删除，并读回验证
source: internal/shortcut/aitable/attachment_composite.go:68
visible_flags: 7

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-id <String>: Record ID
- --field-id <String>: attachment Field ID
- --remove-name <String>: 移除精确文件名的所有匹配项；与 --resource-ids 或 --clear-all=true 三选一
- --resource-ids <StringSlice>: 精确 resourceId 列表；与非空 remove-name 或 clear-all=true 互斥
- --clear-all <Bool>: true 时清空该字段全部附件；与 --remove-name 或 --resource-ids 三选一；false 不选择清空

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
- dws aitable +base-copy
