#!/usr/bin/env python3
"""确定性重建 kb-dws-wiki 的镜像层与实体索引(零 LLM,对齐 kb-dingtalk-open-platform 范式)。

用法: build_dws_kb.py <dws源码目录> [--repo <wiki仓库根,默认脚本上两级>]

产出(全部机器生成,内容通路无 LLM):
  docs/                镜像层(逐字):command-index.md、CHANGELOG.md、products/**(来自
                       skills/mono/references/products/,上游人写的产品线使用文档)
  graph/commands.jsonl 主命令树:命令+描述+适用场景(来自 command-index)+flags(源码静态提取,带 文件:行号)
  graph/shortcuts.jsonl +xxx 短命令:声明式 Flag 结构直接解析(带 文件:行号)
  cards/cmd/*.md       主命令与 shortcut 的确定性答案卡(full/partial 自判)
  cards/index.jsonl    命令 key → 卡片路径/完整度
  meta/documents.jsonl docs/+notes/ 逐篇索引
  meta/BUILD_REPORT.md 对账报告(命令数/归属率/卡片覆盖率/未归属清单)

lint(不过即退出非零):
  - commands.jsonl 条数 == command-index + CLIPath + cobra 树去重后的并集
  - shortcuts.jsonl 条数 == 源码 `Command: "+..."` 声明数
  - 卡片数 == commands + shortcuts、总数 >=900、full 完整率 >=70%
行为语义(notes/)不归本脚本管——那层走 LLM 生成+候选审阅(dws_regen.py --deepen)。


【bin 工具数据契约】bin/dwsdoc(含 ctx)依赖本构建器产物的以下字段,改动前先同步 bin 并跑冒烟:
  graph/commands.jsonl: cmd/usage/usage_verified/example/flags_verified/desc/when/defs[{file,line}]/flags[{name,short,type,required,hidden,help,line}]
  graph/shortcuts.jsonl: product/cmd/desc/file/line/flags[{name,type,desc}]
  meta/documents.jsonl: path/layer/headings
冒烟由 ECS det_build 在 push 前执行(dwsdoc cmd chat + dwsdoc ctx chat)。"""
import json
import os
import re
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))


def rel(p, base):
    return os.path.relpath(p, base)


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def git_head(src):
    r = subprocess.run(["git", "-C", src, "rev-parse", "--short", "HEAD"],
                       capture_output=True, text=True)
    return r.stdout.strip() or "unknown"


# ---------- 镜像层 ----------

def frontmatter(source_path, commit):
    return ("---\n"
            f"source_path: \"{source_path}\"\n"
            f"source_commit: \"{commit}\"\n"
            "layer: mirror   # 逐字镜像,正文与上游一致,勿手工修改\n"
            "---\n\n")


def mirror(src, commit):
    docs = os.path.join(REPO, "docs")
    shutil.rmtree(docs, ignore_errors=True)
    os.makedirs(docs)
    copied = []
    plan = [("docs/command-index.md", "command-index.md"),
            ("CHANGELOG.md", "CHANGELOG.md")]
    prod_src = os.path.join(src, "skills", "mono", "references", "products")
    for root, _, files in os.walk(prod_src):
        for fn in sorted(files):
            sp = os.path.join(root, fn)
            plan.append((rel(sp, src), os.path.join("products", rel(sp, prod_src))))
    for sp_rel, dp_rel in plan:
        sp = os.path.join(src, sp_rel)
        if not os.path.exists(sp):
            continue
        dp = os.path.join(docs, dp_rel)
        os.makedirs(os.path.dirname(dp), exist_ok=True)
        body = open(sp, encoding="utf-8", errors="replace").read()
        if dp.endswith(".md"):
            open(dp, "w", encoding="utf-8").write(frontmatter(sp_rel, commit) + body)
        else:
            shutil.copy(sp, dp)
        copied.append(dp_rel)
    return copied


# ---------- 主命令树:command-index 表格 ----------

ROW = re.compile(r"^\|\s*`dws ([^`]+)`\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")


def parse_index(src):
    cmds = {}
    for line in open(os.path.join(src, "docs", "command-index.md"), encoding="utf-8"):
        m = ROW.match(line.strip())
        if m and m.group(1).strip() != "…":
            cmds[m.group(1).strip()] = {"desc": m.group(2), "when": m.group(3)}
    return cmds


# ---------- flags 静态提取 ----------

USE = re.compile(r'Use:\s*"([^"]+)"')
FLAG = re.compile(r'\.Flags\(\)\.(String|Bool|Int|Int64|Float64|Duration|StringSlice|StringArray|Count)'
                  r'(Var)?(P)?\s*\(')
HIDDEN = re.compile(r'MarkHidden\("([\w-]+)"\)')
STR = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parse_call_args(text):
    """取调用括号内的字符串字面量(跨行,粗粒度但够用)。"""
    depth, buf = 0, []
    for ch in text:
        if ch == "(":
            depth += 1
            if depth == 1:
                continue
        elif ch == ")":
            depth -= 1
            if depth == 0:
                break
        if depth >= 1:
            buf.append(ch)
    return STR.findall("".join(buf))


def extract_flags(src):
    """变量名追踪归属:cmdVar := &cobra.Command{Use:...} ↔ cmdVar.Flags().Xxx(...)。
    flag 调用挂到同名变量在其之前最近一次的 cobra.Command 赋值上(处理 cmd 复用与命名变量远距注册)。"""
    ASSIGN = re.compile(r'(\w+)\s*:?=\s*(?:\w+\()*&cobra\.Command\{')
    FCALL = re.compile(r'(\w+)\.Flags\(\)\.(String|Bool|Int|Int64|Float64|Duration|StringSlice|StringArray|Count)(Var)?(P)?\s*\(')
    REQ = re.compile(r'(\w+)\.MarkFlagRequired\("([\w-]+)"\)')
    HID = re.compile(r'(\w+)\.Flags\(\)\.MarkHidden\("([\w-]+)"\)')
    defs = []
    root = os.path.join(src, "internal")
    for dirpath, _, files in os.walk(root):
        if os.sep + "shortcut" in dirpath:
            continue
        for fn in files:
            if not fn.endswith(".go") or fn.endswith("_test.go"):
                continue
            path = os.path.join(dirpath, fn)
            text = open(path, encoding="utf-8", errors="replace").read()
            # 变量名 cmd/f 在不同函数反复使用；完整性检测必须限制在所属函数体。
            func_spans = []
            starts = list(re.finditer(r'(?m)^func\b', text))
            for i, fm in enumerate(starts):
                limit = starts[i + 1].start() if i + 1 < len(starts) else len(text)
                brace = text.find("{", fm.start(), limit)
                if brace >= 0:
                    body = _scan_block(text, brace)
                    func_spans.append((fm.start(), brace + len(body) + 2))

            def function_scope(pos):
                for a, z in func_spans:
                    if a <= pos < z:
                        return text[a:z]
                return text

            # 严格的一参数 flag helper 可安全递归展开；带额外行为参数的 helper 不解析。
            helper_defs = {}
            for a, z in func_spans:
                scope = text[a:z]
                hm = re.match(r'func\s+(\w+)\s*\(([^)]*)\)', scope)
                if not hm or not hm.group(1).endswith(("Flag", "Flags")):
                    continue
                pm = re.fullmatch(r'\s*(\w+)\s+\*cobra\.Command\s*', hm.group(2))
                if not pm:
                    continue
                name, param = hm.group(1), pm.group(1)
                call_re = re.compile(
                    r'\b' + re.escape(param)
                    + r'\.Flags\(\)\.(String|Bool|Int|Int64|Float64|Duration|StringSlice|StringArray|Count)(Var)?(P)?\s*\(')
                flags = []
                for cm in call_re.finditer(scope):
                    args = STR.findall(scope[cm.end() - 1:cm.end() + 400].split(")\n")[0])
                    if not args:
                        continue
                    typ, is_p = cm.group(1), cm.group(3)
                    fname = args[0]
                    short = args[1] if is_p and len(args) > 1 and len(args[1]) <= 1 else ""
                    help_ = args[-1] if len(args) >= 2 and args[-1] not in (fname, short) else ""
                    flags.append({"name": fname, "short": short, "type": typ,
                                  "help": help_[:160],
                                  "line": text[:a + cm.start()].count("\n") + 1,
                                  "required": False, "hidden": False})
                for mm in re.finditer(r'\b' + re.escape(param) + r'\.Flags\(\)\.MarkHidden\("([\w-]+)"\)', scope):
                    for f in flags:
                        if f["name"] == mm.group(1):
                            f["hidden"] = True
                for mm in re.finditer(r'\b' + re.escape(param) + r'\.MarkFlagRequired\("([\w-]+)"\)', scope):
                    for f in flags:
                        if f["name"] == mm.group(1):
                            f["required"] = True
                nested = re.findall(r'\b(\w*Flags?)\s*\(\s*' + re.escape(param) + r'\s*\)', scope)
                helper_defs[name] = {"flags": flags, "nested": [x for x in nested if x != name]}

            def resolve_helper(name, stack=()):
                if name in stack or name not in helper_defs:
                    return None
                out_flags = [dict(f) for f in helper_defs[name]["flags"]]
                for child in helper_defs[name]["nested"]:
                    sub = resolve_helper(child, stack + (name,))
                    if sub is None:
                        return None
                    out_flags.extend(sub)
                merged = {}
                for f in out_flags:
                    merged.setdefault(f["name"], f)
                return list(merged.values())

            # 变量赋值点 → Use 叶名
            assigns = {}   # var -> [(pos, def_dict)]
            for m in ASSIGN.finditer(text):
                seg = text[m.end():m.end() + 500]
                um = USE.search(seg)
                if not um:
                    continue
                sm = re.search(r'Short:\s*"((?:[^"\\]|\\.)*)"', seg)
                line = text[:m.start()].count("\n") + 1
                d = {"file": rel(path, src), "line": line, "pos": m.start(), "var": m.group(1),
                     "use": um.group(1).split()[0], "use_raw": um.group(1).strip(),
                     "short_desc": (sm.group(1) if sm else ""), "flags": [],
                     "flags_verified": True}
                assigns.setdefault(m.group(1), []).append((m.start(), d))
                defs.append(d)

            def owner(var, pos):
                cands = [d for p0, d in assigns.get(var, []) if p0 < pos]
                return cands[-1] if cands else None

            for m in FCALL.finditer(text):
                d = owner(m.group(1), m.start())
                if d is None:
                    continue
                typ, is_p = m.group(2), m.group(4)
                args = STR.findall(text[m.end() - 1:m.end() + 400].split(")\n")[0])
                if not args:
                    continue
                name = args[0]
                short = args[1] if is_p and len(args) > 1 and len(args[1]) <= 1 else ""
                help_ = args[-1] if len(args) >= 2 and args[-1] not in (name, short) else ""
                d["flags"].append({"name": name, "short": short, "type": typ,
                                   "help": help_[:160],
                                   "line": text[:m.start()].count("\n") + 1,
                                   "required": False, "hidden": False})
            for m in REQ.finditer(text):
                d = owner(m.group(1), m.start())
                if d:
                    for f in d["flags"]:
                        if f["name"] == m.group(2):
                            f["required"] = True
            for m in HID.finditer(text):
                d = owner(m.group(1), m.start())
                if d:
                    for f in d["flags"]:
                        if f["name"] == m.group(2):
                            f["hidden"] = True
            # helper 注入/PersistentFlags/动态变量名无法由上面的直接调用解析完整；
            # 明确标不完整，让答案卡回落正文，不能把“没抽到”误写成“没有 flag”。
            for entries in assigns.values():
                for _, d in entries:
                    var = re.escape(d["var"])
                    scope = function_scope(d["pos"])
                    helper_names = re.findall(
                        r'(?i)(?:\w+\.)?(\w*Flags?)\s*\(\s*' + var + r'\b', scope)
                    unresolved_helper = False
                    for helper_name in helper_names:
                        extra = resolve_helper(helper_name)
                        if extra is None:
                            unresolved_helper = True
                            continue
                        known = {f["name"] for f in d["flags"]}
                        d["flags"].extend(f for f in extra if f["name"] not in known)
                    persistent = re.search(r'\b' + var + r'\.PersistentFlags\(\)', scope)
                    # 只把 `f := cmd.Flags()` 这类真实别名算未解析；`_ = cmd.Flags().MarkHidden(...)`
                    # 不是别名，不能误伤所有带隐藏 flag 的命令。
                    alias_flags = re.search(r'\b[A-Za-z]\w*\s*:?=\s*' + var + r'\.Flags\(\)', scope)
                    dynamic_name = any(not f.get("name") for f in d["flags"])
                    if unresolved_helper or persistent or alias_flags or dynamic_name:
                        d["flags_verified"] = False
    return defs


def extract_clipaths(src):
    """源码里的 CLIPath 标注 = 命令全路径权威来源,用于补 command-index 滞后缺漏。"""
    CP = re.compile(r'CLIPath:\s*"([^"]+)"')
    out = {}
    root = os.path.join(src, "internal")
    for dirpath, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".go") or fn.endswith("_test.go"):
                continue
            path = os.path.join(dirpath, fn)
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in CP.finditer(text):
                # 源码个别 CLIPath 带尾空格；不 strip 会与 index/cobra 的同名路径并存，
                # 生成 aisearch 与 "aisearch " 两条实体，卡片文件名归一后发生覆盖。
                cp = m.group(1).strip()
                if cp:
                    out.setdefault(cp, {"file": rel(path, src),
                                        "line": text[:m.start()].count("\n") + 1})
    return out


# ---------- 源码 Usage/Example:恢复规范全路径与位置参数 ----------
_TEXT_FIELD_RE = re.compile(r'(?:Example|Long):\s*(?:`([^`]*)`|"((?:[^"\\]|\\.)*)")', re.S)


def extract_usage_paths(src):
    """从每个 Cobra 字面量自己的 Long/Example 中恢复规范路径与完整 Usage。

    这比仅按 leaf 名猜父树可靠:同一个 publish 同时存在于 dev app version 与
    dev mcp tool。Example 明写 `dws dev mcp tool publish`,并且与该字面量的
    Use/Short/源码行天然同源。路径截到本命令 leaf 为止,不会把示例位置参数误当子命令。
    """
    out = {}
    root = os.path.join(src, "internal")
    for dirpath, _, files in os.walk(root):
        if os.sep + "shortcut" in dirpath:
            continue
        for fn in files:
            if not fn.endswith(".go") or fn.endswith("_test.go"):
                continue
            path = os.path.join(dirpath, fn)
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r'&cobra\.Command\{', text):
                block = _scan_block(text, m.end() - 1)
                um = _FIELD_RE["Use"].search(block)
                if not um:
                    continue
                use_raw = um.group(1).strip()
                leaf = use_raw.split()[0].lower()
                sm = _FIELD_RE["Short"].search(block)
                short = sm.group(1) if sm else ""
                strings = []
                for tm in _TEXT_FIELD_RE.finditer(block):
                    s = tm.group(1)
                    if s is None:
                        try:
                            s = json.loads('"' + tm.group(2) + '"')
                        except ValueError:
                            s = tm.group(2)
                    strings.append(s)
                for s in strings:
                    for dm in re.finditer(r'(?:^|[\n;])\s*(?:\$\s*)?dws\s+([^\n;#]+)', s):
                        toks = []
                        for tok in dm.group(1).strip().split():
                            tok = tok.strip("\\").lower()
                            if not re.fullmatch(r'[+_a-z][+_a-z0-9-]*', tok):
                                break
                            toks.append(tok)
                            if tok == leaf:
                                cp = " ".join(toks)
                                meta = {"file": rel(path, src),
                                        "line": text[:m.start()].count("\n") + 1,
                                        "usage": " ".join(toks[:-1] + [use_raw]),
                                        "example": "dws " + " ".join(dm.group(1).strip().rstrip("\\").split()),
                                        "desc": short}
                                old = out.get(cp)
                                # 同一字面量通常列多条示例；保留第一条（一般是最小规范用法），
                                # 只在旧记录无描述而新记录有描述时替换。
                                if old is None or (not old["desc"] and short):
                                    out[cp] = meta
                                break
    return out


# ---------- cobra 命令树:补 command-index/CLIPath/Usage 都没有的整族命令 ----------
# 上游 docs/command-index.md 只收产品命令,CLI 自身的 auth/profile/config/connect/
# skill/mcp 等整族一条不收(实录:`grep -c "dws auth" command-index.md` = 0)。
# 后果是 KB 里查不到 `auth login`/`auth status`,而这是最高频的登录态问题 ——
# 助理查不到就可能答"不支持"(同类实录 Q238)。故从 cobra 源码把命令树整棵推出来补漏。
_FUNC_RE = re.compile(r'^func\s+(\w+)\s*\([^)]*\)\s*\*cobra\.Command\s*\{', re.M)
_CALL_RE = re.compile(r'\b(\w+)\s*\(')
_FIELD_RE = {k: re.compile(r'(?:^|\n)\s*%s:\s*"((?:[^"\\]|\\.)*)"' % k)
             for k in ("Use", "Short")}


def _scan_block(text, i, op="{", cl="}"):
    """从 text[i]==op 起配平到闭合,跳过 "…"、`…`、// 注释;返回块内文本。
    必须字符串感知:朴素正则会被 `Aliases: []string{"im"}` 里的 } 截断,回溯到
    下一个命令字面量,把 chat 的 Short 抓成 chat chmod 的(v1 实录)。"""
    depth, j, n = 0, i, len(text)
    while j < n:
        c = text[j]
        if c == '"':
            j += 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
        elif c == "`":
            j += 1
            while j < n and text[j] != "`":
                j += 1
        elif c == "/" and j + 1 < n and text[j + 1] == "/":
            while j < n and text[j] != "\n":
                j += 1
        elif c == op:
            depth += 1
        elif c == cl:
            depth -= 1
            if depth == 0:
                return text[i + 1:j]
        j += 1
    return text[i + 1:]


def extract_cobra_tree(src):
    """返回 {命令全路径: (Short, 文件, 行号)};函数体内第一个字面量 = 该函数返回的命令。"""
    nodes = {}
    for dirpath, _, files in os.walk(os.path.join(src, "internal")):
        if os.sep + "shortcut" in dirpath:
            continue
        for fn in files:
            if not fn.endswith(".go") or fn.endswith("_test.go"):
                continue
            path = os.path.join(dirpath, fn)
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in _FUNC_RE.finditer(text):
                body = _scan_block(text, text.index("{", m.end() - 1))
                lit = None
                for lm in re.finditer(r'&cobra\.Command\{', body):
                    blk = _scan_block(body, lm.end() - 1)
                    um = _FIELD_RE["Use"].search(blk)
                    if um:
                        sm = _FIELD_RE["Short"].search(blk)
                        lit = (um.group(1).split()[0], sm.group(1) if sm else "", um.group(1).strip())
                        break
                if not lit:
                    continue
                kids = []
                for am in re.finditer(r'AddCommand\s*\(', body):
                    kids += _CALL_RE.findall(_scan_block(body, am.end() - 1, "(", ")"))
                nodes[m.group(1)] = {"use": lit[0], "short": lit[1], "use_raw": lit[2],
                                     "kids": kids, "file": rel(path, src),
                                     "line": text[:m.start()].count("\n") + 1}
    referenced = {k for n in nodes.values() for k in n["kids"]}
    paths = {}

    def walk(fn, prefix, seen):
        n = nodes.get(fn)
        if not n or fn in seen:
            return
        path = (prefix + [n["use"]]) if n["use"] != "dws" else []
        if path:
            paths[" ".join(path)] = n
        for k in n["kids"]:
            walk(k, path, seen | {fn})

    for r in (f for f, n in nodes.items() if f not in referenced and n["kids"]):
        walk(r, [], set())
    return paths


def attach(cmds, defs):
    """把源码定义挂到规范全路径；有 source hint 时以同文件+最近行强消歧。

    仅按 leaf 猜会把两个 publish 串线：`dev app version publish` 曾错误挂到
    dev_mcp.go，而真正定义在 devapp.go。Usage/CLIPath 的同源文件行优先级最高。
    """
    by_leaf = {}
    for d in defs:
        by_leaf.setdefault(d["use"], []).append(d)
    out, unresolved = [], []
    for path, meta in sorted(cmds.items()):
        parts = path.split()
        leaf, product = parts[-1], parts[0]
        cand = [] if meta.get("no_attach") else by_leaf.get(leaf, [])
        hint_file, hint_line = meta.get("source_file", ""), meta.get("source_line", 0)
        scored = []
        for d in cand:
            score = 0
            same_file = bool(hint_file and d["file"] == hint_file)
            if hint_file:
                score += 1000 if same_file else -1000
            f = d["file"].lower().replace("-", "").replace("_", "")
            if product.replace("-", "") in f:
                score += 2
            if len(parts) >= 2 and parts[-2].replace("-", "") in f:
                score += 1
            distance = abs(d["line"] - hint_line) if same_file and hint_line else 10**9
            scored.append((-score, distance, d["file"], d["line"], d))
        scored.sort()
        if scored and (not hint_file or -scored[0][0] >= 1000):
            if hint_file:
                best = [scored[0][-1]]
            else:
                top_score = scored[0][0]
                best = [x[-1] for x in scored if x[0] == top_score][:3]
        else:
            best = []

        desc = (meta.get("desc") or (best[0].get("short_desc", "") if best else ""))
        defs_out = ([{"file": d["file"], "line": d["line"]} for d in best]
                    or ([{"file": hint_file, "line": hint_line}] if hint_file else []))
        if meta.get("usage"):
            usage, usage_verified = meta["usage"], True
        elif best and best[0].get("use_raw"):
            usage = " ".join(parts[:-1] + [best[0]["use_raw"]])
            usage_verified = True
        else:
            usage, usage_verified = path, False
        row = {"cmd": path, "usage": usage, "usage_verified": usage_verified,
               "example": meta.get("example", ""),
               "flags_verified": bool(best and best[0].get("flags_verified")),
               "product": product, "desc": desc, "when": meta.get("when", ""),
               "defs": defs_out, "flags": (best[0]["flags"] if best else [])}
        if not defs_out:
            unresolved.append(path)
        out.append(row)
    return out, unresolved


# ---------- shortcuts ----------

SC_CMD = re.compile(r'Command:\s*"(\+[\w-]+)"')
SC_FLAG = re.compile(r'\{\s*Name:\s*"([\w-]+)"\s*,\s*Type:\s*shortcut\.Flag(\w+)'
                     r'(?:\s*,\s*Desc:\s*"((?:[^"\\]|\\.)*)")?')
SC_DESC = re.compile(r'(?:Short|Summary|Desc(?:ription)?):\s*"((?:[^"\\]|\\.)*)"')


def extract_shortcuts(src):
    out = []
    root = os.path.join(src, "internal", "shortcut")
    for dirpath, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".go") or fn.endswith("_test.go"):
                continue
            path = os.path.join(dirpath, fn)
            lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
            marks = [(i, SC_CMD.search(l).group(1))
                     for i, l in enumerate(lines) if SC_CMD.search(l)]
            for mi, (i, name) in enumerate(marks):
                end = marks[mi + 1][0] if mi + 1 < len(marks) else min(i + 80, len(lines))
                seg = "\n".join(lines[i:end])
                dm = SC_DESC.search(seg)
                flags = [{"name": f[0], "type": f[1], "desc": (f[2] or "")[:120]}
                         for f in SC_FLAG.findall(seg)]
                out.append({"cmd": name,
                            "product": rel(dirpath, root).split(os.sep)[0],
                            "desc": (dm.group(1) if dm else "")[:160],
                            "flags": flags,
                            "file": rel(path, src), "line": i + 1})
    return out


# ---------- meta ----------

def headings(path):
    try:
        return [l.lstrip("# ").strip() for l in open(path, encoding="utf-8")
                if l.startswith("#")][:12]
    except OSError:
        return []


def build_documents_jsonl():
    rows = []
    for layer in ("docs", "notes"):
        base = os.path.join(REPO, layer)
        if not os.path.isdir(base):
            continue
        for dirpath, _, files in os.walk(base):
            for fn in sorted(files):
                if not fn.endswith(".md"):
                    continue
                p = os.path.join(dirpath, fn)
                rows.append({"doc_id": os.path.splitext(fn)[0],
                             "path": rel(p, REPO), "layer": layer,
                             "headings": headings(p)})
    with open(os.path.join(REPO, "meta", "documents.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return len(rows)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    src = os.path.abspath(sys.argv[1])
    commit = git_head(src)
    print(f"== build_dws_kb: 源码 {src} @ {commit}")

    copied = mirror(src, commit)
    print(f"镜像层 {len(copied)} 个文件")

    cmds = parse_index(src)
    n_index = len(cmds)
    for cp, hint in extract_clipaths(src).items():
        if "+" in cp:      # shortcut 路径归 shortcuts.jsonl,不重复计
            continue
        meta = cmds.setdefault(cp, {"desc": "", "when": "(source-only: CLIPath,以源码为准)"})
        meta.setdefault("source_file", hint["file"])
        meta.setdefault("source_line", hint["line"])
    n_clipath = len(cmds) - n_index

    usage_paths = extract_usage_paths(src)
    before_usage = len(cmds)
    for cp, hint in usage_paths.items():
        if "+" in cp:
            continue
        meta = cmds.setdefault(cp, {"desc": hint["desc"],
                                    "when": "(source-only: Cobra Usage/Example,以源码为准)"})
        if not meta.get("desc") and hint["desc"]:
            meta["desc"] = hint["desc"]
        # Usage 与命令字面量同源且带精确行,比生成式 CLIPath 的远端 metadata 更适合挂 flags。
        meta.update({"source_file": hint["file"], "source_line": hint["line"],
                     "usage": hint["usage"], "example": hint.get("example", "")})
    n_usage = len(cmds) - before_usage

    # 规范叶路径必然证明其全部父分组存在；先补父路径，但不猜描述/源码，不允许它标 full。
    canonical = dict(cmds)
    before_parents = len(cmds)
    for cp in list(canonical):
        parts = cp.split()
        for i in range(1, len(parts)):
            parent = " ".join(parts[:i])
            cmds.setdefault(parent, {"desc": "", "when": "(derived parent:由规范子命令路径证明)",
                                     "usage": parent, "no_attach": True})
    n_parents = len(cmds) - before_parents

    # 简化 Cobra 树只用于补无 Example 的 utility 叶(如 auth reset)。它可能因方法父级/
    # 局部分组丢失产生假短路径，采用三道通用约束:
    # ①同源附近已有 Usage 规范路径且不同 → 丢弃;
    # ②同首尾存在更长规范路径(oa attachment vs oa approval attachment) → 丢弃;
    # ③只有父路径已被同源规范子路径验证后，才递归接纳其孩子。
    source_paths = {}
    for p, meta in canonical.items():
        if meta.get("source_file"):
            source_paths.setdefault(meta["source_file"], set()).add(p)
    usage_near = list(usage_paths.items())
    verified_tree = set(canonical)
    before_cobra = len(cmds)
    for cp, node in sorted(extract_cobra_tree(src).items(), key=lambda x: len(x[0].split())):
        if "+" in cp:
            continue
        near = [p for p, h in usage_near
                if h["file"] == node["file"] and abs(h["line"] - node["line"]) <= 3]
        if near and cp not in near:
            continue
        parts = cp.split()
        longer_same_ends = any(
            p != cp and len(p.split()) > len(parts)
            and p.split()[0] == parts[0] and p.split()[-1] == parts[-1]
            for p in cmds)
        if longer_same_ends:
            continue
        parent = " ".join(parts[:-1])
        same_source_prefix = any(
            p == cp or p.startswith(cp + " ") for p in source_paths.get(node["file"], set()))
        existing = cmds.get(cp)
        allowed = same_source_prefix or (bool(parent) and parent in verified_tree)
        if not allowed:
            continue
        usage = " ".join(parts[:-1] + [node.get("use_raw") or node["use"]])
        data = {"desc": node["short"], "when": "(source-only: 由可达 cobra 命令树推出,以源码为准)",
                "source_file": node["file"], "source_line": node["line"], "usage": usage}
        if existing and existing.get("no_attach"):
            existing.clear()
            existing.update(data)
        elif not existing:
            cmds[cp] = data
        verified_tree.add(cp)
    n_cobra = len(cmds) - before_cobra
    defs = extract_flags(src)
    rows, unresolved = attach(cmds, defs)
    print(f"命令: index {n_index} + CLIPath {n_clipath} + Usage {n_usage} + "
          f"父分组 {n_parents} + cobra 叶 {n_cobra}")
    shortcuts = extract_shortcuts(src)

    # lint
    sc_grep = int(subprocess.run(
        ["bash", "-c",
         f"grep -ro 'Command:\\s*\"+' {src}/internal/shortcut --include='*.go' "
         f"| grep -v _test.go | wc -l"],
        capture_output=True, text=True).stdout.strip() or 0)
    errs = []
    if len(rows) != len(cmds):
        errs.append(f"commands 条数不符 {len(rows)} != {len(cmds)}")
    if abs(len(shortcuts) - sc_grep) > 0:
        errs.append(f"shortcuts 条数不符 解析{len(shortcuts)} != grep{sc_grep}")
    if errs:
        print("LINT FAIL:", "; ".join(errs))
        return 1

    os.makedirs(os.path.join(REPO, "graph"), exist_ok=True)
    with open(os.path.join(REPO, "graph", "commands.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(os.path.join(REPO, "graph", "shortcuts.jsonl"), "w", encoding="utf-8") as f:
        for r in shortcuts:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # 图谱落盘后立即生成答案卡；build_cards 自带原子替换与三道地板，失败则本构建失败，
    # 不允许每日流水线把半套/低覆盖率卡片 push 出去。
    card_script = os.path.join(HERE, "build_cards.py")
    card_run = subprocess.run([sys.executable, card_script, "--repo", REPO],
                              capture_output=True, text=True)
    if card_run.returncode:
        print(card_run.stdout + card_run.stderr, end="")
        return 1
    print(card_run.stdout.strip())
    card_index = load_jsonl(os.path.join(REPO, "cards", "index.jsonl"))
    card_full = sum(r.get("completeness") == "full" for r in card_index)

    os.makedirs(os.path.join(REPO, "meta"), exist_ok=True)
    ndocs = build_documents_jsonl()
    flagged = sum(1 for r in rows if r["flags"])
    report = (f"# 构建对账\n\n"
              f"- 源码 commit:{commit}\n- 镜像文件:{len(copied)}\n"
              f"- 主命令:{len(rows)}(带 flags:{flagged},归属未定:{len(unresolved)})\n"
              f"- shortcuts:{len(shortcuts)}\n"
              f"- 答案卡:{len(card_index)}(full:{card_full},"
              f"{card_full/len(card_index):.1%};partial:{len(card_index)-card_full})\n"
              f"- 文档索引:{ndocs} 篇\n\n"
              "## 归属未定(退回源码 grep,不影响存在性判断)\n"
              + "\n".join(f"- {u}" for u in unresolved) + "\n")
    open(os.path.join(REPO, "meta", "BUILD_REPORT.md"), "w", encoding="utf-8").write(report)

    mfp = os.path.join(REPO, "meta", "MANIFEST.json")
    try:
        mf = json.load(open(mfp))
    except (OSError, ValueError):
        mf = {}
    mf.update({"build_time": time.strftime("%FT%T+08:00"), "source_commit": commit,
               "layers": {"docs": "mirror", "graph": "extracted", "cards": "deterministic",
                          "notes": "generated+reviewed"},
               "commands": len(rows), "shortcuts": len(shortcuts), "pages": ndocs,
               "cards": len(card_index), "cards_full": card_full})
    json.dump(mf, open(mfp, "w"), ensure_ascii=False, indent=2)
    print(f"OK: 命令 {len(rows)}(flags {flagged}) · shortcuts {len(shortcuts)} · "
          f"cards {len(card_index)}(full {card_full/len(card_index):.1%}) · "
          f"未归属 {len(unresolved)} · 文档 {ndocs}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
