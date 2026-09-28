# dws auth exchange

kind: command
completeness: partial
usage: dws auth exchange
description: 使用外部授权码登录并保存完整身份
example: dws auth exchange --code-stdin --client-id default --format json
source: internal/app/auth_exchange.go:23
visible_flags: 6
partial_reason: unverified_flags,empty_flag_name

## Flags
- --code <String>: 外部授权码；建议通过 --code-stdin 传递
- --code-stdin <Bool>: 从标准输入读取授权码（与 --code 互斥）
- --client-id <String>: default 使用官方默认应用；具体 ID 使用对应授权应用；省略沿用配置或默认应用
- --expected-user-id <String>: 预期 userId，仅作在线身份一致性校验
- --expected-corp-id <String>: 预期 corpId，仅作在线身份一致性校验
- --uid <String>: 预期 userId（同 --expected-user-id，不会覆盖在线身份）

## Related
- dws auth export
- dws auth import
- dws auth login
- dws auth logout
- dws auth migrate-keychain
- dws auth reset
