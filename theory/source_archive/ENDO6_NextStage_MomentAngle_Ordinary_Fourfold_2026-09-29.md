# ENDO-6 Next Stage — Ordinary Fourfold Massey Frontier in the 8-Vertex Moment-Angle Sector

**Date:** 2026-09-29  
**Status:** computer-assisted finite theorem in the stated sector; Frozen v1.0 unchanged.

## Sector

Let \(K\) be a **1-dimensional** simplicial complex on eight vertices partitioned
\[
J_i=\{x_i^0,x_i^1\},\qquad i=1,2,3,4,
\]
with no edge inside any \(J_i\). Work over \(\mathbb F_2\). Let \(\alpha_i\in H^3(\mathcal Z_K;\mathbb F_2)\) be the Hochster class corresponding to the missing edge \(J_i\). Assume each adjacent corridor \(K_{J_i\cup J_{i+1}}\) is connected.

## Theorem — Connected-Corridor Ordinary Fourfold Vanishing

For every such \(K\), the ordinary fourfold Massey product
\[
\langle\alpha_1,\alpha_2,\alpha_3,\alpha_4\rangle
\]
is either undefined or contains \(0\). Hence no non-trivial ordinary fourfold Massey product occurs anywhere in this entire sector.

Equivalently: the interval-homogeneous graph-MC obstruction can be nonzero, but every such nonzero case is killed by ordinary off-interval saturation.

## Exhaustive finite classification

The ambient graph has 24 possible cross-block edges. Connectedness of each of the three adjacent \(K_{2,2}\) corridors leaves exactly \(5^3\cdot2^{12}=512000\) graphs. Every one was classified.

| edges | graphs | pair fail | triple fail | restricted zero | restricted nonzero |
|---:|---:|---:|---:|---:|---:|
| 9 | 64 | 0 | 0 | 64 | 0 |
| 10 | 816 | 48 | 64 | 688 | 16 |
| 11 | 4,812 | 588 | 688 | 3,392 | 144 |
| 12 | 17,393 | 3,313 | 3,360 | 10,144 | 576 |
| 13 | 43,044 | 11,364 | 9,840 | 20,496 | 1,344 |
| 14 | 77,154 | 26,466 | 19,200 | 29,472 | 2,016 |
| 15 | 103,312 | 44,176 | 26,208 | 30,912 | 2,016 |
| 16 | 105,039 | 54,351 | 25,536 | 23,808 | 1,344 |
| 17 | 81,576 | 49,896 | 17,760 | 13,344 | 576 |
| 18 | 48,268 | 34,188 | 8,640 | 5,296 | 144 |
| 19 | 21,516 | 17,292 | 2,800 | 1,408 | 16 |
| 20 | 7,071 | 6,303 | 544 | 224 | 0 |
| 21 | 1,652 | 1,588 | 48 | 16 | 0 |
| 22 | 258 | 258 | 0 | 0 | 0 |
| 23 | 24 | 24 | 0 | 0 | 0 |
| 24 | 1 | 1 | 0 | 0 | 0 |
| **total** | **512,000** | **249,856** | **114,688** | **139,264** | **8,192** |

All **8,192** restricted-nonzero cases admit an explicit ordinary saturation witness that makes the top class exact.

## Why the restricted failures remain ordinary failures

The Hochster/Baskakov DGA is support-graded and the differential preserves support.

* A pair equation has right-hand side supported exactly on \(J_i\cup J_{i+1}\). Off-support terms cannot repair a non-exact expected-support component. Therefore every restricted `pair_fail` remains undefined ordinarily.
* Once pair equations are solvable, the expected-support part of a triple equation depends only on expected-support pair components. In the connected corridor sector those components are unique up to the reduced constant ambiguity already accounted for by the graph integration model. Thus restricted `triple_fail` also remains an ordinary failure.
* `restricted zero` already gives an ordinary defining system containing zero.
* Only the 8,192 `restricted nonzero` cases need saturation analysis.

## Saturation mechanism used in all 8,192 cases

For a disconnected four-vertex support \(S\), a component indicator determines a reduced \(H^0(K_S;\mathbb F_2)\) class and hence a degree-five Hochster cocycle. The exhaustive verifier allows one such off-interval closed variation in the \(12\)-pair filler and one in the \(34\)-pair filler, then solves the two triple equations in the full moment-angle DGA and tests the top class modulo:

1. ordinary degree-nine boundaries;
2. all closed degree-seven variations of the two triple fillers.

For every restricted-nonzero graph, a witness exists. The support pairs used are always one of the four complementary forms
\[
J_1\cup\{x_2^a,x_3^b\}
\quad\text{and}\quad
J_4\cup\{x_2^{1-a},x_3^{1-b}\},
\qquad a,b\in\{0,1\}.
\]
Thus the cancellation is a uniform cross-support \(2+2\) saturation phenomenon, generalizing the original ten-edge counterexample.

## Mathematical consequence

The 1-skeleton-only connected-corridor route cannot produce an extremal eight-vertex ordinary non-trivial fourfold Massey product. Any eight-vertex example outside this theorem must use at least one feature excluded here, in particular:

* disconnected adjacent proper corridors, or
* genuinely higher-dimensional simplices/off-support positive simplicial-degree modes.

So the ENDO frontier has moved: the next natural target is no longer edge minimization inside the connected graph sector, but the first higher-dimensional simplicial mechanism that survives full saturation.

## Literature boundary

The standard literature constructs non-trivial higher Massey products in moment-angle complexes using star deletions, truncations and related combinatorial constructions. A targeted search located the general Grbić–Linton construction and the known classification of lowest-degree triple products, but did not locate this exact 8-vertex connected-corridor ordinary-fourfold vanishing classification. This is not a claim of literature-first originality; systematic checking would still be required.
