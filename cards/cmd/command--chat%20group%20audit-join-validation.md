# dws chat group audit-join-validation

kind: command
completeness: partial
usage: dws chat group audit-join-validation
description: 审批入群验证（通过、拒绝、删除）
example: dws chat group audit-join-validation --conversation-id <openConversationId> --record-id 123456 --applicant <userId> --inviter <userId> --status AuditApprove
source: internal/helpers/chat.go:9700
visible_flags: 5
partial_reason: unverified_flags

## Flags
- --record-id <String> required: 申请记录 ID (必填)
- --status <String> required: 审批动作，真机仅 AuditApprove/AuditDelete 可用；AuditIgnore/AuditRefuse/AuditBlock 服务端拒绝 (必填)
- --applicant <String> required: 申请人 userId (必填)
- --inviter <String> required: 邀请人 userId (必填)
- --description <String>: 审批说明（可选）

## Related
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
- dws chat group invite-url
