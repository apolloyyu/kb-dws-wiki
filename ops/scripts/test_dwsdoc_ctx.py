#!/usr/bin/env python3
"""dwsdoc ctx/card 的快路径与证据边界回归测试。"""
import os
import subprocess
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
    def test_simple_exact_command_keeps_fast_card(self):
        out = run_dwsdoc("ctx", "dws 怎么登录")
        self.assertIn("card=1(fast=1)", out)
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
        self.assertIn("# dws oa approval attachment upload", out)
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
        self.assertIn("行为语义(notes,复杂问法自动并入)", out)

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


if __name__ == "__main__":
    unittest.main()
