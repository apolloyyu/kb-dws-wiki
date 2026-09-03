# dws drive publish set

kind: command
completeness: full
usage: dws drive publish set
description: [危险] 设置文件为互联网公开
example: dws drive publish set --node <fileId> --format json
source: internal/helpers/drive.go:3446
visible_flags: 4

## Flags
- --node <String>: 目标文件 ID (dentryUuid) 或 URL (必填)
- --permission <String>: 公开后的权限: READER / DOWNLOADER(默认) / EDITOR
- --password <String>: 访问密码：传非空值设置/修改密码，传空字符串清除密码，不传则不改变
- --expire-days <Int>: 公开有效期天数：0 表示永久有效

## Related
- dws drive publish get
- dws drive publish unset
