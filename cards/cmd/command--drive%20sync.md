# dws drive sync

kind: command
completeness: full
description: 本地文件夹与钉盘文件夹双向同步（本地 ⇄ Drive）
source: internal/helpers/drive.go:4142
visible_flags: 5

## Flags
- --local-folder <String>: 本地文件夹绝对路径 (必填)
- --remote-folder <String>: 钉盘文件夹 ID (dentryUuid) (必填)
- --space-id <String>: 钉盘空间 ID，不传则使用「我的文件」(可选)
- --on-conflict <String>: 两侧都变更时的策略: skip|remote-wins|local-wins|keep-both|ask；命令会写双端，执行需确认 (可选)
- --quick <Bool>: 快速模式：只比较 modified_time，不计算 MD5 (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
