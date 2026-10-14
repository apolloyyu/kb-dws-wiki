---
title: dws 的限流与后端调用路径
source_refs: docs/architecture.md, internal/app/direct_runtime.go, internal/transport/client.go, internal/transport/diagnostics.go, internal/errors/diagnostics.go, internal/app/runner.go, internal/app/server_failure_classifier.go, internal/app/api_command.go, internal/helpers/devapp_connect.go, internal/shortcut/chat/active_conversations.go, README_zh.md
intents: ratelimit
---

# dws 的限流与后端调用路径

回答「dws 为什么被限流 / 限流阈值是多少 / 怎么提升 / RATE_LIMIT_ERROR 是什么 / dws 是不是走 OpenAPI」时以本篇为准。核对源码 commit `1deba259`。

## 两条调用路径:产品命令 ≠ OpenAPI

- **产品命令(chat、doc、aitable、calendar、todo 等)走钉钉 MCP 网关,不走开放平台 OpenAPI。** 仓库 `docs/architecture.md` 第 3、10 行:dws 是「DingTalk MCP capabilities」的 CLI,`internal/executor` 与 `internal/transport` 执行 MCP JSON-RPC 调用;`internal/app/direct_runtime.go` `mcpGatewayBaseURL`(约 L107-L116)把 `mcp.dingtalk.com` 改写为 `mcp-gw.dingtalk.com`。报错体里的 `"operation": "tools/call"` 与 `server_key`(如 `chat`)就是 MCP 工具调用的标识(`internal/app/server_failure_classifier.go` `newServerFailureAPIError` 约 L140-L142)。
- **只有 `dws api` 直连 OpenAPI**(`api.dingtalk.com` / `oapi.dingtalk.com`,`internal/app/api_command.go` 约 L64),且必须提供自有应用 Client ID/Client Secret;仅用 MCP 默认凭证登录不支持(README_zh.md 约 L647)。

## 限流规则不能互相套用

- 开放平台文档「调用频次与限流」里的规则——单应用 20/60 QPS、标准版 5000 次/月、IP 20 秒 10000 次、错误码 90018/90002/90020/`Forbidden.AccessDenied.*`、「升级专业版扩容」——**只适用于直接调 OpenAPI 或 `dws api`**。dws 产品命令走 MCP 网关,这些数值、错误码和扩容方式都不能套到产品命令上。
- MCP 网关返回的限流(如 `server_error_code: "RATE_LIMIT_ERROR"`)由服务端决定;dws 源码里没有这个字符串,只原样透传服务端给的错误码(`internal/transport/diagnostics.go` 约 L46、L155)。**阈值、计数维度(按人/按应用/按组织/按接口)、恢复时间、能否申请提升,dws 源码与文档都没有写**,回答写「dws 文档未说明」,不得给具体数字。
- 报错里的 `retryable` 来自服务端返回的同名字段,dws 不自行判断(`internal/transport/diagnostics.go` 约 L51;`internal/errors/diagnostics.go` 约 L47-L50);它不代表 dws 会自动重试这次业务错误。

## dws 自己做了什么

- **HTTP 层自动重试 1 次**:仅当 HTTP 状态为 429 或 5xx(`internal/transport/client.go` `retryable` 约 L1003-L1004;`defaultMaxRetries = 1` 约 L68)。间隔默认 0.5 秒起、上限 5 秒;服务端给了 Retry-After 响应头时按它等待(同样封顶 5 秒)(约 L69-L70、L908-L914、`retryDelayForAttempt` 约 L1072)。
- **业务错误不重试**:MCP 工具返回 `success=false` 时(含 `RATE_LIMIT_ERROR`),dws 直接按 `business_error` 报错返回(`internal/app/runner.go` 约 L943-L954),不会自动重试。
- **没有任何参数或配置能提高服务端限额。**

## 用户能做的

- 退避后重试,降低调用频率与并发;能用批量命令的不要逐条调用。
- 分页拉取时加间隔:`--page-delay <毫秒>` **只有以下命令支持**:`chat +chat-messages`、`+chat-list`、`+chat-search`、`+chat-members-list`、`+group-members`、`+recent-conversations`、`+thread-replies`、`api`(以命令卡为准)。其他命令(如 `chat message search-advanced`)没有这个参数,不得推荐。
- 需要实时收消息时用事件订阅(`dws event consume`),不要高频轮询拉消息。
- 持续限流时保留报错里的 Trace ID 和 Server Code,到 dws 开源仓库提 issue 或通过开放平台工单反馈。

## 容易混淆的同名概念

- `dws dev connect --user-rate-limit`(默认 20)是**本地**按发送人限制每分钟处理的消息数,用于防刷(`internal/helpers/devapp_connect.go` 约 L624),和服务端限流无关。

## 常见误解

- 「dws 只是 OpenAPI 的命令行封装,所以受 OpenAPI 同样的 QPS/月配额约束」:**错**。只有 `dws api` 走 OpenAPI。
- 「升级钉钉专业版就能提高 dws 限额」:**无依据**。专业版扩容是 OpenAPI 调用量的规则。
- 「看报错里的 `retry_after` 字段 / `X-RateLimit-*` 响应头就知道阈值」:**无依据**。dws 不打印 `X-RateLimit-*` 响应头;只有服务端在 HTTP 层返回 Retry-After 时,`chat +recent-conversations` 的失败明细会带 `retryAfter`(`internal/shortcut/chat/active_conversations_result.go` 约 L163-L167),它是等待时间,不是阈值。MCP 业务错误(如 `RATE_LIMIT_ERROR`)不经过这条路径。
