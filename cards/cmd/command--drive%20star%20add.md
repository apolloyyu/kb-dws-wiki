# dws drive star add

kind: command
completeness: full
description: 添加协作者
source: internal/helpers/drive.go:2527
visible_flags: 6

## Flags
- --node <String>: 目标节点 ID 或 URL (必填)
- --users <String>: 用户 userId 列表，逗号分隔 (旧格式)
- --role <String>: 角色: MANAGER / EDITOR / DOWNLOADER / READER (旧格式必填)
- --workspace <String>: 知识库 ID (选填)
- --members <String>: 成员列表 JSON 数组（新格式），支持 USER/DEPT/CONVERSATION/TAG 类型（TAG=角色组），与 --users 互斥
- --notify <Bool>: 是否通知被添加的成员（仅 --members 新格式时生效，需显式传入才通知）

## Related
- dws drive star list
- dws drive star remove
