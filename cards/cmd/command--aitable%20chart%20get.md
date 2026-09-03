# dws aitable chart get

kind: command
completeness: full
description: Retrieve a chart's full configuration and metadata.
use_when: When the agent needs to inspect an existing chart to clone it or adjust its configuration.
source: internal/helpers/aitable.go:1812
visible_flags: 1

## Flags
- --base-id <String>: Base 唯一标识。优先使用 base search / base list 返回值 (必填)

## Related
- dws aitable chart create
- dws aitable chart delete
- dws aitable chart update
- dws aitable chart widgets-example
