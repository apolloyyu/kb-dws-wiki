# dws doc update

kind: command
completeness: partial
usage: dws doc update
description: Update the content of a DingTalk Doc (bulk content rewrite rather than block-level edit).
example: dws doc update --node DOC_ID --content "
use_when: When the agent has freshly generated content and needs to overwrite a doc's body.
source: internal/helpers/doc.go:1721
visible_flags: 9
partial_reason: unverified_flags

## Flags
- --mode <String> required: 更新模式: overwrite=覆盖, append=追加 (必填)
- --node <String>: 文档 ID 或 URL (必填)
- --content <String>: 文档内容（短文本字面量）；传 - 表示从 stdin 读取
- --content-file <String>: 从文件读取文档内容（UTF-8）。推荐长/多行/表格内容使用
- --index <Int>: 插入位置（从 0 开始），仅在 mode=append 时生效。指定将内容插入到文档第几个 block 之前。不传时追加到末尾
- --yes <Bool>: 确认执行破坏性写入 (仅 --mode overwrite 需要)
- --dry-run <Bool>: 预览覆盖写入差异，不调用远端 update
- --content-format <String>: 内容格式: 默认为 markdown，可选 jsonml
- --revision <Int>: 传则触发并发检查（与服务端不一致时拒绝写入），不传则直接覆盖

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
