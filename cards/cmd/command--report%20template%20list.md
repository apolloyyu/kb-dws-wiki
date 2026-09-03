# dws report template list

kind: command
completeness: full
usage: dws report template list
description: List the report templates the current user is allowed to use.
example: dws report template list
use_when: When the agent picks the correct report template (e.g. "weekly", "daily") before creating a report.
source: internal/helpers/report.go:98
visible_flags: 0

## Flags
- none

## Related
- dws report template detail
- dws report template get
