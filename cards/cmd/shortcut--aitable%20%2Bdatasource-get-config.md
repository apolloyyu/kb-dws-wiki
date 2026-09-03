# dws aitable +datasource-get-config

kind: shortcut
completeness: full
description: 获取指定数据源表的同步配置信息，包括源配置、是否全量同步、是否自动同步、同步状态等。仅适用于数据源表（sync=true），普通表会返回错误。仅支持 OA 审批数据源（datasourceType=OA），其他数据源类型暂不支持，待后续开放。返回的 sourceConfig 包含数据源连接信息（如审批模板 ID、源表
source: internal/shortcut/aitable/datasource.go:348
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID
- --table-id <String>: 数据源表 ID（通过 +base-get / +table-list 获取，仅允许传入 sync=true 的表）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
