# dws aitable +dashboard-share-update

kind: shortcut
completeness: full
description: 开启/关闭 dashboard 分享并可设置分享类型
source: internal/shortcut/aitable/aitable.go:2332
visible_flags: 5

## Flags
- --base-id <String>: Base ID
- --dashboard-id <String>: Dashboard ID
- --enabled <Bool>: 是否开启分享
- --share-type <String>: 分享类型（仅开启时生效）
- --allow-back-to-doc <Bool>: 是否允许回到文档（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
