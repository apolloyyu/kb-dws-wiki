# dws report create

kind: command
completeness: full
usage: dws report create
description: Create a new report (DingTalk "Report" entry) based on a report template with filled-in content.
example: dws report create --template-id TPL_ID --contents-file ./report.json --to-user-ids userId1,userId2
use_when: When the agent submits a daily/weekly report on behalf of the user.
source: internal/helpers/report.go:458
visible_flags: 6

## Flags
- --template-id <String>: 日志模版 ID (必填)
- --contents <String>: 日志内容 JSON 数组 (必填，或用 --contents-file)，每项含 key/sort/content/contentType/type；传 - 表示从 stdin 读取
- --contents-file <String>: 从文件读取 contents JSON（推荐用于含中文/换行/Markdown 的长内容，避免 shell 引号转义；优先级：--contents-file > --contents - (stdin) > --contents '<json>'）
- --dd-from <String>: 创建来源标识
- --to-chat <Bool>: 是否发送到日志接收人单聊
- --to-user-ids <String> required: 接收人 userId，逗号分隔 (必填)；无接收人的日志提交后对任何人都不可见

## Related
- dws report created
- dws report detail
- dws report entry
- dws report inbox
- dws report list
- dws report outbox
