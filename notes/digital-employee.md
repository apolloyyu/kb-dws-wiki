---
title: 数字员工(dingtalk-tag):是什么、怎么建、怎么开通、群里谁能对话
maintenance: manual
intents: origin, access
triggers: 数字员工, dingtalk-tag, agent-uuid, agentuuid, digital_employee
---

# 数字员工(dingtalk-tag)

## 是什么、和 DEAP 1.0 助理的区别

- **现在说的「数字员工」= dws `dingtalk-tag` 这一套**,标识 `agentUuid`。
  {{quote: docs/products/dingtalk-tag/dingtalk-tag-index.md | 数字员工标识只使用}}
- 后端 MCP server 叫 `deap-dev`,上游文档也称「DEAP 数字员工」——这只是服务名,**不代表要去 DEAP 平台界面里操作**。
  {{quote: docs/products/dingtalk-tag/dingtalk-tag-index.md | deap-dev}}
- **在 DEAP 平台界面「创建智能体/助理 → 配置人设 → 发布 → 加到群」是 DEAP 1.0 的 AI 助理,不是现在的数字员工。** 回答数字员工的创建、配置、入群时不得把 DEAP 平台界面列为任何一种方式(包括「方式一:DEAP 平台可视化创建」),也不要让用户拿 DEAP 平台里的智能体 ID 去比对。
  {{confirmed: 产品方 2026-10-15}}
- 开放平台「提交创建企业自建Agent」接口、开发者后台发布类型里的「数字员工」是否对应 dws 数字员工:文档未说明。不得列为创建方式,不要补「可能是同一底层能力的不同入口」这类推测。

## 怎么创建、发布

- dws 文档给出的创建方式:`manage create` 只建草稿 → `manage set-visibility` 设可见范围 → `manage publish` 发布。
  {{quote: docs/products/dingtalk-tag/dingtalk-tag-index.md | 创建 / 新建数字员工}}
- 是否另有客户端界面入口:文档未说明。不得拿 DEAP 平台界面顶替。

## 怎么开通

- 数字员工功能在灰度中,开通填这张申请表(表名与链接整条照抄,不得改称「DEAP 灰度申请表」等其他名称,不得改写或另造链接):
  {{quote: docs/external/open-platform/dws-cli-log.md | 数字员工创建灰度申请}}
- 不要说成组织内部审批流程,也不要改成让用户找商务或客服。申请表只用于申请开通,不当作咨询渠道。

## 群里谁能和它对话

谁能对话取决于员工的接入方式。源码按绑定里有没有服务端回执(`runtimeBindingId`)分成两种访问策略:
  {{code: internal/helpers/deap_agent_access_policy.go | validMachineString(b.RuntimeBindingID)}}

- **正式 `connect` 绑定的 local_agent(访问策略 `platform`,当前默认)**:由钉钉平台控制,本地不再查白名单。私聊:在可见范围内就能聊,移出可见范围后不再投递。群聊:已在群里时,原生 @ 它的消息会回复,群里不 @ 的消息不处理。可见范围用 `manage set-visibility` 设置,`manage publish` 后由平台生效。
  {{quote: docs/upstream/digital-employee-adapters.md | 钉钉平台保证私聊可见即可以聊天}}
  {{quote: docs/upstream/digital-employee-adapters.md | 投递权限由平台生效}}
  {{code: internal/helpers/deap_agent_runtime.go | employeeBindingAccessPolicy(r.cfg.Binding) == "platform"}}
- **没有服务端绑定回执的其他本地通道(访问策略 `local_allowlist`)**:沿用本地白名单,默认只有主管能用;开放给别人用 `connect --allowed-users`(精确 userId),群消息还要求群在 `--allowed-groups` 里,逐个精确匹配,没有通配。
  {{quote: docs/upstream/digital-employee-adapters.md | 其他本地通道和机器人保留本地用户/群白名单}}
  {{quote: docs/products/dingtalk-tag/manage-and-connect.md | 默认仅主管可用}}
- 上游产品说明(manage-and-connect.md)仍写「默认仅主管可用」,和设计文档、源码的新行为不一致;回答以源码和设计文档为准,并说明这一点适用于没有服务端绑定的旧通道。
- **怎么把数字员工加进群**:文档只说「已入群后」@ 可回复,入群的操作方式未说明。
- `--channel dsh`(DSH 宿主运行)和 `open_code`(平台托管)两种情况下群里谁能对话:文档未说明。

## 常见误解

- **「数字员工通过关联机器人的 robotCode,用 `chat group members add-bot` 入群」:无依据。** `add-bot` 是给应用机器人用的,必须传 `--robot-code`;dingtalk-tag 只用 `agentUuid`,不对用户暴露 robotUid,dws 也不提供获取数字员工 robotCode 的途径。
  {{quote: docs/skills/dingtalk-tag.md | robotUid}}
  {{quote: docs/skills/dingtalk-tag.md | 不要回退到机器人创建流程}}
  {{absent: robotcode @ internal/helpers/deap_agent*.go}}
- **把数字员工加入某个群的操作方式**:dws 源码与文档都没有提供。回答写「文档未说明」,不要编造客户端菜单路径或开放平台接口,也不要建议去灰度申请表、对接人或客服咨询。
