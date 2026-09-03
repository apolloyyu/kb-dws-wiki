# dws devapp +security-config

kind: shortcut
completeness: full
usage: dws devapp +security-config
description: 更新开放平台应用安全配置（整组覆盖，非追加）
source: internal/shortcut/devapp/devapp.go:1567
visible_flags: 4

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --ip-whitelist <StringSlice>: 出口 IP 白名单（整组覆盖）
- --redirect-urls <StringSlice>: 登录重定向 URL（整组覆盖）
- --sso-urls <StringSlice>: 端内免登地址（整组覆盖）

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
