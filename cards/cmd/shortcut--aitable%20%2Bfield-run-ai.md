# dws aitable +field-run-ai

kind: shortcut
completeness: full
usage: dws aitable +field-run-ai
description: 提交 AI 字段运行请求；缺少可靠受理证据时非零退出并保留回执
source: internal/shortcut/aitable/parity_field_ai.go:13
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --field-ids <StringSlice>: 1-10 个 AI 字段 ID
- --record-ids <StringSlice>: 1-500 个记录 ID；省略整列运行

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
