---
title: dws 登录态与 token 的有效期、登录等待时长
maintenance: manual
intents: lifetime
triggers: refresh_token, refresh token, refreshtoken, refreshexpires, refresh_expires, 登录态, 登录状态, dws auth, auth login, auth status, --token, --device, 设备码, 扫码登录, 重新登录, 重新扫码, 掉线
contract:
  - lifetime：下列时长都是 dws CLI 在本地写入或等待的值，只证明 CLI 怎么记录、等多久；服务端实际何时让 refresh_token 失效、刷新时是否续期，源码证明不了，回答须写明这一点，不得说成「钉钉规定」。
---

# dws 登录态与 token 的有效期

回答「登录态多久过期 / refresh_token 有效期 / 手动导入的 token 能用多久 / 扫码要在多久内确认」时以本篇为准。本篇只写判断;源码依据由每日构建核对,上游改了会提示「依据已变更」。

## 登录后 CLI 本地记录的到期时间

- **refresh_token:CLI 拿到 token 时把它的本地到期时间记为「当前时间 + 30 天」,每次刷新成功后同样重置为「刷新时刻 + 30 天」**。所以只要 30 天内有一次触发了刷新(access_token 失效后再执行任意命令),本地到期时间就会往后顺延。这是 CLI 写进本地凭证的值,不是从服务端读出来的;服务端是否同样续期、会不会提前让 refresh_token 失效,源码证明不了——服务端拒绝时 CLI 会报 refresh_token 已过期,需要重新登录。
  {{code: pkg/config/constants.go | DefaultRefreshTokenLifetime = 30 * 24 * time.Hour}}
  {{code: internal/auth/oauth_helpers.go | RefreshExpAt: now.Add(config.DefaultRefreshTokenLifetime)}}
  {{code: internal/auth/oauth_helpers.go | updated, err := p.parseTokenResponse(resp)}}
  {{code: internal/auth/force_refresh.go | refresh_token 已过期}}
- **access_token:优先用服务端返回的 expires_in;服务端没返回时 CLI 按 7200 秒(2 小时)记,并提前 5 分钟视为失效**。失效后,refresh_token 未过期且服务端刷新成功时 CLI 自动换新,用户无感;刷新被拒就要重新登录。
  {{code: pkg/config/constants.go | DefaultAccessTokenExpiry = 7200}}
  {{code: internal/auth/oauth_helpers.go | expiresIn = config.DefaultAccessTokenExpiry}}
  {{code: internal/auth/token.go | Give 5-minute buffer before actual expiry}}
- 本地记录的到期时间可以用 `dws auth status --format json` 查看,字段 `refresh_expires_at`。
  {{code: internal/app/auth_command.go | json:"refresh_expires_at,omitempty"}}

## 手动导入的 token(`dws auth login --token`)

- **CLI 把手动导入的 token 的到期时间记为导入时刻 + 24 小时,且这种方式没有 refresh_token、不会自动续期**,所以「第二天就不能用了」是预期表现;到期后需要重新导入,或改用扫码登录(有 refresh_token,可自动续期)。
  {{code: pkg/config/constants.go | ManualTokenExpiry = 24 * time.Hour}}
  {{code: internal/app/auth_command.go | ExpiresAt:   time.Now().Add(config.ManualTokenExpiry)}}
  {{code: internal/app/auth_command.go | AccessToken: cfg.Token,}}

## 登录时 CLI 等多久

- **设备码登录(`--device`):CLI 轮询等待用户确认,最多 10 分钟,且不超过服务端下发的授权码有效期(服务端没下发时按 900 秒),两者取短**;CLI 会打印「授权码将在 N 秒后过期」。超时后重新执行登录即可。外层另有 16 分钟总上限,正常不会先于前两者触发。
  {{code: internal/auth/device_flow.go | maxPollTotalWait = 10 * time.Minute}}
  {{code: internal/auth/device_flow.go | elapsed >= maxPollTotalWait || elapsed >= deadline}}
  {{code: internal/auth/device_flow.go | resp.ExpiresIn = 900}}
  {{code: pkg/config/constants.go | DeviceFlowTimeout = 16 * time.Minute}}
- **浏览器扫码登录(默认方式):CLI 本地回调最多等 5 分钟**,超时提示「授权超时(5分钟)」;组织需要管理员审批时,整个登录流程最多 6 分钟。
  {{code: internal/auth/oauth_provider.go | oauthLoginTimeout         = 5 * time.Minute}}
  {{code: internal/auth/oauth_provider.go | time.NewTimer(oauthLoginTimeout)}}
  {{code: pkg/config/constants.go | OAuthFlowTimeout = 6 * time.Minute}}
