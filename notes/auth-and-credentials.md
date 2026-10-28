---
title: 认证与凭证(auth / PAT / profile / 密钥存储)
source_refs: internal/app/auth_command.go, internal/auth/oauth_provider.go, internal/auth/device_flow.go, internal/auth/token.go, internal/auth/refresh_failure.go, internal/auth/filelock.go, internal/auth/keychain_store.go, internal/auth/profiles.go, internal/keychain/keychain.go, internal/keychain/file_dek.go, internal/keychain/keychain_linux.go, internal/keychain/keychain_windows.go, internal/pat/chmod.go, internal/pat/browser_policy.go, internal/profilectx/profile.go, internal/app/profile_command.go, internal/app/access_token_resolve.go, internal/transport/client.go, pkg/config/constants.go, internal/app/auth_provider_login.go, internal/app/auth_provider_hooks.go, internal/app/auth_oidc_exchange.go, internal/app/auth_oidc_stdin.go, internal/auth/oidc_provider.go, internal/auth/oidc_exchange.go, internal/auth/oidc_refresh.go, internal/auth/oidc_errors.go, internal/auth/oauth_helpers.go, internal/auth/external_exchange.go, internal/auth/endpoints.go, internal/auth/secret.go, pkg/edition/oidc.go, internal/output/emitter.go
---

# 认证与凭证(auth / PAT / profile / 密钥存储)

本文介绍登录方式、Token 结构与刷新、PAT、keychain 存储、profile 体系与凭证注入。

## 登录方式

登录命令为 `internal/app/auth_command.go` 的 `newAuthLoginCommand`:

- **默认 OAuth Loopback**:127.0.0.1 回调,`internal/auth/oauth_provider.go` 的 `OAuthProvider.Login` 先静默刷新,再打开浏览器;
- **`--device`**:使用 `DeviceFlowProvider`(`device_flow.go`),通过 user_code + 短 URL 轮询;
- **`--token`**:手动导入,有效期为 `config.ManualTokenExpiry` = 24h;
- **`--intl`**:走 `.io`(`LoginRegionInternational`)。
- **`auth provider-login <provider>`**:第三方 IdP 单点登录,隐藏命令,授权实现由 overlay 注册(见下节)。

## 第三方 OIDC 登录(provider-login / 分步换票)

三条命令都是第三方 IdP 集成入口,Cobra `Hidden: true`:不出现在 `dws auth --help` 与 shell 补全,也不进入 Agent Schema(Hidden 且未声明 Identity),但可显式执行。服务地址统一取 `GetMCPBaseURL()`(`mcp_url` 文件或默认地址),登录不修改端点配置。

- `dws auth provider-login <provider>`(`internal/app/auth_provider_login.go`):`<provider>` 为必填位置参数,默认登录超时 12 分钟(隐藏 flag `--login-timeout`);
- `dws auth exchange-prepare --provider <name>`(`internal/app/auth_oidc_exchange.go`):只创建事务并返回 `provider` / `expires_in` / `authorization_request`,不执行 SDK 登录、不保存或切换本地身份、不接受应用凭据;
- `dws auth token-exchange --provider <name> (--code <code> | --code-stdin) --state <state> [--save]`:默认只返回 TokenData 不落盘;`--save` 先在线核验完整身份再经 `persistExternalExchangeTokenWithSecret` 保存,并保留已有默认账号。两条分步命令走统一结果输出(`output.RolloutUnifiedActive`,`Safety` 为 write/medium/not_required/non_idempotent)、各自 1 分钟超时;`--client-id`/`--client-secret` 是根级 flag,必须成对出现且只属于 token-exchange。

授权实现由 overlay 通过 `edition.Hooks.OIDCProviders` 注册(`pkg/edition/oidc.go`):`OIDCProvider{Name, Authorize}`,`Name` 必须匹配 `[a-z][a-z0-9_-]{0,63}`;重复名称、空 `Authorize`、非法名称在 `resolveOIDCAuthorizer`(`internal/app/auth_provider_hooks.go`)中直接判为注册错误。核心只把 `authorization_endpoint` 和一份 `maps.Clone` 出来的参数 map 交给回调;SDK 会话、密码、DWS 换票用的 client secret 和 PKCE verifier 都不在回调的输入输出内,SDK 原始错误文本也不写日志或错误链。

执行顺序(`OIDCLoginProvider.Login`,`internal/auth/oidc_provider.go`):先 POST `/cli/auth/oidc/transactions` 建事务并校验(响应须 201、provider 一致、`expires_in` ∈ (0,600]、参数恰为 8 项且 `response_type=code`、`code_challenge_method=S256`、scope 含 `openid`、`nonce`/`code_challenge` 为 43 位 base64url、`redirect_uri` 为绝对 URL),再在受事务期限约束的 context 里调用回调。未注册实现时事务校验先跑,服务端接受 provider 后返回 `OIDC_SDK_UNAVAILABLE`;help 与 `--dry-run` 不枚举注册项、不初始化 SDK、不联网。回调返回的 code 须非空、≤8192 字节且无控制字符,state 用常量时间比较;授权失败、取消、超时或 state 不匹配都不触发其他 SDK/Mock 兜底,也不换票、不保存凭证。

换票 POST `/cli/auth/oidc/exchange`,body 为 `provider`/`code`/`state`,显式指定应用凭据时再加 `client_id`/`client_secret`。响应里的 DWS `clientId`(不同于 IdP 的 `client_id`)与 Portal 地址一起写入 token;显式 client_id 与响应 `clientId` 不一致时判为错误。Portal 传输统一禁止重定向(`http.ErrUseLastResponse`)、响应体上限 64KiB、拒绝重复 JSON 键、超时上限 15s。code/state 只兑换一次,失败不自动重试,`Exchange` 会把 hint 改成「重新 exchange-prepare 取码」(action 为 `stop` 时除外)。

`--code-stdin` 的等待输入与后续换票共享同一分钟超时;`readOIDCCodeInput`(`internal/app/auth_oidc_stdin.go`)读取上限 8192+3 字节,只去掉末尾一个换行(兼容 `\r\n`),取消/超时保留原有身份分类、不降级为参数错误,也不继续换票。

## Token 结构

`internal/auth/token.go` 定义 `TokenData`,字段包括 `AccessToken`、`RefreshToken`、`PersistentCode`、`ExpiresAt`、`RefreshExpAt`、`CorpID`/`UserID`、`ClientID`、`Source`、`LoginRegion`。

- `IsAccessTokenValid` 带 5 分钟提前量;
- 默认 access token 寿命 7200s(`pkg/config/constants.go`)。

OIDC 会话另存三个字段:`OIDCProvider`(`oidc_provider`,唯一的 OIDC 会话判别位,不再从 Portal 地址或密钥模式推断登录来源)、`MCPBaseURL`(`mcp_base_url`,刷新沿用的 Portal 地址)、`MCPClientSecretRequired`(`mcp_client_secret_required`,是否需要自带应用密钥)。密钥本身存应用 keychain 槽,不进这个 DTO。

## Token 刷新

`oauth_provider.go` 的 `GetTokenSnapshot` 提供快路径;过期且 refresh 有效时走 `lockedRefresh`:`AcquireDualLock`(进程锁 + 文件锁,`filelock.go`)双重检查后执行 `refreshWithRefreshToken`。

`refresh_failure.go` 的 `ClassifyRefreshFailure` 区分 transient / terminal;仅非瞬时失败才 `MarkProfileStatus(ProfileStatusExpired)`。

OIDC 会话(`OIDCProvider` 非空)在 `refreshWithRefreshToken` 入口先跑 `validateOIDCRefreshBinding`(`internal/auth/oidc_refresh.go`):要求 `Source == "mcp"`、合法 `ClientID`/`OIDCProvider` 与合法 `MCPBaseURL`,缺失即报错要求重登,不回退全局应用或默认端点。刷新请求发往 `MCPBaseURL + /oauth2/refreshToken`,`MCPClientSecretRequired` 时用 `LoadClientSecretStrict` 读密钥并放入 `clientSecret`,且走禁重定向的 `oidcJSONRequest` 以免密钥外泄;刷新成功后 OIDC 绑定字段原样保留。`lockedRefreshForProfile` 对 OIDC 会话跳过组织镜像兜底重试,刷新被拒时不读取组织镜像或历史全局凭证,即使同用户同组织也不切换应用。

## auth status

`newAuthStatusCommand` 读取 token,必要时刷新;失败时标记 expired 或清除(`AutoPurgeToken`)。诊断 reason 包括:`ciphertext_key_mismatch`、`dek_missing`、`keychain_unavailable`、`token_refresh_failed`。

## PAT(注意命名)

PAT 是 **Personal Action Token(行为授权)**,不是 Personal Access Token:

- `dws pat chmod <scope>...` 经服务端 MCP 工具批量授权,scope 不落本地(`chmod.go`);
- `dws pat browser-policy` 本地策略存 `<configDir>/pat_policy.json`(`browser_policy.go`);
- host-owned 模式(设置 `DINGTALK_DWS_AGENTCODE`)下,PAT 错误以 stderr JSON + exit=4 返回(`internal/errors/pat.go` `ExitCodePermission=4`)。

## keychain 存储

`internal/keychain/keychain.go`:`Service`=`"dws-cli"`,AES-256-GCM 加密。

| 平台 | 实现 |
|---|---|
| macOS | DEK 存系统 Keychain(go-keyring),密文在 `~/Library/Application Support/dws-cli`;`DWS_DISABLE_KEYCHAIN` 可回退 file-DEK |
| Linux | file-DEK(`file_dek.go`,`~/.local/share/dws-cli/dek`)+ `.enc` 文件(`keychain_linux.go`) |
| Windows | DPAPI + HKCU 注册表(`keychain_windows.go`) |

keychain 槽位(`internal/auth/keychain_store.go`):

- 全局:`auth-token`
- 组织:`auth-token:<corpId>`
- 身份:`auth-token:id:<sha256>`
- 应用密钥:canonical `appsecret:<clientId>`(`secret.go`),legacy `client-secret:<clientId>`;两者冲突时 `LoadClientSecretStrict` 返回 `ErrClientSecretConflict`

`token.json` 仅为标记(`TokenMarker`:`updated_at` / `revision`),不含凭证。

显式 DWS 应用密钥经 `saveClientSecretTransactional` 写入,与 token/profile 写入同处一个事务快照:任一步失败由 `restoreTokenPersistence` 一起回滚,legacy 槽清理失败不降级为成功。

## profile 体系

元数据存 `<configDir>/profiles.json`(`internal/auth/profiles.go` 的 `ProfilesConfig`:`currentProfile` / `primaryProfile` / `orgCurrentProfiles`;`Profile` 含 `corpId` / `userId` / `status`),token 本体在 keychain。

- 切换命令:`internal/app/profile_command.go` 的 `list` / `use` / `switch`;
- 运行时覆盖用进程内变量 `profilectx.Set` / `Get`(`internal/profilectx/profile.go`,`SetRuntimeProfile`);
- selector 形如 `corpId:userId`(`ParseIdentitySelector`);
- 配置目录默认 `~/.dws`,可被 `DWS_CONFIG_DIR` 覆盖(`pkg/config/constants.go` `DefaultConfigDir`)。

`token-exchange --save` 在写锁内以 `cfg.CurrentProfile` 作为持久化选择器,因此保存 OIDC 身份不会顶掉已有默认账号;首次保存(空沙箱)才会成为当前 profile。

## 凭证注入

- 无 token 环境变量注入;
- 显式 token 走 `--token`,`internal/app/access_token_resolve.go` 的 `TokenManager.Get`(`source="explicit"`);
- 请求注入 `Authorization: Bearer`(`internal/transport/client.go`)。

## 过期表现

- `ErrTokenDataNotFound` 提示 `no credentials found, run: dws auth login`;
- 刷新失败提示重新登录;refresh_token 过期有单独提示;
- profile 状态置 expired 后,`dws auth status` 显示未登录 + 原因。

OIDC 会话的刷新失败改由 `oidcRefreshReauthorizationError` 给出提示:重新执行 `dws auth provider-login <provider>` 或重复原 `exchange-prepare` / `token-exchange --save` 流程;`MCPClientSecretRequired` 时追加「沿用原 `--client-id`/`--client-secret`」。`ClassifyRefreshFailure` 判为 transient 的失败(网络、取消、超时等)原样返回错误并保留凭证,不强制重登。

OIDC 三条命令的 Portal 错误保留公开诊断(`internal/auth/oidc_errors.go` 的 `portalError`):从响应体 `error.code` / `error.action` / `trace_id` 解析,响应体缺失或无效时回退合法的 `X-Dws-Trace-Id` 头;后端日志专用的 `reason` 不进入客户端输出。已定义错误码转为固定可读文案(`oidcErrorMessage`,覆盖配置、事务/state、授权码、身份校验、限流、上游调用与 DWS 会话签发),未定义码统一为 `OIDC portal rejected the login request`;`action` 只接受 `stop` / `restart_login`,`stop` 提示检查参数与 provider/应用配置或带 Trace ID 联系管理员。诊断标识限长 256 且只允许 `[A-Za-z0-9._:-]`,与请求中的 code/state/client_secret 等凭据相同或包含其值时丢弃。错误标记为不可重试,分类与退出码不变。JSON 复用现有字段:传统输出 `error.server_error_code`,统一输出 `error.upstream_code`,两者均带 `error.trace_id` 与 `error.details.action`/`http_status`/`provider`;人类可读输出追加 `Trace ID` 与 `Server Code` 行(`internal/output/emitter.go`)。
