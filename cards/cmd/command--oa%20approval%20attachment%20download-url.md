# dws oa approval attachment download-url

kind: command
completeness: partial
usage: dws oa approval attachment download-url
description: —
source: internal/helpers/oa.go:380
visible_flags: 3
partial_reason: missing_description

## Flags
- --instance-id <String> required: 审批实例 ID (必填)
- --file-id <String> required: 审批附件文件 ID (必填)
- --with-comment-attachment <Bool>: 是否包含评论中的附件

## Related
- dws oa approval attachment authorize-download
- dws oa approval attachment authorize-preview
- dws oa approval attachment upload
