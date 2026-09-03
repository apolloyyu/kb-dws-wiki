# dws devapp +webapp-config

kind: shortcut
completeness: full
description: 配置网页应用能力
source: internal/shortcut/devapp/devapp.go:1028
visible_flags: 5

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --h5-page-type <String>: 网页应用生效端/页面类型；至少提供一项非空的网页应用配置
- --homepage-url <String>: 移动端首页地址；至少提供一项非空的网页应用配置
- --pc-homepage-url <String>: PC 端首页地址；至少提供一项非空的网页应用配置
- --omp-url <String>: 管理后台地址；至少提供一项非空的网页应用配置

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
