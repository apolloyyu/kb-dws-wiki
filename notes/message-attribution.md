---
title: 消息角标、产品标识与发送入口的范围
maintenance: manual
intents: message_attribution
triggers: 通过AI发送, AI发送, AI角标, AI标识, 消息小尾巴, DWS_AGENT_PRODUCT, ai-tag, clawType
contract:
  - 角标开关、产品标识和客户端最终显示是不同层次；须核验当前发送入口，不能查一条机器人入口就否定其他发送入口，也不能承诺任意自定义展示文案。
---

# 消息角标、产品标识与发送入口的范围

- 原生用户消息 send/reply 提供 ai-tag 开关，默认true；实现按开关决定是否使用发行版提供的 ClawType。此契约不自动适用于机器人发送等其他入口。
  {{code: internal/helpers/chat.go | chatMessageSendCmd.Flags().Bool("ai-tag", true}}
  {{code: internal/helpers/chat.go | chatMessageReplyCmd.Flags().Bool("ai-tag", true}}
  {{code: internal/helpers/chat.go | aiTag, _ := cmd.Flags().GetBool("ai-tag")}}
  {{code: internal/helpers/chat.go | clawType = edition.ClawType()}}
- DWS_AGENT_PRODUCT 是调用方产品标识，会用于 IM 小尾巴；值须满足源码校验，不等于可以任意传入中文或任意文案。它不改变 HTTP claw-type/PAT 身份。版本说明只适用于包含该变更的发行版，不能套用到用户未升级的版本。
  {{quote: docs/CHANGELOG.md | **Agent Product identity separation**}}
  {{code: internal/app/agent_product.go | 作为 x-dws-agent-product 发送并用于 IM 小尾巴}}
  {{code: internal/app/agent_product.go | DWS_AGENT_PRODUCT must be at most 64 bytes}}
