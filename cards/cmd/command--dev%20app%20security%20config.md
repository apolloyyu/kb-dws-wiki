# dws dev app security config

kind: command
completeness: partial
usage: dws dev app security config
description: —
source: internal/helpers/devapp.go:1136
visible_flags: 4
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --ip-whitelist <String>: 出口 IP 白名单，多个用逗号或分号分隔（整组覆盖，非追加）
- --redirect-urls <String>: 登录重定向 URL，多个用逗号或分号分隔（整组覆盖，非追加）
- --sso-urls <String>: 端内免登地址，多个用逗号或分号分隔（整组覆盖，非追加）

## Related
- none
