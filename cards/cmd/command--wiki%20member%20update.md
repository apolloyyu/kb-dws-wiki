# dws wiki member update

kind: command
completeness: full
description: 更新知识库成员权限
source: internal/helpers/wiki.go:663
visible_flags: 5

## Flags
- --workspace <String>: 知识库 ID 或 URL (必填)
- --users <String>: 被更新的用户 userId 列表，逗号分隔 (旧格式，单次最多 30 个)
- --role <String>: 新权限角色: MANAGER / EDITOR / DOWNLOADER / READER (旧格式必填，大小写不敏感)
- --members <String>: 成员列表 JSON 数组（新格式），支持 USER/DEPT/CONVERSATION/TAG 类型（TAG=角色组），与 --users 互斥
- --notify <Bool>: 是否通知被变更的成员（仅 --members 新格式时生效）

## Related
- dws wiki member add
- dws wiki member list
- dws wiki member remove
