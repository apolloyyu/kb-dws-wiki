---
title: 数字员工在哪创建、与 DEAP 智能体的关系
source_refs: internal/helpers/deap_agent.go, docs/products/dingtalk-tag/dingtalk-tag-index.md, docs/products/dingtalk-tag/manage.md
intents: origin
---

# 数字员工在哪创建、与 DEAP 智能体的关系

回答「数字员工在哪创建 / 是不是 DEAP 里的智能体 / AI 助理是不是改名成了数字员工 / 怎么开通」时以本篇为准。先给能确定的,再说文档没写明的部分和自查方法;不要先下结论再改口。

## 能确定的

- **在 dws 里创建**:`dws dingtalk-tag manage create --name <名称> --description <职责> --type open_code|local_agent`,只建草稿(`deap_agent.go` 约 L232);上线还要 `manage set-visibility` 设可见范围、`manage publish` 发布(`docs/products/dingtalk-tag/manage.md`)。
- **后端服务**:dingtalk-tag 命令固定调用 MCP server `deap-dev`(`dingtalk-tag-index.md`「全局约束」)。这只说明 dws 数字员工的管理接口由 `deap-dev` 提供。
- **开通**:dws 数字员工功能在灰度中,开通以开放平台文档「dws 更新日志」里的灰度申请表为准(原文链接须从开放平台文档取)。不要说成组织内部审批流程,也不要改成让用户找商务或客服。

## 文档没写明的

- DEAP 后台的「智能体」、开放平台的「提交创建企业自建Agent」接口、开发者后台发布类型里的「数字员工」(AI 助理),是否就是 dws 的 dingtalk-tag 数字员工,dws 文档没有写。
- 回答写「文档未说明」,**不得把它们列为 dws 数字员工的创建方式**,也不要补「可能是同一底层能力的不同入口」这类推测。

## 用户想自己确认时

拿 DEAP 后台显示的智能体 ID,自己运行(`manage.md`「detail / list — 查询」):

```bash
dws dingtalk-tag manage detail --agent-uuid <该ID> --format json
dws dingtalk-tag manage list --keyword "<智能体名称>" --format json
```

能查到同一个 agentUuid,即可判断是同一实体;查不到不能据此断定不是(可能尚未开通灰度,或命令本身失败)。
