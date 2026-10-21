---
title: AI表格产品权限与接口授权的边界
maintenance: manual
intents: table_permissions
triggers: 字段权限, 列权限, 查看权限, 字段级权限, 高级权限
---

# AI表格产品权限与接口授权的边界
- 以下文档明确属于 AI 表格（aitable）的 Base 高级权限和自定义角色，不应外推到普通在线电子表格。原文覆盖按字段或行配置权限；不能从开放API的Base读写权限点推断产品只有文档级权限，也不能把隐藏视图列当作访问控制。
  {{quote: docs/products/aitable/aitable-advperm.md | 控制 Base 的高级权限总开关}}
  {{quote: docs/products/aitable/aitable-advperm.md | "按字段或行配置权限"}}
  {{quote: docs/products/aitable/aitable-advperm.md | 字段/行级细化规则}}
- 角色规则的生效条件、成员绑定入口与管理员要求应分别说明。创建/修改角色与把用户绑定到角色不同；CLI未实现成员绑定不代表产品没有该能力。
  {{quote: docs/products/aitable/aitable-advperm.md | 只有开启后角色配置才会真正限制成员}}
  {{quote: docs/products/aitable/aitable-advperm.md | 角色 ↔ 成员绑定}}
  {{quote: docs/products/aitable/aitable-advperm.md | 创建自定义角色 | ✅ 需管理员}}
