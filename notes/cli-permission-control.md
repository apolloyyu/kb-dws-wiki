---
title: DWS CLI 组织权限管控:几层开关、各自默认值与生效时延
maintenance: manual
intents: cliperm
triggers: cli 数据访问, cli数据访问, cli 使用权限, cli使用权限, cli 权限, cli权限, cli 设置, cli设置, cli 管控, cli管控, cli 开通, cli开通, 开通 cli, 开通cli, 组织总开关, agent 渠道, agent渠道, 其他渠道, 千问办公渠道, 生效范围, 申请开关, 成员权限申请, 立即申请
contract:
  - cliperm_timing：原文只给了一个时延——Agent 渠道「生效范围」修改保存后约 5 分钟生效；组织总开关、渠道启用开关、申请开关、权限项的生效时延原文都没写，不得套用「5 分钟」。总开关重新开启后原文只说成员需重新登录授权(dws auth login)。
  - cliperm_values：渠道生效范围只有「全员可用」「部分成员可用(按部门、角色圈选)」两种；渠道能不能用由该渠道的「启用开关」决定，不是生效范围的某个取值，原文没有「全员禁止」这类取值。
---

# DWS CLI 组织权限管控

回答「CLI 怎么开通 / 成员登录提示组织已禁止 CLI 数据访问 / 生效范围怎么设 / 开了多久生效」时以本篇为准。管控原文在开放平台文档站的几篇里,本篇只把它们串起来;每条结论后的原文行逐字摘自镜像。

## 管控分几层,各自默认值

- **组织总开关**(第一层,其余设置的前提):在 CLI 设置页「DWS CLI管理」卡片右上角,默认开启;关闭时组织成员都不能用 CLI。
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | 「DWS CLI管理」卡片右上角开关}}
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | 当组织总开关关闭时，该组织成员没有CLI的使用权限}}
- **Agent 渠道**(第二层):千问办公渠道默认开启;其他渠道(企业自建 Agent、Codex 等第三方 Agent)默认关闭,要用须先把该渠道打开。
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | 与钉钉深度集成，开箱即用，默认开启}}
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | 默认关闭，其他渠道包含企业自建Agent和其他Agent产品}}
  每个渠道的「设置」里有三项,互相独立:启用开关管渠道能不能用;生效范围管谁能用;权限范围管能用哪些权限项。
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | **启用开关**：控制该渠道 CLI 能力是否可用}}
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | **生效范围**：支持全员可用，或按部门、角色圈选}}
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | 生效范围选择部分成员可用}}
- **权限项**(第三层):CLI 管控配置里按业务域逐项设可用范围(全员或指定人员)。
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | **可用范围**：全员可用或指定人员}}
- **成员权限申请**:申请开关在渠道「设置」里,默认关闭;打开后范围外成员可在登录时点「立即申请」,管理员审批通过后再重新登录。
  {{quote: docs/external/open-platform/cli-permissions-organizational-members.md | **申请开关位置**：CLI 设置页 -Agent渠道-设置-组织成员权限申请开关}}
  {{quote: docs/external/open-platform/dingtalk-dws-cli-install-guide.md | 管理员收到请求卡片后进行审批}}

## 生效时延:只有生效范围写了「约 5 分钟」

- 原文唯一的时延是「修改渠道生效范围,保存后约 5 分钟生效」。用户问组织总开关、渠道启用开关或申请开关开了多久生效时,只能说原文没写这几项的时延,不能套用 5 分钟。
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | 然后保存，5分钟后生效}}
  {{quote: docs/external/open-platform/cli-permissions-organizational-members.md | 生效范围修改保存后约 5 分钟生效}}
- 组织总开关:关闭后已登录的 CLI 会话立即失效;重新开启后成员需重新登录授权。
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | 重新开启后成员需重新登录授权}}

## 成员用不了时的排查顺序

不要只归因到某一个开关;按原文顺序逐层查:组织总开关 → 成员所在渠道的启用开关与生效范围 → 对应权限项的可用范围 → 是否已通过权限申请审批。
  {{quote: docs/external/open-platform/dws-permission-management-guide.md | 按顺序检查四处}}
  {{quote: docs/external/open-platform/cli-permissions-organizational-members.md | ④ 该成员是否已通过权限申请审批}}
