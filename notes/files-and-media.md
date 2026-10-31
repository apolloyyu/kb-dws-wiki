---
title: 富媒体与文件
source_refs: internal/helpers/drive.go, internal/helpers/drive_transfer.go, internal/helpers/doc_media_upload.go, internal/helpers/chat_media_upload.go, internal/helpers/form_share.go, internal/helpers/sheet_float_image_file.go, internal/helpers/aitable.go, internal/helpers/aitable_form_share_result.go, internal/helpers/doc.go, internal/helpers/sheet.go, internal/shortcut/doc/content_shortcuts.go, internal/shortcut/doc/common.go, internal/localio/download.go, internal/localio/upload.go, internal/localio/publish.go, internal/localio/input.go
---

# 富媒体与文件

本篇覆盖云盘上传/下载、文档与群聊媒体上传、AI 表格表单封面与二维码、doc/sheet 命令组织，以及产品共享的安全本地 I/O（`internal/localio`）。

## 云盘命令（internal/helpers/drive.go）

`newDriveCommand()`（约 L363）构建 `dws drive` 命令组，主要子命令：

| 子命令 | 入口 | 说明 |
|---|---|---|
| `upload` | 约 L1284，RunE=`runDriveUpload` | 上传本地文件到云盘 |
| `download` | 约 L684 | 从云盘下载文件 |
| `upload-info` / `commit` | 上传流程的独立步骤命令 | 获取上传凭证 / 提交上传 |
| `pull` / `push` / `sync` | 约 L3328 起 | 云盘与本地的同步 |

语义目录与快捷方式位于 `internal/shortcut/drive/`，配套目录数据见 `semantic_catalog_drive.json`。

## 上传机制：三步凭证化 PUT（非 multipart）

云盘上传不使用 multipart，而是纯 HTTP PUT + 凭证化，共三步：

1. `get_upload_info` —— 获取上传凭证；响应由 `parseDriveUploadInfo`（drive.go 约 L227）解析；
2. `httpPutFile` —— 携带凭证 PUT 上传文件体，见 `driveUploadPut`（drive_transfer.go）；
3. `commit_upload` —— 提交完成上传。

要点：

- 中心协议为 `uploadType=httpToCenterWithToken`；
- PUT 遇到 401/403 时重取凭证重试一次；
- `decorateUploadSizeError` 为超限错误补充友好提示；
- `httpPutFile` 是可注入变量（helpers/doc.go 约 L29），便于测试替换。

## 下载机制：两步 + 分片并发 + 断点续传

下载同样两步：先 `download_file` 取下载 URL 与 headers，再 GET 文件体。传输实现为 `driveTransferDownload`（drive_transfer.go）：

- 文件 ≥ 2×partSize 时先用 `probeRangeSupport` 探测 Range 支持，随后并发分片下载（`downloadRangedParts` / `fetchRangeInto`），默认分片 16MB、并发 4；
- 支持断点续传：中间文件 `<dest>.dwspart` 与元数据 `.dwspart.meta`，状态由 `driveDownloadCheckpoint` 维护；
- 下载中遇到 401/403 经 `driveCredentialState.refresh` single-flight 刷新凭证后重试，避免并发分片重复取凭证。

## 媒体上传（文档附件 / 群文件）

- 文档媒体上传：`internal/helpers/doc_media_upload.go` 的 `runDocMediaUpload`，流程为 `get_doc_attachment_upload_info` → PUT；doc media 命令组在 doc.go 约 L2966。
- 群聊文件上传：`internal/helpers/chat_media_upload.go`，命令挂在 chat.go 约 L2130。

## 表单封面与二维码（internal/helpers/form_share.go）

`dws aitable form share update` 的封面有三个互斥入口（`MarkFlagsMutuallyExclusive` + `corecmd.MutuallyExclusive`，aitable.go L10112 / L10125）：`--form-cover`（已公开的 URL）、`--form-cover-file`（本地图片）、`--form-cover-resource-id`（当前 Base 已上传的图片资源 ID）。标准命令与 shortcut 共用 `RunAitableFormShareUpdate`（form_share.go L133）。

- `--form-cover` 只校验 URL 结构，不验证可达性或图片内容（`ValidateFormShareURL`，L64）：必须字面 `https://` 前缀且主机名精确匹配 `formCoverAllowedHosts`（L54，共 6 个：img.alicdn.com、static.dingtalk.com、down-cdn.dingtalk.com、alidocs.oss-cn-zhangjiakou / alidocs2.oss-cn-zhangjiakou / alidocs.oss-cn-hangzhou.aliyuncs.com），端口只允许缺省或 443；含空白、未编码引号/括号、鉴权信息、查询参数、片段或 `/core/api/resources` 内部鉴权路径一律拒绝；空值/空白值直接报错，即省略保留原封面、不支持清空。
- `--form-cover-file` 的本地文件须为非空普通文件（复用 sheet 浮动图片的 `openFloatImageLocalFileNamed` / `validateFloatImageFileInfoNamed`，sheet_float_image_file.go L121 / L157），大小 ≤ 10 MiB，并用 `image.DecodeConfig` 嗅探真实格式、只接受 PNG/JPEG/GIF；`mimeType` 与上传文件名的扩展名都按嗅探结果重写，不信任输入文件名（L161-171）。
- 上传复用文档附件凭证契约：`get_doc_attachment_upload_info`（`resolveFloatImageUploadInfo`，封面路径把 `baseId` 当 `nodeId` 传入）→ PUT（`putFloatImageFileWithClient`）。该 PUT 客户端 5 分钟超时、`CheckRedirect` 返回 `http.ErrUseLastResponse`（不跟随重定向）、只接受 200，错误文案固定，不把签名 URL 或响应体写进错误；它有意不复用 `doc.defaultHTTPPutFile` 与 `localio.PutFile`（sheet_float_image_file.go L311-344）。
- 凭证本身也受校验：`uploadUrl` 必须是 HTTPS（仅当 `DWS_ALLOW_HTTP_ENDPOINTS=1` 且主机为 localhost / 127.0.0.1 / ::1 时放行 HTTP），`resourceUrl` 必须是不带 host、query、fragment 的相对路径（L264-291）。
- `--dry-run` 不上传，`formCoverResourceId` 用占位符 `<uploaded-image-resource-id>`（form_share.go L172-175）。
- 本地封面上传成功但 `update_share_form` 失败时，`formCoverUpdateError`（L195）克隆原错误而不是包装重放：保留错误分类/退出码与原始诊断，把 `formCoverResourceId` 补进 `details`，并置 `Retryable=false`、`RetryableSet=true`、`RetryAfterSeconds=nil`、`NextRetryAt=nil`，即整条命令禁止自动重试、清除重试时间建议；提示先回读 `form share get`，勿重复上传或原样重放（重放会再上传一个资源），且资源已公开无法随后续配置失败回滚。
- 终态校验里回读的 `formCover` 只是公开 URL，不能证明由哪个资源 ID 生成，因此 `formCoverResourceId` 保持 unverified（aitable_form_share_result.go L165）；判定为部分失败时仍从请求里把 `formCoverResourceId` 带进 `details`（L82）。

`dws aitable form share url` 先用与 `share get` 相同的只读退避重试读取 `get_share_form_config`，读取成功后才生成一次链接和二维码（aitable.go L6467-6475）：`writeFormShareURL`（form_share.go L92）只在 `enabled` 为真、未 `punished` 且 `shareFormUuid` 非空时交付链接；指定 `--qr-file` 时用 `qrcode.Encode(link, qrcode.Medium, 512)` 生成 PNG，并经 `localio.PublishBytes`（`BaseDir: "."`、`PreferredName: "form-qr.png"`）走与远端下载相同的符号链接安全 + fsync + 原子 no-clobber 落盘，结果里返回绝对路径。

## doc / sheet 命令组织

- 文档：`newDocCommand()`（internal/helpers/doc.go 约 L1249）；快捷层在 `internal/shortcut/doc/`。
- 电子表格：`newSheetCommand()`（internal/helpers/sheet.go 约 L23），按能力细分为 `sheet_dimension` / `sheet_chart` / `sheet_comment` / `sheet_float_image` / `sheet_filter_view` / `sheet_batch.go` 等文件；快捷层在 `internal/shortcut/sheet/`。

## 文档创建的标题去重（doc +create / doc create）

Markdown 正文开头与文档名相同的一级标题会在写入前被剥离，避免标题既进文档名又进正文：

- 实现为 `helpers.StripDuplicateTitle(markdown, name)`（internal/helpers/doc.go L5284）；`dws doc +create` 在 `--doc-format markdown` 且内容与名称均非空时调用（internal/shortcut/doc/content_shortcuts.go L106），标准命令 `dws doc create` 在 markdown 分支同样调用（doc.go L1741），JSONML 分支不做去重；
- `+create` 省略 `--name` 时先由 `docDefaultTitle` 从 Markdown 首个一级标题推断名称（content_shortcuts.go L103），再执行同一去重，因此推断出的标题也会被剥离；
- 判定规则：先跳过前导空行；首个非空行不是 `# ` 开头、或其前导空格超过 3 个（4 空格 / Tab 缩进即缩进代码块）时原样返回；标题文本经 `normalizeHeadingText`（doc.go L5323）去掉尾部 ATX `#` 与 `**` / `__` / `~~` / `*` / `_` / 反引号 后小写比较，与文档名不同则原样返回；
- 正文只剩该标题时结果为空字符串，`markdown` 参数不再下发（`--dry-run` 预览里也没有 `markdown` 字段）；
- 去重发生在分片（`SplitMarkdownForAppend`）与回读校验之前，`+create` 的回读校验比对的是剥离后的正文；
- `--content` 的字面量 / `-`（stdin）/ `@file` 三种输入都保留内容首尾空白（TrimSpace 后的值只用于判定 `-` 与 `@` 前缀），并统一把 CRLF / CR 归一为 LF（internal/shortcut/doc/common.go L63）。

## internal/localio：产品共享的安全本地 I/O

`internal/localio` 提供所有产品共用的安全文件操作：

- **download.go `Download`**：`ValidateDownloadURL` 仅信任 `dingtalk.com` / 阿里云 OSS 的 HTTPS 地址；解析目标 IP 排除公网 IP 防 SSRF；用 `os.Root` 打开目录防符号链接逃逸；写临时文件 + fsync 后原子 rename 发布；单文件上限 512MB。
- **upload.go `PutFile`**：向预签名 URL PUT 上传；拒绝 HTTP 重定向；上限 5GiB。
- **publish.go `PublishBytes`**：字节内容的安全落盘发布。
- **input.go `ReadTextInput`**：解析文本输入字面量 / `-`（stdin）/ `@file` 三种形式，上限 8MB。
