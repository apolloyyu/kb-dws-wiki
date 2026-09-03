# dws doc read

kind: command
completeness: full
description: Read the content of a DingTalk Doc as Markdown.
use_when: When the agent needs the document body as text for summarization, Q&A, or further editing.
source: internal/helpers/doc.go:1456
visible_flags: 10

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --content-format <String>: 输出格式: 默认为 markdown，可选 jsonml
- --output <String>: 输出到本地文件路径（仅 --content-format jsonml 时生效）
- --scope <String>: 按 scope 筛选节点(需 --content-format jsonml): outline(全部 h1-h6 标题)/range(区间)/section(单块)/tags(配合 --tags 自定义 tag)
- --tags <String>: 自定义 JSONML tag 列表(逗号分隔, 如 h1,h2,table); 仅在 --scope tags 时使用且必填
- --max-depth <Int>: 筛选遍历最大深度, 0 表示不限(仅 --scope 时生效)
- --start-block-id <String>: range/section 起始块 ID(节点 uuid); scope=range/section 时必填
- --end-block-id <String>: range 结束块 ID(节点 uuid); \"-1\"或空=到文档末尾(仅 scope=range 生效)
- --password <String>: 互联网公开文档开启密码保护时的访问密码；普通文档无需传入
- --version <Int>: 读取指定历史版本内容(版本号从 doc version list 获取, 0 表示初始版本, 需要文档编辑权限)；缺省读最新版

## Related
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
- dws doc export
- dws doc import
