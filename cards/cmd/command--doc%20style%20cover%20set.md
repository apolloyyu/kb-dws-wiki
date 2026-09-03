# dws doc style cover set

kind: command
completeness: full
usage: dws doc style cover set
description: 设置文档封面
example: dws doc style cover set --node DOC_ID --image https://img.example.com/cover.png
source: internal/helpers/doc_style.go:44
visible_flags: 4

## Flags
- --node <String>: 目标文档标识，支持 URL 或 ID (必填)
- --image <String>: 封面图片 URL (外链会自动转存为内部地址)
- --file <String>: 本地图片文件路径 (与 --image 互斥)
- --position <Float64>: 封面竖直位置 [0,1]，默认 0.5

## Related
- dws doc style cover clear
