# dws wiki feed list

kind: command
completeness: full
usage: dws wiki feed list
description: 查询知识库动态列表
example: dws wiki feed list --workspace <workspaceId>
source: internal/helpers/wiki.go:1432
visible_flags: 4

## Flags
- --workspace <String>: 知识库 ID 或 URL (必填)
- --limit <Int>: 每页数量 (默认 10，最大 20)。用户未明确要求条数时禁止加此 flag，让服务端走默认 10
- --cursor <String>: 分页游标 (首页留空)
- --exclude-file <Bool>: 排除普通文件、媒体文件、文件夹及 Office 文件动态，仅保留在线文档操作（创建/更新/评论/点赞）。用户要求排除文件/只看文档操作时必须使用此 flag，禁止客户端过滤

## Related
- none
