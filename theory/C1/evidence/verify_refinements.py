#!/usr/bin/env python3
"""Exact regression for the C1 DGLA and elementary closure refinements.

This verifies stated finite algebraic identities. It does not prove the
categorical results, classification claims, or priority of any theorem.
Python standard library only; deterministic; no network access.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

BASIS = ('v1','v2','v3','v4','e12','e34','p12','p34','w')
DEG = (1,1,1,1,1,1,2,2,2)
N = len(BASIS)
def vec(i: int) -> tuple[Fraction,...]:
    return tuple(Fraction(int(j == i)) for j in range(N))
ZERO = (Fraction(0),)*N

def add(a,b,scale=1):
    return tuple(x+scale*y for x,y in zip(a,b))

def diff(a):
    out=list(ZERO)
    out[6]=a[4]
    out[7]=a[5]
    return tuple(out)

def br(a,b):
    out=list(ZERO)
    out[6]=-(a[0]*b[1]+a[1]*b[0])
    out[7]=-(a[2]*b[3]+a[3]*b[2])
    out[8]=(a[4]*b[5]+a[5]*b[4])
    return tuple(out)

def sign(n): return -1 if n%2 else 1

def poly_add(a,b,scale=1):
    out=dict(a)
    for mon,c in b.items():
        out[mon]=out.get(mon,0)+scale*c
        if out[mon]==0: del out[mon]
    return out

def monomial(indices):
    out=[0]*6
    for i in indices: out[i]+=1
    return tuple(out)

def multiply_squarefree_masks(masks):
    u=0
    for s in masks:
        if u&s: return None
        u|=s
    return u

def main():
    counts={}
    for i in range(N):
        assert diff(diff(vec(i)))==ZERO
    counts['d_squared_basis']=N
    for i,j in product(range(N),repeat=2):
        x,y=vec(i),vec(j)
        assert br(x,y)==tuple(-sign(DEG[i]*DEG[j])*v for v in br(y,x))
        assert diff(br(x,y))==add(br(diff(x),y),br(x,diff(y)),sign(DEG[i]))
    counts['graded_skew_basis_pairs']=N*N
    counts['differential_derivation_basis_pairs']=N*N
    for i,j,k in product(range(N),repeat=3):
        x,y,z=vec(i),vec(j),vec(k)
        lhs=tuple(sign(DEG[i]*DEG[k])*v for v in br(x,br(y,z)))
        lhs=add(lhs,br(y,br(z,x)),sign(DEG[j]*DEG[i]))
        lhs=add(lhs,br(z,br(x,y)),sign(DEG[k]*DEG[j]))
        assert lhs==ZERO
    counts['graded_Jacobi_basis_triples']=N**3

    # Derive each coefficient of d(x)+1/2[x,x] as a sparse polynomial,
    # independently using the linear differential and the bracket function.
    coeff=[{} for _ in range(N)]
    for i in range(6):
        for k,c in enumerate(diff(vec(i))):
            if c: coeff[k]=poly_add(coeff[k],{monomial([i]):c})
    for i,j in product(range(6),repeat=2):
        for k,c in enumerate(br(vec(i),vec(j))):
            if c: coeff[k]=poly_add(coeff[k],{monomial([i,j]):Fraction(c,2)})
    expected=[{} for _ in range(N)]
    expected[6]={monomial([4]):Fraction(1),monomial([0,1]):Fraction(-1)}
    expected[7]={monomial([5]):Fraction(1),monomial([2,3]):Fraction(-1)}
    expected[8]={monomial([4,5]):Fraction(1)}
    assert coeff==expected
    counts['MC_polynomial_coefficient_identities']=N

    # Verify all support patterns in the product
    # (eps_1+higher)*(eps_2+higher)*(eps_3+higher)*(eps_4+higher).
    # Each factor has 1 singleton option plus 11 support>=2 options.
    # Thus arbitrary coefficients on all higher supports cannot change
    # the top coefficient: all perturbation monomials vanish separately.
    higher=[m for m in range(1,16) if m.bit_count()>=2]
    options=[[(1<<i)]+higher for i in range(4)]
    total=0
    for masks in product(*options):
        value=multiply_squarefree_masks(masks)
        baseline=all(masks[i]==1<<i for i in range(4))
        assert value==15 if baseline else value is None
        total+=1
    counts['all_squarefree_support_patterns']=total

    # Exhaust all inflationary monotone endomaps of the 2-generator
    # Boolean lattice, then verify their finite fixed-point closures.
    elems=range(4)
    le=lambda a,b: (a&b)==a
    choices=[[b for b in elems if le(a,b)] for a in elems]
    nT=0; closurechecks=0
    for T in product(*choices):
        if not all(not le(a,b) or le(T[a],T[b]) for a,b in product(elems,repeat=2)):
            continue
        nT+=1; cl=[]
        for x in elems:
            y=x
            for _ in range(5):
                if T[y]==y: break
                y=T[y]
            else: raise AssertionError('finite increasing chain did not stabilize')
            assert le(x,y) and T[y]==y
            assert all(not (le(x,z) and T[z]==z) or le(y,z) for z in elems)
            cl.append(y)
        for x in elems:
            assert cl[cl[x]]==cl[x]
            closurechecks+=1
        assert all(not le(x,y) or le(cl[x],cl[y]) for x,y in product(elems,repeat=2))
    counts['all_monotone_inflationary_B2_maps']=nT
    counts['closure_idempotence_checks']=closurechecks
    result={'status':'PASS','arithmetic':'exact rational/integer; standard library',
            'tests':counts,
            'not_verified':['512000 ordinary Massey classification','all historical regression counts',
                            'DHH proof chain','SNT literature originality','formal proof-assistant verification']}
    path=Path(__file__).with_name('refinement_results.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
