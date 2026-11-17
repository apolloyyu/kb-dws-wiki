# dws dev liteapp update

kind: command
completeness: partial
usage: dws dev liteapp update <unifiedAppId>
description: —
source: internal/helpers/dev_liteapp.go:175
visible_flags: 6
partial_reason: missing_description

## Flags
- --name <String>: 应用名称；不传=不修改，空串拒绝
- --homepage-url <String>: 移动端首页地址；不传=不修改，空串拒绝
- --pc-url <String>: PC 端首页地址；不传=不修改，空串拒绝
- --desc <String>: 应用描述；不传=不修改，空串拒绝
- --icon-media-id <String>: 图标文件 media_id；不接受 http 地址；不传=不修改
- --redirect-uris <String>: OAuth 回调地址列表，逗号分隔；不传=不修改，传入=整体覆盖

## Related
- dws dev liteapp create
- dws dev liteapp credential
- dws dev liteapp delete
- dws dev liteapp detail
- dws dev liteapp list
