---
title: 数字员工在哪创建、与 DEAP 1.0 助理的区别
source_refs: internal/helpers/deap_agent.go, skills/mono/references/products/dingtalk-tag/dingtalk-tag-index.md, skills/mono/references/products/dingtalk-tag/manage.md, 仓库 docs/deap-digital-employee-detail.md, 仓库 skills/mono/SKILL.md, 产品方确认(2026-10-15)
intents: origin
---

# 数字员工在哪创建、与 DEAP 1.0 助理的区别

回答「数字员工在哪创建 / 是不是 DEAP 里的智能体 / AI 助理是不是改名成了数字员工 / 怎么开通」时以本篇为准。直接给结论,不要先推测再改口。

## 能确定的

- **现在说的「数字员工」= dws `dingtalk-tag` 这一套**(标识 `agentUuid`)。dws 仓库文档称其为「DEAP 数字员工」(`docs/deap-digital-employee-detail.md`),命令固定调用后端 MCP server `deap-dev`(`dingtalk-tag-index.md`「全局约束」)——这只是后端服务名,**不代表要去 DEAP 平台界面里操作**。
- **在 DEAP 平台界面里「创建智能体 / 助理 → 配置人设 → 发布 → 加到群」是 DEAP 1.0 的 AI 助理,不是现在的数字员工**(产品方确认,2026-10-15)。回答数字员工的创建、入群、配置时,**不得把 DEAP 平台界面列为任何一种方式**(包括「方式一:DEAP 平台可视化创建」),也不要让用户拿 DEAP 平台里的智能体 ID 去比对。
- **dws 文档给出的创建方式**:`dws dingtalk-tag manage create --name <名称> --description <职责> --type open_code|local_agent`,只建草稿(`deap_agent.go` 约 L232);上线还要 `manage set-visibility` 设可见范围、`manage publish` 发布(`docs/products/dingtalk-tag/manage.md`)。查已有数字员工用 `manage list` / `manage detail --agent-uuid <agentUuid>`。数字员工是否另有客户端界面入口、在哪,dws 文档没写,回答写「文档未说明」,不得拿 DEAP 平台界面顶替。
- **开通**:数字员工功能在灰度中,开通填开放平台文档「dws 更新日志」(https://open.dingtalk.com/document/development/dws-cli-log ,2026-10-03 一期「数字员工(灰度中)」)里的灰度申请表:[钉钉数字员工创建灰度申请（DWS 内&&界面功能）](https://alidocs.dingtalk.com/notable/share/form/v013BMqYy5D4dLEmqwZ_MPojg9m_23zNs0R?source=link)。表名与链接整条照抄,不得改称「DEAP 灰度申请表」等其他名称,不得改写或另造链接。不要说成组织内部审批流程,也不要改成让用户找商务或客服。

## 文档没写明的

- 开放平台「提交创建企业自建Agent」接口、开发者后台发布类型里的「数字员工」与 dws 数字员工是否对应,dws 文档没写。回答写「文档未说明」,**不得把它们列为 dws 数字员工的创建方式**,不要补「可能是同一底层能力的不同入口」这类推测,也不要建议去灰度申请表或对接人咨询。
