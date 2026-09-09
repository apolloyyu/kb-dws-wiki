# dws drive pull

kind: command
completeness: full
usage: dws drive pull
description: 把钉盘文件夹单向镜像到本地（Drive → 本地）
example: dws drive pull --local-folder /abs/path/repo --remote-folder <dentryUuid>
source: internal/helpers/drive.go:4096
visible_flags: 4

## Flags
- --local-folder <String>: 本地文件夹绝对路径 (必填)
- --remote-folder <String>: 钉盘文件夹 ID (dentryUuid) (必填)
- --space-id <String>: 钉盘空间 ID，不传则使用「我的文件」(可选)
- --if-exists <String>: 本地文件已存在时的策略: skip|smart|overwrite；命令会写本地，执行需确认 (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
