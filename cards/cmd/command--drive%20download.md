# dws drive download

kind: command
completeness: full
usage: dws drive download
description: Fetch a temporary download URL for a file stored in DingTalk Drive.
example: dws drive download --node <dentryUuid>
use_when: When the agent needs to retrieve a Drive-hosted file for local use or for handing to another service.
source: internal/helpers/drive.go:788
visible_flags: 9

## Flags
- --node <String>: 文件 ID (dentryUuid) (必填)
- --space-id <String>: 文件所属空间 ID (可选)
- --output <String>: 本地保存路径 (文件路径或目录，可选，默认当前目录)
- --overwrite <Bool>: 目标文件已存在时允许覆盖 (默认 false 时拒绝并报错)
- --url-only <Bool>: 只返回带签名的下载地址与请求头，不落盘 (与 --output/--overwrite/--part-size/--parallel/--no-resume 互斥)
- --version <Int>: 下载指定历史版本号（兼容别名，等价 download-version）
- --part-size <String>: 分片下载的分片大小，如 8MB/16MB/1GB，范围 1MB-1GB (可选)
- --parallel <Int>: 分片下载并发数，范围 1-8 (可选)
- --no-resume <Bool>: 关闭断点续传 (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download-version
