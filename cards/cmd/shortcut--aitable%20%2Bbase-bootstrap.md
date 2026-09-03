# dws aitable +base-bootstrap

kind: shortcut
completeness: full
description: 一次创建 Base、数据表和字段，逐层读回验证并在中断时报告已知副作用
source: internal/shortcut/aitable/base_composite.go:42
visible_flags: 4

## Flags
- --name <String>: 新 Base 名称
- --folder-id <String>: 目标知识库文件夹 ID（可选）
- --template-id <String>: 模板 ID（可选）
- --tables <String>: —

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-copy
