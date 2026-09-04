# dws aitable base update

kind: command
completeness: full
usage: dws aitable base update
description: Update mutable properties of an AI table (Base), such as its name or icon.
example: dws aitable base update --base-id BASE_ID --name "新名称"
use_when: When the agent needs to rename or rebrand an existing Base without touching its data.
source: internal/helpers/aitable.go:1909
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --name <String>: 新名称，1-50 字符 (必填)
- --desc <String>: 备注文本

## Related
- dws aitable base copy
- dws aitable base create
- dws aitable base delete
- dws aitable base get
- dws aitable base get-primary-doc-id
- dws aitable base list
