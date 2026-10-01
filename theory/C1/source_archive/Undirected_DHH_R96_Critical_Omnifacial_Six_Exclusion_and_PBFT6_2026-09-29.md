# Undirected DHH — R96
## Critical Omnifacial Six-Exclusion, Closure of the \(A_2^5\) Carrier Gap, and PBFT\(_6\)

**Date:** 2026-09-29

## Status

This note closes the single gap isolated in R95.

The decisive result is stronger than the requested relative filling:

\[
\boxed{
\operatorname{Omni}_6(A_2^5)=\varnothing.
}
\]

Together with R95's already proved absence in degrees \(q\le5\), this gives

\[
\boxed{
(B_5)_q=(N_1A_2^5)_q
\qquad(q\le6),
}
\]

where \(B_5\) is the non-omnifacial safe-patch union.

Therefore

\[
C_6(N_1A_2^5,B_5)=0
\]

and in particular

\[
\boxed{
H_6(N_1A_2^5,B_5;\mathbb Z)=0.
}
\]

Using R95's reduction, this supplies the formal \(A_2^5\) carrier input for
the \(D_6\) curvature tower.  The proper-link actualization is already
covered recursively by R94.  Hence the R95 conditional implication closes
and yields

\[
\boxed{\mathrm{PBFT}_6},
\qquad
\boxed{N_1D_6\simeq S^4}.
\]

No large graph-cube enumeration is used.

---

# 1. Signed-face model

Let

\[
K_5=\partial O^5.
\]

Its ten vertices are five opposite pairs.  The Hasse graph of nonempty
faces is

\[
H(K_5)\cong A_2^5.
\]

The ten rank-one Hasse vertices will be called the **facet centers**.

Let

\[
f:Q_6\longrightarrow A_2^5
\]

be a graph cube.

Assume for contradiction that \(f\) is omnifacial.

For each of the ten facet centers choose one source preimage.  Let

\[
W\subseteq V(Q_6)
\]

be the resulting set of ten chosen **witnesses**.

The ten witnesses are distinct.

---

# 2. First local constraints

### Lemma 2.1 — witnesses are independent

No two distinct witnesses are source-adjacent.

### Proof

Distinct facet centers are distinct rank-one vertices of the Hasse graph.
Two distinct rank-one Hasse vertices are not adjacent.  A graph map sends a
source edge only to an equal or adjacent target pair.  Hence two witnesses
cannot be adjacent.
\(\square\)

For a source vertex \(x\notin W\), write

\[
\nu(x)=|N_{Q_6}(x)\cap W|.
\]

### Lemma 2.2 — no triple witness neighborhood

\[
\nu(x)\le2.
\]

### Proof

If \(x\) were adjacent to three distinct witnesses, then \(f(x)\) would be
equal or Hasse-adjacent to three distinct rank-one target vertices.

A target Hasse vertex which is equal or adjacent to a rank-one vertex has
rank \(1\) or \(2\).  A rank-two face contains exactly two rank-one
subfaces.  Hence no target vertex lies in the closed neighborhoods of three
distinct facet centers.
\(\square\)

Put

\[
Z_j=\{x\in Q_6\setminus W:\nu(x)=j\},
\qquad j=0,1,2.
\tag{2.1}
\]

---

# 3. Vertices with two witness neighbors are forced rank-two states

Fix

\[
z\in Z_2.
\]

Let its two witness neighbors be

\[
a,b\in W.
\]

Write their target singleton labels as

\[
\alpha=f(a),
\qquad
\beta=f(b).
\]

### Lemma 3.1 — forced midpoint

The two labels \(\alpha,\beta\) are nonopposite, and

\[
\boxed{
f(z)=\{\alpha,\beta\},
}
\tag{3.1}
\]

the unique rank-two face joining them.

### Proof

The source path

\[
a-z-b
\]

has length two.  Therefore the target distance between \(\alpha\) and
\(\beta\) is at most two.  Opposite facet centers have Hasse distance four,
so \(\alpha,\beta\) are not opposite.

Two distinct nonopposite rank-one vertices have one and only one common
closed Hasse neighbor: their rank-two union.  Since \(f(z)\) must be a
closed neighbor of both, (3.1) follows.
\(\square\)

---

# 4. The four unused neighbors of a forced midpoint see no witness

A vertex of \(Q_6\) has degree six.  The vertex \(z\in Z_2\) already has the
two witness neighbors \(a,b\).

Let

\[
x
\]

be one of its other four source neighbors.

### Lemma 4.1

\[
\boxed{x\in Z_0.}
\tag{4.1}
\]

### Proof

Suppose \(x\) were adjacent to a witness \(c\in W\).

Because \(Q_6\) is triangle-free, \(c\) cannot equal \(a\) or \(b\): an
"other" neighbor \(x\) of \(z\) is at source distance two from both
\(a\) and \(b\).

Thus the singleton label

\[
\gamma=f(c)
\]

is distinct from both \(\alpha,\beta\).

Now \(x\sim c\) forces \(f(x)\) to be equal or adjacent to the singleton
\(\gamma\), whereas \(x\sim z\) and (3.1) force \(f(x)\) to be equal or
adjacent to the rank-two face \(\{\alpha,\beta\}\).

No Hasse vertex has both properties when
\(\gamma\notin\{\alpha,\beta\}\):

- a rank-one common neighbor would have to equal \(\gamma\), but
  \(\gamma\) is not a subface of \(\{\alpha,\beta\}\);
- a rank-two neighbor of \(\gamma\) contains \(\gamma\), and cannot equal
  the distinct rank-two face \(\{\alpha,\beta\}\);
- rank at least three is not adjacent to a rank-one vertex.

Contradiction.
\(\square\)

Hence every \(z\in Z_2\) has exactly four edges into \(Z_0\).

Therefore the number of \(Z_2\)--\(Z_0\) source edges is

\[
\boxed{
e(Z_2,Z_0)=4|Z_2|.
}
\tag{4.2}
\]

---

# 5. A zero-witness vertex sees at most three forced midpoints

Fix

\[
x\in Z_0.
\]

Suppose that

\[
z_1,\ldots,z_k\in Z_2
\]

are distinct neighbors of \(x\).

For each \(z_i\), let

\[
P_i=\{a_i,b_i\}\subset W
\]

be its pair of witness neighbors, and let

\[
F_i=\{f(a_i),f(b_i)\}
\]

be the forced rank-two target face from Lemma 3.1.

### Lemma 5.1 — the forced faces \(F_i\) are distinct

If \(i\ne j\), then

\[
F_i\ne F_j.
\]

### Proof

The chosen witnesses have distinct singleton labels, so equality of
\(F_i,F_j\) would imply equality of the unordered witness pairs:

\[
P_i=P_j=\{a,b\}.
\]

Then \(z_i,z_j\) are the two common source neighbors of the distance-two
vertices \(a,b\).

In a hypercube, those two common neighbors have exactly \(a,b\) as their
own common neighbors.  Since \(x\) is adjacent to both \(z_i,z_j\), it
would have to equal \(a\) or \(b\), contrary to \(x\in Z_0\).
\(\square\)

### Lemma 5.2 — common-neighbor classification for rank-two Hasse faces

Let \(F_1,\ldots,F_k\) be distinct rank-two faces of a simplicial Hasse
graph.  If one target vertex is equal or adjacent to every \(F_i\), then
either

1. \(k\le3\); or
2. all \(F_i\) contain one common rank-one vertex.

### Proof

A closed neighbor of a rank-two Hasse vertex has rank \(1,2\), or \(3\).

- A rank-two common neighbor can equal only one of the distinct \(F_i\).
- A rank-three face has exactly three rank-two subfaces.
- A rank-one common neighbor is precisely a singleton contained in every
  \(F_i\).

This gives the dichotomy.
\(\square\)

### Lemma 5.3 — capacity of \(Z_0\)

\[
\boxed{
|N(x)\cap Z_2|\le3.
}
\tag{5.1}
\]

### Proof

Assume \(k\ge4\).

Since \(x\sim z_i\), the target value \(f(x)\) is a common closed Hasse
neighbor of the distinct rank-two faces \(F_i\).

By Lemma 5.2, all \(F_i\) contain one common singleton label \(\lambda\).

Let \(w\in W\) be the unique chosen witness carrying label \(\lambda\).
Then every witness pair \(P_i\) contains \(w\), so every \(z_i\) is adjacent
to \(w\).

Thus \(z_1,\ldots,z_k\) are common source neighbors of \(x\) and \(w\).

Because \(x\in Z_0\), \(x\) is neither equal nor adjacent to \(w\).
Two vertices of a hypercube have common neighbors only when their Hamming
distance is two, and then they have exactly two common neighbors.

Therefore \(k\le2\), contradicting \(k\ge4\).

Hence \(k\le3\).
\(\square\)

Consequently

\[
\boxed{
e(Z_2,Z_0)\le3|Z_0|.
}
\tag{5.2}
\]

Combining (4.2) and (5.2),

\[
\boxed{
4|Z_2|\le3|Z_0|.
}
\tag{5.3}
\]

---

# 6. Global incidence count

The witness set has ten vertices, each of degree six.

By Lemma 2.1, every edge incident with a witness goes to
\(Q_6\setminus W\).

Therefore

\[
10\cdot6=60
\]

is the total witness--nonwitness incidence count.

Using Lemma 2.2,

\[
\boxed{
|Z_1|+2|Z_2|=60.
}
\tag{6.1}
\]

There are

\[
64-10=54
\]

nonwitness source vertices, so

\[
\boxed{
|Z_0|+|Z_1|+|Z_2|=54.
}
\tag{6.2}
\]

Eliminate \(|Z_1|\) from (6.1)--(6.2):

\[
|Z_0|
=
54-(60-2|Z_2|)-|Z_2|
=
|Z_2|-6.
\tag{6.3}
\]

Insert this into (5.3):

\[
4|Z_2|
\le
3(|Z_2|-6).
\]

Hence

\[
|Z_2|\le-18,
\]

which is impossible.

We have proved:

### Theorem 6.1 — Critical Omnifacial Six-Exclusion

\[
\boxed{
\operatorname{Omni}_6(A_2^5)=\varnothing.
}
\tag{6.4}
\]

The proof is purely combinatorial and integral.

---

# 7. Closure of the R95 critical group

R95 already proves

\[
\operatorname{Omni}_q(A_2^5)=\varnothing
\qquad(q\le5).
\]

Together with Theorem 6.1,

\[
\boxed{
\operatorname{Omni}_q(A_2^5)=\varnothing
\qquad(q\le6).
}
\tag{7.1}
\]

Therefore the non-omnifacial safe-patch union satisfies

\[
\boxed{
(B_5)_q=(N_1A_2^5)_q
\qquad(q\le6).
}
\tag{7.2}
\]

In particular,

\[
C_6(N_1A_2^5,B_5)=0,
\]

so

\[
\boxed{
H_6(N_1A_2^5,B_5;\mathbb Z)=0.
}
\tag{7.3}
\]

R95 proves

\[
H_6(N_1A_2^5,\mathscr A_5)
\cong
H_6(N_1A_2^5,B_5).
\]

Hence

\[
\boxed{
H_6(N_1A_2^5,\mathscr A_5;\mathbb Z)=0.
}
\tag{7.4}
\]

This is exactly the formal carrier input needed for the \(D_6\) curvature
tower.

---

# 8. PBFT\(_6\)

R95 proves the conditional implication:

\[
H_6(N_1A_2^5,\mathscr A_5)=0
\Longrightarrow
\mathsf{AE}(5)
\Longrightarrow
\mathrm{PBFT}_6.
\]

The first arrow uses:

- the R94 actual puncture-link evaluator on all proper links;
- the coupled curvature tower
  \[
  \Omega_4,\Omega_3,\Omega_2;
  \]
- finite joint transport-support descent.

The second arrow uses R54's PBFT tail criterion.

Equation (7.4) supplies the missing hypothesis.

Therefore:

### Theorem 8.1 — PBFT\(_6\)

\[
\boxed{
\mathscr B_6
\xrightarrow{\sim}
N_1D_6.
}
\tag{8.1}
\]

Since

\[
|\mathscr B_6|\simeq S^4,
\]

we obtain

\[
\boxed{
N_1D_6\simeq S^4.
}
\tag{8.2}
\]

Thus PBFT is now proved for

\[
\boxed{
m=3,4,5,6.
}
\]

---

# 9. Why this does not contradict carrier universality

R46 proves that omnifacial Hasse cubes can carry arbitrary finite connected
carriers in sufficiently high source dimension.

Theorem 6.1 is a **critical low-degree exclusion**:

\[
Q_6\to H(\partial O^5).
\]

It uses the exact numerical coincidence

\[
|W|=10,\qquad
\deg Q_6=6,
\]

and the rank-two closed-neighbor structure of the Hasse graph.

There is no conflict with R46's large-dimensional layered constructions.

---

# 10. General counting form and the next frontier

The same two-level counting argument can be written for

\[
A_2^d=H(\partial O^d)
\]

at source degree

\[
q=d+1.
\]

There are \(2d\) chosen singleton witnesses.

Let \(n_0,n_1,n_2\) count nonwitness source vertices with
\(0,1,2\) witness neighbors.

The same local Hasse argument gives:

1. no vertex has three witness neighbors;
2. every \(Z_2\)-vertex has \(q-2=d-1\) remaining neighbors in \(Z_0\);
3. every \(Z_0\)-vertex has at most three \(Z_2\)-neighbors.

Hence

\[
(d-1)n_2\le3n_0.
\tag{10.1}
\]

The incidence equations give

\[
n_0
=
n_2
+
2^{d+1}
-
2d(d+2).
\tag{10.2}
\]

For \(d=5\),

\[
n_0=n_2-6,
\]

and (10.1) is impossible.

For \(d=6\), however,

\[
n_0=n_2+32,
\]

and the inequality no longer contradicts nonnegativity.

Therefore this argument closes precisely the \(A_2^5\) critical carrier,
but does not automatically eliminate the next critical sector

\[
H_7(N_1A_2^6,B_6).
\]

That is now the next formal frontier toward PBFT\(_7\).

---

# 11. Strict status

## Newly proved

1.
   \[
   \operatorname{Omni}_6(A_2^5)=\varnothing.
   \]
2.
   \[
   H_6(N_1A_2^5,B_5)=0.
   \]
3.
   \[
   H_6(N_1A_2^5,\mathscr A_5)=0.
   \]
4.
   \[
   \boxed{\mathrm{PBFT}_6}.
   \]
5.
   \[
   \boxed{N_1D_6\simeq S^4}.
   \]

## Current next obstruction

\[
\boxed{
H_7(N_1A_2^6,B_6)
}
\]

for the \(A_2^6\) critical omnifacial sector.

No claim of general PBFT or complete undirected DHH is made beyond the
proved range \(m\le6\).
