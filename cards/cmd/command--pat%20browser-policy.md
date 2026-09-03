# dws pat browser-policy

kind: command
completeness: full
description: 配置 PAT 授权时是否打开浏览器
source: internal/pat/browser_policy.go:240
visible_flags: 2

## Flags
- --enabled <Bool>: PAT 撞墙时是否允许本地打开浏览器
- --agentCode <String>: Agent 唯一标识（可选；不填则写入全局默认策略，不从 env DINGTALK_DWS_AGENTCODE 回退）

## Related
- dws pat chmod
