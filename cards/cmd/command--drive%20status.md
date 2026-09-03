# dws drive status

kind: command
completeness: full
description: 比较本地文件夹与钉盘文件夹的差异
source: internal/helpers/drive.go:4064
visible_flags: 4

## Flags
- --local-folder <String>: 本地文件夹绝对路径 (必填)
- --remote-folder <String>: 钉盘文件夹 ID (dentryUuid) (必填)
- --space-id <String>: 钉盘空间 ID，不传则使用「我的文件」(可选)
- --quick <Bool>: 快速模式：只比较 modified_time，不计算 MD5 (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
