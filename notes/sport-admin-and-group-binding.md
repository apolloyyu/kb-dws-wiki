---
title: 企业运动的管理员预判与比赛群绑定
source_refs: internal/helpers/sport.go, internal/helpers/sport_read.go, skills/mono/references/products/sport.md, skills/multi/dingtalk-misc/references/sport.md
---

# 企业运动的管理员预判与比赛群绑定

## 核对当前用户的管理员身份

`dws sport org admin --format json` 查询当前用户的企业管理员身份。`sport_read.go` 中的命令读取平台注入的用户与企业，上游 `sport.md` 说明其三个结果。成功且 `result=true` 表示企业主或子管理员，`result=false` 表示确认是非管理员。组织服务查询失败时先保留错误并提示重试，管理员身份仍待确认。

这条只读查询可用于受限操作前的提示。导出、删除或审批时，服务端会再检查实际权限。

{{code: internal/helpers/sport_read.go | func newSportOrgAdminCmd()}}

## 选择比赛所绑定的群标识

执行 `dws sport competition create` 时，`sport.go` 要求至少提供一个有效群标识。已知道数字群 ID 时填 `--group-id`，只有加密会话 ID 时填 `--open-conversation-id`。两者齐全时服务端以数字群 ID 为准。只给加密会话 ID 时，服务端解析后补齐群 ID。

上游 `sport.md` 建议从 `competition list`、`config` 或 `my-list` 的返回值取数字群 ID。通过 `dws chat` 取得的加密会话 ID 对应 `--open-conversation-id`。

{{code: internal/helpers/sport.go | 与 group-id 至少一个}}
