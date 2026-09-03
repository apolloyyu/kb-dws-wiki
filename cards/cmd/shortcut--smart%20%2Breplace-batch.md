# dws smart +replace-batch

kind: shortcut
completeness: full
usage: dws smart +replace-batch
description: 预检并批量执行多组听记文字替换，逐项验证且失败必定非零
source: internal/shortcut/smart/replace_batch.go:46
visible_flags: 5

## Flags
- --id <String>: 听记 taskUuid（必填）
- --pair <StringSlice>: —
- --json <String>: 替换规则 JSON 字面量、@相对文件或 - 表示 stdin
- --failure-policy <String>: —
- --page-limit <Int>: —

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
