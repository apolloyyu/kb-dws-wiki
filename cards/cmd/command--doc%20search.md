# dws doc search

kind: command
completeness: full
usage: dws doc search
description: Search DingTalk Docs the user can access by keyword.
example: dws doc search --query "会议纪要"
use_when: When the agent needs to locate a document by title or content before reading or editing it.
source: internal/helpers/doc.go:1222
visible_flags: 12

## Flags
- --query <String>: 搜索关键词 (不传则返回最近访问)
- --extensions <StringSlice>: 按文件扩展名过滤，不含点号，逗号分隔 (如 pdf,docx,png)。支持的在线文档类型后缀名: adoc=文字, axls=表格, appt=演示文稿, awbd=白板, adraw=画板, amind=脑图, able=多维表格, aform=收集表
- --created-from <Int64>: 创建时间起始 (毫秒时间戳，含)
- --created-to <Int64>: 创建时间截止 (毫秒时间戳，含)
- --visited-from <Int64>: 访问时间起始 (毫秒时间戳，含)
- --visited-to <Int64>: 访问时间截止 (毫秒时间戳，含)
- --creator-uids <StringSlice>: 按创建者用户 ID 过滤，逗号分隔
- --editor-uids <StringSlice>: 按编辑者用户 ID 过滤，逗号分隔
- --mentioned-uids <StringSlice>: 按 @提及的用户 ID 过滤，逗号分隔
- --workspace-ids <StringSlice>: 按知识库 ID 过滤，支持知识库 URL，逗号分隔
- --limit <Int>: 每页数量 (默认 10，最大 30)
- --cursor <String>: 分页游标 (从上次结果的 nextPageToken 获取)

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
