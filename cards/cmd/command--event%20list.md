# dws event list

kind: command
completeness: partial
usage: dws event list
description: 列出个人事件目录
example: dws event list --category card --format json
source: internal/app/event_command.go:837
visible_flags: 10
partial_reason: unverified_flags

## Flags
- --all <Bool>: 列出当前 edition 下所有 ClientID 的消费者
- --all-editions <Bool>: 跨 edition 列出（罕用，调试用）
- --client-id <String>: 指定具体 ClientID（覆盖凭证解析）
- --format (-f) <String>: 输出格式: table|json
- --as <String>: 事件身份: user
- --category <String>: 个人事件目录分类：im|oa|voip|todo|card|contact|minutes|calendar|appEvent；远端目录可能返回其他分类
- --keyword <String>: 按 eventKey 精确匹配（忽略大小写，登录后由远端目录执行）
- --producer-app-id <String>: 按事件生产者应用 ID 筛选应用事件
- … 2 more; use dwsdoc cmd/short for full flags

## Related
- dws event consume
- dws event schema
- dws event send
- dws event status
- dws event stop
