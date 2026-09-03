#!/usr/bin/env python3
"""从 graph/ 确定性生成 dws 答案卡。

输入:
  graph/commands.jsonl   主命令树
  graph/shortcuts.jsonl  +shortcut
输出:
  cards/cmd/*.md         一命令一卡（主命令与 shortcut 共目录）
  cards/index.jsonl      精确 key → 卡片路径/完整度

生成规则只依赖 graph schema，不跟具体产品/命令名走；新增命令无需改代码。
卡片仅在 description、source 齐全且可见 flag <=14、无空 flag 名时标 full；
其余标 partial，由 dwsdoc ctx 自动回落产品正文，宁可慢也不丢字段。
"""
import argparse
import json
import os
import shutil
import sys
from urllib.parse import quote

VISIBLE_FLAG_LIMIT = 14
PARTIAL_FLAG_LIMIT = 8


def load_jsonl(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def card_name(kind, key):
    return f"{kind}--{quote(key, safe='-_.')}.md"


def clean(s):
    return " ".join(str(s or "").split())


def command_source(r):
    defs = r.get("defs") or []
    if not defs:
        return ""
    d = defs[0]
    return f"{d.get('file', '')}:{d.get('line', '')}".rstrip(":")


def shortcut_source(r):
    return f"{r.get('file', '')}:{r.get('line', '')}".rstrip(":")


def related_commands(row, commands):
    key = row["cmd"].strip()
    parts = key.split()
    if len(parts) >= 2:
        parent = parts[:-1]
        hits = [r["cmd"].strip() for r in commands
                if r["cmd"].strip() != key
                and r["cmd"].strip().split()[:-1] == parent]
    else:
        hits = [r["cmd"].strip() for r in commands
                if r["cmd"].strip() != key and r.get("product") == row.get("product")]
    return sorted(dict.fromkeys(hits))[:6]


def related_shortcuts(row, shortcuts):
    key = f"{row.get('product', '')} {row['cmd']}".strip()
    hits = [f"{r.get('product', '')} {r['cmd']}".strip() for r in shortcuts
            if r.get("product") == row.get("product")
            and f"{r.get('product', '')} {r['cmd']}".strip() != key]
    return sorted(dict.fromkeys(hits))[:6]


def render(kind, key, desc, when, source, flags, related):
    visible = [f for f in flags if not f.get("hidden") and f.get("name")]
    bad_flag = any(not f.get("name") for f in flags)
    full = bool(desc and source and len(visible) <= VISIBLE_FLAG_LIMIT and not bad_flag)
    completeness = "full" if full else "partial"
    shown = visible if full else ([f for f in visible if f.get("required")]
                                  + [f for f in visible if not f.get("required")][:PARTIAL_FLAG_LIMIT])
    # required 与普通列表拼接后去重
    uniq, seen = [], set()
    for f in shown:
        if f["name"] not in seen:
            seen.add(f["name"])
            uniq.append(f)

    lines = [f"# dws {key}", "", f"kind: {kind}", f"completeness: {completeness}",
             f"description: {clean(desc) or '—'}"]
    if when and not str(when).startswith("(source-only:"):
        lines.append(f"use_when: {clean(when)}")
    lines.append(f"source: {source or '—'}")
    lines.append(f"visible_flags: {len(visible)}")
    if not full:
        reasons = []
        if not desc:
            reasons.append("missing_description")
        if not source:
            reasons.append("missing_source")
        if len(visible) > VISIBLE_FLAG_LIMIT:
            reasons.append(f"too_many_flags:{len(visible)}")
        if bad_flag:
            reasons.append("empty_flag_name")
        lines.append("partial_reason: " + ",".join(reasons))
    lines += ["", "## Flags"]
    if uniq:
        for f in uniq:
            req = " required" if f.get("required") else ""
            short = f" (-{f['short']})" if f.get("short") else ""
            help_ = clean(f.get("help") or f.get("desc"))
            lines.append(f"- --{f['name']}{short} <{f.get('type') or 'value'}>{req}: {help_ or '—'}")
    else:
        lines.append("- none")
    if not full and len(visible) > len(uniq):
        lines.append(f"- … {len(visible) - len(uniq)} more; use dwsdoc cmd/short for full flags")
    lines += ["", "## Related"]
    lines += [f"- dws {x}" for x in related] or ["- none"]
    return "\n".join(lines) + "\n", completeness


def build(repo):
    commands = load_jsonl(os.path.join(repo, "graph", "commands.jsonl"))
    shortcuts = load_jsonl(os.path.join(repo, "graph", "shortcuts.jsonl"))
    if not commands or not shortcuts:
        raise RuntimeError(f"graph 输入为空: commands={len(commands)} shortcuts={len(shortcuts)}")

    cards_root = os.path.join(repo, "cards")
    target = os.path.join(cards_root, "cmd")
    tmp = os.path.join(cards_root, ".cmd-building")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp, exist_ok=True)
    index, full_count = [], 0

    for r in sorted(commands, key=lambda x: x["cmd"].strip()):
        key = r["cmd"].strip()
        fn = card_name("command", key)
        body, completeness = render("command", key, r.get("desc"), r.get("when"),
                                    command_source(r), r.get("flags") or [],
                                    related_commands(r, commands))
        with open(os.path.join(tmp, fn), "w", encoding="utf-8") as f:
            f.write(body)
        full_count += completeness == "full"
        index.append({"kind": "command", "key": key,
                      "path": f"cards/cmd/{fn}", "completeness": completeness,
                      "product": r.get("product") or key.split()[0]})

    for r in sorted(shortcuts, key=lambda x: (x.get("product", ""), x["cmd"])):
        key = f"{r.get('product', '')} {r['cmd']}".strip()
        fn = card_name("shortcut", key)
        body, completeness = render("shortcut", key, r.get("desc"), "",
                                    shortcut_source(r), r.get("flags") or [],
                                    related_shortcuts(r, shortcuts))
        with open(os.path.join(tmp, fn), "w", encoding="utf-8") as f:
            f.write(body)
        full_count += completeness == "full"
        index.append({"kind": "shortcut", "key": key,
                      "path": f"cards/cmd/{fn}", "completeness": completeness,
                      "product": r.get("product") or ""})

    # 构建成功后再替换，避免中途失败留下半套 cards。
    shutil.rmtree(target, ignore_errors=True)
    os.replace(tmp, target)
    os.makedirs(cards_root, exist_ok=True)
    with open(os.path.join(cards_root, "index.jsonl"), "w", encoding="utf-8") as f:
        for r in sorted(index, key=lambda x: (x["kind"], x["key"])):
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")

    files = [x for x in os.listdir(target) if x.endswith(".md")]
    if len(files) != len(index):
        raise RuntimeError(f"卡片数不符: files={len(files)} index={len(index)}")
    ratio = full_count / len(index)
    if len(index) < 900:
        raise RuntimeError(f"卡片地板未达标: {len(index)} < 900")
    if ratio < 0.70:
        raise RuntimeError(f"full 完整率未达标: {ratio:.1%} < 70%")
    return {"cards": len(index), "full": full_count, "partial": len(index) - full_count,
            "full_ratio": ratio, "commands": len(commands), "shortcuts": len(shortcuts)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    args = ap.parse_args()
    try:
        s = build(os.path.abspath(args.repo))
    except Exception as e:
        print(f"CARD BUILD FAIL: {type(e).__name__}: {e}")
        return 1
    print(f"OK: cards {s['cards']} = command {s['commands']} + shortcut {s['shortcuts']} · "
          f"full {s['full']}({s['full_ratio']:.1%}) · partial {s['partial']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
