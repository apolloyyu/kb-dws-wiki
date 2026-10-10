# dws dingtalk-tag manage save-draft

kind: command
completeness: partial
usage: dws dingtalk-tag manage save-draft
description: —
source: internal/helpers/deap_agent.go:390
visible_flags: 9
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 数字员工 ID
- --name <String>: 数字员工名称（最多 30 个 Unicode 码点）
- --description <String>: 数字员工职责描述（最多 300 个 Unicode 码点）；不传保持原值
- --avatar-url <String>: 公网 HTTP(S) 头像地址，或本地 jpg/jpeg/png/gif/webp 图片路径（最大 10 MiB）；本地文件由 CLI 自动上传，不传保持原值
- --dept-id <String>: 归属部门 ID；不传保持原部门，不支持清空
- --prompt <String>: 人设/System Prompt（最多 5000 个 Unicode 码点）
- --supervisor-user-id <String>: 直属上级 userId
- --type <String>: 可选主程序类型：open_code 或 local_agent；未修改时省略（保持草稿原值），也可显式传 open_code；保持或切换为本地 Agent/DSH 模式时传 local_agent
- --response-mode <String>: 响应模式：mention_only、targeted_proactive，或英文逗号分隔的组合 mention_only,targeted_proactive；未传时保持草稿原值

## Related
- dws dingtalk-tag manage create
- dws dingtalk-tag manage delete
- dws dingtalk-tag manage detail
- dws dingtalk-tag manage list
- dws dingtalk-tag manage login
- dws dingtalk-tag manage publish
