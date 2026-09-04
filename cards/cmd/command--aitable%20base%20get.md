# dws aitable base get

kind: command
completeness: full
usage: dws aitable base get
description: Retrieve metadata for a single AI table (Base), including name, owner, and structural summary.
example: dws aitable base get --base-id BASE_ID
use_when: When the agent needs to inspect a specific Base before performing further operations on it.
source: internal/helpers/aitable.go:1824
visible_flags: 1

## Flags
- --base-id <String>: Base 唯一标识。优先使用 base search / base list 返回值 (必填)

## Related
- dws aitable base copy
- dws aitable base create
- dws aitable base delete
- dws aitable base get-primary-doc-id
- dws aitable base list
- dws aitable base search
