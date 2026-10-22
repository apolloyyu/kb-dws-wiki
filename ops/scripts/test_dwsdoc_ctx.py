#!/usr/bin/env python3
"""dwsdoc ctx/card 的快路径与证据边界回归测试。"""
import os
import re
import subprocess
import unittest
from test_dwsdoc_subjects import SubjectEvidenceTest  # 主门禁同时执行主体/小节回归。


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
    def test_repaired_source_and_scope_contracts(self):
        for q in ['如何实时监听群消息，并主动回复', '如果没有直接@你，会实时监听群消息，并主动回复吗？通过DWS对接Agent']:
            out = run_dwsdoc('ctx', q)
            self.assertIn('指定群的监听参数是 chat-id 或 chat-query', out)
            self.assertIn('监听我的所有单聊消息', out)
        for q in ['dws auth status refresh_token_valid=true 为什么没有成功', 'dws auth login重新授权后还是不能自动刷新']:
            out = run_dwsdoc('ctx', q)
            self.assertIn('包含时间比较', out)
            self.assertIn('裸 logout 默认退出全部账号', out)
        out = run_dwsdoc('ctx', '使用 DWS CLI 删除个人聊天记录，云端也会被删吗')
        self.assertIn('clear_conversation_messages', out)
        self.assertIn('仅清空当前用户视角的消息', out)
        self.assertNotIn('# 清空会话记录的调用与作用域', run_dwsdoc('ctx', '删除邮件记录'))
        self.assertIn('投影前另有解密分支', run_dwsdoc('ctx', '卡片消息能不能解析'))
        self.assertIn('按字段或行配置权限', run_dwsdoc('ctx', '钉钉表格可以根据字段分配查看权限吗'))
        self.assertNotIn('# AI表格产品权限', run_dwsdoc('ctx', '用户详情的字段查看权限'))
        self.assertNotIn('# AI表格产品权限', run_dwsdoc('ctx', '--prev', 'AI表格的字段查看权限', '邮件附件查看权限失败'))
        self.assertNotIn('# 认证重置与恢复的作用域', run_dwsdoc('ctx', 'dws chat +messages-mget --profile corp:user 查看消息状态和卡片能否解析'))
        switched = run_dwsdoc('ctx', '--prev', 'dws auth status token 刷新异常', 'dws chat +messages-mget --profile corp:user 查看消息状态和卡片能否解析')
        self.assertNotIn('# 认证重置与恢复的作用域', switched)
        self.assertIn('notes/auth-and-credentials.md', switched)  # 原有--prev回退仍保留；新增认证恢复note不得挤占。
        for q in ['auth reset 会删除哪些数据', 'auth login 重新授权失败']:
            self.assertIn('# 认证重置与恢复的作用域', run_dwsdoc('ctx', q))

    def test_workflow_questions_expand_parameter_and_scope_evidence(self):
        out = run_dwsdoc('ctx', '获取消息拉不到非本组织的群信息')
        self.assertIn('--target-org-id 和 --all 必须且只能指定一个', out)
        out = run_dwsdoc('ctx', '如何做到单聊或者群聊的实时回复')
        self.assertIn('群自动回复使用顶层', out)
        self.assertIn('统一发送入口的群目标参数是group', out)
        for question in ['chat消息如何自动回复', 'IM实时回复']:
            self.assertIn('群自动回复使用顶层', run_dwsdoc('ctx', question))
        out = run_dwsdoc('ctx', 'DWS能获取用户在钉钉及宜搭的操作记录不')
        self.assertIn('企业内部应用 + App Token + 服务端 OpenAPI', out)
        self.assertIn('audit是本地CLI操作审计', out)

    def test_new_workflow_notes_do_not_capture_other_products(self):
        for question, title in [
            ('mapping字段的参数是什么意思', '# 事件系统的来源、投递与心跳边界'),
            ('宜搭附件通过 drive download 能断点续传吗', '# 个人行为检索、业务变更记录与本地审计的范围'),
            ('跨组织日历数据导入', '# 跨组织消息数据授权的目标与范围'),
            ('设置邮件自动回复', '# 实时消息监听到回复的参数与标识契约'),
            ('IM查询已完成，设置邮件自动回复', '# 实时消息监听到回复的参数与标识契约'),
            ('IM查询已完成；设置邮件自动回复', '# 实时消息监听到回复的参数与标识契约'),
            ('邮件新消息自动回复失败', '# 实时消息监听到回复的参数与标识契约'),
            ('监听群消息，然后自动回复邮件失败为什么', '# 实时消息监听到回复的参数与标识契约'),
            ('监听群消息，并自动回复日历邀请', '# 实时消息监听到回复的参数与标识契约'),
            ('日历提醒消息实时回复', '# 实时消息监听到回复的参数与标识契约'),
            ('获取非本组织的邮件消息', '# 跨组织消息数据授权的目标与范围')]:
            self.assertNotIn(title, run_dwsdoc('ctx', question))

    def test_message_attribution_uses_primary_source_and_scope(self):
        out = run_dwsdoc('ctx', '“通过AI发送”文案支持修改吗')
        self.assertIn('fast=0', out)
        self.assertIn('# 消息角标、产品标识与发送入口的范围', out)
        self.assertIn('DWS_AGENT_PRODUCT', out)
        self.assertIn('原生用户消息 send/reply 提供 ai-tag 开关', out)
        self.assertIn('internal/helpers/chat.go', out)
        self.assertNotIn('# 消息角标、产品标识与发送入口的范围',
                         run_dwsdoc('ctx', 'dws chat message list'))

    def test_event_followup_preserves_active_implementation_boundary(self):
        out = run_dwsdoc('ctx', '怎么检测到断连，有心跳包吗')
        self.assertIn('不能把协议类型或静默接收分支称为已经启用', out)
        out = run_dwsdoc('ctx', '事件监听持续机制是什么样的，如果token过期了会发生什么')
        self.assertIn('既有 WebSocket', out)
        self.assertIn('不能由取票刷新逻辑推导', out)

    def test_inherited_flags_are_not_denied_by_leaf_card(self):
        for q in ('请解释 dws auth login --profile "<corpId>:<userId>"，保留占位符，不要执行',
                  'dws event consume --client-id abc 怎么用', 'dws chat message list --format json',
                  'dws auth login -f table', 'dws auth login -v', 'dws auth login -y',
                  'dws auth login -vy', 'dws auth login -o result.json'):
            out = run_dwsdoc('ctx', q)
            self.assertIn('fast=0', out)
            self.assertIn('# 根命令参数与叶子参数的证据范围', out)
            self.assertIn('bindPersistentFlags', out)
        out = run_dwsdoc('ctx', 'dws agoal strategy detail --profile-id abc')
        self.assertNotIn('# 根命令参数与叶子参数的证据范围', out)
        self.assertIn('card=1(fast=1)', run_dwsdoc('ctx', 'dws auth login'))

    def test_event_transport_contract_is_expanded(self):
        out = run_dwsdoc("ctx", "dws event consume 心跳与断连怎么处理")
        self.assertIn("fast=0", out)
        self.assertIn("SYSTEM ping", out)
        self.assertIn("不能证明服务端如何重投", out)
        self.assertNotIn("服务端据未确认状态重投", out)
        self.assertNotIn("/blob/main/internal/event/", out)
        unrelated = run_dwsdoc("ctx", "日历事件有哪些类型")
        self.assertNotIn("SYSTEM ping", unrelated)

    def test_reset_scope_is_not_profile_local(self):
        out = run_dwsdoc("ctx", "dws auth reset --profile abc 清除范围是什么")
        self.assertIn("所有 profile", out)
        self.assertIn("不证明服务端令牌吊销", out)
        self.assertIn("先恢复或统一原登录密钥", out)
        login = run_dwsdoc("ctx", "dws auth login")
        self.assertNotIn("# 认证重置与恢复的作用域", login)

    def test_auth_failure_original_wording_and_followup(self):
        out = run_dwsdoc("ctx", "二号 Token 刷新失败: 旧版登录态已无法由当前认证服务刷新；本地 profile 已保留，请重新运行 dws auth login 完成一次重新授权；Token 自动刷新一直失败，什么解决")
        self.assertIn("所有 profile", out)
        followup = run_dwsdoc("ctx", "--prev", "Token 刷新失败，请重新运行 dws auth login", "二号 重新授权后，新的 token 格式还是不能正常自动刷新")
        self.assertIn("所有 profile", followup)
        self.assertIn("lockedRefresh", followup)

    def test_event_followup_uses_previous_subject_only(self):
        out = run_dwsdoc("ctx", "--prev", "二号 事件监听连接会突然断开，比如网络中断等问题怎么处理的", "二号 怎么检测到断连，有心跳包吗")
        self.assertIn("SYSTEM ping", out)
        self.assertIn("本地 IPC", out)
        repeat = run_dwsdoc("ctx", "事件监听持续机制是什么样的，如果token过期了会发生什么")
        self.assertIn("SYSTEM ping", repeat)
        self.assertIn("lockedRefresh", repeat)
        simple = run_dwsdoc("ctx", "--prev", "事件监听的机制是什么", "dws auth login")
        self.assertNotIn("SYSTEM ping", simple)

    def test_product_tokens_do_not_trigger_login_reset(self):
        for q in ("dws aitable +record-write-result 的 clientToken 不匹配怎么办", "Webhook Token 失效怎么办", "开放平台应用 access_token 刷新失败怎么办", "dws aitable +record-write-result 的 clientToken 不匹配，已经运行 dws auth login 仍失败怎么办", "我已运行 dws auth status，开放平台应用 access_token 刷新失败怎么办"):
            with self.subTest(q=q):
                out = run_dwsdoc("ctx", q)
                self.assertNotIn("# 认证重置与恢复的作用域", out)

    def test_explicit_reset_wins_over_credential_field_words(self):
        for q in ("dws auth reset 会删除应用凭证吗", "dws auth reset 删除 appSecret 吗", "dws auth reset，清除应用凭证吗", "dws auth reset, 清除 appSecret 吗"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("# 认证重置与恢复的作用域", out)
            self.assertIn("应用凭证", out)

    def test_credential_owner_wins_over_login_history(self):
        for owner in ("企业内部应用的 access_token", "机器人的 access_token", "第三方应用 refresh_token"):
            for history in ("我已经运行 dws auth login，", "我已经运行 dws auth status，"):
                with self.subTest(owner=owner, history=history):
                    out = run_dwsdoc("ctx", history + owner + " 刷新失败怎么办")
                    self.assertNotIn("# 认证重置与恢复的作用域", out)
                    followup = run_dwsdoc("ctx", "--prev", history + owner + " 刷新失败怎么办", "还是刷新失败，怎么恢复？")
                    self.assertNotIn("# 认证重置与恢复的作用域", followup)
        for current in ("现在问 dws auth login 报错无法登录怎么恢复", "现在运行 dws auth login 报错无法登录怎么恢复", "现在问 dws auth login，报错无法登录怎么恢复"):
            switched = run_dwsdoc("ctx", "--prev", "机器人的 access_token 失效", current)
            self.assertIn("# 认证重置与恢复的作用域", switched)

    def test_exact_command_keeps_fast_card(self):
        out = run_dwsdoc("ctx", "dws auth login")
        self.assertIn("card=1(fast=1)", out)
        self.assertIn("== 证据契约(覆盖状态) ==", out)
        self.assertIn("card_present: yes", out)

    def test_natural_login_question_keeps_full_context(self):
        out = run_dwsdoc("ctx", "dws 怎么登录")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("== 证据契约(覆盖状态) ==", out)
        self.assertIn("card_present: yes", out)

    def test_support_and_card_capability_force_full_context(self):
        out = run_dwsdoc("ctx", "dws 能解析卡片消息吗")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("投影前另有解密分支", out)
        self.assertIn("runtime_observed: no", out)

    def test_id_format_claim_forces_full_context(self):
        out = run_dwsdoc("ctx", "oa approval detail 的 instance-id 格式必须是 UUID 吗")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("card_present: yes", out)
        self.assertIn("runtime_observed: no", out)

    def test_error_causality_forces_full_context(self):
        out = run_dwsdoc("ctx", "oa approval detail 返回 PARAM_ERROR 的根因是什么")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("runtime_observed: no", out)

    def test_enumeration_forces_full_context(self):
        out = run_dwsdoc("ctx", "oa approval 有哪些命令")
        self.assertIn("fast=0", out)

    def test_unclosed_structured_input_forces_full_context(self):
        out = run_dwsdoc("ctx", 'oa approval detail {"instanceId":"abc"')
        self.assertIn("fast=0", out)
        self.assertIn("input_complete: no", out)

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
        self.assertIn("尚未解密的 ciphertext", out)
        self.assertIn("投影前另有解密分支", out)
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
        self.assertIn("支持性问题的命令候选", out)
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
        self.assertIn("runtime_observed: no", out)

    def test_card_command_also_prints_contract(self):
        out = run_dwsdoc("card", "oa approval detail")
        self.assertIn("# dws oa approval detail", out)
        self.assertIn("== 证据契约(覆盖状态) ==", out)
        self.assertIn("runtime_observed: no", out)


    def test_digital_employee_group_access_uses_whitelist_note(self):
        # 实录 2026-10-10:检索给出 add-bot/@所有人,模型编出「数字员工靠关联机器人 robotCode 入群」并在群内复读
        for q in ("如何让群所有人可以与数字员工对话", "数字员工怎么拉进群",
                  "怎么让别人也能和我的数字员工对话", "数字员工的 robotCode 在哪看"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("notes/digital-employee.md", out, q)
            self.assertIn("allowed-groups", out, q)
            # 上游 10-13(a3c7d486) 起正式 connect 绑定走平台访问策略,不再是「默认仅主管+白名单」
            self.assertRegex(out, r"> 原文\(\[DWS 文档依据\]\(https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli/blob/[0-9a-f]+/docs/digital-employee-adapters\.md\)\): `manage create` 创建并通过正式", q)
            self.assertIn("platform", out, q)
            self.assertIn("notes_present: yes", out, q)
            self.assertIn("card=1(fast=0)", out, q)
            self.assertRegex(out, r"(?m)^# dws dingtalk-tag ", q)
            self.assertNotIn("add-bot --robot-code", out, q)
            self.assertIn("runtimeBindingId", out, q)
            self.assertNotIn("- notes：行为说明只作依据", out, q)

    def test_digital_employee_origin_uses_origin_note(self):
        # 实录 2026-10-12:把 DEAP 智能体/企业自建 Agent 接口列为创建方式,随后又称「关系未说明」并撤回
        for q in ("DEAP创建的智能体就是你所谓的数字员工吗", "那你说的数字员工到底在哪儿创建的？不是DEAP这？",
                  "AI 助理改名为数字员工了吗", "数字员工怎么创建"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("notes/digital-employee.md", out, q)
            self.assertIn("notes_present: yes", out, q)
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
            self.assertIn("> 原文([DWS 文档依据](https://open.dingtalk.com/document/development/dws-cli-log)", out, q)
            self.assertIn(form, out, q)
            self.assertNotIn("其他域名一律不造", out, q)
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
        self.assertIn("rate-limit-and-backend.md", out)
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
            self.assertIn("notes_present: yes", out, q)
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
        self.assertIn("notes_present: yes", out)

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
            self.assertIn("rate-limit-and-backend.md", out, q)
            self.assertIn("走钉钉 MCP 网关", out, q)
            self.assertIn("direct_runtime.go", out, q)
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
            self.assertRegex(out, r"--ai-tag\s*\(Bool\)", q)

    def test_help_text_flag_recall_does_not_add_noise(self):
        # 单个泛词(发送/消息)或偶撞词不得把无关 flag 拉进来
        out = run_dwsdoc("ctx", "创建空会话转发")
        self.assertNotIn("--ai-tag", out)
        self.assertNotIn("--client-token", out)

    def test_capability_question_keeps_long_modifier_before_action(self):
        for q in ("钉钉表格可以根据字段分配查看权限吗",
                  "可以按照成员所在部门配置记录的查看范围吗？",
                  "消息能按发送者和群聊分别限制可见范围吗?"):
            out = run_dwsdoc("ctx", q)
            self.assertIn("fast=0", out, q)
            self.assertIn("runtime_observed: no", out, q)
        self.assertIn("fast=1", run_dwsdoc("ctx", "dws auth login 文档在哪"))

    def test_challenge_turns_off_fast_card(self):
        # R10.5 回退 Q175:用户质疑后仍走快卡,模型复读卡片
        out = run_dwsdoc("ctx", "所以你的意思dws auth login 判断状态其实不准的对吧？")
        self.assertIn("card=1(fast=0)", out)
        self.assertIn("card=1(fast=1)", run_dwsdoc("ctx", "dws auth login 文档在哪"))

    def test_prev_question_joins_follow_up_terms(self):
        out = run_dwsdoc("ctx", "--prev", "dws 发送消息怎么不显示AI标识", "那默认是true还是false")
        self.assertRegex(out, r"--ai-tag\s*\(Bool\)")

    def test_any_merged_notes_forbid_citing_note_files(self):
        # R10.6.0 盲测 Q227/Q232/Q242:禁引只在专属 note 命中时出现,泛 notes 并入时回复参考区列出 notes/event-system.md
        out = run_dwsdoc("ctx", "二号 如果在同一台机器上启用多个事件监听，这个应该是可行的吧")
        self.assertIn("== 行为语义(notes", out)
        self.assertIn("notes_present: yes", out)

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
            self.assertIn("token-lifetime.md", out, q)
            self.assertRegex(out, r"\[源码依据\]\(https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli/blob/[0-9a-f]{7,40}/", q)
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
        self.assertRegex(out, r"\[源码依据\]\(https://\S+#L\d+\)")
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

if __name__ == "__main__":
    unittest.main()
