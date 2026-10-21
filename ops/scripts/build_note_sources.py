#!/usr/bin/env python3
"""Mirror complete Go declarations enclosing existing code-reference anchors.

Build requires the local Go standard-library parser. Runtime retrieval is pure
Python. Ambiguous/outside-function anchors retain their original source links.
"""
import hashlib,json,os,pathlib,re,subprocess,sys

def parse_sources(sources):
    env={**os.environ,'GO111MODULE':'off','GOWORK':'off','GOTOOLCHAIN':'local','GOPROXY':'off'}
    tool=pathlib.Path(__file__).with_name('extract_go_functions.go')
    p=subprocess.run(['go','run',str(tool)],input=json.dumps(sources),capture_output=True,text=True,env=env,timeout=180)
    if p.returncode:raise RuntimeError('Go source parser failed: '+p.stderr[-1000:])
    return json.loads(p.stdout)

def functions(text):
    # Unit-test helper; production build batches all source files in one call.
    return parse_sources({'source.go':text})['source.go'].get('functions') or []

def build(repo,source,commit):
    repo,source=pathlib.Path(repo),pathlib.Path(source)
    if not re.fullmatch('[0-9a-f]{40}',commit):raise ValueError('fixed full source commit required')
    anchors=[];seen=set();cache={};rows=[];missing=[]
    for note in sorted((repo/'notes').glob('*.md')):
        for path,needle in re.findall(r'\{\{code:\s*([^|{}]+)\|([^{}]+)\}\}',note.read_text()):
            path,needle=path.strip(),needle.strip();key=(path,needle)
            if key in seen:continue
            seen.add(key);fp=source/path
            if not fp.is_file():missing.append([path,needle,'missing_file']);continue
            anchors.append(key)
            if path not in cache:cache[path]=fp.read_text()
    parsed=parse_sources(cache)
    for path,needle in anchors:
        text=cache[path];hits=[i for i,line in enumerate(text.splitlines(),1) if needle in line]
        choices=[f for f in (parsed[path].get('functions') or []) if len(hits)==1 and f['line']<=hits[0]<=f['end_line'] and needle in f['source']]
        if len(choices)!=1:missing.append([path,needle,'parse_error'if parsed[path].get('error')else'ambiguous_or_outside_function']);continue
        f=choices[0]
        rows.append({'path':path,'needle':needle,'source_commit':commit,
            'source_sha256':hashlib.sha256((source/path).read_bytes()).hexdigest(),**f,
            'coverage':'literal enclosing function only; callers and callees not expanded'})
    target=repo/'graph/note-sources.json'
    target.write_text(json.dumps({'source_commit':commit,'parser':'Go standard-library go/parser; build time only','entries':rows,'not_expanded':missing},ensure_ascii=False,indent=2)+'\n')
    return {'anchors':len(rows),'unexpanded':len(missing),'functions':len({(r['path'],r['line'])for r in rows})}
if __name__=='__main__':print(json.dumps(build(*sys.argv[1:4])))
