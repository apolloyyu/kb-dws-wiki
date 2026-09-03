# dws 域 — 检索协议(v3,答案卡加速 + 三层事实结构)

本库是 dws CLI(DingTalk Workspace CLI,开源命令行工具)的知识库,结构对齐
kb-dingtalk-open-platform 范式:**事实走确定性层(零 LLM),行为语义走生成+审阅层**。
构建信息见 `meta/MANIFEST.json`(source_commit / build_time / 各层统计)。

## 答案卡 + 三层结构

| 层 | 内容 | 生成方式 | 可信度/用途 |
|---|---|---|---|
| `cards/` | 每条主命令/shortcut 的紧凑卡(cmd、描述、flags、源码、相关命令) | 从 graph 确定性生成,数量/完整率地板 | `completeness: full` 且 ctx 标 `fast=1` 时可直接作答；partial 必须继续查正文 |
| `graph/` | commands.jsonl(规范路径+完整 Usage+flags 完整度+源码行号)、shortcuts.jsonl(+xxx 短命令) | 源码静态提取,lint 对账 | **命中即事实**,可直接回引 文件:行号 |
| `docs/` | command-index.md、CHANGELOG.md、products/**(上游人写的产品线文档) | 逐字镜像 | 与上游仓库原文一致 |
| `notes/` | 行为语义篇(投递模型/锁/ACK 等"为什么") | LLM 实读源码生成+人工审阅 | 加速层,行号结论仍以源码为准 |

## 检索顺序(强烈建议)

0. **首选一次打包** → `python3 bin/dwsdoc ctx '<完整用户问题>'`
   - 输出含 `card=1(fast=1)` 且卡为 `completeness: full`：卡片字段齐全，直接据卡作答，不再 cat；
   - `fast=0` / `partial` / 机制、数值、复杂支持性、排障、枚举题：ctx 自动保留正文/notes，按输出继续核验；
   - 强制深查或卡片疑似异常：`python3 bin/dwsdoc ctx --full '<问题>'`；全局回退可设 `KB_NO_CARDS=1`，行为字节级回到 v2；
   - 精查单条卡：`python3 bin/dwsdoc card '<完整命令路径>'`。
   ctx 始终带 cmd/short/flag/find/notes 命中数审计，仍是「三查」的机械凭证。
1. **命令/flag 存在性与拼写** → `python3 bin/dwsdoc cmd|short|flag <词>`
   命中即得 flags 全表+源码行号;查不到≠不存在,回退源码 grep(见 4)。
2. **产品用法/使用场景** → `python3 bin/dwsdoc find <词>` 定位 `docs/products/<产品>.md` 后 cat 原文。
3. **行为语义(为什么/机制)** → `notes/` 对应篇;结论须以其标注的 文件:行号 回源码复核。
4. **兜底** → dws 源码仓库(github.com/DingTalk-Real-AI/dingtalk-workspace-cli)grep,
   版本判定看 `docs/CHANGELOG.md`(本库镜像,与上游同源)。

## 硬性纪律

- 说「命令/flag 不存在」前,必须三查皆空(ctx 审计行即凭证,或 cmd+short+flag 逐一查),并回源码枚举确认;
- `docs/` 与 `notes/` 冲突时以 `docs/`(镜像)与源码为准;
- 本库 `docs/`+`graph/`+`cards/` 由流水线确定性重建,**勿手工修改**;`notes/` 走候选-审阅制(dws_regen --deepen)。
