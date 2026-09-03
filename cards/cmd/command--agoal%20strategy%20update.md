# dws agoal strategy update

kind: command
completeness: full
usage: dws agoal strategy update
description: 更新战略解码
example: dws agoal strategy update --profile-id PROFILE_ID --content '[{"id":"entity1","title":{"title":"新目标"},"entityType":"OGSM_OBJECTIVE","status":"NORMAL","executors":["dingId1"],"teams":["deptDingId1"]}]'
source: internal/helpers/agoal.go:98
visible_flags: 3

## Flags
- --profile-id <String>: 战略解码 id (必填)
- --content <String>: 实体列表 JSON 数组 (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal strategy detail
- dws agoal strategy list
