# dws drive download-version

kind: command
completeness: partial
description: 下载文件历史版本到本地
source: internal/helpers/drive.go:998
visible_flags: 8
partial_reason: empty_flag_name

## Flags
- --node <String>: 文件 ID (dentryUuid) 或 URL (必填)
- --version <Int>: 历史版本号 (必填，正整数，从 drive list --versions 获取)
- --output <String>: 本地保存路径 (文件路径或目录，可选，默认当前目录)
- --overwrite <Bool>: 目标文件已存在时允许覆盖 (默认 false 时拒绝并报错)
- --url-only <Bool>: 只返回带签名的下载地址与请求头，不落盘 (与 --output/--overwrite/--part-size/--parallel/--no-resume 互斥)
- --part-size <String>: 分片下载的分片大小，如 8MB/16MB/1GB，范围 1MB-1GB (可选)
- --parallel <Int>: 分片下载并发数，范围 1-8 (可选)
- --no-resume <Bool>: 关闭断点续传 (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
