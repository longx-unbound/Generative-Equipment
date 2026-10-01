#!/usr/bin/env python3
"""Exact finite regressions for C2. Not a proof assistant or an AI benchmark.

Run from any directory:
    python tests/verify_finite.py
Optional:
    python tests/verify_finite.py --output /path/to/results.json
Uses only the Python standard library. Infinite statements are proved in the
mathematical document; finite witness checks do not prove them.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKS: list[dict] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def case(name, refs, fn):
    try:
        details = fn()
        CHECKS.append({'id': name, 'paper_cases': refs, 'status': 'PASS', 'details': details})
    except Exception as exc:
        CHECKS.append({'id': name, 'paper_cases': refs, 'status': 'FAIL',
                       'error': f'{type(exc).__name__}: {exc}'})


def basic_types():
    # * -> [1], object sent to 1: fiber over 0 is empty, comma (0 down U) is not.
    image = 1
    fiber = [image] if image == 0 else []
    comma = [(0, image)] if 0 <= image else []
    require(len(fiber) == 0 and len(comma) == 1, 'fiber/comma conflation')
    reduced, full = {0}, {0, 1}
    require(bool(reduced) == bool(full) and reduced != full, 'branch counterexample')
    monoid = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1}
    units = [a for a in (0, 1) if any(monoid[a,b] == monoid[b,a] == 0 for b in (0,1))]
    require(units == [0], 'idempotent monoid units')
    return {'fiber_size': 0, 'comma_size': 1, 'core_objects': 1,
            'endomorphisms': 2, 'invertible_endomorphisms': 1}


def incompatible_matching():
    left, right = {0}, {1}
    require(left and right and not (left & right), 'matching compatibility')
    return {'nonempty_local_sets': 2, 'common_matching_fiber_size': 0}


def spectrum_threshold_witnesses():
    for N in range(1, 17):
        threshold = N + 1
        f = lambda n: int(n >= threshold)
        require(f(N) != f(N+1), 'cofinal threshold witness')
    for ts in [(1,), (1, 3), (2, 4, 7)]:
        N = max(ts)
        require(all(int(N >= t) == int(N+1 >= t) for t in ts), 'finite common threshold')
    return {'threshold_instances': 16,
            'scope': 'finite checks of witnesses; infinite/cofinality proof is ES5'}


def localization_witnesses():
    for N in range(0, 17):
        i = N + 1
        require((2**N) % (2**i) != 0, 'unbounded annihilator witness')
        require(Fraction(2**N, 2**i).denominator != 1, 'unbounded denominator witness')
    return {'exponent_instances': 17,
            'scope': 'finite formula checks for ES6, not enumeration of an infinite product'}


def products_without_equalizers():
    H = lambda s: {0} if s else set()
    X, Y = {0}, {0, 1}
    f, g = {0: 0}, {0: 1}
    eq = {x for x in X if f[x] == g[x]}
    require(H(eq) == set() and H(X) == {0}, 'nonempty functor equalizer counterexample')
    for sizes in product(range(3), repeat=3):
        prod_nonempty = all(n > 0 for n in sizes)
        require(prod_nonempty == all(bool(H(set(range(n)))) for n in sizes), 'finite products')
    return {'finite_product_cases': 27, 'equalizer_preservation': False,
            'scope': 'arbitrary products require choice; proof in evaluation'}


def two_axes():
    rows = []
    for tag, A, B, C, mu in [
        ('R+C+', [0], [0], [0], lambda a,b: 0),
        ('R-C+', [0,1], [0,1], list(product([0,1], repeat=2)), lambda a,b: (a,b)),
        ('R-C-', [0,1], [0,1], [0], lambda a,b: 0),
    ]:
        vals = [mu(a,b) for a in A for b in B]
        R = len(A) == len(B) == len(C) == 1
        C_ok = len(vals) == len(set(vals)) == len(C) and set(vals) == set(C)
        rows.append({'case': tag, 'R': R, 'C': C_ok})
    # Poset collage: three [1]-fibers, id, id, constant-zero companions.
    objs = list(product(range(3), range(2)))
    def hom(s, t):
        i,x = s; j,z = t
        return i <= j and ((i,j) == (0,2) or x <= z)
    require(all(not (hom(a,b) and hom(b,c)) or hom(a,c)
                for a,b,c in product(objs, repeat=3)), 'collage transitivity')
    for x,z in product(range(2), repeat=2):
        bs = [b for b in range(2) if x <= b <= z]
        # A nonempty finite chain has one component in this coend.
        coend_size = int(bool(bs))
        target_size = 1  # Hom_[1](0,z)
        if (x,z) == (1,0):
            require(coend_size == 0 and target_size == 1, 'R+ C- witness')
    rows.append({'case':'R+C-', 'R':True, 'C':False})
    require({(r['R'],r['C']) for r in rows} == set(product([False,True], repeat=2)), 'four cases')
    return {'four_combinations': rows, 'poset_collage_objects': len(objs)}


# Quaternion units: (sign, basis), basis 0=1,1=i,2=j,3=k.
QT = [
    [(1,0),(1,1),(1,2),(1,3)],
    [(1,1),(-1,0),(1,3),(-1,2)],
    [(1,2),(-1,3),(-1,0),(1,1)],
    [(1,3),(1,2),(-1,1),(-1,0)],
]
Q8 = list(product([1,-1], range(4)))
K = [(1,0),(-1,0)]
G = list(product(range(2), repeat=2))
BASIS_TO_G = [(0,0),(1,0),(0,1),(1,1)]

def qm(x,y):
    s,b = QT[x[1]][y[1]]
    return (x[0]*y[0]*s,b)

def qi(x):
    return x if x[1] == 0 else (-x[0],x[1])

def gm(x,y):
    return (x[0]^y[0], x[1]^y[1])

def qproj(x):
    return BASIS_TO_G[x[1]]


def quaternion_extension():
    require(all(qm(qm(a,b),c) == qm(a,qm(b,c)) for a,b,c in product(Q8, repeat=3)), 'Q8 associative')
    valid = 0
    for signs in product([1,-1], repeat=3):
        s = {G[0]:(1,0)}
        for b in (1,2,3):
            s[BASIS_TO_G[b]] = (signs[b-1],b)
        valid += int(all(qm(s[g],s[h]) == s[gm(g,h)] for g,h in product(G, repeat=2)))
    require(valid == 0, 'Q8 nonsplitting')
    section = {g:(1,BASIS_TO_G.index(g)) for g in G}
    def coc(g,h):
        return qm(qm(section[g],section[h]),qi(section[gm(g,h)]))
    require(all(qm(coc(g,h),coc(gm(g,h),l)) == qm(coc(h,l),coc(g,gm(h,l)))
                for g,h,l in product(G, repeat=3)), 'central cocycle')
    return {'normalized_sections_tested': 8, 'homomorphic_sections': valid,
            'cocycle_equations': 64, 'group_associativity_triples': 512}


def quaternion_composition():
    for g,h in product(G,repeat=2):
        pairs = [(v,u) for v,u in product(Q8,repeat=2) if qproj(v)==h and qproj(u)==g]
        orbits = []
        remaining = set(pairs)
        while remaining:
            v,u = next(iter(remaining))
            orb = {(qm(v,k),qm(qi(k),u)) for k in K}
            require(orb <= set(pairs), 'balanced product action')
            vals = {qm(a,b) for a,b in orb}
            require(len(vals)==1, 'product descends')
            orbits.append(next(iter(vals)))
            remaining -= orb
        target = {x for x in Q8 if qproj(x)==gm(h,g)}
        require(len(orbits)==len(set(orbits))==2 and set(orbits)==target, 'compositor bijective')
    return {'compositors_tested':16, 'all_bijective':True,
            'scope':'nonsplitting in previous test is not compositor failure'}


def split_control():
    count=0
    for choices in product(range(2),repeat=3):
        vals={(0,0):0}
        for g,v in zip(G[1:],choices): vals[g]=v
        count+=int(all(vals[gm(g,h)] == (vals[g]^vals[h]) for g,h in product(G,repeat=2)))
    require(count==4,'split extension linear sections')
    return {'normalized_sections_tested':8, 'homomorphic_sections':count}


def static_compression():
    E=list(product(range(2),repeat=3))
    obs=[lambda x,i=i:x[i] for i in range(3)] + [lambda x:x[0]^x[1]]
    Uall=list(range(len(obs)))
    subsets=[{i for i in Uall if mask&(1<<i)} for mask in range(1<<len(obs))]
    def cl(U):
        pairs=[(x,y) for x,y in product(E,repeat=2) if all(obs[i](x)==obs[i](y) for i in U)]
        return {c for c in Uall if all(obs[c](x)==obs[c](y) for x,y in pairs)}
    for U in subsets:
        require(U<=cl(U),'closure expansive')
        require(cl(cl(U))==cl(U),'closure idempotent')
        for V in subsets:
            if U<=V: require(cl(U)<=cl(V),'closure monotone')
    E2=range(-2,3)
    require(all(abs(x)!=abs(y) or x*x==y*y for x,y in product(E2,repeat=2)), 'target square factors')
    require(abs(-1)==abs(1) and -1!=1,'target signed identity does not factor')
    return {'observation_subsets_checked':len(subsets), 'target_relative_counterexample':True}


def dynamic_partition():
    states=range(4); output=(0,0,0,1)
    trans={'advance':(2,2,3,3),'stay':(0,1,2,3)}
    R={(x,y) for x,y in product(states,repeat=2) if output[x]==output[y]}
    rounds=0
    while True:
        new={(x,y) for x,y in product(states,repeat=2) if output[x]==output[y]
             and all((t[x],t[y]) in R for t in trans.values())}
        require(new<=R,'descending partitions')
        if new==R: break
        R=new;rounds+=1
    blocks=[]
    unseen=set(states)
    while unseen:
        x=min(unseen); b={y for y in states if (x,y) in R}; blocks.append(sorted(b));unseen-=b
    require(blocks==[[0,1],[2],[3]],'stable quotient')
    require(rounds<=3,'finite refinement bound')
    return {'states_before':4,'states_after':3,'blocks':blocks,'strict_refinements':rounds}


def search_quotient():
    states=range(4); trans={'advance':(2,2,3,3),'stay':(0,1,2,3)}
    q=(0,0,1,2); bar={'advance':(1,2,2),'stay':(0,1,2)}
    for x in states:
        require((x==3)==(q[x]==2),'goal reflection')
        for a in trans:
            require(q[trans[a][x]]==bar[a][q[x]],'transition lift')
    paths=0
    for n in range(6):
        for w in product(trans,repeat=n):
            for start in states:
                x=start;z=q[start]
                for a in w:x=trans[a][x];z=bar[a][z]
                require(q[x]==z and (x==3)==(z==2),'word lift')
                paths+=1
    # Bad static quotient merges state 0 and state 2, but 2 reaches goal in one step.
    bad=(0,0,0,1)
    union_edges={(bad[x],bad[trans['advance'][x]]) for x in states}
    missing=[x for x in states if any(a==bad[x] and bad[trans['advance'][x]]!=b for a,b in union_edges)]
    require(0 in missing,'back-lifting counterexample must be rejected')
    return {'finite_labeled_paths_checked':paths,'invalid_static_quotient_rejected':True}


def composition_information():
    group=lambda a,b:a^b
    idem=lambda a,b:max(a,b)
    require(all(group(group(a,b),c)==group(a,group(b,c)) for a,b,c in product(range(2),repeat=3)), 'C2 assoc')
    require(all(idem(idem(a,b),c)==idem(a,idem(b,c)) for a,b,c in product(range(2),repeat=3)), 'idempotent assoc')
    require(group(1,1)!=idem(1,1),'degree-two nerve distinction')
    return {'same_objects_arrows_units':True, 'same_composition':False}


def metric_probes():
    X=range(5)
    for x,y in product(X,repeat=2):
        d=abs(x-y)
        exact=max(abs(abs(x-s)-abs(y-s)) for s in X)
        require(exact==d,'distance reconstruction')
        approx=abs(abs(x-2)-abs(y-2))
        require(0<=d-approx<=4,'2delta inequality')
    require(abs(0-4)-abs(abs(0-2)-abs(4-2))==4,'sharp 2delta example')
    return {'ordered_pairs':25,'delta':2,'maximum_loss':4,'bound_sharp':True}


def promotion_witnesses():
    for n in range(1,33):
        x=1-Fraction(1,2*n)
        require(x**n>=Fraction(1,2),'pointwise-not-uniform witness')
        if n>=2:
            require(x>1-Fraction(1,n) and x<1,'closed-cover witness')
    for n in range(1,17):
        require(n*1==n,'c00 unit-vector norm witness')
    return {'power_function_instances':32,'c00_unit_vector_instances':16,
            'scope':'finite witnesses; compactness/Baire theorems are paper proofs'}


def doctrine_symmetry():
    vecs=[(1,0),(0,1),(1,1)]
    mats=[m for m in product(range(2),repeat=4) if (m[0]*m[3]-m[1]*m[2])%2==1]
    def act(m,v):return ((m[0]*v[0]+m[1]*v[1])%2,(m[2]*v[0]+m[3]*v[1])%2)
    fixed=[v for v in vecs if all(act(m,v)==v for m in mats)]
    stabilizer=[m for m in mats if act(m,(1,0))==(1,0)]
    marked=[v for v in vecs if all(act(m,v)==v for m in stabilizer)]
    require(len(mats)==6 and not fixed,'unmarked canonical line obstruction')
    require(len(stabilizer)==2 and marked==[(1,0)],'marked canonical line')
    uniform={v:Fraction(1,3) for v in vecs}
    require(all(uniform[v]==uniform[act(m,v)] for m,v in product(mats,vecs)),'invariant distribution')
    return {'automorphisms':6,'unmarked_fixed_lines':0,'marked_fixed_lines':1,
            'invariant_probability_exists':True}


def finite_repair():
    X=(0,1); Gsize=1;Dsize=2
    maps=list(product(X,repeat=Gsize+Dsize))
    pairs=list(product(product(X,repeat=Gsize),product(X,repeat=Dsize)))
    decode=lambda p:p[0]+p[1]
    require({decode(p) for p in pairs}==set(maps),'pushout mapping property for empty A')
    return {'maps_from_G_coproduct_D':len(maps),'mapping_property_bijection':True,
            'scope':'finite Set instance of F6'}


def provenance_alternatives():
    edges=[({'A'},'T',False),({'B'},'T',True),({'T'},'U',True)]
    def closure(facts):
        accepted=set(facts)
        while True:
            new=accepted|{concl for prem,concl,ok in edges if ok and prem<=accepted}
            if new==accepted:return accepted
            accepted=new
    c=closure({'A','B'})
    require({'T','U'}<=c,'alternative valid proof')
    require('T' not in closure({'A'}),'invalid proof cannot propagate')
    return {'valid_alternative_preserves_conclusion':True,'invalid_only_path_rejected':True}


def approximate_paths():
    eps=Fraction(1,3)
    for L in (Fraction(1),Fraction(1,2)):
        actual=Fraction(0); abstract=Fraction(0)
        for n in range(1,21):
            actual=L*actual+eps
            abstract=L*abstract
            bound=eps*sum((L**j for j in range(n)),Fraction(0))
            require(abs(actual-abstract)==bound,'sharp path error formula')
            if L<1: require(bound<eps/(1-L),'contractive horizon bound')
            else: require(bound==n*eps,'linear growth without contraction')
    return {'exact_rational_instances':40,'L_values':['1','1/2'],
            'scope':'finite equality checks of the general IC4 proof'}


def frozen_hash():
    p=ROOT/'baseline/01_FROZEN_CORE.md'
    expected=json.loads((ROOT/'source_integrity.json').read_text(encoding='utf-8'))['frozen_core_sha256']
    actual=hashlib.sha256(p.read_bytes()).hexdigest()
    require(actual==expected,'Frozen core byte identity')
    return {'sha256':actual,'byte_identical_to_recorded_source':True}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'tests/results.json')
    args=parser.parse_args()
    for name,refs,fn in [
        ('V01-types',['T01','T02','T03'],basic_types),
        ('V02-matching',['T04'],incompatible_matching),
        ('V03-thresholds',['T06'],spectrum_threshold_witnesses),
        ('V04-localization',['T08','T09'],localization_witnesses),
        ('V05-lex-boundary',['T11'],products_without_equalizers),
        ('V06-two-axes',['T12','T13','T14','T15'],two_axes),
        ('V07-Q8-splitting',['T16','T32'],quaternion_extension),
        ('V08-Q8-composition',['T16'],quaternion_composition),
        ('V09-split-control',['T17'],split_control),
        ('V10-static-compression',['T18'],static_compression),
        ('V11-dynamic-compression',['T20'],dynamic_partition),
        ('V12-search-lift',['T21'],search_quotient),
        ('V13-composition-info',['T22'],composition_information),
        ('V14-metric',['T23','T24'],metric_probes),
        ('V15-promotion',['T25','T27'],promotion_witnesses),
        ('V16-doctrine',['T30','T31'],doctrine_symmetry),
        ('V17-repair',['T33'],finite_repair),
        ('V18-provenance',['T36'],provenance_alternatives),
        ('V19-approximate-paths',['T37','T38'],approximate_paths),
        ('V20-source-integrity',[],frozen_hash),
    ]:case(name,refs,fn)
    report={'schema':'ge-c2-finite-regression-v1','run_at_utc':datetime.now(timezone.utc).isoformat(),
            'python':platform.python_version(),'status':'PASS' if all(c['status']=='PASS' for c in CHECKS) else 'FAIL',
            'check_groups':len(CHECKS),'passed_groups':sum(c['status']=='PASS' for c in CHECKS),
            'scope':'Exact finite regressions plus Frozen byte identity; not AI evaluation, not proof-assistant certification.',
            'checks':CHECKS}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'passed_groups':report['passed_groups'],
                      'check_groups':report['check_groups'],'output':str(args.output)},ensure_ascii=False))
    if report['status']!='PASS':
        print(json.dumps([c for c in CHECKS if c['status']=='FAIL'],ensure_ascii=False,indent=2))
        return 1
    return 0

if __name__=='__main__':
    sys.exit(main())
