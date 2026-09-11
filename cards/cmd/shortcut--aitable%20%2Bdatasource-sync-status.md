# dws aitable +datasource-sync-status

kind: shortcut
completeness: full
usage: dws aitable +datasource-sync-status
description: 按任务 ID 查询指定数据源表的同步任务状态。与 +datasource-sync / +datasource-create / +datasource-update 配对使用，单次最多 5 个 taskId。仅 RUNNING 需要继续轮询；FINISHED、FAILED、NOT_FOUND 为终态；UNKNOWN
source: internal/shortcut/aitable/datasource.go:298
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID
- --table-id <String>: 数据源表 ID（通过 +base-get / +table-list 获取，仅允许传入 sync=true 的表）
- --task-ids <StringSlice>: 待查询的同步任务 ID 列表（由 +datasource-sync / +datasource-create / +datasource-update 返回）。单次最多 5 个，超出请拆分多次调用。

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
