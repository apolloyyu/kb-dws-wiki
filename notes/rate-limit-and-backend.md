---
title: dws 的限流与后端调用路径
maintenance: manual
intents: ratelimit
contract:
  - ratelimit：dws 产品命令走钉钉 MCP 网关(mcp-gw.dingtalk.com)，不走开放平台 OpenAPI；开放平台「调用频次与限流」的 QPS、月调用量、IP 维度、90018/90002/90020、升级专业版扩容只适用于 dws api 直调 OpenAPI，不得套用到产品命令；RATE_LIMIT_ERROR 的阈值/计数维度/能否提升 dws 未说明，不得给具体数字，但 dws 对该错误码固定提示「等待 10 秒后重试」，可照此转述并说明那是客户端重试建议、不是服务端承诺的恢复时间；--page-delay 只能推荐给命令卡里有该参数的命令。
---

# dws 的限流与后端调用路径

回答「dws 为什么被限流 / 限流阈值是多少 / 怎么提升 / RATE_LIMIT_ERROR 是什么 / dws 是不是走 OpenAPI」时以本篇为准。本篇只写判断;原文由依据标记在输出时从镜像层逐字取出,源码依据由每日构建核对。

## 两条调用路径:产品命令 ≠ OpenAPI

- **产品命令(chat、doc、aitable、calendar、todo 等)走钉钉 MCP 网关,不走开放平台 OpenAPI。** 报错体里的 `"operation": "tools/call"` 与 `server_key`(如 `chat`)就是 MCP 工具调用的标识。
  {{quote: docs/upstream/architecture.md | execute MCP JSON-RPC calls}}
  {{code: internal/app/direct_runtime.go | mcp-gw.dingtalk.com}}
  {{code: internal/app/server_failure_classifier.go | operation := "tools/call"}}
- **只有 `dws api` 直连 OpenAPI**(`api.dingtalk.com` / `oapi.dingtalk.com`),且必须提供自有应用 Client ID/Client Secret;仅用 MCP 默认凭证登录不支持。
  {{code: internal/app/api_command.go | 直接调用钉钉 OpenAPI}}
  {{code: README_zh.md | 仅通过 MCP 默认凭证登录不支持 Raw API 调用}}

## 限流规则不能互相套用

- 开放平台文档「调用频次与限流」里的规则——单应用 20/60 QPS、标准版 5000 次/月、IP 20 秒 10000 次、错误码 90018/90002/90020/`Forbidden.AccessDenied.*`、「升级专业版扩容」——**只适用于直接调 OpenAPI 或 `dws api`**。dws 产品命令走 MCP 网关,这些数值、错误码和扩容方式都不能套到产品命令上。
- MCP 网关返回的限流(`server_error_code: "RATE_LIMIT_ERROR"`)由服务端判定,dws 透传该错误码;但 dws 对这个码有专门分类,会把面向用户的提示改写成固定文案「等待 10 秒后重试」。**这 10 秒是 dws 客户端给的重试建议,不是服务端承诺的恢复时间,也不代表限额口径**;可以照 dws 的文案转述,但要说明它的来源。
  {{code: internal/app/server_failure_classifier.go | if code == "RATE_LIMIT_ERROR"}}
  {{code: internal/app/server_failure_classifier.go | 请等待 10 秒后重试}}
  {{code: internal/transport/diagnostics.go | server_error_code}}
- **阈值、计数维度(按人/按应用/按组织/按接口)、能否申请提升,dws 源码与文档仍然没有写**,这几项一律回答「dws 文档未说明」,不得给具体数字。
  {{absent: qps @ internal/**/*.go}}
  {{absent: 限流阈值 @ internal/**/*.go}}
- 报错里的 `retryable` 来自服务端返回的同名字段,dws 不自行判断;它不代表 dws 会自动重试这次业务错误。
  {{code: internal/transport/diagnostics.go | "retryable", "server_retryable"}}

## dws 自己做了什么

- **HTTP 层自动重试 1 次**:仅当 HTTP 状态为 429 或 5xx;间隔默认 0.5 秒起、上限 5 秒,服务端给了 Retry-After 响应头时按它等待。
  {{code: internal/transport/client.go | defaultMaxRetries    = 1}}
  {{code: internal/transport/client.go | statusCode == http.StatusTooManyRequests || statusCode >= http.StatusInternalServerError}}
- **业务错误不重试**:MCP 工具返回 `success=false` 时(含 `RATE_LIMIT_ERROR`),dws 直接按 `business_error` 报错返回。
  {{code: internal/app/runner.go | "business_error",}}
- **没有任何参数或配置能提高服务端限额。**

## 用户能做的

- 退避后重试,降低调用频率与并发;能用批量命令的不要逐条调用。
- 分页拉取时加间隔:`--page-delay <毫秒>` 只能推荐给命令卡里有该参数的命令(如 `chat +chat-messages`、`+recent-conversations` 等);其他命令(如 `chat message search-advanced`)没有这个参数,不得推荐。
  {{quote: docs/products/chat.md | `--page-delay` 默认 200ms}}
- 需要实时收消息时用事件订阅(`dws event consume`),不要高频轮询拉消息。
- 持续限流时保留报错里的 Trace ID 和 Server Code,到 dws 开源仓库提 issue 或通过开放平台工单反馈。

## 容易混淆的同名概念

- `dws dev connect --user-rate-limit`(默认 20)是**本地**按发送人限制每分钟处理的消息数,用于防刷,和服务端限流无关。
  {{code: internal/helpers/devapp_connect.go | "user-rate-limit", 20}}

## 常见误解

- 「dws 只是 OpenAPI 的命令行封装,所以受 OpenAPI 同样的 QPS/月配额约束」:**错**。只有 `dws api` 走 OpenAPI。
- 「升级钉钉专业版就能提高 dws 限额」:**无依据**。专业版扩容是 OpenAPI 调用量的规则。
- 「看报错里的 `retry_after` 字段 / `X-RateLimit-*` 响应头就知道阈值」:**无依据**。dws 不打印 `X-RateLimit-*` 响应头;只有服务端在 HTTP 层返回 Retry-After 时,`chat +recent-conversations` 的失败明细会带 `retryAfter`,它是等待时间,不是阈值。MCP 业务错误(如 `RATE_LIMIT_ERROR`)不经过这条路径。
  {{absent: x-ratelimit @ internal/transport/*.go !_test.go}}
  {{code: internal/shortcut/chat/active_conversations_result.go | details["retryAfter"]}}
