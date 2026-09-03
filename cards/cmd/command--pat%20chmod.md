# dws pat chmod

kind: command
completeness: full
description: 授予指定权限
source: internal/pat/chmod.go:246
visible_flags: 8

## Flags
- --agentCode <String>: Agent 唯一标识（可选；也可通过 env DINGTALK_DWS_AGENTCODE 注入，flag 优先；未传则由服务端默认兜底）
- --grant-type <String>: 授权策略: once|session|permanent
- --session-id <String>: 会话标识（session 模式下必填）
- --product <StringArray>: 产品编码，可重复；与 --products 等价；执行批量授权需 --yes
- --products <StringSlice>: 产品编码列表，逗号分隔；执行批量授权需 --yes
- --domain <StringArray>: 产品域/产品编码，可重复；按产品 scope 模板批量授权；执行授权需 --yes
- --domains <StringSlice>: 产品域/产品编码列表，逗号分隔；执行批量授权需 --yes
- --recommend <Bool>: 使用推荐 scope 集合批量授权；执行授权需 --yes

## Related
- dws pat browser-policy
