# dws drive mkdir

kind: command
completeness: full
usage: dws drive mkdir
description: Create a new folder in DingTalk Drive.
example: dws drive mkdir --name "项目资料"
use_when: When the agent organizes Drive output into a fresh folder before uploading files.
source: internal/helpers/drive.go:1204
visible_flags: 3

## Flags
- --name <String>: 文件夹名称，最长 50 字符 (必填)
- --space-id <String>: 目标空间 ID，不传则使用「我的文件」 (可选)
- --folder <String>: 父节点 ID (dentryUuid)，不传则在空间根目录下创建 (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
