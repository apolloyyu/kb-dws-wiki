# dws whiteboard render

kind: command
completeness: partial
usage: dws whiteboard render
description: —
source: internal/helpers/whiteboard_render.go:31
visible_flags: 3
partial_reason: missing_description

## Flags
- --source <String> required: OpenNodes V1 JSON、@文件、文件路径或 -（必填）
- --output <String> required: 输出 SVG 文件路径（必填）
- --force <Bool>: 允许原子替换指定输出文件，仍须确认本地写入

## Related
- dws whiteboard create-with-content
- dws whiteboard export
- dws whiteboard export-get
- dws whiteboard query
- dws whiteboard template
- dws whiteboard update
