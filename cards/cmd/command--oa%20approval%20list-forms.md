# dws oa approval list-forms

kind: command
completeness: full
description: List approval process templates (forms) the current user is allowed to initiate.
use_when: When the agent needs to pick the right approval form before submitting a new request.
source: internal/helpers/oa.go:1360
visible_flags: 3

## Flags
- --cursor <String>: 分页游标（默认 0，翻页传返回的 cursor）
- --limit <String>: 每页大小（默认 100，最大 100）
- --size <String>: 每页大小（默认 100，最大 100）

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
