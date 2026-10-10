# dws dev app robot submit

kind: command
completeness: partial
usage: dws dev app robot submit
description: —
source: internal/helpers/devapp.go:1191
visible_flags: 6
partial_reason: missing_description

## Flags
- --name <String> required: 智能体应用名称，长度 2-20，企业内唯一 (必填)
- --robot-name <String> required: 承载机器人名称，用于客户端展示 (必填)
- --desc <String> required: 机器人功能描述，不超过 200 字 (必填)
- --icon-media-id <String>: 机器人图标 mediaId；为空时使用默认图标
- --preview-media-id <String>: 机器人预览图 mediaId；为空时复用图标
- --task-id <String>: 失败重试时传入原 taskId；为空时服务端自动生成

## Related
- dws dev app robot config
- dws dev app robot disable
- dws dev app robot enable
- dws dev app robot get
- dws dev app robot result
