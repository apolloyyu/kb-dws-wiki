# dws devapp +robot-config

kind: shortcut
completeness: full
usage: dws devapp +robot-config
description: 创建或更新现有应用的机器人配置（upsert）
source: internal/shortcut/devapp/devapp.go:1647
visible_flags: 11

## Flags
- --unified-app-id <String>: 开放平台统一应用 ID
- --name <String>: 机器人名称；至少提供一项非空机器人配置；布尔开关显式传入 false 也算配置
- --brief <String>: 机器人简介；至少提供一项非空机器人配置；布尔开关显式传入 false 也算配置
- --desc <String>: 机器人描述；至少提供一项非空机器人配置；布尔开关显式传入 false 也算配置
- --icon-media-id <String>: 机器人图标 mediaId；至少提供一项非空机器人配置；布尔开关显式传入 false 也算配置
- --outgoing-url <String>: 消息回调地址；至少提供一项非空机器人配置；布尔开关显式传入 false 也算配置
- --event-callback-url <String>: 事件回调地址；至少提供一项非空机器人配置；布尔开关显式传入 false 也算配置
- --mode <String>: —
- --skills <StringSlice>: 技能列表；至少提供一项非空机器人配置；布尔开关显式传入 false 也算配置
- --add-scope <Bool>: 是否自动添加机器人相关权限；至少提供一项非空机器人配置；布尔开关显式传入 false 也算配置
- --disable-ssl-verify <Bool>: 回调地址是否关闭 SSL 校验；至少提供一项非空机器人配置；布尔开关显式传入 false 也算配置

## Related
- dws devapp +create
- dws devapp +credentials-get
- dws devapp +delete
- dws devapp +disable
- dws devapp +enable
- dws devapp +event-list
