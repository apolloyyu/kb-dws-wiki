# dws aitable +datasource-sync

kind: shortcut
completeness: full
usage: dws aitable +datasource-sync
description: 对指定 AI 表格中的数据源表触发一次手动同步。单次最多 5 张表，每张表独立提交，部分失败不影响其他表。该工具仅触发任务即返回，不会等待同步完成。返回结果包含文档链接，用户可打开文档查看同步进度与最终数据。同步运行中（errorCode=4014）属于幂等冲突，会被标记为 failed 并允许调用方稍后重试。非数据源
source: internal/shortcut/aitable/datasource.go:219
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID
- --table-ids <StringSlice>: 待触发同步的数据源表 ID 列表（通过 +base-get / +table-list 获取，仅允许 sync=true 的表，1-5 个）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
