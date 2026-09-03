# dws report template detail

kind: command
completeness: full
usage: dws report template detail
description: Retrieve the detailed schema of a report template by name, including required fields.
example: dws report template detail --name <templateName>
use_when: When the agent needs to know a template's field structure before calling `report create`.
source: internal/helpers/report.go:177
visible_flags: 1

## Flags
- --name <String>: 模版名称 (必填)

## Related
- dws report template get
- dws report template list
