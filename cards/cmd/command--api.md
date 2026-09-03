# dws api

kind: command
completeness: full
usage: dws api <METHOD> <PATH> [flags]
description: 调用钉钉 OpenAPI (Raw HTTP)
example: dws api GET /v1.0/microApp/allApps
source: internal/app/api_command.go:61
visible_flags: 7

## Flags
- --params <String>: 查询参数 JSON (支持 @file 或 - 从 stdin 读取)
- --data <String>: 请求体 JSON (支持 @file 或 - 从 stdin 读取)
- --file <String>: multipart 文件 [field=]path 或 [field=]-
- --page-all <Bool>: 自动遍历所有分页
- --page-limit <Int>: 最大翻页数 (0=不限, 默认10, 硬上限500)
- --page-delay <Int>: 分页间隔毫秒
- --base-url <String>: 覆盖 API 基础 URL (默认 https://api.dingtalk.com)

## Related
- none
