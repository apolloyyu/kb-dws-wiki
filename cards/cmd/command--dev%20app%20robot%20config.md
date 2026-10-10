# dws dev app robot config

kind: command
completeness: partial
usage: dws dev app robot config
description: —
source: internal/helpers/devapp.go:1321
visible_flags: 14
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --name <String>: 机器人名称
- --brief <String>: 机器人简介
- --desc <String>: 机器人描述
- --icon-media-id <String>: 机器人图标 mediaId
- --outgoing-url <String>: 消息回调地址
- --event-callback-url <String>: 事件回调地址
- --mode <String>: 机器人模式：HTTPS / STREAM / AISKILL
- --skills <String>: 技能列表，多个用逗号或分号分隔
- … 5 more; use dwsdoc cmd/short for full flags

## Related
- dws dev app robot disable
- dws dev app robot enable
- dws dev app robot get
- dws dev app robot result
- dws dev app robot submit
