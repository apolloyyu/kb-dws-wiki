# dws oa approval attachment authorize-preview

kind: command
completeness: partial
usage: dws oa approval attachment authorize-preview
description: —
source: internal/helpers/oa.go:493
visible_flags: 3
partial_reason: missing_description

## Flags
- --instance-id <String> required: 审批实例 ID (必填)
- --file-ids <StringSlice> required: 附件 ID 列表，多个用逗号分隔 (必填)
- --with-comment-attachment <Bool>: 是否包含评论中的附件

## Related
- dws oa approval attachment authorize-download
- dws oa approval attachment download-url
- dws oa approval attachment upload
