# dws whiteboard +insert-image

kind: shortcut
completeness: full
usage: dws whiteboard +insert-image
description: 把本地 PNG/JPEG 插入已有文档内嵌或独立白板
source: internal/shortcut/whiteboard/insert_image.go:71
visible_flags: 8

## Flags
- --node <String>: —
- --part-id <String>: 文档内白板 part ID；
- --page-id <String>: 独立白板目标页面 ID；
- --file <String>: —
- --x <Int>: —
- --y <Int>: —
- --width <Int>: 显示宽度，整数像素；不提供时最大 800px；
- --height <Int>: 显示高度，整数像素；

## Related
- dws whiteboard +diff
- dws whiteboard +query
- dws whiteboard +update
