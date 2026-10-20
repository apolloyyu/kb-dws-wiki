#!/usr/bin/env python3
"""精确控件/跨产品机制证据的离线回归。"""
import os
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]


def ctx(query):
    p = subprocess.run(["python3", str(ROOT / "bin/dwsdoc"), "ctx", query],
                       capture_output=True, text=True, timeout=30, env=os.environ.copy())
    if p.returncode:
        raise AssertionError(p.stderr or p.stdout)
    return p.stdout


class SubjectEvidenceTest(unittest.TestCase):
    def test_exact_component_section_overview_cannot_replace_it(self):
        for q in ("DDHolidayField 是oa审批的什么组件模板，有文档吗", "请说明 DDHolidayField 的提交格式"):
            with self.subTest(q=q):
                out = ctx(q)
                self.assertIn("== 篇目[1/", out)
                first = out.split("== 篇目[1/", 1)[1].split("\n", 1)[0]
                self.assertIn("oa-form-components.md", first)
                self.assertIn("### DDHolidayField（请假套件）", out)
                self.assertIn("leave-duration / leave-check", out)
                self.assertIn("--request", out)
                self.assertIn("单表单最大控件数", out)
                self.assertIn("fast=0", out)

    def test_attachment_value_and_name_survive_body_cap(self):
        for q in ("审批携带附件的情况是如何发起的", "DDAttachment 的 value 怎么写"):
            with self.subTest(q=q):
                out = ctx(q)
                self.assertIn("### DDAttachment（附件控件）", out)
                self.assertIn("spaceId、fileName、fileSize、fileType、fileId", out)
                self.assertIn("JSON 数组转义字符串", out)
                self.assertIn("props.label", out)

    def test_event_token_query_not_mcp_development(self):
        for q in ("事件监听持续机制是什么样的，如果token过期了会发生什么", "监听断线重连时 access token 如何刷新"):
            with self.subTest(q=q):
                out = ctx(q)
                self.assertRegex(out, r"(?m)^# dws event ")
                first = out.split("== 篇目[1/", 1)[1].split("\n", 1)[0]
                self.assertIn("docs/products/event.md", first)
                self.assertIn("lockedRefresh", out)
                self.assertIn("transient", out)
                self.assertIn("ProfileStatusExpired", out)

    def test_existing_positive_evidence_is_retained(self):
        out = ctx("我在同一台机器多次启用dws event consume，只有一个收到消息，其余没有反应")
        self.assertIn("全部匹配者", out)
        self.assertIn("扇出", out)
        out = ctx("通过AI发送文案支持修改吗")
        self.assertIn("--ai-tag", out)
        self.assertIn("DWS_AGENT_PRODUCT", out)

    def test_mirror_references_are_pinned(self):
        out = ctx("DDHolidayField 是什么组件")
        refs = [l for l in out.splitlines() if l.startswith("引用:") and "oa-form-components.md" in l]
        self.assertTrue(refs)
        self.assertTrue(all("/blob/main/" not in r for r in refs))

    def test_common_fields_and_platform_are_not_model_anchors(self):
        out = ctx("dws device登陆可以取到UserID吗，还是只是绑定CorpID")
        self.assertNotIn("摘录：", out)
        first = out.split("== 篇目[1/", 1)[1].split("\n", 1)[0]
        self.assertNotIn("docs/products/oa.md", first)
        out = ctx("dws event stop 在 Windows 报错 signal bus not supported by windows，如何排查")
        first = out.split("== 篇目[1/", 1)[1].split("\n", 1)[0]
        self.assertIn("docs/products/event.md", first)


if __name__ == "__main__":
    unittest.main()
