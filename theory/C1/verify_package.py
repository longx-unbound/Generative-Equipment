#!/usr/bin/env python3
"""Integrity and reference checks for the C1 consolidated theory package.

No mathematical proof checking is performed. Re-run from any directory:
    python verify_package.py
Optional output:
    python verify_package.py --output registry/integrity_results.json
"""
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, json, re, zipfile
from collections import Counter

ROOT=Path(__file__).resolve().parent

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def require(ok: bool, message: str) -> None:
    if not ok: raise AssertionError(message)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=str)
    args=parser.parse_args()
    sources=json.loads((ROOT/'registry/source_manifest.json').read_text())
    claims=json.loads((ROOT/'registry/claim_registry.json').read_text())
    bib=json.loads((ROOT/'registry/bibliography.json').read_text())
    sids={s['id'] for s in sources}; cids={c['id'] for c in claims}; bids={b['id'] for b in bib}
    require(len(sids)==len(sources),'Duplicate source IDs')
    require(len(cids)==len(claims),'Duplicate claim IDs')
    require(len(bids)==len(bib),'Duplicate bibliography IDs')
    for s in sources:
        f=ROOT/s['path']; require(f.is_file(),f'Missing source {s["id"]}')
        raw=f.read_bytes()
        require(len(raw)==s['bytes'],f'Source size changed: {s["id"]}')
        require(sha(raw)==s['sha256'],f'Source bytes changed: {s["id"]}')
    frozen_count=0
    with zipfile.ZipFile(ROOT/'evidence/Generative_Equipment_Frozen_v1_0_ORIGINAL.zip') as z:
        for entry in z.infolist():
            if entry.is_dir():continue
            p=ROOT/'frozen_original'/Path(entry.filename).name
            require(p.is_file(),f'Missing frozen archive member: {entry.filename}')
            require(z.read(entry)==p.read_bytes(),f'Frozen bytes changed: {p.name}')
            frozen_count+=1
    byid={c['id']:c for c in claims}
    allowed={'DEF','STD','DER','COND','REPORT','OPEN','RETRACT'}
    for c in claims:
        require(c['status'] in allowed,'Unknown status')
        require(c.get('proof_assistant_verified') is False,'Unsupported formal-proof flag')
        require(all(s in sids for s in c['sources']),f'Unknown source for {c["id"]}')
        require(all(d in cids for d in c['depends_on']),f'Unknown dependency for {c["id"]}')
        if c['status'] in {'STD','DER','COND'}:
            require(all(byid[d]['status'] not in {'RETRACT','REPORT','OPEN'} for d in c['depends_on']),
                    f'Unproved dependency promoted by {c["id"]}')
        match=re.match(r'^(.+?\.md)(?:\s|$)',c['proof_location'])
        require(match is not None,f'Invalid proof location for {c["id"]}')
        doc=match.group(1)
        require((ROOT/doc).is_file(),f'Missing proof document {doc}')
    seen=set(); active=set(); edges=0
    def visit(i):
        require(i not in active,f'Dependency cycle at {i}')
        if i in seen:return
        active.add(i)
        for d in byid[i]['depends_on']:visit(d)
        active.remove(i); seen.add(i)
    for c in claims:
        visit(c['id']); edges+=len(c['depends_on'])
    checked_links=0; checked_refs=0
    docs=sorted(ROOT.glob('[0-9][0-9]_*.md'))
    for doc in docs:
        t=doc.read_text(encoding='utf-8')
        # Check only [Snn] and [Bnn] style references, not source spelling.
        for block in re.findall(r'\[((?:S|B)\d{2}[^\]\n]*)\]',t):
            for ref in re.findall(r'\b[SB]\d{2}\b',block):
                require(ref in sids|bids,f'Unknown reference {ref} in {doc.name}')
                checked_refs+=1
        for link in re.findall(r'\]\(([^)]+)\)',t):
            if link.startswith(('https:','http:','#','mailto:')):continue
            loc=link.split('#')[0]
            require((doc.parent/loc).is_file(),f'Broken local link {loc} in {doc.name}')
            checked_links+=1
    result={
      'status':'PASS',
      'scope':'byte integrity, registry types/dependencies, reference/link existence; NOT mathematical proof checking',
      'source_units':len(sources),'frozen_members_byte_identical':frozen_count,
      'claim_records':len(claims),'claim_status_counts':dict(Counter(c['status'] for c in claims)),
      'dependency_edges':edges,'dependency_acyclic':True,
      'unsupported_formal_proof_flags':0,
      'bibliography_records':len(bib),'compiled_documents_checked':len(docs),
      'reference_occurrences_checked':checked_refs,'local_links_checked':checked_links,
      'unproved_dependencies_promoted':0,
    }
    if args.output:
        out=Path(args.output)
        if not out.is_absolute():out=ROOT/out
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
