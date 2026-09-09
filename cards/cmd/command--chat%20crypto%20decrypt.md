# dws chat crypto decrypt

kind: command
completeness: full
usage: dws chat crypto decrypt
description: 解密一条三方密文消息
source: internal/helpers/chat_crypto_command.go:74
visible_flags: 3

## Flags
- --layer <String>: 解密层: full|safechat|ding
- --text <String>: 输入文本
- --file <String>: 输入文件路径；- 表示 stdin

## Related
- none
