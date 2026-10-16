---
title: 数字员工(dingtalk-tag):是什么、怎么建、怎么开通、群里谁能对话
maintenance: manual
intents: origin, access
triggers: 数字员工, dingtalk-tag, agent-uuid, agentuuid, digital_employee
contract:
  - deap1：现在的数字员工 = dws dingtalk-tag(标识 agentUuid)；DEAP 平台界面「创建智能体/助理→发布→加到群」是 DEAP 1.0 的 AI 助理，不得列为数字员工的创建、配置或入群方式(含「方式一：DEAP 平台可视化创建」)。
  - access：可见范围(set-visibility)与对话白名单(connect --allowed-users/--allowed-groups)是两层；群里多人使用须同时给出 --allowed-groups 与 --allowed-users；原文没写的入群方式只答「文档未说明」；应用机器人命令(add-bot/robotCode)不得套用到数字员工。
  - origin：创建走 manage create(只建草稿)→set-visibility→publish；开通填 notes 里逐字给出的灰度申请表，申请表只用于申请开通，不当作咨询渠道。
---

# 数字员工(dingtalk-tag)

回答数字员工的定义、创建、开通、群里谁能对话、和机器人/DEAP 的关系时以本篇为准。本篇只写判断;原文由依据标记在输出时从镜像层逐字取出,上游改了会随之更新。直接给结论,不要先推测再改口。

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

- **可见范围 ≠ 对话白名单,两层互不替代。** `set-visibility --visibility ALL` 不等于群里所有人都能对话。
- **默认只有主管能用**;要开放给别人,接入普通本地 Agent 时用 `connect --allowed-users`(精确 userId)和 `--allowed-groups`(群会话 ID)。群消息要求群**和**发送人都在白名单,逐个精确匹配,没有通配或「所有人」选项。不在名单内的人 @ 它,消息被直接丢弃,没有任何回复。
  {{quote: docs/upstream/digital-employee-adapters.md | 默认仅主管能触发}}
  {{quote: docs/products/dingtalk-tag/manage-and-connect.md | 默认仅主管可用}}
- 让一个群里的多人使用,须同时给出 `--allowed-groups` 与 `--allowed-users`:

```bash
dws dingtalk-tag connect --agent-uuid <agentUuid> --channel <agent> \
  --allowed-groups <openConversationId> --allowed-users <userId1>,<userId2> --dry-run --format json
```

- `--channel dsh`(DSH 宿主运行)和 `open_code`(平台托管)两种情况下群里谁能对话:文档未说明。

## 常见误解

- **「数字员工通过关联机器人的 robotCode,用 `chat group members add-bot` 入群」:无依据。** `add-bot` 是给应用机器人用的,必须传 `--robot-code`;dingtalk-tag 只用 `agentUuid`,不对用户暴露 robotUid,dws 也不提供获取数字员工 robotCode 的途径。
  {{quote: docs/skills/dingtalk-tag.md | robotUid}}
  {{quote: docs/skills/dingtalk-tag.md | 不要回退到机器人创建流程}}
  {{absent: robotcode @ internal/helpers/deap_agent*.go}}
- **把数字员工加入某个群的操作方式**:dws 源码与文档都没有提供。回答写「文档未说明」,不要编造客户端菜单路径或开放平台接口,也不要建议去灰度申请表、对接人或客服咨询。
