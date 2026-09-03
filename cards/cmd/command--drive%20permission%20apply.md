# dws drive permission apply

kind: command
completeness: full
description: 发起权限申请
source: internal/helpers/drive.go:3201
visible_flags: 5

## Flags
- --node <String>: 目标节点 ID 或 URL (必填)
- --role <String>: 申请的角色: EDITOR / DOWNLOADER / READER (必填)
- --users <String>: 审批人 userId 列表，逗号分隔 (必填)
- --notify-mode <String>: 通知方式: DEFAULT / MSG_ACCOUNT / SINGLE_CHAT
- --reason <String>: 申请理由，最长 200 字符

## Related
- dws drive permission add
- dws drive permission apply-info
- dws drive permission get-setting
- dws drive permission list
- dws drive permission remove
- dws drive permission transfer-owner
