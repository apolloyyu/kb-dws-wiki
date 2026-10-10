# dws dev app webapp config

kind: command
completeness: partial
usage: dws dev app webapp config
description: —
source: internal/helpers/devapp.go:849
visible_flags: 5
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --h5-page-type <String>: 网页应用生效端/页面类型
- --homepage-url <String>: 移动端首页地址
- --pc-homepage-url <String>: PC 端首页地址
- --omp-url <String>: 管理后台地址

## Related
- dws dev app webapp get
