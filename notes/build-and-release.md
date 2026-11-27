---
title: 构建发布与版本
source_refs: Makefile, scripts/dev/build.sh, scripts/dev/build-all.sh, internal/app/version.go, pkg/cli/cli.go, internal/app/upgrade.go, internal/upgrade/github.go, internal/upgrade/version.go, internal/upgrade/downloader.go, internal/upgrade/verify.go, internal/upgrade/replacer.go, internal/upgrade/rollback.go, Formula/dingtalk-workspace-cli.rb, .goreleaser.yaml, scripts/release/run-goreleaser-cross.sh, scripts/release/post-goreleaser.sh, scripts/release/publish-homebrew-formula.sh, build/homebrew.rb.tmpl, build/homebrew-release.rb.tmpl, internal/buildversion/version.go, internal/buildversion/stamp.go, internal/upgrade/paths.go, internal/app/flags.go, internal/upgrade/source.go, internal/upgrade/registry.go
---

# 构建发布与版本

本篇覆盖 Makefile 目标、构建脚本、版本注入、`dws upgrade` 自升级与发布物。

## Makefile 主要目标

| 目标 | 说明 |
|---|---|
| `build` / `rebuild` | 调 `scripts/dev/build.sh` |
| `test` | `go test ./...` |
| `policy` | 跑 `scripts/policy/` 下检查：`check-open-source-assets.sh`、`check-schema-catalog.sh`、`check-schema-binary.sh` 等 |
| `generate-schema` | `go generate ./internal/cli` + `check-schema-assembly.sh`；仅刷新 `param_aliases_generated.go` 并验证装配确定性 |
| `package` | `build-all.sh` + `scripts/release/post-goreleaser.sh` |
| `release-pre` / `release-stable` | `scripts/release/release.sh` |
| `publish-homebrew-formula` | 发布 Homebrew 配方 |

## 构建脚本

- `scripts/dev/build.sh`：先跑 `scripts/policy/check-runtime-payload.sh --allow-unsupported-tools`，再 `CGO_ENABLED="${CGO_ENABLED:-1}" go build -buildmode=pie -trimpath -ldflags="-s -w" -o dws ./cmd`，最后按当前 OS/架构调 `scripts/build/attach-runtime-payload.sh <os> <arch> dws` 附加 runtime payload（无法识别的平台/架构打印提示后 `exit 0`）。**注意**：裸 `go build ./cmd` 会失败（输出名与目录冲突），必须 `-o dws`。
- `scripts/dev/build-all.sh`：不再自己拼 ldflags，改为 `VERSION`（默认 `0.0.0-SNAPSHOT`）去掉前导 `v` 后，以 `DWS_PACKAGE_VERSION` + `GORELEASER_CURRENT_TAG` 调 `scripts/release/run-goreleaser-cross.sh release --snapshot --clean --skip=publish --parallelism=2`。
- `scripts/release/run-goreleaser-cross.sh`：在摘要固定的 `ghcr.io/goreleaser/goreleaser-cross:v1.26.2` 容器内跑 GoReleaser（宿主必须有 `docker` 与 `curl`），按 SHA256 校验下载并缓存 GoReleaser 2.16.0 与 Zig 0.15.2；Linux 用 `zig cc` 锁 `gnu.2.17`，Darwin 走 osxcross 并固定 `MACOSX_DEPLOYMENT_TARGET=11.0`，Windows 走 mingw / llvm-mingw；`--exec` 模式用同一套 CGO 工具链执行传入命令。
- `.goreleaser.yaml`：ldflags `-s -w` + `-X internal/app.version=v{{.Version}}` / `gitCommit={{.Commit}}` / `buildTime={{.CommitDate}}` 注入版本信息；`CGO_ENABLED=1`、`GOTOOLCHAIN=go1.25.9`、`-buildmode=pie -trimpath`；darwin/linux/windows × amd64/arm64 共 6 平台交叉构建；归档 `dws-{os}-{arch}.tar.gz`（windows 为 zip），内含 LICENSE/NOTICE/README.md/CHANGELOG.md；产出 `checksums.txt`（SHA256）；snapshot 版本取 `DWS_PACKAGE_VERSION`；release 为 `draft: true`、`mode: replace`、owner 取 `GITHUB_REPOSITORY_OWNER`。
- `scripts/release/post-goreleaser.sh`（`make package` 第二步）：版本解析优先级 `DWS_PACKAGE_VERSION` → `git describe --tags --exact-match` → `internal/app/version.go` 的 `var version`（仍为 `dev` 则报错）；随后为各平台归档注入 runtime payload 并确定性重打包（同步改写 `checksums.txt` 对应行）、签名 darwin 归档（配置 `DWS_APPLE_CERTIFICATE_P12` + `DWS_APPLE_CERTIFICATE_PASSWORD_FILE` 时用 `rcodesign` 做 Developer ID 签名，否则 ad-hoc：`codesign` 或 `rcodesign`）、生成 `dist/dws-skills.zip`、暂存 npm 包到 `dist/npm/dingtalk-workspace-cli/`、渲染 Homebrew 配方到 `dist/homebrew/`。

## 版本变量

- `internal/app/version.go`：`var version = "dev"`，提供 `SetVersion()` / `RawVersion()`；
- `pkg/cli/cli.go`：`SetVersion` 供 overlay 注入。
- `internal/buildversion`：版本戳与二进制封印的唯一归属。`Set(version, commit, buildTime)` 保存戳（默认 `dev`/`unknown`/`unknown`，空入参保留原值），`Format` 产出 `version (commit, buildTime)`；`Digest()` 是持久化 Schema 缓存身份必须匹配的二进制封印——已打戳的构建只用戳材料，未打戳的本地构建再折进 `os.Executable()` 的 path/size/mtime 指纹（刻意不做整文件哈希）。`internal/app/version.go` 的 `init()` 与 `SetVersion()` 都会把 ldflags 注入值同步到这里。

## 自升级（dws upgrade）

命令入口 `internal/app/upgrade.go`，支持 `--check` / `--list` / `--all` / `--version` / `--rollback` / `--force` / `--skip-skills` / `--beta` / `--dry-run`；`--beta` 与 `--version` 互斥（装指定 beta 直接用 `--version vX.Y.Z-beta.N`）；`--dry-run`（“预览操作内容，不实际执行”）与 `-y`/`--yes` 是根命令持久 flag（`internal/app/flags.go`），新增 `--proxy`（核心 HTTP 出口：auto、direct 或代理 URL）与 `--no-proxy`（直连目标 CSV；显式空值清空绕过列表）亦为根命令持久 flag，`--list` 默认只显示最近 10 个版本，`--all` 显示所选轨道全部；嵌入模式（embedded）下禁用自升级。`internal/upgrade` 各模块： （来源：`internal/app/flags.go:30-37`、`internal/app/flags.go:44-55`）

| 模块 | 职责 |
|---|---|
| `github.go` | `Client` / `ReleaseTrack`（release / beta / all，`all` 供 `FetchAllReleases` 不过滤轨道）；`NewClient` 默认查 npm Registry，仅当设置了 `DWS_UPGRADE_URL` 或 `DWS_UPGRADE_REPOSITORY` 时才用 GitHub（默认 `api.github.com`，仓库 `DingTalk-Real-AI/dingtalk-workspace-cli`）；`DWS_UPGRADE_URL` 覆盖 API 地址、`DWS_UPGRADE_REPOSITORY` 覆盖 owner/repo、`GITHUB_TOKEN`/`GH_TOKEN` 提升限额（`anonymous` 客户端不附带 token）；资产名固定 `dws-skills.zip` / `checksums.txt`；Registry 模式下 `--version` 先按 npm semver 校验再取该版本 manifest，而 `FetchLatestReleaseForTrack(all)` 直接报“未知升级轨道”（来源：`internal/upgrade/github.go:52-60`、`internal/upgrade/github.go:124-141`、`internal/upgrade/github.go:181-199`、`internal/upgrade/github.go:231-236`、`internal/upgrade/github.go:386-390`、`internal/upgrade/registry.go:78-84`） |
| `registry.go` | npm Registry 版本源：默认 `https://registry.npmjs.org` 上的 `dingtalk-workspace-cli` 包，`DWS_UPGRADE_REGISTRY` 覆盖根地址（只接受无凭据/查询/片段的 HTTPS，loopback HTTP 例外）；校验包名、semver、`deprecated` 与 SHA-512/SHA-256 `integrity`；非公共发行版且未显式配置升级源时拒绝安装公开 npm 包（来源：`internal/upgrade/registry.go:26-30`、`internal/upgrade/registry.go:57-65`、`internal/upgrade/registry.go:88-100`、`internal/upgrade/registry.go:153-170`） |
| `source.go` | `DownloadSource`（auto / github / npmmirror）与 `ParseDownloadSource`；`NewClientForSource` 固定来源时仍用 npm 主包元数据（`github` → npmjs，`npmmirror` → 镜像）且仅限公共发行版；`DownloadEvent` + `WithDownloadObserver` 同步上报来源/切换/尝试（来源：`internal/upgrade/source.go:19-32`、`internal/upgrade/source.go:43-60`、`internal/upgrade/source.go:64-88`） |
| `version.go` | `CompareVersions` / `NeedsUpgrade` |
| `downloader.go` | 下载发布包：默认 3 次尝试、单次 10 分钟超时、15 秒无进展停滞超时、1 GiB 上限；用 `Range` + `If-Match`（强 ETag）断点续传，412/416 或范围/ETag 不匹配则重下；拒绝 ≥10 跳、带凭据或 https→http 降级的重定向（来源：`internal/upgrade/downloader.go:41-49`、`internal/upgrade/downloader.go:186-192`、`internal/upgrade/downloader.go:203-208`、`internal/upgrade/downloader.go:222-243`） |
| `verify.go` | SHA256 校验：`VerifySHA256` 先 hex 解码期望值并要求 32 字节（否则报“无效的 SHA256 校验值”），`ParseChecksumFile` 解析 `hash  filename` 行，`VerifyFileFromChecksums` 按文件名查表校验（来源：`internal/upgrade/verify.go:16-31`、`internal/upgrade/verify.go:52-67`、`internal/upgrade/verify.go:70-77`） |
| `replacer.go` | `ReplaceSelf` 原子替换二进制 |
| `rollback.go` | `RollbackManager`，备份存放于 `~/.dws/data/backups` |
| `paths.go` | `EnsureUpgradeDirectories` 创建 `~/.dws`、`~/.dws/data/backups`、`~/.dws/cache/downloads`（0700）；`DownloadCacheDir` 为升级临时目录；Skill 安装以 `~/.agents/skills` 为 canonical，检测到的非 universal Agent 目录放相对链接（拒绝链接的文件系统回退直接拷贝），被替换的旧副本备份到 `~/.dws/skill-backups/<UTC 时间戳>/`（只保留最近 5 份，且只清理带 `.dws-skill-backup` 标记的目录），`.real` 等黑名单目录绝不触碰；新增 `.workbuddy/skills` 为 DWS-only 已知 Skill 目录（产品兼容保留），可用 `WORKBUDDY_CONFIG_DIR` 覆盖其根目录 （来源：`internal/upgrade/paths.go:105-113`、`internal/upgrade/paths.go:737-746`） |

升级分两阶段：Phase 1 在临时目录内完成下载、SHA256 校验（优先 `checksums.txt`，退回 GitHub asset digest，两者都没有才跳过）、解压与新二进制验证，零副作用；Phase 2 才替换二进制并安装 Skill。用户可见 5 步：备份 → 下载 → 校验 → 解压验证 → 替换+安装。替换后调 `cli.InvalidatePersistedSchemaCacheIdentities` 丢弃持久化 Schema 身份，让下个进程按新二进制的实时声明重建；备份按 `Cleanup(5)` 只留最近 5 份。darwin 上新二进制若被 amfid SIGKILL（“signal: killed”），会 ad-hoc `codesign` + 去掉 `com.apple.quarantine` 后重试一次。Phase 1 的下载按来源分三条路径：平台分包（`ResolvePlatformReleaseForSource` + `DownloadPlatformAssetForSource`）、npm 主包（`PrepareNPMPackage` 返回二进制归档、技能归档与 `checksums.txt` 内容）、GitHub 资产直下；npm 主包路径在替换前还要求新二进制的 `version` 输出确认目标版本，否则不替换（来源：`internal/app/upgrade.go:508-519`、`internal/app/upgrade.go:586-616`、`internal/app/upgrade.go:698-703`、`internal/app/upgrade.go:808-837`）。

### 升级下载来源

- `--source auto` 是默认模式，保留 `DWS_UPGRADE_*` 的来源配置。独立安装默认先下载 GitHub 同版本资源，遇到可重试的网络错误才切到 npmmirror 同版本分包。校验失败、磁盘错误和取消会终止升级。
- 公共发行版可显式选择 `--source github` 或 `--source npmmirror`。两者分别从 npmjs 和 npmmirror 主包查版本与弃用状态，下载固定来源的资源，不回退。显式固定来源优先于 `DWS_UPGRADE_REGISTRY`、`DWS_UPGRADE_URL` 和 `DWS_UPGRADE_REPOSITORY`。
- npm/pnpm 安装支持 `auto` 和 `npmmirror`，Homebrew 安装只接受 `auto`。包管理器接管这两类安装的升级流程，`--skip-skills` 和 `--rollback` 仅适用于独立安装。独立安装的回滚使用本地备份，只接受 `auto`。
- npmmirror 分包先校验 npm integrity，再核对包身份、归档结构、资源大小和 SHA256，通过后才进入替换阶段。

[固定版本的升级下载说明](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli/blob/0d2f0ffecc56f3f9f2a31e70612ef9d11d70e98e/docs/upgrade-download-sources.md)

## 发布物

- `Formula/dingtalk-workspace-cli.rb`（及 `-beta.rb`）：Homebrew 配方，下载 URL 指向 GitHub Releases；
- 根目录 `CHANGELOG.md`：记录版本历史。
- `build/homebrew.rb.tmpl` / `build/homebrew-release.rb.tmpl`：配方模板，由 `post-goreleaser.sh` 渲染到 `dist/homebrew/`——版本含 `-`（预发布）时渲染 `dingtalk-workspace-cli-beta.rb`（class `DingtalkWorkspaceCliBeta`，keg_only），否则渲染 `dingtalk-workspace-cli.rb`；另有一份本地校验用 `dingtalk-workspace-cli-local.rb`（`file://` URL + keg_only）。
- `scripts/release/publish-homebrew-formula.sh`（`make publish-homebrew-formula`）：把 `dist/homebrew/dingtalk-workspace-cli.rb`（`DWS_FORMULA_SOURCE` 可覆盖）推到 `DWS_TAP_REPO_URL` 的 `Formula/dingtalk-workspace-cli.rb`；先校验配方无 `__占位符__` 残留且 `ruby -c` 通过；直推模式只允许 stable/beta 两个配方路径、提交只能含该文件、最多 3 次非强推重试（目标分支移动则重新 clone）；设置 `DWS_TAP_PR_REPOSITORY` + `DWS_TAP_PR_BRANCH` 时改走 PR（`--force-with-lease` 推分支 + `gh pr create`）。
- `dist/dws-skills.zip`：zip 根是 `skills/mono` 的副本（兼容只在根找 `SKILL.md` 的旧安装脚本），另含 `mono/` 与 `multi/` 两棵树；`dws upgrade` 与 Homebrew 配方的 `skills` resource 都消费它。

## 测试与策略门

```bash
DWS_PACKAGE_VERSION=0.0.0-test go test ./...
./scripts/policy/check-generated-drift.sh   # 生成物漂移检查
./scripts/policy/check-schema-catalog.sh    # Schema 契约检查
```
