---
title: 认证重置与恢复的作用域
maintenance: manual
intents: auth_recovery
triggers: dws auth, auth login, auth reset, 登录态, 认证服务, profile, keychain
---

# 认证重置与恢复的作用域
- 旧凭据需重新授权的专门错误码，只证明客户端将该返回分类为 requiresReauthorization；不能由错误文案推断服务端协议升级、Token格式变更或排除服务端缺陷。先按可核验分类给恢复建议；用户已重登仍复现时，应继续核对同次调用与版本，不重复承诺登录必能修复。
  {{code: internal/auth/oauth_helpers.go | const legacyMCPRefreshRejectedCode = "invalidParameter.authCode.notFound"}}
  {{code: internal/auth/oauth_helpers.go | return strings.TrimSpace(e.Code) == legacyMCPRefreshRejectedCode}}
- 重新授权保留指定身份须显式携带该身份的 profile；不要保证裸 login 一定保留原身份。退出命令也有范围：裸 logout 默认退出全部账号；组织选择器退出该组织全部账号，精确账号或本地 profile 名才限制为一个账号。恢复单个账号不应建议裸 logout。
  {{code: internal/app/auth_command.go | targetCorpID, historyProfileSelector, historyProfileSelectorExplicit, err := resolveAuthLoginTarget}}
  {{code: internal/app/auth_command.go | 默认退出全部账号。--profile 传组织时退出该组织全部账号}}
- auth status 的 refresh_token_valid 由 IsRefreshTokenValid 计算，包含时间比较，不是只检查数据存在。普通 status 在 access token 失效而 refresh token 有效时会尝试刷新；readonly 模式不刷新。
  {{code: internal/app/auth_command.go | resp.RefreshTokenValid = data.IsRefreshTokenValid()}}
  {{code: internal/auth/token.go | return time.Now().Before(t.RefreshExpAt)}}
  {{code: internal/app/auth_command.go | if !data.IsAccessTokenValid() && data.IsRefreshTokenValid()}}
  {{code: internal/app/auth_command.go | 使用 --readonly 只读本地快照，不获取认证锁}}
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
