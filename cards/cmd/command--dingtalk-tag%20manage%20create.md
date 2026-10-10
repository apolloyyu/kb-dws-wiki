# dws dingtalk-tag manage create

kind: command
completeness: partial
usage: dws dingtalk-tag manage create
description: —
source: internal/helpers/deap_agent.go:232
visible_flags: 8
partial_reason: missing_description

## Flags
- --name <String> required: 数字员工名称，同组织内唯一（最多 30 个 Unicode 码点）
- --description <String> required: 数字员工职责描述（最多 300 个 Unicode 码点）
- --type <String> required: 必填主程序类型：open_code 或 local_agent；必须显式填写且不能为空；接入本地 Agent/DSH 时传 local_agent
- --prompt <String>: 可选人设/System Prompt（最多 5000 个 Unicode 码点）；local_agent 省略时自动设置默认人设，其他类型省略时提醒补齐；不能显式为空
- --dept-id <String>: 归属部门 ID；不传时服务端使用操作人主任职部门
- --avatar-url <String>: 公网 HTTP(S) 头像地址，或本地 jpg/jpeg/png/gif/webp 图片路径（最大 10 MiB）；本地文件由 CLI 自动上传
- --supervisor-user-id <String>: 直属上级 userId
- --response-mode <String>: 响应模式：mention_only、targeted_proactive，或英文逗号分隔的组合 mention_only,targeted_proactive；未提供或空值时默认 mention_only

## Related
- dws dingtalk-tag manage delete
- dws dingtalk-tag manage detail
- dws dingtalk-tag manage list
- dws dingtalk-tag manage login
- dws dingtalk-tag manage publish
- dws dingtalk-tag manage save-draft
