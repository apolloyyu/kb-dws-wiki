---
title: 个人行为检索、业务变更记录与本地审计的范围
maintenance: manual
intents: behavior_records
triggers: 操作记录, 行为记录, 自动写日报
---

# 个人行为检索、业务变更记录与本地审计的范围
- 个人行为可先用AI搜问行为检索；类型和行为范围以该模块原文为准，不能把一个模块的类型表当成整个客户端全部能力。
  {{quote: docs/products/aisearch.md | dws aisearch behavior}}
- 既有产品命令未封装的服务端OpenAPI存在专门发现与调用流程；不能反过来承诺所有用户接口都能用，需要先核验应用和令牌资格。具体业务接口及权限仍应联查开平文档。
  {{quote: docs/products/openapi-explorer.md | 当现有 DWS 产品命令无法覆盖企业内部应用的服务端 OpenAPI 时}}
  {{quote: docs/products/openapi-explorer.md | 仅允许“企业内部应用 + App Token + 服务端 OpenAPI”}}
- audit是本地CLI操作审计，不能直接当作企业内所有用户操作或管理员行为的审计接口。
  {{code: internal/app/audit_command.go | 查看、导出和校验本地操作审计日志。}}
