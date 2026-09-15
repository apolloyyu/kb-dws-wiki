# dws doc +script

kind: shortcut
completeness: full
usage: dws doc +script
description: 初始化本地文档草稿，或检查Markdown/JSONML结构和字数
source: internal/shortcut/doc/script_shortcut.go:24
visible_flags: 7

## Flags
- --command <String>: —
- --content <String>: —
- --node <String>: parse可读取的文档ID/URL；与content互斥；parse恰好提供content或node；init-draft不接受二者；字数上下界非负且顺序正确
- --doc-format <String>: —
- --min-words <Int>: 最少字数，0不限制；汉字逐字、其他字母数字连续词计数；parse恰好提供content或node；init-draft不接受二者；字数上下界非负且顺序正确
- --max-words <Int>: 最多字数，0不限制；parse恰好提供content或node；init-draft不接受二者；字数上下界非负且顺序正确
- --required-blocks <StringSlice>: 要求至少出现一次的块类型，如heading,paragraph,table（Markdown）或h1,p,table（JSONML）

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
