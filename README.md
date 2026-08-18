# kb-dws-wiki — dws CLI 整理版知识库

DingTalk Workspace CLI(dws)的答疑知识库:基于源码由模型实读生成,每篇 frontmatter 的 `source_refs` 锚定事实来源,`meta/MANIFEST.json` 的 `source_commit` 锚定生成时的源码版本。

- Agent 使用入口:[AGENTS.md](AGENTS.md)(检索协议)
- 篇目索引:[index.md](index.md) · 机器索引:`meta/documents.jsonl`
- 上游源码:https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli

## 更新机制与协作规则

本仓库是**知识库组**的一员,遵循 KB Spec v1(布局与元数据见 `meta/MANIFEST.json`)。

- **正规更新通道**:源码变更驱动的**增量链**(检测→定向重生成→候选→人工审阅 diff→入库直推),由维护方平台调度;每篇只在其 source_refs 涉及的源码变更时才会重写
- **可以手改的**:认知/策展层(如 TOPICS、README、AGENTS)欢迎直接 PR;
- **不要手改的**:docs/ 正文(下次定向重生成会覆盖对应篇目;发现事实错误请提 Issue 触发重生成)
- 勘误与建议:提 Issue,或联系维护人(MANIFEST 的 contact)。
