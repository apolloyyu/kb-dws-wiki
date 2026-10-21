---
title: 跨组织消息数据授权的目标与范围
maintenance: manual
intents: cross_org_data
triggers: 跨组织, 非本组织, 其他组织, 外部群, 跨企业
---

# 跨组织消息数据授权的目标与范围
- 消息数据授权入口及其适用范围以产品原文为准，不能自动扩展成发送/群管理权限。
  {{quote: docs/products/chat.md | 用于跨组织消息拉取等数据访问场景，不用于发送、撤回、群管理等操作。}}
- 目标选择有互斥且必需的约束，不能只给一个无目标的授权命令。授权策略还有对应条件，时长不能凭经验补成永久。
  {{quote: docs/products/chat.md | --target-org-id 和 --all 必须且只能指定一个。}}
  {{quote: docs/products/chat.md | --grant-type=session 时必须传 --session-id。}}
  {{quote: docs/products/chat.md | --grant-type=timed 时必须传 --ttl。}}
  {{quote: docs/products/chat.md | 授权策略: once|session|timed|permanent (default "timed")}}
- 切换profile的语法不是“必须登录目标组织”的产品前提依据；是否可访问由目标、授权和接口返回决定，不能自行补授权永久有效或目标组织账号必备等条件。
  {{quote: docs/products/chat.md | 固定使用数据授权类别：`scope=chat.data:cross-org`、`grantCategory=data`。}}
