# dws report template detail

kind: command
completeness: full
description: Retrieve the detailed schema of a report template by name, including required fields.
use_when: When the agent needs to know a template's field structure before calling `report create`.
source: internal/helpers/report.go:177
visible_flags: 0

## Flags
- none

## Related
- dws report template get
- dws report template list
