---
title: 会话与消息(chat)
source_refs: internal/helpers/chat.go, internal/helpers/chat_media_upload.go, internal/shortcut/chat/unified_send.go, internal/shortcut/chat/chat_message.go, internal/shortcut/chat/chat_group.go, internal/shortcut/chat/chat_bot.go, internal/shortcut/chat/lark_alignment.go, internal/shortcut/chat/resource_download.go, internal/shortcut/chatmsg/chatmsg.go, internal/shortcut/builtin/builtin.go, internal/shortcut/adapter.go, internal/shortcut/runner.go, internal/helpers/ding.go, internal/shortcut/ding/ding.go
---

# 会话与消息(chat)

chat 能力分两层组织:原子 MCP 命令层与快捷命令层;DING 消息独立成组。

## 原子 MCP 命令层

`internal/helpers/chat.go`(约 10500 行)定义 `chatCmd`,`Use` 为 `chat`,下含:

- `group`:create / members add / remove / add-bot / rename;
- `message`:list / list-direct / list-all / list-by-sender / list-mentions / list-focused / list-topic-replies / search / search-advanced / send / send-by-bot / send-by-webhook / recall / recall-by-bot / edit / reply / forward / download-media / read-status / query-send-status,以及 emoji 回应(add-emoji / remove-emoji)、文字表情、置顶、收藏等消息级操作;
- `bot search`、`category`、`text` 等。

`file upload` 与 `media upload` 兼容入口(`internal/helpers/chat_media_upload.go`)均已下线:CLI 不再提供本地文件到 mediaId 的上传,发送本地图片/文件统一走 `chat message send --msg-type file --file`(CLI 内部完成上传并以可下载文件消息发送,不渲染为内联图片);已有 mediaId 时可用 `--msg-type image --media-id`。

经 `callMCPTool` / `callMCPToolOnServer("im"|"bot"|"chat", ...)` 路由到不同 MCP server。

## 快捷命令层

`internal/shortcut/chat/*.go` 为声明式 `shortcut.Shortcut`(`Service` 为 `"chat"`,命令名以 `+xxx` 形式),各文件 `init()` 调用 `shortcut.Register`;由 `internal/shortcut/builtin/builtin.go` 空白导入聚合,`shortcut.Commands()` 生成 cobra 树;`adapter.go` / `runner.go` 负责执行,`RuntimeContext.CallMCP` 落地。

## 关键映射(消息)

`internal/shortcut/chat/` 下的消息映射:

| Shortcut | 映射 |
|---|---|
| `unified_send.go` `+messages-send` | `send_personal_message` |
| `chat_message.go` `+messages-send-by-bot` | `send_robot_group_message` |
| `chat_message.go` `+messages-batch-send-by-bot` | `batch_send_robot_msg_to_users` |
| `chat_message.go` `+messages-send-by-webhook` | `send_message_by_custom_robot` |
| `chat_message.go` `+messages-recall` | 撤回 |
| `chat_message.go` `+messages-list` | 消息列表 |
| `resource_download.go` `+messages-resource-download` | 资源下载 |

## 群管理映射

| Shortcut | 说明 |
|---|---|
| `lark_alignment.go` `+chat-create` | 建群 |
| `chat_group.go` `+chat-search` | 群搜索 |
| `+chat-members-get` | 成员查询 |
| `+chat-transfer-owner` | 群主转让 |
| `+chat-quit` / `+chat-dismiss` | 退群 / 解散 |
| `+chat-set-admin` | 设置管理员 |
| `+chat-mute`(-member) | 禁言 |
| `+chat-role-*` | 角色相关 |
| `+chat-add-bot` | `add_robot_to_group` |
| `+chat-remove-bot` / `+chat-bots` | 移除/列出机器人 |

## 机器人

`chat_bot.go`:`+bot-search` / `+bot-find`。

## 消息结果投影与卡片读取边界

`internal/shortcut/chatmsg/chatmsg.go` 提供 `ProjectMessageV1`、`MessageResultContract` 只读投影;另有 `card_update.go`、`card_ref.go`、`send_status.go`、`search.go`。

`chat message list` 的稳定输出包含 `messageId` 与 `text`(`internal/helpers/chat.go:3301-3313`)。投影层会从 `content` / `text` 等字段读取内容并经 `CleanText` 生成可读文本(`internal/shortcut/chatmsg/chatmsg.go:238-259,347-370`)；对可识别的富内容卡片还会提取 `items[].data.text`(`:1196-1266,1284-1313`)。因此，命令没有承诺把任意卡片还原成完整原始 JSON 或结构化字段，但也不能概括成「卡片只有 msgType、没有任何可读文本」。

卡片能力须分开判断：

- **原始结构**：当前稳定投影不承诺返回完整原始卡片 JSON；
- **可读文本**：可识别富内容卡片会提取可读文本；
- **结构化解析**：只证明源码明确投影的字段，不能从可读文本反推完整结构；
- **渲染**：发送/更新卡片命令不证明读取路径能还原渲染结果；
- **解密**：加密的 card/robot ciphertext 只返回「无法解码」标记，不应与普通富内容卡片混为一谈。

## DING 消息

- 原子命令 `internal/helpers/ding.go`(`ding message` 组):
  - `send` → `send_ding_message`;
  - `recall`;
  - `list` → `list_ding_messages`(im server);
  - `receiver-status`;
  - `send-personal` → `send_personal_ding`;
  - `send-by-message` → `send_ding_by_message`;
  - `recall-personal`。
- 快捷命令 `internal/shortcut/ding/ding.go`:`+list`、`+receiver-status`、`+send-personal`(Product 均为 `"im"`)。
