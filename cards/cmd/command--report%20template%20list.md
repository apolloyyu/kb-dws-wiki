# dws report template list

kind: command
completeness: full
description: List the report templates the current user is allowed to use.
use_when: When the agent picks the correct report template (e.g. "weekly", "daily") before creating a report.
source: internal/helpers/report.go:98
visible_flags: 0

## Flags
- none

## Related
- dws report template detail
- dws report template get
