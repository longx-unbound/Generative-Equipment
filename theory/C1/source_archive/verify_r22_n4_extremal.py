#!/usr/bin/env python3
"""Exhaustive verification for the R22 fourfold extremal theorem.

The coefficient field is F_2.  The eight vertices are (i,b), where
i in {1,2,3,4} is the support block and b in {0,1}.  The ambient graph
is the one-skeleton of (S^0)^{*4}: every edge between distinct blocks
is allowed and no edge within a block is allowed.

We enumerate every 9- and 10-edge graph whose three adjacent corridors
G_{12}, G_{23}, G_{34} are connected, solve the R18 graph Maurer--Cartan
equations by root-normalized path integration, and test the top curvature.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from itertools import combinations, product


Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]
Co0 = dict[Vertex, int]
Co1 = dict[Edge, int]

BLOCKS = {i: {(i, 0), (i, 1)} for i in range(1, 5)}
VERTICES = set().union(*BLOCKS.values())


def edge(u: Vertex, v: Vertex) -> Edge:
    return tuple(sorted((u, v)))  # type: ignore[return-value]


AMBIENT = {
    edge((i, a), (j, b))
    for i, j in combinations(range(1, 5), 2)
    for a, b in product((0, 1), repeat=2)
}


def induced(edges: set[Edge], indices: tuple[int, ...]) -> tuple[set[Edge], set[Vertex]]:
    vertices = set().union(*(BLOCKS[i] for i in indices))
    return {e for e in edges if set(e) <= vertices}, vertices


def connected(edges: set[Edge], vertices: set[Vertex]) -> bool:
    root = min(vertices)
    seen = {root}
    adjacency: dict[Vertex, list[Vertex]] = defaultdict(list)
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return seen == vertices


def add(*cochains: Co1) -> Co1:
    keys = set().union(*(set(c) for c in cochains))
    return {e: sum(c.get(e, 0) for c in cochains) % 2 for e in keys}


def product_00(left: Co0, right: Co0, edges: set[Edge],
               left_support: set[Vertex], right_support: set[Vertex]) -> Co1:
    """Baskakov product of two degree-zero cochains over F_2."""
    result: Co1 = {}
    for e in edges:
        u, v = e
        if u in left_support and v in right_support:
            result[e] = left.get(u, 0) & right.get(v, 0)
        elif v in left_support and u in right_support:
            result[e] = left.get(v, 0) & right.get(u, 0)
        else:
            result[e] = 0
    return result


def integrate(curvature: Co1, edges: set[Edge], vertices: set[Vertex]) -> Co0 | None:
    """Return the root-normalized potential, or None if holonomy is nonzero."""
    root = min(vertices)
    potential: Co0 = {root: 0}
    adjacency: dict[Vertex, list[Vertex]] = defaultdict(list)
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in sorted(adjacency[u]):
            if v not in potential:
                potential[v] = potential[u] ^ curvature.get(edge(u, v), 0)
                queue.append(v)
    if len(potential) != len(vertices):
        return None
    if any((potential[u] ^ potential[v]) != curvature.get(edge(u, v), 0)
           for u, v in edges):
        return None
    return potential


def fourfold_status(edges: set[Edge]) -> str:
    """Solve the five proper equations and test the top obstruction."""
    inputs = {i: {(i, 0): 1, (i, 1): 0} for i in range(1, 5)}
    fillers: dict[tuple[int, int], Co0] = {}

    for i in range(1, 4):
        corridor_edges, vertices = induced(edges, (i, i + 1))
        curvature = product_00(
            inputs[i], inputs[i + 1], corridor_edges, BLOCKS[i], BLOCKS[i + 1]
        )
        filler = integrate(curvature, corridor_edges, vertices)
        if filler is None:
            return "pair_fail"
        fillers[(i, i + 1)] = filler

    for i in (1, 2):
        corridor_edges, vertices = induced(edges, (i, i + 1, i + 2))
        curvature = add(
            product_00(
                inputs[i], fillers[(i + 1, i + 2)], corridor_edges,
                BLOCKS[i], BLOCKS[i + 1] | BLOCKS[i + 2],
            ),
            product_00(
                fillers[(i, i + 1)], inputs[i + 2], corridor_edges,
                BLOCKS[i] | BLOCKS[i + 1], BLOCKS[i + 2],
            ),
        )
        filler = integrate(curvature, corridor_edges, vertices)
        if filler is None:
            return "triple_fail"
        fillers[(i, i + 2)] = filler

    top = add(
        product_00(
            inputs[1], fillers[(2, 4)], edges,
            BLOCKS[1], BLOCKS[2] | BLOCKS[3] | BLOCKS[4],
        ),
        product_00(
            fillers[(1, 2)], fillers[(3, 4)], edges,
            BLOCKS[1] | BLOCKS[2], BLOCKS[3] | BLOCKS[4],
        ),
        product_00(
            fillers[(1, 3)], inputs[4], edges,
            BLOCKS[1] | BLOCKS[2] | BLOCKS[3], BLOCKS[4],
        ),
    )
    return "defined_zero" if integrate(top, edges, VERTICES) is not None else "defined_nonzero"


def connected_corridors(edges: set[Edge]) -> bool:
    for i in range(1, 4):
        corridor_edges, vertices = induced(edges, (i, i + 1))
        if not connected(corridor_edges, vertices):
            return False
    return True


def missing_adjacent_edges(edges: set[Edge]) -> tuple[Edge, Edge, Edge]:
    missing: list[Edge] = []
    for i in range(1, 4):
        possible = {
            edge((i, a), (i + 1, b)) for a, b in product((0, 1), repeat=2)
        }
        absent = possible - edges
        if len(absent) != 1:
            raise ValueError("expected exactly one missing edge in each adjacent corridor")
        missing.append(next(iter(absent)))
    return tuple(missing)  # type: ignore[return-value]


def predicted_ten_edge_nonzero(edges: set[Edge]) -> bool:
    """Closed-form R22 pattern for a defined nonzero 10-edge graph."""
    try:
        e12, e23, e34 = missing_adjacent_edges(edges)
    except ValueError:
        return False

    a1, b2 = e12[0][1], e12[1][1]
    a2, b3 = e23[0][1], e23[1][1]
    a3, b4 = e34[0][1], e34[1][1]
    adjacent = {
        edge((i, a), (i + 1, b))
        for i in range(1, 4)
        for a, b in product((0, 1), repeat=2)
    }
    nonadjacent_edges = edges - adjacent
    return (
        b2 != a2
        and b3 != a3
        and nonadjacent_edges == {edge((1, a1), (4, b4))}
    )


def enumerate_by_size(size: int) -> list[set[Edge]]:
    return [set(es) for es in combinations(sorted(AMBIENT), size)
            if connected_corridors(set(es))]


def main() -> None:
    nine = enumerate_by_size(9)
    ten = enumerate_by_size(10)

    nine_counts = Counter(fourfold_status(g) for g in nine)
    ten_counts = Counter(fourfold_status(g) for g in ten)
    predicted = {frozenset(g) for g in ten if predicted_ten_edge_nonzero(g)}
    observed = {frozenset(g) for g in ten if fourfold_status(g) == "defined_nonzero"}

    assert len(nine) == 64
    assert nine_counts == Counter({"defined_zero": 64})
    assert len(ten) == 816
    assert ten_counts == Counter({
        "defined_zero": 688,
        "triple_fail": 64,
        "pair_fail": 48,
        "defined_nonzero": 16,
    })
    assert observed == predicted

    print("9-edge connected-corridor graphs:", len(nine), dict(nine_counts))
    print("10-edge connected-corridor graphs:", len(ten), dict(ten_counts))
    print("10-edge nonzero graphs matching closed form:", len(observed))
    print("R22 exhaustive verification: PASS")


if __name__ == "__main__":
    main()
