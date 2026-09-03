# dws aisearch +search-behavior

kind: shortcut
completeness: full
description: 搜索发送、创建、分享、编辑或接收等企业行为记录
source: internal/shortcut/aisearch/aisearch.go:151
visible_flags: 6

## Flags
- --queries <StringSlice>: 内容关键词列表；汇总场景可留空
- --types <StringSlice>: —
- --behavior <String>: —
- --chat-scope <String>: 仅 IM 搜索时的会话或群范围
- --time-range <String>: 服务端自然语言时间范围
- --direction <String>: 交互方向，如我->同事

## Related
- dws aisearch +search-enterprise
- dws aisearch +search-person
