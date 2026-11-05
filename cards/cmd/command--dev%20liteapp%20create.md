# dws dev liteapp create

kind: command
completeness: partial
usage: dws dev liteapp create
description: —
source: internal/helpers/dev_liteapp.go:128
visible_flags: 6
partial_reason: missing_description

## Flags
- --name <String> required: 应用名称，必填，trim 后非空
- --homepage-url <String> required: 移动端首页地址，必填，http(s) URL
- --pc-url <String>: PC 端首页地址，可选，缺省取移动端首页地址
- --desc <String>: 应用描述，可选
- --icon-media-id <String>: 图标文件 media_id（logoImg 格式）；不接受 http 地址；不传自动生成默认图标
- --request-id <String>: 可选请求 ID；不传不保证幂等，传入后同键同参数重试返回首次结果、参数变化拒绝

## Related
- dws dev liteapp credential
- dws dev liteapp delete
- dws dev liteapp detail
- dws dev liteapp list
- dws dev liteapp update
