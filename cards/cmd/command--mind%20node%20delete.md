# dws mind node delete

kind: command
completeness: partial
usage: dws mind node delete
description: —
source: internal/helpers/mind.go:192
visible_flags: 5
partial_reason: missing_description

## Flags
- --node-id <String> required: 脑图文件 ID，不是主题 ID（必填）
- --page-id <String> required: 真实页面 ID（必填）
- --request-id <String> required: 稳定幂等键；恢复必须复用（必填）
- --topic-id <String> required: 真实主题 ID（必填）
- --expected-version <String>: 可选的期望版本；十进制字符串

## Related
- dws mind node create
- dws mind node list
- dws mind node update
