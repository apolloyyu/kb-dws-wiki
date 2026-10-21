#!/usr/bin/env python3
"""notes 依据标记的解析、展开与核对(bin/dwsdoc 与 build_dws_kb.py 共用,python3 stdlib)。

notes 只写判断,原文与源码依据用标记引用,不在 note 里转述:
  {{quote: <docs/ 下路径> | <原文片段>}}   ctx 输出时替换为镜像原文中含该片段的整行(逐字)
  {{code: <源码路径> | <源码片段>}}        每日构建核对源码仍含该片段;ctx 只显示出处
  {{absent: <词> @ <glob> [!排除后缀]}}   每日构建核对源码中该词仍为 0 处(否定类结论的依据)
  {{confirmed: <谁 日期>}}                人工确认,无法自动核对,原样标注
依据失效时 ctx 在该处输出 ⚠ 警告,模型不得把该条当确定结论;构建只记录不失败。
"""
import fnmatch
import glob
import json
import os
import re

MARKER = re.compile(r"\{\{(quote|code|absent|confirmed):\s*([^{}\s][^{}]*?)\s*\}\}")
WARN = "⚠依据已变更({})，此条待复核，不得作为确定结论"
GH = "https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli/blob/main/"


def parse(body):
    """返回 [(kind, arg, span)]。"""
    return [(m.group(1), m.group(2), m.span()) for m in MARKER.finditer(body)]


def _split(arg):
    path, _, needle = arg.partition("|")
    return path.strip(), needle.strip()


def quote_line(root, arg):
    """在镜像文件中找含片段的整行;返回 (行文本, 行号, 文件 frontmatter) 或 None。"""
    path, needle = _split(arg)
    fp = os.path.join(root, path)
    if not needle or not os.path.isfile(fp):
        return None
    lines = open(fp, encoding="utf-8", errors="replace").read().splitlines()
    for i, line in enumerate(lines, 1):
        if needle in line:
            return line.strip(), i, _frontmatter(lines)
    return None


def _frontmatter(lines):
    meta = {}
    if lines and lines[0].strip() == "---":
        for line in lines[1:40]:
            if line.strip() == "---":
                break
            k, _, v = line.partition(":")
            meta[k.strip()] = v.split("#", 1)[0].strip().strip('"')
    return meta


def check_code(src, arg):
    path, needle = _split(arg)
    fp = os.path.join(src, path)
    if not os.path.isfile(fp):
        return False, f"源码文件已不存在: {path}", 0
    for i, line in enumerate(open(fp, encoding="utf-8", errors="replace"), 1):
        if needle in line:
            return True, "", i
    return False, f"{path} 已不含「{needle}」", 0


def check_absent(src, arg):
    term, _, spec = arg.partition("@")
    parts = spec.split()
    pattern = parts[0] if parts else ""
    excludes = [p[1:] for p in parts[1:] if p.startswith("!")]
    term = term.strip().lower()
    hits = []
    for fp in glob.glob(os.path.join(src, pattern), recursive=True):
        if not os.path.isfile(fp) or any(fp.endswith(e) for e in excludes):
            continue
        if term in open(fp, encoding="utf-8", errors="replace").read().lower():
            hits.append(os.path.relpath(fp, src))
    if not glob.glob(os.path.join(src, pattern), recursive=True):
        return False, f"源码中已无匹配 {pattern} 的文件", []
    return (not hits), (f"源码已出现「{term}」: {', '.join(hits[:3])}" if hits else ""), hits


def check_all(root, src):
    """核对全部 notes 的标记;返回行列表(写 meta/notes-check.jsonl)。"""
    rows = []
    nd = os.path.join(root, "notes")
    for fn in sorted(os.listdir(nd)) if os.path.isdir(nd) else []:
        if not fn.endswith(".md"):
            continue
        body = open(os.path.join(nd, fn), encoding="utf-8", errors="replace").read()
        for kind, arg, _ in parse(body):
            row = {"note": fn, "kind": kind, "arg": arg, "ok": True, "detail": "", "line": 0}
            if kind == "quote":
                hit = quote_line(root, arg)
                if hit:
                    row["line"] = hit[1]
                else:
                    row.update(ok=False, detail=f"镜像原文已不含该片段: {arg}")
            elif kind == "code":
                ok, detail, line = check_code(src, arg)
                row.update(ok=ok, detail=detail, line=line)
            elif kind == "absent":
                ok, detail, _ = check_absent(src, arg)
                row.update(ok=ok, detail=detail)
            rows.append(row)
    return rows


def load_check(root):
    p = os.path.join(root, "meta", "notes-check.jsonl")
    if not os.path.exists(p):
        return {}
    out = {}
    for line in open(p, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            out[(r["note"], r["kind"], r["arg"])] = r
    return out


def expand(root, fn, body, checks=None):
    """ctx 输出前展开标记:quote 现场取镜像原文,code/absent 读构建核对结果。"""
    checks = checks if checks is not None else load_check(root)
    # 构建核对的行号属于 MANIFEST 固定源码，不能给会随主干漂移的链接。
    source_prefix = GH
    try:
        with open(os.path.join(root, "meta", "MANIFEST.json"), encoding="utf-8") as handle:
            commit = json.load(handle).get("source_commit", "")
        if re.fullmatch(r"[0-9a-f]{7,40}", commit):
            source_prefix = GH.replace("/blob/main/", f"/blob/{commit}/")
    except (OSError, ValueError):
        pass

    def sub(m):
        kind, arg = m.group(1), m.group(2).strip()
        if kind == "quote":
            hit = quote_line(root, arg)
            if not hit:
                return WARN.format(f"引用原文已不存在: {_split(arg)[0]}")
            line, no, meta = hit
            src = meta.get("source_url")
            if not src and meta.get("source_path"):
                # Mirrored product docs carry a repository-relative source_path,
                # not a public URL. Use their own fixed commit and omit line
                # numbers because mirror frontmatter shifts local lines.
                commit = meta.get("source_commit", "")
                prefix = GH.replace("/blob/main/", f"/blob/{commit}/") if re.fullmatch(r"[0-9a-f]{7,40}", commit) else source_prefix
                src = prefix + meta["source_path"].lstrip("/")
            src = src or _split(arg)[0]
            when = f" · {meta['updated_at'][:10]}" if meta.get("updated_at") else ""
            return f"> 原文({src}{when}): {line}"
        if kind == "confirmed":
            return f"(人工确认: {arg};源码与文档中无此信息)"
        r = checks.get((fn, kind, arg))
        if r and not r["ok"]:
            return WARN.format(r["detail"])
        if kind == "code":
            # 给可点的上游深链而不是裸「路径:行号」:后者会被模型原样当出处写进回复
            path, needle = _split(arg)
            at = f"#L{r['line']}" if r and r.get("line") else ""
            return f"(源码依据: {source_prefix}{path}{at})"
        term, _, spec = arg.partition("@")
        return f"(源码核对: {spec.split()[0] if spec.split() else spec} 中无「{term.strip()}」)"

    return MARKER.sub(sub, body)


def contract_lines(body):
    """frontmatter 里 contract: 下的 `  - xxx` 行(证据契约要点,事实只存在 note 里)。"""
    m = re.match(r"---\n(.*?)\n---", body, re.S)
    if not m:
        return []
    out, on = [], False
    for line in m.group(1).splitlines():
        if re.match(r"contract:\s*$", line):
            on = True
        elif on and re.match(r"\s+-\s+", line):
            out.append(re.sub(r"^\s+-\s+", "", line))
        elif on:
            break
    return out


def declared_intents(body):
    m = re.search(r"(?m)^intents:(.*)$", body[:800])
    return [x.strip() for x in m.group(1).split(",")] if m else []


def triggers(body):
    m = re.search(r"(?m)^triggers:(.*)$", body[:800])
    return [x.strip().lower() for x in m.group(1).split(",") if x.strip()] if m else []


def is_manual(body):
    return bool(re.search(r"(?m)^maintenance:\s*manual\s*$", body[:800]))


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("用法: notes_refs.py <wiki 根> <dws 源码根>   # 核对并打印失效依据")
        sys.exit(2)
    bad = [r for r in check_all(sys.argv[1], sys.argv[2]) if not r["ok"]]
    for r in bad:
        print(f"FAIL {r['note']} {r['kind']}: {r['detail']}")
    print(f"notes 依据核对: 失效 {len(bad)} 处")
    sys.exit(1 if bad else 0)
