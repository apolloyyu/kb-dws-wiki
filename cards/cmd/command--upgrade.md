# dws upgrade

kind: command
completeness: full
usage: dws upgrade
description: 升级 DWS CLI 到最新版本
example: dws upgrade
source: internal/app/upgrade.go:96
visible_flags: 8

## Flags
- --check <Bool>: 仅检查是否有新版本
- --list <Bool>: 列出正式 release 版本（配合 --beta 查看 beta）
- --all <Bool>: 与 --list 搭配，显示所选轨道的全部版本
- --version <String>: 升级到指定版本
- --beta <Bool>: 使用最新 beta 预发布版本（默认使用正式 release）
- --rollback <Bool>: 回滚到上一版本
- --force <Bool>: 即使已是最新版本也强制重新安装当前版本
- --skip-skills <Bool>: 跳过技能包更新

## Related
- none
