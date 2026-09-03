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
  graph/commands.jsonl: cmd/desc/when/defs[{file,line}]/flags[{name,short,type,required,hidden,help,line}]
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
            # 变量赋值点 → Use 叶名
            assigns = {}   # var -> [(pos, def_dict)]
            for m in ASSIGN.finditer(text):
                seg = text[m.end():m.end() + 500]
                um = USE.search(seg)
                if not um:
                    continue
                sm = re.search(r'Short:\s*"((?:[^"\\]|\\.)*)"', seg)
                line = text[:m.start()].count("\n") + 1
                d = {"file": rel(path, src), "line": line,
                     "use": um.group(1).split()[0],
                     "short_desc": (sm.group(1) if sm else ""), "flags": []}
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
                    out.setdefault(cp, rel(path, src))
    return out


# ---------- cobra 命令树:补 command-index 与 CLIPath 都没有的整族命令 ----------
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
                        lit = (um.group(1).split()[0], sm.group(1) if sm else "")
                        break
                if not lit:
                    continue
                kids = []
                for am in re.finditer(r'AddCommand\s*\(', body):
                    kids += _CALL_RE.findall(_scan_block(body, am.end() - 1, "(", ")"))
                nodes[m.group(1)] = {"use": lit[0], "short": lit[1], "kids": kids,
                                     "file": rel(path, src),
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
    """把 flag 定义挂到 command-index 的完整路径上:叶名匹配+父级/产品词消歧。"""
    by_leaf = {}
    for d in defs:
        by_leaf.setdefault(d["use"], []).append(d)
    out, unresolved = [], []
    for path, meta in sorted(cmds.items()):
        parts = path.split()
        leaf, product = parts[-1], parts[0]
        cand = by_leaf.get(leaf, [])
        scored = []
        for d in cand:
            score = 0
            f = d["file"].lower().replace("-", "").replace("_", "")
            if product.replace("-", "") in f:
                score += 2
            if len(parts) >= 2 and parts[-2].replace("-", "") in f:
                score += 1
            scored.append((score, d))
        scored.sort(key=lambda x: -x[0])
        best = [d for sc, d in scored if scored and sc == scored[0][0]]
        desc = meta["desc"] or (best[0].get("short_desc", "") if best else "")
        row = {"cmd": path, "product": product, "desc": desc, "when": meta["when"],
               "defs": [{"file": d["file"], "line": d["line"]} for d in best[:3]],
               "flags": (best[0]["flags"] if best else [])}
        if not best:
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
    for cp in extract_clipaths(src):
        if "+" in cp:      # shortcut 路径归 shortcuts.jsonl,不重复计
            continue
        if cp not in cmds:
            cmds[cp] = {"desc": "", "when": "(source-only: command-index 未收录,以源码为准)"}
    n_clipath = len(cmds) - n_index
    # cobra 树补漏:只填 index/CLIPath 都没有的路径,已有条目的 desc 一律不覆盖
    # (index 是上游文档,业务描述比源码 Short 权威)
    for cp, node in extract_cobra_tree(src).items():
        if cp not in cmds:
            cmds[cp] = {"desc": node["short"],
                        "when": "(source-only: 由 cobra 命令树推出,以源码为准)"}
    defs = extract_flags(src)
    rows, unresolved = attach(cmds, defs)
    print(f"命令: index {n_index} + CLIPath {n_clipath} + cobra 树 "
          f"{len(cmds)-n_index-n_clipath}")
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
