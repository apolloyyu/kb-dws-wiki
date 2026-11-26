# DWS CLI 知识库

本库为钉钉 Workspace CLI（DWS）提供命令契约、产品用法和运行行为说明。

## 查资料

- 按 [检索协议](AGENTS.md) 使用 `python3 bin/dwsdoc ctx '完整问题'`。看到 `card=1(fast=1)` 时可直接按卡片回答命令契约，复杂问题继续核对正文和源码。
- [篇目索引](meta/documents.jsonl) 收录镜像正文和 notes。[答案卡索引](cards/index.jsonl) 收录主命令和快捷命令。
- [DWS 上游源码](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli) 提供行为依据，按对应提交核对实现。

## 日更和审阅

1. 定时任务拉取上游源码，重建 `docs/`、`graph/` 和 `cards/`，并重建索引和证据核对结果。[构建清单](meta/MANIFEST.json) 的 `source_commit` 标记这次确定性构建使用的源码版本。
2. notes 选篇按每篇 frontmatter 的 `source_refs` 匹配改动文件。命中自动维护篇目时生成待审候选，批准后入库。`notes_commit` 记录增量审阅推进到的源码版本。标有 `maintenance: manual` 的篇目由维护者复核。
3. 候选入库时把仍未覆盖的源码路径写入 `notes_uncovered`，后续日更继续检查这些路径。镜像须与当轮上游版本的正文相符。单测和测试覆盖对账配置由回归流程处理，篇目显式引用的测试仍可触发选篇。需要补行为说明时，按源码补写篇目和实际使用的 `source_refs`。

维护说明和新增篇目通过代码评审提交。镜像正文、命令图、答案卡及生成索引由构建产出。勘误可通过 Issue 或构建清单的 `contact` 联系维护者。
