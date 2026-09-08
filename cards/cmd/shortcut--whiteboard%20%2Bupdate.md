# dws whiteboard +update

kind: shortcut
completeness: full
usage: dws whiteboard +update
description: 确认后更新文档内嵌或独立白板并精确读回
source: internal/shortcut/whiteboard/whiteboard.go:271
visible_flags: 6

## Flags
- --node <String>: 承载文档或独立白板的节点 ID/URL；--node 去除空白后不能为空
- --part-id <String>: 文档内白板 part ID；显式提供时选择内嵌分支。显式非空 part-id 选择内嵌分支并禁止 revision/requestId；未提供 part-id 时独立分支要求 expected-revision/request-id，ove
- --source <String>: OpenNodes V1 JSON，不能为空；支持字面量、@相对文件或 - 从 stdin 读取
- --page-id <String>: 目标页面 ID；独立白板 overwrite 时必填。显式非空 part-id 选择内嵌分支并禁止 revision/requestId；未提供 part-id 时独立分支要求 expected-revision/request-id，ov
- --expected-revision <Int>: 独立白板最新 revision；必须为非负整数。显式非空 part-id 选择内嵌分支并禁止 revision/requestId；未提供 part-id 时独立分支要求 expected-revision/request-id，overw
- --request-id <String>: 独立白板 1-128 字符稳定幂等请求 ID。显式非空 part-id 选择内嵌分支并禁止 revision/requestId；未提供 part-id 时独立分支要求 expected-revision/request-id，overwr

## Related
- dws whiteboard +query
