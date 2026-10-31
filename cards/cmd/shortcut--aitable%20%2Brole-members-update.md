# dws aitable +role-members-update

kind: shortcut
completeness: full
usage: dws aitable +role-members-update
description: 完整替换自定义角色成员并显式保留默认角色
source: internal/shortcut/aitable/aitable.go:3268
visible_flags: 5

## Flags
- --base-id <String>: 目标 Base ID（String）
- --role-id <String>: 目标自定义角色 ID（long 形态 String）
- --members <String>: DWS 必填，非空全替换，[] 清空，不接受 null；
- --default-role-mode <Int>: DWS 必填，仅支持 0/1/2，须按 role-list 回读值保留默认角色：0=无兜底、1=指定自定义角色、2=继承文档权限
- --default-role-id <String>: 仅 default-role-mode=1 时必填且非空，使用当前默认自定义角色 ID（long 形态 String）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
