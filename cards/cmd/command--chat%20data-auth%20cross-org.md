# dws chat data-auth cross-org

kind: command
completeness: full
usage: dws chat data-auth cross-org
description: 授予跨组织 chat 数据访问权限
example: dws chat data-auth cross-org --target-org-id 439446171
source: internal/helpers/chat.go:3023
visible_flags: 7

## Flags
- --target-org-id <String>: 目标组织 ID（与 --all 二选一）
- --all <Bool>: 授权所有目标组织
- --agentCode <String>: Agent 标识，默认 wukong
- --grant-type <String>: 授权策略: once|session|timed|permanent
- --ttl <String>: timed 授权有效期，如 1h/4h/24h/7d
- --session-id <String>: session 授权的会话标识
- --yes (-y) <Bool>: 确认执行跨组织 chat 数据授权

## Related
- none
