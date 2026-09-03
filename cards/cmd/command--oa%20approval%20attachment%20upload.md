# dws oa approval attachment upload

kind: command
completeness: full
usage: dws oa approval attachment upload
description: 上传本地文件为审批附件（初始化+PUT+提交，一步完成）
example: dws oa approval attachment upload --file ./合同.pdf
source: internal/helpers/oa.go:549
visible_flags: 3

## Flags
- --file <String> required: 本地文件路径 (必填)
- --file-name <String>: 完整文件名，例如 合同.pdf (默认使用文件名)
- --md5 <String>: 文件原始字节内容的 MD5，32位十六进制字符串 (可选，不传则自动计算)

## Related
- dws oa approval attachment authorize-download
- dws oa approval attachment authorize-preview
- dws oa approval attachment download-url
