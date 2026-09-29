# Generative Equipment — Horizon Effectivity and Coherence at Infinity
## Finite-Visibility Promotion, Derived-Limit Obstructions, Cross-Sector Validation, and the CP^2 Return Test

**Date:** 2026-09-29  
**Status:** derived theory over Frozen v1.0; no core modification.  
**Purpose:** complete the five-step feedback program: pause sector expansion, abstract the topology mechanism, identify coherence-at-infinity obstructions, test them outside topology, then return to the torsion two-cell topology problem.

---

# 0. Executive result

The topology branch has now been fed back into Generative Equipment rather than allowed to become an independent homotopy-theory project.

The central new derived structure is a **horizon realization tower**

\[
\mathcal R_0(\xi)\leftarrow \mathcal R_1(\xi)\leftarrow\cdots
\]

for a formal datum \(\xi\), together with a comparison

\[
\eta_\xi:\operatorname{EffFib}(\xi)
\longrightarrow
\operatorname*{holim}_n\mathcal R_n(\xi).
\]

When \(\eta_\xi\) is an equivalence, global effectivity is exactly the homotopy-limit problem of the finite horizons.

The resulting obstruction theory has three distinct layers:

1. **component compatibility** — whether
   \[
   \lim_n\pi_0\mathcal R_n(\xi)
   \]
   is nonempty;
2. **coherence-at-infinity branching** — the Milnor term
   \[
   \lim_n^1\pi_1\mathcal R_n(\xi);
   \]
3. **higher reconstruction corrections** — for \(q\ge1\),
   \[
   0\to\lim_n^1\pi_{q+1}\mathcal R_n
   \to\pi_q\operatorname{EffFib}(\xi)
   \to\lim_n\pi_q\mathcal R_n\to0.
   \]

Thus the old slogan

\[
\forall n\ \exists\text{ finite solution}
\not\Rightarrow
\exists\text{ one global solution}\ \forall n
\]

is refined: finite-horizon existence can fail to globalize either because the components do not form a compatible inverse branch, or because compatible finite data acquire extra global branching/coherence detected by derived limits.

The topology SNT theory becomes an exact special case: the spaces

\[
B\operatorname{Aut}(P_nX)
\]

are connected horizon moduli, and Wilkerson's

\[
SNT(X)\cong\lim{}^1\operatorname{Aut}(P_nX)
\]

is precisely the \(\lim^1\pi_1\) coherence-at-infinity sector.

A separate I-adic completion test confirms the mechanism outside topology.

---

# 1. Step 1 — stop sector drift and extract the reusable datum

Let

\[
C:\mathsf{Actual}\to\mathsf{Formal}
\]

be the Frozen actual/formal comparison, and fix

\[
\xi\in\mathsf{Formal}.
\]

Assume a sequence of observation horizons

\[
q_n:\mathsf{Formal}\to\mathsf{Formal}_{\le n}
\]

with transition functors \(q_{n+1,n}\).

Let \(C_n\) denote the induced finite-horizon comparison and define the horizon realization space

\[
\boxed{
\mathcal R_n(\xi)
=
\operatorname{EffFib}_{C_n}(q_n\xi).
}
\]

Transition maps induce a tower

\[
\cdots\to\mathcal R_{n+1}(\xi)\to\mathcal R_n(\xi)\to\cdots.
\]

The global realization space is

\[
\mathcal R_\infty(\xi)
=
\operatorname{EffFib}_{C}(\xi).
\]

There is a canonical map

\[
\boxed{
\eta_\xi:
\mathcal R_\infty(\xi)
\to
\operatorname*{holim}_n\mathcal R_n(\xi).
}
\]

## Definition — horizon-complete effectivity

The datum \((C,\xi,\{q_n\})\) is **horizon-complete** when \(\eta_\xi\) is an equivalence.

This is a substantive condition.  It must never be inferred merely from equality of all finite invariants.

---

# 2. Step 2 — Horizon Effectivity Theorem

## Theorem H1 — Global effectivity from the horizon tower

Assume horizon-complete effectivity. Then

\[
\boxed{
\xi\text{ is actualizable}
\iff
\operatorname*{holim}_n\mathcal R_n(\xi)\neq\varnothing.
}
\]

This is immediate from \(\eta_\xi\).

The point is therefore to understand when a tower of nonempty finite-horizon realization spaces has nonempty homotopy limit.

---

## Definition — component Mittag–Leffler

The component tower is

\[
\cdots\to\pi_0\mathcal R_{n+1}\to\pi_0\mathcal R_n\to\cdots.
\]

It is **Mittag–Leffler** when for each fixed \(n\), the descending family

\[
\operatorname{im}(\pi_0\mathcal R_m\to\pi_0\mathcal R_n),
\qquad m\ge n,
\]

is eventually constant.

## Theorem H2 — Component-ML Promotion

Assume:

1. every \(\mathcal R_n(\xi)\) is nonempty;
2. the component tower is Mittag–Leffler;
3. the effectivity datum is horizon-complete.

Then

\[
\boxed{
\operatorname{EffFib}(\xi)\neq\varnothing.
}
\]

### Proof

For each \(n\), let \(I_n\subseteq\pi_0\mathcal R_n\) be the stable image of sufficiently high stages.  ML implies the restricted transition maps

\[
I_{n+1}\to I_n
\]

are surjective.  Since each \(I_n\neq\varnothing\), dependent choice produces a compatible sequence of components, hence

\[
\lim_n\pi_0\mathcal R_n\neq\varnothing.
\]

After replacing the tower by a fibrant tower, the standard \(q=0\) Milnor exact sequence gives a surjection

\[
\pi_0\operatorname*{holim}_n\mathcal R_n
\twoheadrightarrow
\lim_n\pi_0\mathcal R_n.
\]

Thus the homotopy limit is nonempty, and H1 finishes the proof. \(\square\)

---

## Corollary H2.1 — finite-visibility compactness

If each set \(\pi_0\mathcal R_n(\xi)\) is finite and nonempty, then the component tower is automatically ML. Hence, under horizon completeness,

\[
\boxed{
\forall n\;\mathcal R_n(\xi)\neq\varnothing
\quad\Longrightarrow\quad
\mathcal R_\infty(\xi)\neq\varnothing.
}
\]

This is the cleanest finite-visibility promotion theorem.

It is not a universal compactness principle: its crucial hypotheses are finiteness/ML of the *realization components* and horizon completeness of the comparison.

---

# 3. Step 3 — Coherence-at-Infinity Profile

For a fibrant tower of pointed spaces, the standard Milnor exact sequence gives, for \(q\ge1\),

\[
\boxed{
0\to
\lim_n^1\pi_{q+1}\mathcal R_n
\to
\pi_q\operatorname*{holim}_n\mathcal R_n
\to
\lim_n\pi_q\mathcal R_n
\to0.
}
\]

For \(q=0\) there is an exact sequence of pointed sets whose left term is \(\lim^1\pi_1\).

Under horizon completeness these become exact statements about the global effectivity fiber itself.

## Definition — coherence-at-infinity profile

Define

\[
\boxed{
\mathfrak C_\infty(\xi)
=
\left(
\lim\pi_0\mathcal R_n,
\lim{}^1\pi_1\mathcal R_n,
\{\lim{}^1\pi_{q+1}\mathcal R_n\}_{q\ge1}
\right).
}
\]

Interpretation:

- \(\lim\pi_0\): existence of a compatible *branch of finite realizations*;
- \(\lim^1\pi_1\): extra global components invisible at every fixed horizon;
- higher \(\lim^1\): discrepancy between finite-horizon higher deformation data and global higher deformation data.

This replaces the overly coarse phrase “the obstruction is \(\lim^1\)” by a typed obstruction profile.

---

## Theorem H3 — rigidity under ML

Assume horizon completeness and a compatible component branch.  If the corresponding tower of fundamental groups is ML, then

\[
\lim{}^1\pi_1\mathcal R_n=*,
\]

so there is no additional component branching above that compatible finite branch.

More generally, if the towers \(\pi_{q+1}\mathcal R_n\) are ML, their Milnor \(\lim^1\)-corrections vanish.

This is the abstract form of the mechanism that appeared in the Postnikov/SNT calculation.

---

# 4. Step 3b — finite-visibility rigidity as a sector criterion

Suppose for every horizon \(n\) there is a finite-control subsystem \(V_n\) and a map

\[
V_n\to\mathcal R_n(\xi)
\]

whose image contains the eventual image of every higher horizon.

If \(\pi_0(V_n)\) is finite, component ML follows.

If in addition the relevant automorphism/fundamental-group image at horizon \(n\) has finite index in \(\pi_1\mathcal R_n\), then the descending higher-horizon images are trapped among finitely many intermediate subgroups whenever the ambient quotient is finite.  This is the mechanism behind the finite-visible Postnikov rigidity argument.

This criterion is deliberately stated as a sufficient sector engine, not a new primitive axiom.

---

# 5. SNT as an exact coherence-at-infinity sector

Let \(X\) be a connected CW space and \(P_nX\) its Postnikov sections.

Wilkerson's classification gives

\[
\boxed{
SNT(X)
\cong
\lim_n^1\operatorname{Aut}(P_nX).
}
\]

Now define connected horizon moduli

\[
\mathcal M_n(X)=B\operatorname{Aut}(P_nX).
\]

Then

\[
\pi_1\mathcal M_n(X)=\operatorname{Aut}(P_nX),
\qquad
\pi_0\mathcal M_n(X)=*.
\]

Hence the \(q=0\) Milnor term says schematically

\[
\pi_0\operatorname*{holim}_n\mathcal M_n(X)
\cong
\lim_n^1\operatorname{Aut}(P_nX),
\]

which is exactly the SNT classification.

Therefore:

\[
\boxed{
SNT(X)
\text{ is a pure coherence-at-infinity branching invariant.}
}
\]

There is no finite-horizon object-existence defect here: every \(P_nX\) exists.  The issue is whether infinitely many finite-stage identifications glue to a unique global homotopy type.

For countable automorphism groups, McGibbon–Møller prove

\[
\lim{}^1\operatorname{Aut}(P_nX)=*
\iff
\{\operatorname{Aut}(P_nX)\}
\text{ is Mittag–Leffler},
\]

and nontrivial \(\lim^1\) is uncountable.

Thus the topology branch is not a detour: it supplies an exact model of the general \(\lim^1\pi_1\) coherence layer.

---

# 6. Step 4 — Cross-sector test: I-adic actualization

Take

\[
A=k[[t]],
\qquad
A_n=A/(t^n).
\]

Consider a compatible tower of modules

\[
M_n=A_n^r
\]

with the canonical reductions.

Define

\[
M=\lim_nM_n.
\]

Then

\[
\boxed{M\cong A^r}
\]

and

\[
M/t^nM\cong M_n.
\]

This is the simplest explicit instance of the general completion theorem for compatible module towers over finitely generated ideals.

The actual/formal comparison is therefore effective: all compatible finite horizons algebraize to one complete module.

### Automorphism coherence

The automorphism tower is

\[
GL_r(A_{n+1})\to GL_r(A_n).
\]

Each reduction map is surjective: an invertible matrix modulo \(t^n\) can be lifted entrywise, and its determinant remains a unit after lifting.

Therefore the tower is ML and

\[
\lim{}^1 GL_r(A_n)=*.
\]

Moreover

\[
GL_r(A)\cong\lim_nGL_r(A_n).
\]

Thus this sector realizes the positive pattern:

\[
\boxed{
\text{finite-horizon existence}
+\text{surjective coherence}
\Longrightarrow
\text{global actualization with no hidden }\lim^1\text{ branching}.
}
\]

This is not new commutative algebra; it is a cross-sector validation of the derived Generative Equipment mechanism.

---

# 7. Negative cross-control: the solenoid tower

Consider

\[
\cdots\xrightarrow{2}S^1\xrightarrow{2}S^1\xrightarrow{2}S^1.
\]

Every finite horizon is connected, so

\[
\pi_0(S^1)=*.
\]

But on fundamental groups the tower is

\[
\cdots\xrightarrow{\times2}\mathbb Z
\xrightarrow{\times2}\mathbb Z.
\]

It is not ML, and

\[
\lim{}^1(\mathbb Z\xleftarrow{\times2}\mathbb Z\xleftarrow{\times2}\cdots)
\]

is nontrivial (indeed produces the familiar uncountable component phenomenon of the 2-adic solenoid).

Thus finite-horizon connectedness does **not** imply global connectedness/rigidity.

This is the exact negative control needed for the theory.

---

# 8. Step 5 — Return to \(X=\Omega\Sigma\mathbf{CP}^2\)

Let

\[
K=\Sigma\mathbf{CP}^2
\simeq
S^3\cup_{\eta_3}e^5,
\qquad
X=\Omega K.
\]

The attaching map \(\eta_3\) has order two.

The low homotopy data include

\[
\pi_2X\cong\mathbb Z,
\qquad
\pi_3X=0,
\qquad
\pi_4X\cong\mathbb Z,
\qquad
\pi_5X\cong\mathbb Z/6.
\]

In particular

\[
P_4X\simeq K(\mathbb Z,2)\times K(\mathbb Z,4).
\]

The fourth-stage self-equivalence group contains the integral shear direction

\[
v\longmapsto \pm v+c\,u^2,
\qquad c\in\mathbb Z,
\]

where \(u\) is the degree-two generator and \(v\) the degree-four generator.

For \(m\ge4\), define

\[
G_m
=
\operatorname{im}
\left[
\operatorname{Aut}(P_mX)	o\operatorname{Aut}(P_4X)
\right]
\]

and let

\[
D_m=G_m\cap\mathbb Z_{\rm shear}.
\]

Every \(D_m\) is a subgroup of \(\mathbb Z\), hence

\[
D_m=d_m\mathbb Z
\]

for some \(d_m\ge0\), and

\[
D_{m+1}\subseteq D_m.
\]

## Theorem/Diagnostic CP2-H1 — shear horizon test

If the chain

\[
D_4\supseteq D_5\supseteq D_6\supseteq\cdots
\]

fails to stabilize, then the automorphism tower cannot be Mittag–Leffler.  Consequently

\[
SNT(X)\neq*,
\]

and, since the relevant groups are countable, the SNT set is uncountable.

Thus a strict unbounded divisibility pattern

\[
d_4\mid d_5\mid d_6\mid\cdots,
\qquad d_m\to\infty,
\]

would be a concrete certificate of non-rigidity.

Conversely, stabilization of \(D_m\) removes only this *particular* shear source of non-ML; other horizons or other automorphism directions could still fail ML.

This is therefore an exact one-direction diagnostic, not a false equivalence.

---

# 9. Prime-support reduction survives the new framework

At every odd prime \(p\), the order-two attachment vanishes after \(p\)-localization:

\[
K_{(p)}\simeq S^3_{(p)}\vee S^5_{(p)}.
\]

The previously established finite-visibility/Hilton–Milnor argument for odd-spherical wedges therefore supplies the odd-primary rigid sector.

Hence any unresolved coherence-at-infinity for the integral \(X\) must interact with the 2-primary attaching information; however SNT does not decompose naively as a product of its localizations, so this is a reduction of the difficult source, not an integral proof.

---

# 10. What the abstract theory adds to the CP^2 problem

Before this feedback step, the problem was phrased only as

\[
\lim{}^1\operatorname{Aut}(P_nX)=*\ ?
\]

The new theory splits this into testable layers:

1. **finite horizon visibility:** identify the finite part of \(P_nX\) actually controlling self-equivalences;
2. **stable image chains:** for each fixed horizon \(r\), study
   \[
   I_{r,m}=\operatorname{im}
   [\operatorname{Aut}(P_mX)\to\operatorname{Aut}(P_rX)];
   \]
3. **first coherence defect:** find the least \(r\) for which \(I_{r,m}\) fails to stabilize, if one exists;
4. **typed obstruction:** determine whether failure lies in a visible arithmetic direction (such as the \(P_4\) shear) or in a genuinely higher automorphism component.

For \(\Omega\Sigma CP^2\), the first explicit candidate is the integer shear tower \(D_m\).

This is a stronger research interface than “compute all automorphism groups”: it asks only for eventual images at a fixed low horizon.

---

# 11. Completion status of the five requested steps

### Step 1 — pause topology and recover the mechanism

**Complete.**  The topology branch is recast as a horizon-effectivity sector of Frozen v1.0.

### Step 2 — general finite-visibility / horizon-effectivity theorem

**Complete.**  H1–H2 give the global effectivity criterion and the ML/finite-component promotion theorem.

### Step 3 — abstract coherence-at-infinity obstruction

**Complete.**  The obstruction is a typed Milnor profile, not a single undifferentiated \(\lim^1\).  SNT is identified as the connected \(\lim^1\pi_1\) special case.

### Step 4 — independent sector test

**Complete.**  I-adic module completion gives a positive actualization/ML example; the solenoid gives a negative control.

### Step 5 — return to the CP^2 topology problem

**Complete as a theory stress test.**  The new abstraction does not magically solve the SNT problem.  It reduces it to stable-image/coherence diagnostics, with the \(P_4\) integer shear tower \(D_m\) as the first explicit candidate and the odd-primary part separated from the 2-primary attachment difficulty.

A full proof of

\[
SNT(\Omega\Sigma CP^2)=*
\]

is **not** claimed.

---

# 12. Consequence for Generative Equipment

The topology detour has now produced a genuine derived theorem schema:

\[
\boxed{
\textbf{finite-horizon visibility}
\;\longrightarrow\;
\textbf{component ML / coherent branch}
\;\longrightarrow\;
\textbf{global effectivity},
}
\]

with

\[
\boxed{
\lim{}^1\pi_1
}
\]

measuring hidden component branching and higher \(\lim^1\) terms measuring higher reconstruction defects.

This should be added to the derived layer, not the Frozen primitive core.

The mechanism is independently instantiated in:

- Postnikov/SNT topology;
- I-adic completion;
- pro-object effectivity / DHH-type towers;
- potentially formal geometry and derived completion.

The next theoretical question is no longer whether this mechanism exists, but how to recognize **horizon completeness** \(\eta_\xi\simeq\) in broad classes of sectors.  That is the correct next general theorem target.
