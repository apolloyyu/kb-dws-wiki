#!/usr/bin/env python3
"""dwsdoc ctx/card 的快路径与证据边界回归测试。"""
import json
import os
import re
import runpy
import shutil
import subprocess
import tempfile
import unittest


REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DWSDOC = os.path.join(REPO, "bin", "dwsdoc")


def run_dwsdoc(*args):
    p = subprocess.run(["python3", DWSDOC, *args], cwd=REPO,
                       text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       timeout=30)
    if p.returncode != 0:
        raise AssertionError(f"dwsdoc {' '.join(args)} rc={p.returncode}\nstdout={p.stdout}\nstderr={p.stderr}")
    return p.stdout


class DwsdocCtxContractTest(unittest.TestCase):
    def test_ack_and_dedup_question_keeps_event_evidence(self):
        out = run_dwsdoc("ctx", "去重需要客户端做吗，服务端有没有 ACK 机制")
        self.assertIn("个人事件 ACK 机制", out)
        self.assertIn("成功 ACK", out)
        self.assertIn("不能证明服务端重投策略", out)
        self.assertIn("8192", out)
        self.assertNotIn("== 命令契约: dws pat", out)

    def test_refresh_expiry_field_keeps_login_lifetime_note(self):
        out = run_dwsdoc("ctx", '"refreshExpiresAt": "2026-09-09T04:21:01.494Z"，那为啥没发刷新token回来')
        self.assertIn("notes/token-lifetime.md", out)
        self.assertIn("30 天", out)
        self.assertIn("服务端是否同样续期", out)

    def test_followup_keeps_event_subject_evidence(self):
        out = run_dwsdoc("ctx", "--prev", "dws event consume 监听个人事件", "那去重需要客户端做吗，服务端有没有 ACK 机制")
        self.assertIn("个人事件 ACK 机制", out)
        self.assertIn("重连重复投递与去重", out)

    def test_exact_command_keeps_fast_card(self):
        out = run_dwsdoc("ctx", "dws auth login")
        self.assertIn("card=1(fast=1)", out)
        self.assertIn("== 证据契约(回答边界) ==", out)
        self.assertIn("命令卡只证明", out)

    def test_related_tie_does_not_make_card_confident(self):
        confident = runpy.run_path(DWSDOC)["_card_confident"]
        rows = [{"cmd": "auth login", "_ctx_score": 10, "_ctx_name_score": 5},
                {"cmd": "auth provider-login", "_ctx_score": 10, "_ctx_name_score": 5}]
        card = {"kind": "command", "body": "## Related\n- dws auth provider-login\n"}
        self.assertFalse(confident(rows, card))
        self.assertFalse(confident(rows, {"kind": "command", "body": ""}))
        self.assertFalse(confident([]))
        rows[0]["_ctx_score"] = 12
        self.assertTrue(confident(rows, card))
        rows[0]["_ctx_score"] = 2000
        self.assertTrue(confident(rows, card))

    def test_natural_login_question_keeps_full_context(self):
        out = run_dwsdoc("ctx", "dws 怎么登录")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("== 证据契约(回答边界) ==", out)
        self.assertIn("命令卡只证明", out)

    def test_support_and_card_capability_force_full_context(self):
        out = run_dwsdoc("ctx", "dws 能解析卡片消息吗")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("原始卡片结构、可读文本提取、结构化字段解析、渲染、解密", out)
        self.assertIn("某条命令存在只证明该入口存在", out)

    def test_id_format_claim_forces_full_context(self):
        out = run_dwsdoc("ctx", "oa approval detail 的 instance-id 格式必须是 UUID 吗")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("String 类型、示例外观、长度或前缀都不是格式约束", out)
        self.assertIn("缺少显式校验源码时不得判 ID/参数非法", out)

    def test_error_causality_forces_full_context(self):
        out = run_dwsdoc("ctx", "oa approval detail 返回 PARAM_ERROR 的根因是什么")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("报错根因/生命周期/机制须有对应代码路径", out)

    def test_enumeration_forces_full_context(self):
        out = run_dwsdoc("ctx", "oa approval 有哪些命令")
        self.assertIn("fast=0", out)

    def test_unclosed_structured_input_forces_full_context(self):
        out = run_dwsdoc("ctx", 'oa approval detail {"instanceId":"abc"')
        self.assertIn("fast=0", out)
        self.assertIn("input_complete=no", out)

    def test_embedded_command_and_backend_validation_evidence(self):
        out = run_dwsdoc(
            "ctx",
            "二号 请求未通过后端参数校验；请核对当前 leaf Help/Schema 和稳定 ID 类型后重试。"
            "这个报错是为什么？命令是：dws oa approval detail --instance-id "
            "03MbL8dhSXKwbem0IIGaZQ07181785831689 --format json",
        )
        self.assertIn("# dws oa approval detail", out)
        self.assertIn("只检查必填值是否存在，然后原样映射到 `processInstanceId`", out)
        self.assertIn("没有 UUID/pattern 校验", out)
        self.assertIn("card=1(fast=0)", out)

    def test_explicit_card_command_stays_ahead_of_capability_expansion(self):
        out = run_dwsdoc("ctx", "命令 dws chat message send-card --conversation-id x 能不能解析卡片")
        first_card = next(line for line in out.splitlines() if line.startswith("# dws "))
        self.assertEqual("# dws chat message send-card", first_card)
        self.assertIn("card=1(fast=0)", out)

    def test_card_message_question_selects_read_projection(self):
        out = run_dwsdoc("ctx", "二号   卡片消息能不能解析")
        self.assertIn("# dws chat message list", out)
        self.assertIn("消息结果投影与卡片读取边界", out)
        self.assertIn("可识别的富内容卡片还会提取 `items[].data.text`", out)
        self.assertIn("加密的 card/robot ciphertext", out)
        self.assertIn("card=1(fast=0)", out)

    def test_generic_support_uses_product_context_without_unrelated_notes(self):
        out = run_dwsdoc("ctx", "oa审批实例发起，在有附件的情况下，是否需要先拿到文件的 media id 或钉盘文件 id")
        # LeafSpec flag/描述补齐后 authorize-download 也成为合格首卡候选；本题契约是
        # upload 入口与其正文必须进上下文，而非固定由它占首卡。
        self.assertIn("dws oa approval attachment upload", out)
        self.assertIn("上传本地文件为审批附件", out)
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("notes=0", out)
        self.assertIn("docs/products/oa.md", out)

    def test_capability_wording_without_support_particle_loads_notes(self):
        out = run_dwsdoc("ctx", "dws 卡片消息解析能力")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("notes=1", out)
        self.assertIn("消息结果投影与卡片读取边界", out)

    def test_validation_wording_without_error_loads_notes(self):
        out = run_dwsdoc("ctx", "oa approval detail 的 instance-id 格式要求")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("notes=1", out)
        self.assertIn("参数校验与后端报错归因边界", out)

    def test_mechanism_wording_without_why_loads_notes(self):
        out = run_dwsdoc("ctx", "event bus 生命周期")
        self.assertIn("fast=0", out)
        self.assertRegex(out, r"notes=[1-9]")
        self.assertIn("行为语义(notes,复杂问法自动并入", out)

    def test_cross_boundary_tokenization_and_cross_org_listing(self):
        out = run_dwsdoc("ctx", "获取消息好像拉不到非本组织的群信息？")
        self.assertIn("否定前必读", out)
        head = out.split("== 答案卡", 1)[0]
        self.assertIn("data-auth cross-org", head)
        self.assertIn("card=1(fast=0)", out)

    def test_fanout_wording_reaches_event_notes(self):
        out = run_dwsdoc("ctx", "我在同一台机器多次启用dws event consume，只有一个能正常收到消息，其余的都是连接成功，没反应")
        self.assertIn("扇出", out)
        self.assertRegex(out, r"notes=[1-9]")

    def test_support_question_brings_changelog_lines(self):
        out = run_dwsdoc("ctx", "“通过AI发送”文案支持修改吗")
        self.assertIn("CHANGELOG 命中行", out)
        self.assertIn("DWS_AGENT_PRODUCT", out)

    def test_confirmation_phrasing_blocks_fast_path(self):
        out = run_dwsdoc("ctx", "client-id 参数不是钉钉应用的ID吗，这个对组织是一样的吧")
        self.assertIn("fast=0", out)

    def test_explicit_full_disables_cards(self):
        out = run_dwsdoc("ctx", "--full", "dws 怎么登录")
        self.assertIn("card=0(fast=0)", out)
        self.assertIn("检索命中只证明所引原文明确写出的事实", out)

    def test_card_command_also_prints_contract(self):
        out = run_dwsdoc("card", "oa approval detail")
        self.assertIn("# dws oa approval detail", out)
        self.assertIn("== 证据契约(回答边界) ==", out)
        self.assertIn("运行结果、当前登录态或服务端行为", out)


    def test_digital_employee_group_access_uses_whitelist_note(self):
        # 实录 2026-10-10:检索给出 add-bot/@所有人,模型编出「数字员工靠关联机器人 robotCode 入群」并在群内复读
        for q in ("如何让群所有人可以与数字员工对话", "数字员工怎么拉进群",
                  "怎么让别人也能和我的数字员工对话", "数字员工的 robotCode 在哪看"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("notes/digital-employee.md", out, q)
            self.assertIn("allowed-groups", out, q)
            # 上游 10-13(a3c7d486) 起正式 connect 绑定走平台访问策略,不再是「默认仅主管+白名单」
            self.assertIn("> 原文(docs/digital-employee-adapters.md): `manage create` 创建并通过正式", out, q)
            self.assertIn("platform", out, q)
            self.assertIn("- access：", out, q)
            self.assertIn("card=1(fast=0)", out, q)
            self.assertRegex(out, r"(?m)^# dws dingtalk-tag ", q)
            self.assertNotIn("add-bot --robot-code", out, q)
            self.assertIn("不叠加本地白名单", out, q)
            self.assertIn("- notes：行为说明只作依据", out, q)

    def test_digital_employee_origin_uses_origin_note(self):
        # 实录 2026-10-12:把 DEAP 智能体/企业自建 Agent 接口列为创建方式,随后又称「关系未说明」并撤回
        for q in ("DEAP创建的智能体就是你所谓的数字员工吗", "那你说的数字员工到底在哪儿创建的？不是DEAP这？",
                  "AI 助理改名为数字员工了吗", "数字员工怎么创建"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("notes/digital-employee.md", out, q)
            self.assertIn("- origin：", out, q)
            self.assertIn("card=1(fast=0)", out, q)
            self.assertRegex(out, r"(?m)^# dws dingtalk-tag manage create", q)
            self.assertIn("manage detail --agent-uuid", out, q)
            self.assertIn("申请表只用于申请开通", out, q)

    def test_digital_employee_enable_gives_verbatim_form_link(self):
        # 实录 2026-10-15:只写「以更新日志为准」不给链接,模型编出 alidocs/i/nodes/… 的 404 链接。
        # 链接不再写死:note 用 {{quote:}} 引用开放平台更新日志的外部镜像,ctx 输出时现场取原文。
        with open(os.path.join(REPO, "docs", "external", "open-platform", "dws-cli-log.md"), encoding="utf-8") as fh:
            src = fh.read()
        form = next(l.strip() for l in src.splitlines() if "数字员工创建灰度申请" in l)
        self.assertIn("alidocs.dingtalk.com/notable/share/form/", form)
        with open(os.path.join(REPO, "notes", "digital-employee.md"), encoding="utf-8") as fh:
            self.assertNotIn("alidocs.dingtalk.com", fh.read(), "note 里不得写死链接")
        for q in ("数字员工灰度怎么申请", "DIGITAL_EMPLOYEE_NOT_ENABLED 怎么开通", "数字员工怎么开通"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("> 原文(https://open.dingtalk.com/document/development/dws-cli-log", out, q)
            self.assertIn(form, out, q)
            self.assertIn("其他域名一律不造", out, q)
            self.assertNotIn("⚠依据已变更(", out, q)
            self.assertNotIn("{{", out, q)

    def test_note_refs_all_valid_and_stale_is_flagged(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("notes_refs", os.path.join(REPO, "bin", "notes_refs.py"))
        nr = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(nr)
        # 镜像层(quote)依据全部有效;code/absent 由构建核对写入 meta/notes-check.jsonl
        nd = os.path.join(REPO, "notes")
        for fn in os.listdir(nd):
            with open(os.path.join(nd, fn), encoding="utf-8") as fh:
                for kind, arg, _ in nr.parse(fh.read()):
                    if kind == "quote":
                        self.assertIsNotNone(nr.quote_line(REPO, arg), f"{fn}: {arg}")
        for r in nr.load_check(REPO).values():
            self.assertTrue(r["ok"], f"{r['note']} {r['kind']}: {r['detail']}")
        body = "- 结论\n  {{quote: docs/products/chat.md | 这段原文不存在XYZ}}\n  {{code: a.go | x}}"
        out = nr.expand(REPO, "t.md", body, {("t.md", "code", "a.go | x"): {"ok": False, "detail": "a.go 已不含「x」"}})
        self.assertEqual(out.count("⚠依据已变更"), 2)
        self.assertEqual(nr.parse("x {{quote:}} y"), [])

    def test_contract_facts_live_in_notes_not_code(self):
        with open(DWSDOC, encoding="utf-8") as fh:
            code = fh.read()
        for fact in ("DEAP 1.0", "mcp-gw.dingtalk.com", "notable/share/form", "默认仅主管"):
            self.assertNotIn(fact, code, f"dwsdoc 里不得写死事实: {fact}")
        out = run_dwsdoc("ctx", "dws发送消息限流规则是什么")
        self.assertIn("- ratelimit：", out)
        out = run_dwsdoc("ctx", "dws chat message list 怎么用")
        self.assertNotIn("- ratelimit：", out)
        self.assertNotIn("- deap1：", out)

    def test_truncation_never_splits_links(self):
        import runpy
        mod = runpy.run_path(DWSDOC, run_name="dwsdoc_test_module")
        cut, span = mod["_cut"], mod["_LINK_SPAN_RE"]
        self.assertEqual(cut("ab [x](http://e.test/aaaa) cd", 12), "ab [x](http://e.test/aaaa)")
        self.assertEqual(cut("ab [x](http://e.test/" + "a" * 500 + ")", 12), "ab ")
        bad = []
        for layer in ("docs", "notes"):
            for dp, _, fs in os.walk(os.path.join(REPO, layer)):
                for fn in fs:
                    if not fn.endswith(".md"):
                        continue
                    with open(os.path.join(dp, fn), encoding="utf-8", errors="replace") as fh:
                        body = fh.read()
                    for cap in (2000, 3000, 6000):
                        if len(body) > cap:
                            k = len(cut(body, cap))
                            if any(m.start() < k < m.end() for m in span.finditer(body, max(0, k - 2500))):
                                bad.append(f"{fn}@{cap}")
        self.assertEqual(bad, [])

    def test_deap_platform_ui_is_deap1_not_digital_employee(self):
        # 实录 2026-10-15 正式群:答「方式一:登录 DEAP 平台→创建智能体→发布→加到群」。产品方确认那是 DEAP 1.0 的 AI 助理
        for q in ("在三方应用群内添加数字员工（类似本群的钉仔）怎么做", "数字员工怎么创建",
                  "DEAP 平台创建的智能体是数字员工吗", "怎么给群里加一个数字员工", "数字员工可以在界面上创建吗"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("- deap1：", out, q)
            self.assertIn("DEAP 1.0 的 AI 助理", out, q)
            self.assertIn("notes/digital-employee.md", out, q)
            self.assertNotIn("拿 DEAP 后台显示的智能体 ID", out, q)
            self.assertIn("(人工确认: 产品方 2026-10-15", out, q)

    def test_digital_employee_create_and_group_merges_both_notes(self):
        out = run_dwsdoc("ctx", "创建好的数字员工怎么拉进群")
        self.assertRegex(out, r"(?m)^# dws dingtalk-tag connect")
        self.assertIn("notes/digital-employee.md", out)
        self.assertIn("notes/digital-employee.md", out)

    def test_cmd_prefix_lists_all_hits(self):
        # 实录 R10.5.10:只显示前 12 条,模型答「oa approval 仅有 12 个子命令、不支持退回」
        out = run_dwsdoc("cmd", "oa approval")
        self.assertIn("dws oa approval revert-task", out)
        self.assertIn("已全部列出", out)

    def test_digital_employee_vs_robot_uses_access_note(self):
        out = run_dwsdoc("ctx", "数字员工和机器人有什么区别")
        self.assertIn("notes/digital-employee.md", out)
        self.assertIn("- access：", out)

    def test_robot_join_group_without_digital_employee_keeps_chat_context(self):
        out = run_dwsdoc("ctx", "怎么把机器人拉进群")
        self.assertNotIn("notes/digital-employee.md", out)
        self.assertIn("add-bot", out)

    def test_rate_limit_uses_mcp_gateway_note(self):
        # 实录 2026-10-14:14 条回复把 OpenAPI 的 QPS/月配额/90018 套到 dws 产品命令上
        for q in ("dws发送消息限流规则是什么", "dws的限流怎么升级", "RATE_LIMIT_ERROR 是什么意思",
                  "使用dws总是返回限流的原因是什么", "dws使用的 也是 钉钉 OpenAPI 吗",
                  "你之前说过dws的部分接口并不跟openapi共享的我记得"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("notes/rate-limit-and-backend.md", out, q)
            self.assertIn("- ratelimit：", out, q)
            self.assertIn("mcp-gw.dingtalk.com", out, q)
            self.assertIn("只有 `dws api` 直连 OpenAPI", out, q)
            self.assertNotIn("ctx 总量截断", out, q)

    def test_rate_limit_note_not_pulled_by_unrelated_or_local_limit(self):
        for q in ("dws chat message list 怎么用", "dev connect --user-rate-limit 是什么"):
            out = run_dwsdoc("ctx", q)
            self.assertNotIn("notes/rate-limit-and-backend.md", out, q)

    def test_natural_question_recalls_flag_by_help_text(self):
        # R10.5 回退 Q250/Q251:flag 只按名子串匹配,自然问句召不回 --ai-tag(答案在 help「AI 发送角标」)
        for q in ("现在为何通过dws发送的都会显示ai发送？", "如何让消息不带ai标识"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("--ai-tag(Bool)", out, q)

    def test_help_text_flag_recall_does_not_add_noise(self):
        # 单个泛词(发送/消息)或偶撞词不得把无关 flag 拉进来
        out = run_dwsdoc("ctx", "创建空会话转发")
        self.assertNotIn("--ai-tag", out)
        self.assertNotIn("--client-token", out)

    def test_challenge_turns_off_fast_card(self):
        # R10.5 回退 Q175:用户质疑后仍走快卡,模型复读卡片
        out = run_dwsdoc("ctx", "所以你的意思dws auth login 判断状态其实不准的对吧？")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("card=1(fast=1)", run_dwsdoc("ctx", "dws auth login 文档在哪"))

    def test_prev_question_joins_follow_up_terms(self):
        out = run_dwsdoc("ctx", "--prev", "dws 发送消息怎么不显示AI标识", "那默认是true还是false")
        self.assertIn("--ai-tag(Bool)", out)

    def test_any_merged_notes_forbid_citing_note_files(self):
        # R10.6.0 盲测 Q227/Q232/Q242:禁引只在专属 note 命中时出现,泛 notes 并入时回复参考区列出 notes/event-system.md
        out = run_dwsdoc("ctx", "二号 如果在同一台机器上启用多个事件监听，这个应该是可行的吧")
        self.assertIn("== 行为语义(notes", out)
        self.assertIn("- notes：行为说明只作依据，不是出处", out)

    def test_every_cited_source_has_a_link(self):
        # 只给本地路径时模型把 auth-and-credentials.md、event.md 当出处(10-15 全量 14/300 题);每个出处都附可照抄的引用行
        out = run_dwsdoc("ctx", "你知道dws的登录态，如果我不使用它，多长时间会过期吗")
        for m in re.finditer(r"(?m)^== 篇目\[\d+/\d+\] (\S+) \[(\w+)\] ==\n(.*)$", out):
            self.assertTrue(m.group(3).startswith("引用: "), m.group(1))
            with open(os.path.join(REPO, m.group(1)), encoding="utf-8") as fh:
                has_src = re.search(r"(?m)^source_(?:path|url):", fh.read(800))
            if has_src:   # 镜像篇都有 source_path;只断言有来源的篇,上游新增无 frontmatter 的篇不应卡住每日构建
                self.assertIn("https://", m.group(3), m.group(1))
        self.assertNotRegex(out, r"(?m)^\s*源码: ", "源码位置须以引用深链给出")

    def test_lifetime_question_gets_lifetime_note(self):
        # R10.6.0 Q168-171:30 天只在源码常量里,docs/notes 都没写,四次答「源码中未找到」。
        # 改为人工 note + {{code:}} 依据(每日核对),不做全局常量模糊检索:第 2 轮审查发现
        # 启发式匹配会给出带深链但含义不对的数(分页「页数」当「每页条数」、--groups-file 1MiB 当附件上限)。
        for q in ("你知道dws的登录态，如果我不使用它，多长时间会过期吗",
                  "只要我在30天 内执行过一次 dws contact user get-self ，授权就不会丢对吗",
                  "我用 dws auth login --token 导入的 token，第二天就不能用了，正常吗",
                  "How long does the dws refresh token last?"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("--- notes/token-lifetime.md", out, q)
            self.assertIn("- lifetime：", out, q)
            self.assertIn("(源码依据: https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli/blob/main/", out, q)
        for q in ("扫码登录要在几分钟内完成", "隔几天不用 dws 就要重新登录吗", "dws 每次都要重新扫码，很烦",
                  "dws 掉线了", "dws 授权过期了怎么办"):
            self.assertIn("--- notes/token-lifetime.md", run_dwsdoc("ctx", q), q)
        # 第 3 轮审查的误触发:开放平台应用 access_token、业务字段里的「过期」、PAT 行为授权都不是 dws 登录态
        for q in ("dws chat message list 怎么用", "dws auth login", "dws 分页每页多少条", "dws 上传附件最大多大",
                  "开放平台 access_token 有效期多久", "企业内部应用 access_token 过期了怎么刷新",
                  "aitable 记录过期时间字段", "dws todo 截止时间过期提醒", "PAT 授权多久", "dws pat chmod 授权多久有效",
                  "token 怎么获取", "dws auth login 报错 invalid_client"):
            self.assertNotIn("notes/token-lifetime.md", run_dwsdoc("ctx", q), q)
        # 依据须有构建核对记录(带行号深链),新 note 不能等 ECS 重建才有
        out = run_dwsdoc("ctx", "dws 登录态多久过期")
        self.assertRegex(out, r"源码依据: https://\S+#L\d+")
        self.assertNotIn("依据已变更(", out)

    def test_named_version_is_a_changelog_key(self):
        # R10.6.0 Q259:按 release/beta 词 grep 只命中最新几条,答成「不存在 1.0.7」;答案是 requires v1.0.7+
        out = run_dwsdoc("ctx", "二号 github里提示要安装1.0.7及以上的版本，但github里只有1.0.58 beta版本，1.0.7在哪里下载呢")
        cl = out.split("== CHANGELOG 命中行", 1)[1]
        self.assertIn("requires v1.0.7+", cl)

    def test_changelog_lines_carry_their_version(self):
        # 审查 R10.6.1:命中行不带所属版本,1.0.62-beta.8 的条目被算到问句的 1.0.64;不存在的版本无任何提示
        cl = run_dwsdoc("ctx", "upgrade 到 1.0.64 有什么变化").split("== CHANGELOG 命中行", 1)[1].split("\n== ", 1)[0]
        for l in [x.strip() for x in cl.splitlines()[1:] if x.strip()]:
            self.assertRegex(l, r"^(## \[|\[|CHANGELOG 没有|CHANGELOG 记录的)", l)
        self.assertIn("CHANGELOG 没有 1.0.99 的条目", run_dwsdoc("ctx", "1.0.99 什么时候发布"))
        # 「要不要升级」「最新版是多少」须带最新版本行,否则只能拿点名版本自己比
        for q in ("我是 1.0.58，要升级吗", "dws 最新版本是多少"):
            self.assertRegex(run_dwsdoc("ctx", q), r"CHANGELOG 记录的最新正式版 \d+\.\d+\.\d+\(\d{4}-", q)
        for q in ("机器人上线后群里收不到消息", "dws 能正常使用审批吗", "aitable 字段类型兼容 excel 吗", "dws 3.5.1 文档链接"):
            out = run_dwsdoc("ctx", q)
            self.assertNotIn("最新正式版", out, q)
            self.assertNotIn("CHANGELOG 没有", out, q)

    def test_find_splits_quoted_words_and_says_when_nothing_hits(self):
        # 引号多词按整串子串匹配恒为 0 且无任何输出(与 dkdoc 同修)
        one = run_dwsdoc("find", "event 订阅 取消")
        self.assertIn("docs/products/event.md", one)
        self.assertIn("按命中词数排序", one)
        self.assertIn("docs/products/event.md", run_dwsdoc("find", "event"))
        self.assertIn("篇目标题层无命中", run_dwsdoc("find", "不存在的词xyz 另一个xyz"))
        self.assertGreater(len(run_dwsdoc("find", "md").splitlines()), 30)   # 全中照旧全列，不截断

    def test_cli_permission_question_expands_open_platform_doc(self):
        # 11-02 日评:CLI 开通/组织权限/渠道开关只写在开放平台「钉钉 CLI」分类,本库此前只镜像更新日志,
        # 21 题依据都在这几篇,正文一篇没展开(实录:「组织管理员如何管理 CLI 权限」展开 attendance.md;
        # 「当前组织已禁止 CLI 数据访问权限」快卡命中 chat data-auth cross-org,正文清零)
        for q, doc in (("组织管理员如何管理组织的 CLI 权限", "dws-permission-management-guide.md"),
                       ("如何开通组织成员CLI权限申请", "cli-permissions-organizational-members.md"),
                       ('个人数据授权管理页面显示"当前组织已禁止CLI数据访问权限"，请联系组织管理员',
                        "dws-permission-management-guide.md")):
            out = run_dwsdoc("ctx", q)
            m = re.search(r"(?m)^== 篇目\[\d+/\d+\] docs/external/open-platform/" + re.escape(doc)
                          + r" \[docs\] ==\n(.*)$", out)
            self.assertTrue(m, q)
            self.assertTrue(m.group(1).startswith("引用: https://open.dingtalk.com/document/"), q)
        out = run_dwsdoc("ctx", '个人数据授权管理页面显示"当前组织已禁止CLI数据访问权限"，请联系组织管理员')
        self.assertIn("card=1(fast=1)", out)   # 快卡仍在,只是不再叫模型只按卡作答
        self.assertNotIn("仅按卡内 CLI 契约直接作答", out)

    def test_cli_permission_question_gets_control_note(self):
        # 11-04 验收:展开管控原文后,13 道目标题新答 8 个 C 是同一种串层——把只属于生效范围的时延套到组织总开关,
        # 或编出原文没有的生效范围取值。管控 note 把几层开关与时延串起来,依据逐字取自镜像。
        for q in ("CLI怎么开通", "当前组织已禁止CLI 数据访问权限 请联系组织管理员在后台安全设置中授权 在哪里操作",
                  "dingtalk cli 要组织授权才能使用吗", "允许成员通过 CLI 访问个人数据", "其他渠道的生效范围怎么设置"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("--- notes/cli-permission-control.md", out, q)
            self.assertIn("- cliperm_timing：", out, q)
            self.assertIn("> 原文(https://open.dingtalk.com/document/development/", out, q)
            self.assertNotIn("⚠依据已变更(", out, q)
            self.assertNotIn("{{", out, q)
            self.assertNotIn("仅按卡内 CLI 契约直接作答", out, q)   # 带了 note 就不叫模型只按卡作答
        # 只多带 note,不退出快卡路径:否则会多展开一篇无关产品正文(实测 chat.md)
        out = run_dwsdoc("ctx", "当前组织已禁止CLI 数据访问权限 请联系组织管理员在后台安全设置中授权 在哪里操作")
        self.assertIn("(fast=1)", out)
        self.assertNotRegex(out, r"(?m)^== 篇目\[\d+/\d+\] docs/products/")
        for q in ("dws cli 怎么开启 debug 日志", "client_id 权限不足", "dws chat message list 怎么用",
                  "dws auth login 报错 invalid_client", "dws cli 版本怎么升级", "dws发送消息限流规则是什么"):
            out = run_dwsdoc("ctx", q)
            self.assertNotIn("notes/cli-permission-control.md", out, q)
            self.assertNotIn("- cliperm_", out, q)

    def test_open_platform_docs_stay_out_of_command_questions(self):
        # 同分时外部篇不能靠路径字母序(docs/external < docs/products)当首篇;更新日志仍只在版本问法参与
        for q in ("dws chat 怎么给群发消息", "dws auth login", "dws chat message list 怎么用"):
            out = run_dwsdoc("ctx", q)
            self.assertNotRegex(out, r"(?m)^== 篇目\[\d+/\d+\] docs/external/", q)
        self.assertIn("仅按卡内 CLI 契约直接作答", run_dwsdoc("ctx", "dws auth login"))
        # 更新日志小标题含「AI 表格：角色成员精细管」,不限版本问法时会被当外部首篇追加
        self.assertNotIn("dws-cli-log.md", run_dwsdoc("ctx", "AI 表格角色成员怎么管"))
        self.assertRegex(run_dwsdoc("ctx", "dws 最新版本更新了什么"),
                         r"(?m)^== 篇目\[\d+/\d+\] docs/external/open-platform/dws-cli-log\.md ")

    def test_find_lists_open_platform_docs(self):
        self.assertIn("docs/external/open-platform/cli-permissions-organizational-members.md",
                      run_dwsdoc("find", "CLI 权限"))

    def test_unindexed_external_mirror_is_searchable(self):
        # staging 只带新增镜像文件、不重建 meta/documents.jsonl,外部篇也要进检索;已索引的以索引为准
        import tempfile
        fn = runpy.run_path(DWSDOC, run_name="dwsdoc_test_module")["_doc_rows"]
        with tempfile.TemporaryDirectory() as root:
            ext = os.path.join(root, "docs", "external", "kb")
            os.makedirs(ext)
            os.makedirs(os.path.join(root, "meta"))
            with open(os.path.join(root, "meta", "documents.jsonl"), "w", encoding="utf-8") as fh:
                fh.write('{"doc_id": "a", "path": "docs/external/kb/a.md", "layer": "docs", "headings": ["索引标题"]}\n')
            for name in ("a", "b"):
                with open(os.path.join(ext, name + ".md"), "w", encoding="utf-8") as fh:
                    fh.write("---\nsource_url: https://example.com\n# 不是标题\n---\n# 文件标题\n正文\n## 小节\n")
            old = fn.__globals__["ROOT"]
            fn.__globals__["ROOT"] = root
            try:
                rows = fn()
            finally:
                fn.__globals__["ROOT"] = old
        self.assertEqual([(r["path"], r["headings"]) for r in rows],
                         [("docs/external/kb/a.md", ["索引标题"]), ("docs/external/kb/b.md", ["文件标题", "小节"])])
        self.assertEqual(rows[1]["layer"], "docs")


class ExternalMirrorTargetsTest(unittest.TestCase):
    def test_sections_select_and_fall_back_to_previous_mirror(self):
        # 按分类节选篇,不逐篇点名;开放平台库读不到时沿用上一版镜像,不因此删掉已镜像篇
        import tempfile
        targets = runpy.run_path(os.path.join(REPO, "ops", "scripts", "build_dws_kb.py"),
                                 run_name="build_dws_kb_test")["external_targets"]
        rows = [{"tab": "钉钉 CLI", "slug": "faq", "breadcrumb": ["常见问题"]},
                {"tab": "钉钉 CLI", "slug": "openclaw", "breadcrumb": ["OpenClaw 接入"]},
                {"tab": "应用开发", "slug": "other", "breadcrumb": ["新手入门"]},
                {"tab": "钉钉 CLI", "slug": "dws-cli-log", "breadcrumb": ["新手入门"]}]
        self.assertEqual(targets(rows, "/nonexistent"),
                         [("open-platform", "dws-cli-log"), ("open-platform", "faq")])
        with tempfile.TemporaryDirectory() as prev:
            os.makedirs(os.path.join(prev, "open-platform"))
            for name in ("dws-cli-log.md", "faq.md", "notes.txt"):
                open(os.path.join(prev, "open-platform", name), "w").close()
            self.assertEqual(targets([], prev), [("open-platform", "dws-cli-log"), ("open-platform", "faq")])
            # 索引还在但字段改名、一篇都选不出,同样沿用上一版
            self.assertEqual(targets([{"category": "钉钉 CLI", "slug": "faq"}], prev),
                             [("open-platform", "dws-cli-log"), ("open-platform", "faq")])
        self.assertEqual(targets([], "/nonexistent"), [("open-platform", "dws-cli-log")])


class SupplementDocsTest(unittest.TestCase):
    """运营补充篇(supplement/,ops 从钉钉文档同步):能被 ctx/find/cat 命中,不给链接、不露 frontmatter,冲突不按日期裁决,
    同分不压官方篇;无 frontmatter/无日期/BOM/坏格式/读不了都不拖垮检索。全部在临时知识库根里跑(复制 bin/,其余顶层
    条目软链回本库),中断也不会在真实库留下样例。没有运营篇时其余输出不变,由空目录重放逐字节比对保证。"""
    SAMPLE = "zz-test-ops-sample.md"

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(REPO, "meta", "documents.jsonl"), encoding="utf-8") as f:
            rows = [json.loads(l) for l in f if l.strip()]
        cls.twin = next(r for r in rows if r["path"].startswith("docs/products/") and r.get("headings")
                        and 6 <= len(r["headings"][0]) <= 30)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        shutil.copytree(os.path.join(REPO, "bin"), os.path.join(self.root, "bin"))
        for name in os.listdir(REPO):
            if name not in ("bin", "supplement") and not name.startswith("."):
                os.symlink(os.path.join(REPO, name), os.path.join(self.root, name))
        files = {
            self.SAMPLE: "---\ntitle: dws 开源交流群怎么加入\nsource: ops\nupdated_at: 2026-11-05T18:00:00+08:00\n"
                         "stage: trial\nquestions:\n  - dws 交流群群号是多少\n  - 怎么加入 dws 开源交流群\n---\n"
                         "开发者可以扫描 dws 开源仓库 README 里的二维码加入开源交流群，入群后按群公告提问。\n",
            "zz-test-ops-twin.md": f"---\ntitle: {self.twin['headings'][0]}\nsource: ops\nupdated_at: 2026-11-05\n---\n"
                                   "同名运营补充篇正文。\n",
            "zz-test-ops-nofm.md": "没有 frontmatter 的运营补充篇正文。\n",
            "zz-test-ops-nodate.md": "---\ntitle: 无日期运营篇\nsource: ops\n---\n没有日期的运营补充篇正文。\n",
            "zz-test-ops-bom.md": "﻿---\ntitle: 带BOM运营篇\nsource: ops\nupdated_at: 2026-11-04T09:00:00+08:00\n---\n"
                                  "开头带 BOM 的运营补充篇正文。\n",
            "zz-test-ops-bad.md": "---\ntitle: 坏格式运营篇\nupdated_at: 2026-11-05\n  - 普通字段后面跟了列表项\n---\n坏格式运营篇正文。\n",
            "zz-test-ops-noperm.md": "---\ntitle: 读不了的运营篇\n---\n正文\n",
        }
        os.makedirs(os.path.join(self.root, "supplement"))
        for fn, text in files.items():
            with open(os.path.join(self.root, "supplement", fn), "w", encoding="utf-8") as f:
                f.write(text)
        self.noperm = os.path.join(self.root, "supplement", "zz-test-ops-noperm.md")
        os.chmod(self.noperm, 0)

    def tearDown(self):
        os.chmod(self.noperm, 0o600)
        self.tmp.cleanup()

    def cli(self, *args, ok=True):
        p = subprocess.run(["python3", os.path.join(self.root, "bin", "dwsdoc"), *args], cwd=self.root,
                           text=True, capture_output=True, timeout=60)
        if ok and p.returncode != 0:
            raise AssertionError(f"dwsdoc {' '.join(args)} rc={p.returncode}\nstdout={p.stdout}\nstderr={p.stderr}")
        return p

    def test_ctx_find_cat_hit_without_link(self):
        r = self.cli("ctx", "dws 交流群群号是多少")
        out = r.stdout
        self.assertRegex(out, r"(?m)^== 篇目\[\d+/\d+\] supplement/zz-test-ops-sample.md \[supplement\] ==")
        self.assertIn("钉仔运营补充说明,更新于 2026-11-05", out)
        self.assertIn("README 里的二维码", out)
        self.assertNotIn("source: ops", out)        # frontmatter 不进正文
        self.assertIn("不按日期裁决", out)
        self.assertNotIn("日期较新者为准", out)
        if not os.access(self.noperm, os.R_OK):    # root 下 chmod 0 仍可读,跳过
            self.assertIn("跳过运营补充篇 supplement/zz-test-ops-noperm.md", r.stderr)
        self.assertIn("supplement/zz-test-ops-sample.md", self.cli("find", "交流群").stdout)
        cat = self.cli("cat", "supplement/zz-test-ops-sample.md").stdout
        self.assertIn("据钉仔运营补充说明(2026-11-05)", cat)
        self.assertNotIn("questions:", cat)
        self.assertNotIn("http", cat.splitlines()[0])

    def test_command_questions_keep_official_first(self):
        for q in ("dws chat 怎么给群发消息", "dws auth login", "dws chat message list 怎么用"):
            self.assertNotIn(self.SAMPLE, self.cli("ctx", q).stdout, q)

    def test_same_title_ranks_after_official(self):
        out = self.cli("ctx", self.twin["headings"][0]).stdout
        twin = "supplement/zz-test-ops-twin.md"
        if twin in out:
            self.assertIn(self.twin["path"], out)
            self.assertLess(out.index(self.twin["path"]), out.index(twin))

    def test_unrelated_questions_unchanged(self):
        """运营篇不改变无关问题的检索：分词只用官方篇的词料(运营篇小标题「安装和使用」曾把外部安装指南挤出正文)；
        只撞上一个常见短词(「含义」)的运营篇不参与排序。对口问题照常展开。"""
        vocab = ("---\ntitle: 错误码 ZZ-7319 的含义\nsource: ops\nupdated_at: 2026-11-05\n---\n## 安装和使用说明\n"
                 "接口返回 ZZ-7319 表示示例环境的调用配额已用完，次日零点恢复。\n")
        qs = ("DWS是什么？如何安装和使用 DWS（钉钉开发者工具）？我没有开发者权限也能用吗？",
              "dws chat 消息里 msgType 参数的含义", "钉钉开发者后台关闭了dws cli 文档导出后，使用dws上传文档失败，怎么回事")
        def root(td, files):
            shutil.copytree(os.path.join(REPO, "bin"), os.path.join(td, "bin"))
            for name in os.listdir(REPO):
                if name not in ("bin", "supplement") and not name.startswith("."):
                    os.symlink(os.path.join(REPO, name), os.path.join(td, name))
            os.makedirs(os.path.join(td, "supplement"))
            for fn, text in files.items():
                with open(os.path.join(td, "supplement", fn), "w", encoding="utf-8") as f:
                    f.write(text)
            return td

        def run(r, q):  # 检索审计行里的命中计数会把运营篇算进去，其余逐字节比
            out = subprocess.run(["python3", os.path.join(r, "bin", "dwsdoc"), "ctx", q], cwd=r, text=True,
                                 capture_output=True, timeout=60).stdout
            return re.sub(r"(?m)^.*\bfind=\d+.*$", "", out)
        with tempfile.TemporaryDirectory() as t0, tempfile.TemporaryDirectory() as t1:
            bare, with_sup = root(t0, {}), root(t1, {"zz-test-ops-vocab.md": vocab})
            for q in qs:
                self.assertEqual(run(bare, q), run(with_sup, q), q)
            self.assertIn("supplement/zz-test-ops-vocab.md [supplement]", run(with_sup, "错误码 ZZ-7319 是什么意思"))

    def test_edge_files_do_not_break_retrieval(self):
        nofm = self.cli("cat", "supplement/zz-test-ops-nofm.md").stdout
        self.assertIn("没有 frontmatter", nofm)
        self.assertIn("更新日期未知", nofm)
        nodate = self.cli("cat", "supplement/zz-test-ops-nodate.md").stdout
        self.assertIn("「据钉仔运营补充说明」", nodate)
        self.assertNotIn("()", nodate)
        bom = self.cli("cat", "supplement/zz-test-ops-bom.md").stdout
        self.assertIn("更新于 2026-11-04", bom)
        self.assertNotIn("title:", bom)
        self.assertIn("supplement/zz-test-ops-bom.md", self.cli("find", "带BOM运营篇").stdout)
        self.assertIn("坏格式运营篇正文", self.cli("cat", "supplement/zz-test-ops-bad.md").stdout)
        if not os.access(self.noperm, os.R_OK):
            r = self.cli("cat", "supplement/zz-test-ops-noperm.md", ok=False)
            self.assertEqual(r.returncode, 1)
            self.assertIn("读不了运营补充篇", r.stdout)


if __name__ == "__main__":
    unittest.main()
