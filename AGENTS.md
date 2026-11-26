# DWS 检索协议

在 `cards/` 和 `graph/` 查命令契约，在 `docs/` 查产品用法，在 `notes/` 查运行行为与边界。[构建清单](meta/MANIFEST.json) 记录确定性构建的 `source_commit`、增量审阅推进到的 `notes_commit` 和各层统计。

## 答案卡 + 三层结构

| 层 | 内容 | 生成方式 | 可信度/用途 |
|---|---|---|---|
| `cards/` | 每条主命令/shortcut 的紧凑卡(cmd、描述、flags、源码、相关命令) | 从 graph 确定性生成,数量/完整率地板 | `completeness: full` 且 ctx 标 `fast=1` 时仅可直接回答卡内 CLI 契约；partial 必须继续查正文 |
| `graph/` | commands.jsonl(规范路径+完整 Usage+flags 完整度+源码行号)、shortcuts.jsonl(+xxx 短命令) | 源码静态提取,lint 对账 | **命中即事实**;回复里引用输出中的「引用:」深链,不写裸 文件:行号 |
| `docs/` | 命令索引、更新日志、产品文档和 Skill 入口 | 从记录的上游路径镜像 | 用于核对产品用法，文件开头记录来源 |
| `notes/` | 行为语义篇(投递模型/锁/ACK 等"为什么") | LLM 实读源码生成+人工审阅 | 加速层,行号结论仍以源码为准 |

## 检索顺序(强烈建议)

0. **首选一次打包** → `python3 bin/dwsdoc ctx '<完整用户问题>'`
   - 输出含 `card=1(fast=1)` 且卡为 `completeness: full`：仅按卡内 CLI 路径、Usage、参数、描述与源码锚点作答，不再 cat；
   - `fast=0` / `partial` / 支持性、因果、ID/参数合法性、机制、数值、排障、枚举、版本或未闭合输入：ctx 自动保留正文/notes，按输出继续核验；
   - 强制深查或卡片疑似异常：`python3 bin/dwsdoc ctx --full '<问题>'`；全局回退可设 `KB_NO_CARDS=1`；
   - 精查单条卡：`python3 bin/dwsdoc card '<完整命令路径>'`。
   支持性/确认/枚举问法（能不能/有没有/是不是/拉不到…）ctx 会在最前面输出「否定前必读」清单（本轮命中的命令、shortcut 与篇目），说「没有/不支持」前须逐条说明为何不满足所问；支持性/版本题另附「CHANGELOG 命中行」（按实现名 grep，产品行为变更以此为准）。ctx/card 都附「证据契约」：命令存在不证明后端值校验、运行结果或服务端行为；卡片问题须把原始结构、可读文本、结构化解析、渲染、解密分开核验。ctx 始终带 cmd/short/flag/find/notes 命中数审计，仍是「三查」的机械凭证；`ops/scripts/test_dwsdoc_ctx.py` 已接入每日确定性构建，回归失败禁止推送。
1. **命令/flag 存在性与拼写** → `python3 bin/dwsdoc cmd|short|flag <词>`
   命中即得 flags 全表+源码行号;查不到≠不存在,回退源码 grep(见 4)。
2. **产品用法/使用场景** → `python3 bin/dwsdoc find <词>` 定位 `docs/products/<产品>.md` 后 cat 原文。
3. **行为语义(为什么/机制)** → `notes/` 对应篇;结论须以其标注的 文件:行号 回源码复核。
4. **兜底** → dws 源码仓库(github.com/DingTalk-Real-AI/dingtalk-workspace-cli)grep,
   版本判定看 `docs/CHANGELOG.md`(本库镜像,与上游同源)。

## 硬性纪律

- 说「命令/flag 不存在」前,必须三查皆空(ctx 审计行即凭证,或 cmd+short+flag 逐一查),并回源码枚举确认;
- `docs/` 与 `notes/` 冲突时以 `docs/`(镜像)与源码为准;
- `docs/`、`graph/`、`cards/` 和生成索引由流水线构建。notes 的候选经过审阅后入库。

## 维护 notes

- 在 `source_refs` 中列出正文实际依赖的上游相对路径。定时任务按路径精确选篇。章节中写出对应的源码文件名和行为依据，供增量更新定位。标为 `maintenance: manual` 的篇目由人维护。
- 确定性构建和 notes 审阅各自记录源码版本。批准候选时，`notes_uncovered` 记录当轮待补路径，供后续日更继续核对。镜像覆盖依据当轮上游版本和正文。显式列入 `source_refs` 的测试路径也参与选篇。
- 告警出现时先核对上游差异和镜像来源。需要补新的行为说明时，通过代码评审添加篇目及其 `source_refs`，再运行定时检查或后台检查，按差异审阅候选。
