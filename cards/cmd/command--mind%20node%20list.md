# dws mind node list

kind: command
completeness: partial
usage: dws mind node list
description: —
source: internal/helpers/mind.go:85
visible_flags: 7
partial_reason: missing_description

## Flags
- --node-id <String> required: 脑图文件 ID，不是主题 ID（必填）
- --page-id <String>: 真实页面 ID
- --topic-id <String>: 真实主题 ID；ROOT 模式省略
- --mode <String>: ROOT/NODE/CHILDREN/SUBTREE(可选: ROOT|NODE|CHILDREN|SUBTREE)
- --depth <String>: 查询层数 1-8，包含起点
- --max-results <String>: 单页最多主题数 1-200
- --next-token <String>: 上页返回的 mindc1_ 分页游标；空字符串按首次查询处理

## Related
- dws mind node create
- dws mind node delete
- dws mind node update
