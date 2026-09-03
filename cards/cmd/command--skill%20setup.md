# dws skill setup

kind: command
completeness: full
usage: dws skill setup
description: 安装 dws 自身 skill 到 Agent 目录
example: dws skill setup --mode multi --target claude --dry-run
source: internal/app/skill_setup.go:192
visible_flags: 6

## Flags
- --mode <String>: skill 模式：mono | multi（不指定则交互询问）
- --target <String>: 目标 Agent：all |
- --source <String>: skill 源目录（默认使用二进制内嵌的 skill 源，与当前版本一致）
- --yes <Bool>: 跳过确认提示（仅供脚本使用；删除操作仍会先备份到 ~/.dws/skill-backups/）
- --skill (-s) <StringSlice>: multi 模式：仅安装指定子 skill（可重复，接受短名 aitable 或全名 dingtalk-aitable）
- --exclude (-x) <StringSlice>: multi 模式：从全装中剔除指定子 skill（可重复，与 --skill 互斥）

## Related
- dws skill add
- dws skill find
- dws skill get
- dws skill install
- dws skill search
