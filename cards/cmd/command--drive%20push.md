# dws drive push

kind: command
completeness: full
usage: dws drive push
description: 把本地文件夹单向镜像到钉盘（本地 → Drive）
example: dws drive push --local-folder /abs/path/repo --remote-folder <dentryUuid>
source: internal/helpers/drive.go:4115
visible_flags: 4

## Flags
- --local-folder <String>: 本地文件夹绝对路径 (必填)
- --remote-folder <String>: 钉盘目标文件夹 ID (dentryUuid) (必填)
- --space-id <String>: 钉盘空间 ID，不传则使用「我的文件」(可选)
- --if-exists <String>: 远端文件已存在时的策略: skip|smart|overwrite；命令会写钉盘，执行需确认 (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
