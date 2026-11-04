# dws minutes template update

kind: command
completeness: partial
usage: dws minutes template update
description: —
source: internal/helpers/minutes.go:2393
visible_flags: 4
partial_reason: missing_description

## Flags
- --template-key <String> required: 本人个人模板templateKey，不是系统templateId
- --title <String>: 新标题，非空白，最多150个UTF-16单元
- --prompt <String>: 新提示词，原样保留格式；支持@文件或-
- --brief-intro <String>: 新简介；显式空串保留旧值

## Related
- dws minutes template create
- dws minutes template delete
- dws minutes template list-custom
- dws minutes template list-system
- dws minutes template set-default
