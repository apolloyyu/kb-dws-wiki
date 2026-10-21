---
title: 清空会话记录的调用与作用域
maintenance: manual
intents: message_deletion
triggers: 删除聊天记录, 清空聊天记录, 删除个人聊天记录, 清空会话, 聊天记录删除, 聊天记录清理
contract:
  - 清空记录、撤回消息和清除红点不同；本人可见范围不证明云端物理删除、数据保留或跨设备同步机制。
---

# 清空会话记录的调用与作用域
- DWS 有清空指定会话中当前用户聊天记录的入口，调用服务端的 clear_conversation_messages；契约说明仅本人视角、不影响其他成员，且不可逆。不能把它说成只有本地缓存操作，也不能把「仅本人」推成云端物理保留或彻底删除结论。后两者及跨客户端同步须有服务端原文明示，否则标待核验。
  {{code: internal/shortcut/chat/chat_conversation.go | Command:     "+conversation-clear-messages"}}
  {{code: internal/shortcut/chat/chat_conversation.go | return rt.CallMCP("clear_conversation_messages"}}
  {{code: internal/helpers/chat.go | 仅清空当前用户视角的消息，不影响其他成员。}}
