# dws drive commit

kind: command
completeness: full
usage: dws drive commit
description: Commit a file upload to DingTalk Drive after the binary has been pushed to the presigned URL.
example: dws drive commit --file-name "报告.pdf" --file-size 102400 --upload-id <uploadId>
use_when: When the agent finalizes a Drive upload step; pairs with `drive upload-info`.
source: internal/helpers/drive.go:1339
visible_flags: 5

## Flags
- --file-name <String>: 文件名（含扩展名），须与 get_upload_info 时一致 (必填)
- --file-size <Int64> required: 文件大小（字节），须与 get_upload_info 时一致 (必填)
- --upload-id <String>: 上传 ID，来自 get_upload_info 返回的 uploadId (必填)
- --space-id <String>: 空间 ID，不传则使用「我的文件」 (可选)
- --folder <String>: 父节点 ID (dentryUuid)，不传则提交到根目录 (可选)

## Related
- dws drive comment
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
- dws drive download-version
