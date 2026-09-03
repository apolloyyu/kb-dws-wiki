# dws auth login

kind: command
completeness: full
description: 登录钉钉（自动刷新 token，必要时扫码）
source: internal/app/auth_command.go:116
visible_flags: 9

## Flags
- --token <String>: Access token
- --device <Bool>: Use device authorization flow
- --intl <Bool>: Use DingTalk international (.io) login and service endpoints
- --international <Bool>: Use DingTalk international (.io) login and service endpoints
- --pre-url <String>: Override pre-release login/MCP base URL for this login
- --mcp-url <String>: Override MCP base URL for this login
- --force <Bool>: 兼容保留；login 默认已忽略缓存并进入授权流程
- --recommend <Bool>: 登录成功后无交互批量授权服务端推荐权限
- --no-browser <Bool>: Suppress browser launch

## Related
- dws auth exchange
- dws auth logout
- dws auth migrate-keychain
- dws auth reset
- dws auth status
