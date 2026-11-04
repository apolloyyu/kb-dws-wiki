# dws minutes template create

kind: command
completeness: partial
usage: dws minutes template create
description: —
source: internal/helpers/minutes.go:2372
visible_flags: 3
partial_reason: missing_description

## Flags
- --title <String> required: 非空白标题，最多150个UTF-16单元
- --prompt <String> required: 完整提示词，保留格式；支持@文件或-
- --brief-intro <String>: 模板简介；省略或空串由服务异步生成

## Related
- dws minutes template delete
- dws minutes template list-custom
- dws minutes template list-system
- dws minutes template set-default
- dws minutes template update
