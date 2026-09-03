# dws chat text translate

kind: command
completeness: full
usage: dws chat text translate
description: 翻译文本内容
example: dws chat text translate --query "你好世界" --to en_US
source: internal/helpers/chat.go:10948
visible_flags: 2

## Flags
- --query <String> required: 待翻译的文本内容 (必填)
- --to <String> required: 目标语言代码 (必填，默认 en_US)

## Related
- none
