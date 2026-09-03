# dws chat bot search

kind: command
completeness: full
usage: dws chat bot search
description: Search robots (bots) created by the current user by keyword.
example: dws chat bot search --page 1
use_when: When the agent needs to resolve one of its own bots by name to a robot code before sending bot messages.
source: internal/helpers/chat.go:5049
visible_flags: 3

## Flags
- --page <Int>: 页码，从1开始
- --size <Int>: 每页条数 (默认50)
- --name <String>: 按名称搜索

## Related
- dws chat bot find
