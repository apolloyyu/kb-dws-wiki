# dws doc media download

kind: command
completeness: full
usage: dws doc media download
description: 下载文档附件
example: dws doc media download --node DOC_ID --resource-id RESOURCE_ID
source: internal/helpers/doc.go:2881
visible_flags: 2

## Flags
- --node <String>: 目标文档的标识，支持传入 URL 或 ID (必填)
- --resource-id <String>: 附件资源 ID，可通过 dws doc block list 获取 (必填)

## Related
- dws doc media insert
- dws doc media upload
