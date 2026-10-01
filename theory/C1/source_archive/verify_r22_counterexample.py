#!/usr/bin/env python3
"""Exact, single-example certificate for the R22 scope correction.

No graph search and no external packages are used.  Coefficients are F_2.
The DGA is the standard squarefree cellular/Koszul model of a
moment-angle complex.  A monomial is u_U v_V, with U and V disjoint,
v_V supported on a simplex.  Degrees: |u|=1, |v|=2; d(u)=v.

This certificate proves that one specified ORDINARY fourfold Massey
product contains zero.  It does NOT prove that the space is formal.
Run with Python 3.10 or later: python verify_r22_counterexample.py
"""
from __future__ import annotations
from itertools import combinations

Monomial = tuple[frozenset[int], frozenset[int]]
Cochain = frozenset[Monomial]
ZERO: Cochain = frozenset()
VERTICES = frozenset(range(8))
J = {i: frozenset((2 * (i - 1), 2 * (i - 1) + 1)) for i in range(1, 5)}
p = {i: 2 * (i - 1) for i in J}
q = {i: 2 * (i - 1) + 1 for i in J}
EDGES = frozenset(frozenset(e) for e in (
    (p[1], q[2]), (q[1], p[2]), (q[1], q[2]),
    (p[2], p[3]), (p[2], q[3]), (q[2], q[3]),
    (p[3], p[4]), (p[3], q[4]), (q[3], q[4]),
    (p[1], p[4]),
))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def is_face(v: frozenset[int]) -> bool:
    return len(v) <= 1 or (len(v) == 2 and v in EDGES)


def add(*cochains: Cochain) -> Cochain:
    terms: set[Monomial] = set()
    for cochain in cochains:
        terms.symmetric_difference_update(cochain)
    return frozenset(terms)


def mul(left: Cochain, right: Cochain) -> Cochain:
    terms: set[Monomial] = set()
    for u1, v1 in left:
        for u2, v2 in right:
            if (u1 | v1) & (u2 | v2):
                continue  # u_i^2 = u_i v_i = v_i^2 = 0.
            u, v = u1 | u2, v1 | v2
            if is_face(v):
                term = (u, v)
                if term in terms:
                    terms.remove(term)
                else:
                    terms.add(term)
    return frozenset(terms)


def differential(cochain: Cochain) -> Cochain:
    out = ZERO
    for u, v in cochain:
        for vertex in u:
            new_v = v | {vertex}
            if is_face(new_v):
                out = add(out, frozenset(((u - {vertex}, new_v),)))
    return out


def c(vertex: int, support: frozenset[int]) -> Cochain:
    require(vertex in support, "Characteristic vertex must belong to its support")
    return frozenset(((support - {vertex}, frozenset((vertex,))),))


def degree(cochain: Cochain, expected: int) -> bool:
    return all(len(u) + 2 * len(v) == expected for u, v in cochain)


def verify_proper(a: dict[int, Cochain], b: dict[str, Cochain]) -> None:
    equations = {
        "12": mul(a[1], a[2]),
        "23": mul(a[2], a[3]),
        "34": mul(a[3], a[4]),
        "123": add(mul(a[1], b["23"]), mul(b["12"], a[3])),
        "234": add(mul(a[2], b["34"]), mul(b["23"], a[4])),
    }
    for key, rhs in equations.items():
        require(differential(b[key]) == rhs, f"Defining equation {key} failed")
        require(degree(b[key], 2 * len(key) + 1), f"Wrong degree at {key}")


def top(a: dict[int, Cochain], b: dict[str, Cochain]) -> Cochain:
    return add(mul(a[1], b["234"]), mul(b["12"], b["34"]),
               mul(b["123"], a[4]))


def cycle_pairing(cochain: Cochain) -> int:
    cycle = (p[1], q[2], q[1], p[2], p[3], p[4], p[1])
    cycle_edges = {frozenset((x, y)) for x, y in zip(cycle, cycle[1:])}
    require(cycle_edges <= EDGES, "Invalid cycle")
    return sum(1 for u, v in cochain
               if u | v == VERTICES and v in cycle_edges) % 2


def main() -> None:
    require(len(EDGES) == 10, "Expected the stated ten-edge graph")
    require(not any(all(frozenset(e) in EDGES for e in combinations(t, 2))
                    for t in combinations(VERTICES, 3)), "Graph must be triangle-free")
    a = {i: c(p[i], J[i]) for i in J}
    for i in J:
        require(not differential(a[i]), "Input is not a cocycle")
        require(degree(a[i], 3), "Input has wrong degree")

    b = {
        "12": ZERO,
        "23": c(p[3], J[2] | J[3]),
        "34": c(p[4], J[3] | J[4]),
        "123": ZERO,
        "234": c(p[4], J[2] | J[3] | J[4]),
    }
    verify_proper(a, b)
    omega = top(a, b)
    expected = frozenset(((VERTICES - {p[1], p[4]},
                           frozenset((p[1], p[4]))),))
    require(omega == expected, "Original curvature is not the long-edge monomial")
    require(not differential(omega), "Original curvature is not closed")
    require(cycle_pairing(omega) == 1, "Missing nonzero restricted obstruction")
    for v in VERTICES:
        require(cycle_pairing(differential(c(v, VERTICES))) == 0,
                "Cycle must annihilate each full-support vertex coboundary")

    z = c(p[1], J[1] | J[3])
    t = c(p[4], J[2] | J[4])
    require(not differential(z) and not differential(t), "Corrections are not cycles")
    require(not mul(z, a[3]) and not mul(a[2], t), "Proper equations would change")
    require(not mul(z, b["34"]), "Expected overlap product to vanish")
    require(mul(z, t) == omega, "Cross-support product must cancel the curvature")

    modified = dict(b)
    modified["12"] = z
    modified["34"] = add(b["34"], t)
    verify_proper(a, modified)
    require(not top(a, modified), "Modified top curvature must be exactly zero")
    print("PASS: the five original proper defining equations hold.")
    print("PASS: the original full-support curvature pairs to 1 with a graph cycle.")
    print("PASS: noninterval degree-5 cocycles preserve all proper equations.")
    print("PASS: the modified top curvature is exactly zero over F_2.")
    print("Conclusion: 0 belongs to this ORDINARY fourfold Massey product.")
    print("No claim about formality of the whole space is made.")


if __name__ == "__main__":
    main()
