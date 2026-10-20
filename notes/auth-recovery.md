---
title: 认证重置与恢复的作用域
maintenance: manual
intents: auth_recovery
triggers: dws auth, auth login, auth reset, 登录态, 认证服务, profile, keychain
contract:
  - 区分单 profile 退出、全量 reset、密钥迁移；恢复建议必须说明影响范围与前提，不将 reset 当无损重试。
---

# 认证重置与恢复的作用域
- `auth reset` 调用 DeleteAllTokenData，清理所有 profile 及旧格式 token 数据；还清理本地兼容入口、应用凭证和运行时缓存。即使带 profile，也不能把这条全量清理描述为仅重置当前用户。清理的是本机配置，不证明服务端令牌吊销。
  {{code: internal/app/auth_command.go | Use:               "reset"}}
  {{code: internal/app/auth_command.go | if err := authDeleteAllTokenData(configDir)}}
  {{code: internal/auth/token.go | DeleteAllTokenData removes all profile-scoped and legacy token data.}}
  {{code: internal/app/auth_command.go | authRemove(filepath.Join(configDir, "mcp_url"))}}
  {{code: internal/app/auth_command.go | if err := authDeleteAppConfig(configDir)}}
  {{code: internal/app/auth_command.go | ResetRuntimeTokenCache()}}
  {{code: internal/app/auth_command.go | clearCompatCache()}}
- 密钥不匹配先恢复或统一原登录密钥；确认旧登录态不可恢复后才建议 reset 并重新登录。macOS 从系统 Keychain 迁移到 file-DEK，源码提供先 dry-run 预检、通过后加 --yes 的路径；不能把所有认证错误都直接归因于 token 过期。
  {{code: internal/app/auth_command.go | 请先恢复或统一原登录密钥；确认旧登录态不可恢复后}}
  {{code: internal/app/auth_command.go | env -u DWS_DISABLE_KEYCHAIN dws auth migrate-keychain --to file-dek --dry-run}}
