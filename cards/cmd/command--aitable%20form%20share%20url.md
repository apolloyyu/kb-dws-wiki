# dws aitable form share url

kind: command
completeness: full
usage: dws aitable form share url
description: 获取可复制的表单分享链接
example: dws aitable form share url --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID
source: internal/helpers/aitable.go:6448
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID (必填)
- --qr-file <String>: 二维码 PNG 输出相对路径，不覆盖已有文件

## Related
- dws aitable form share get
- dws aitable form share notify
- dws aitable form share update
