# dws wiki member remove

kind: command
completeness: full
usage: dws wiki member remove
description: 移除知识库成员
example: dws wiki member remove --workspace <workspaceId> --users uid1
source: internal/helpers/wiki.go:856
visible_flags: 3

## Flags
- --workspace <String>: 知识库 ID 或 URL (必填)
- --users <String>: 被移除的用户 userId 列表，逗号分隔 (旧格式，单次最多 30 个)
- --members <String>: 成员列表 JSON 数组（新格式），只需 type 和 id（USER/DEPT/TAG 还需 corpId），与 --users 互斥

## Related
- dws wiki member add
- dws wiki member list
- dws wiki member update
