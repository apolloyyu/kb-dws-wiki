# dws minutes hot-word add

kind: command
completeness: full
usage: dws minutes hot-word add
description: Add a custom personal hot word to improve future speech-recognition accuracy on the user's minutes.
example: dws minutes hot-word add --words "钉钉"
use_when: When the user has domain-specific jargon or proper nouns that the ASR model mistranscribes.
source: internal/helpers/minutes.go:1254
visible_flags: 1

## Flags
- --words <String>: 要添加的热词，多个用逗号分隔 (必填)

## Related
- dws minutes hot-word delete
- dws minutes hot-word list
