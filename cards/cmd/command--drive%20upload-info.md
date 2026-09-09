# dws drive upload-info

kind: command
completeness: full
usage: dws drive upload-info
description: Obtain a presigned upload URL and token for pushing a local file into DingTalk Drive.
example: dws drive upload-info --file-name "报告.pdf" --file-size 102400
use_when: When the agent starts a Drive upload; pairs with `drive commit` to finalize.
source: internal/helpers/drive.go:1273
visible_flags: 5

## Flags
- --file-name <String>: 文件名，须包含扩展名，如 报告.pdf (必填)
- --file-size <Int64> required: 文件大小（字节）(必填)
- --space-id <String>: 目标空间 ID，不传则使用「我的文件」 (可选)
- --mime-type <String>: 文件 MIME 类型，如 application/pdf，不传则自动推断 (可选)
- --folder <String>: 父节点 ID (dentryUuid)，不传则上传到空间根目录 (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
