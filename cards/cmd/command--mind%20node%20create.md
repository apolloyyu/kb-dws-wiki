# dws mind node create

kind: command
completeness: partial
usage: dws mind node create
description: —
source: internal/helpers/mind.go:122
visible_flags: 7
partial_reason: missing_description

## Flags
- --node-id <String> required: 脑图文件 ID，不是主题 ID（必填）
- --page-id <String> required: 真实页面 ID（必填）
- --request-id <String> required: 稳定幂等键；恢复必须复用（必填）
- --parent-topic-id <String> required: 真实父主题 ID（必填）
- --topic <String> required: 主题 JSON 或文件：id、type、text（必填）
- --before-topic-id <String>: 插入到指定真实兄弟主题之前
- --expected-version <String>: 可选的期望版本；十进制字符串

## Related
- dws mind node delete
- dws mind node list
- dws mind node update
