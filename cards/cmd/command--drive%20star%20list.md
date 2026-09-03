# dws drive star list

kind: command
completeness: full
usage: dws drive star list
description: 获取收藏列表
example: dws drive star list
source: internal/helpers/drive.go:3884
visible_flags: 6

## Flags
- --limit <Int>: 每页条数 (默认 20，最大 20)
- --cursor <String>: 分页游标
- --order-by <String>: 排序字段: createTime
- --sort <String>: 排序方向: asc|desc
- --resource-types <StringSlice>: 资源大类: DENTRY, TEAM, WORKSPACE
- --content-types <StringSlice>: 内容类型: doc,sheet,ppt,whiteboard,mind,notable,pdf,other,folder

## Related
- dws drive star add
- dws drive star remove
