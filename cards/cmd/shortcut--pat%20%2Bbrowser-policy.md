# dws pat +browser-policy

kind: shortcut
completeness: full
usage: dws pat +browser-policy
description: 安全配置 PAT 授权时是否允许打开本地浏览器
source: internal/shortcut/pat/pat.go:45
visible_flags: 2

## Flags
- --enabled <Bool>: —
- --agent-code <String>: 可选 Agent 标识必须为 1 到 64 位字母、数字、下划线或连字符；只用于定位本地策略项且不会出现在结果中

## Related
- dws pat +authorize
