# Two-Cell Loop-Space Postnikov Rigidity — R1
## SNT/ML reduction, finite-wedge rigidity, and the first torsion-attaching core

**Date:** 2026-09-29  
**Target:** for
\[
Z_\alpha=S^m\cup_\alpha e^n,\qquad X_\alpha=\Omega Z_\alpha,
\]
characterize when
\[
SNT(X_\alpha)=\{[X_\alpha]\}.
\]
Throughout the clean simply-connected loop-space discussion, assume \(m\ge3\).

---

## 1. Exact SNT reduction

For a connected CW complex \(X\), Wilkerson's classification gives a pointed-set bijection
\[
SNT(X)\cong \lim{}^1_r\operatorname{Aut}(P_rX).
\]
For a tower of countable groups, McGibbon--Møller prove
\[
\lim{}^1G_r=*
\iff
\{G_r\}\text{ is Mittag--Leffler},
\]
and otherwise \(\lim{}^1G_r\) is uncountable.

Hence for the finite-type nilpotent spaces occurring here,
\[
\boxed{
SNT(X)=*
\iff
\{\operatorname{Aut}(P_rX)\}\text{ is Mittag--Leffler}.
}
\]
Writing
\[
I_{r,s}=\operatorname{Im}\bigl(\operatorname{Aut}(P_sX)\to\operatorname{Aut}(P_rX)\bigr),
\]
this is the stabilization condition
\[
\forall r\;\exists N(r)\;\forall s\ge N(r):
I_{r,s}=I_{r,N(r)}.
\]

---

## 2. A finite-factor Mittag--Leffler criterion

### Theorem 2.1
Let \(X\) be a connected CW complex. Assume that for every \(r\) there is a product decomposition
\[
X\simeq Y_r\times Z_r
\]
such that:

1. \(P_rZ_r\simeq *\);
2. the image of
   \[
   \operatorname{Aut}(Y_r)\to\operatorname{Aut}(P_rY_r)
   \]
   has finite index.

Then
\[
\boxed{SNT(X)=*.}
\]

### Proof
Set
\[
G_r=\operatorname{Aut}(P_rX),
\qquad
I_{r,s}=\operatorname{Im}(\operatorname{Aut}(P_sX)\to G_r).
\]
Because \(P_rZ_r\simeq*\),
\[
P_rX\simeq P_rY_r.
\]
Every \(f\in\operatorname{Aut}(Y_r)\) extends to
\[
f\times\operatorname{id}_{Z_r}\in\operatorname{Aut}(X).
\]
Therefore the image
\[
H_r=\operatorname{Im}(\operatorname{Aut}(X)\to G_r)
\]
contains a finite-index subgroup of \(G_r\); hence \(H_r\) itself has finite index.

For every \(s\ge r\), a global self-equivalence truncates to a self-equivalence of \(P_sX\), so
\[
H_r\subseteq I_{r,s}\subseteq G_r.
\]
There are only finitely many subgroups of \(G_r\) containing a fixed finite-index subgroup \(H_r\), since each is a union of left cosets of \(H_r\). Thus the descending chain \(I_{r,s}\) stabilizes. The automorphism tower is Mittag--Leffler, and Wilkerson's classification gives \(SNT(X)=*\).  ∎

---

## 3. Finite wedges of spheres are loop-SNT rigid

### Theorem 3.1
Let
\[
K=\bigvee_{i=1}^q S^{d_i},
\qquad d_i\ge3,
\]
with \(q<\infty\). Then
\[
\boxed{SNT(\Omega K)=*.}
\]

### Proof
Hilton--Milnor gives a weak-product decomposition
\[
\Omega K\simeq\prod_{w\in\mathcal B_q}'\Omega S^{N(w)},
\]
where \(w\) ranges over basic Lie words and \(N(w)\to\infty\) with word length.

Fix \(r\). Only finitely many factors satisfy
\[
N(w)-1\le r,
\]
because \(\Omega S^{N(w)}\) is \((N(w)-2)\)-connected. Let
\[
Y_r=\prod_{N(w)\le r+1}\Omega S^{N(w)},
\qquad
Z_r=\prod_{N(w)>r+1}'\Omega S^{N(w)}.
\]
Then
\[
\Omega K\simeq Y_r\times Z_r,
\qquad
P_rZ_r\simeq*.
\]
Moreover
\[
Y_r\simeq\Omega K_r,
\qquad
K_r=\prod_{N(w)\le r+1}S^{N(w)}.
\]
The finite complex \(K_r\) is simply connected and rationally elliptic. The McGibbon--Møller loop-space rigidity theorem, together with the rational-elliptic extension recorded by Félix--Thomas, gives
\[
SNT(Y_r)=*.
\]
Since \(Y_r\) is a 1-connected H-space of finite type, McGibbon--Møller's automorphism criterion implies that
\[
\operatorname{Aut}(Y_r)\to\operatorname{Aut}(P_rY_r)
\]
has finite-index image. Apply Theorem 2.1. ∎

### Consequence
The previously proposed first hyperbolic test
\[
\Omega(S^3\vee S^4)
\]
is already rigid:
\[
\boxed{SNT(\Omega(S^3\vee S^4))=*.}
\]

---

## 4. Rational classification of two-cell complexes

Let
\[
Z_\alpha=S^m\cup_\alpha e^n,
\qquad m\ge3,
\qquad n>m.
\]

### Adjacent-cell case \(n=m+1\)
Then \(\alpha:S^m\to S^m\) has degree \(d\).

- If \(d\ne0\), \(Z_\alpha\) is rationally contractible, hence rationally elliptic.
- If \(d=0\), \(Z_\alpha\simeq S^m\vee S^{m+1}\), handled by Theorem 3.1.

Thus every adjacent-cell case is loop-SNT rigid.

### Higher attachment \(n\ge m+2\)
The rational homotopy of a sphere implies that
\[
\pi_{n-1}(S^m)\otimes\mathbb Q\ne0
\]
with \(n-1>m\) only when \(m\) is even and \(n=2m\).

- If \(m\) is even, \(n=2m\), and \(\alpha_\mathbb Q\ne0\), the cofiber is rationally of truncated-polynomial type (generalized \(\mathbb CP^2\) type), hence rationally elliptic; therefore \(SNT(\Omega Z_\alpha)=*\).
- Otherwise \(\alpha_\mathbb Q=0\), and
  \[
  (Z_\alpha)_\mathbb Q\simeq S^m_\mathbb Q\vee S^n_\mathbb Q,
  \]
  which is rationally hyperbolic.
- If in this latter branch \(\alpha=0\) integrally, Theorem 3.1 again gives rigidity.

Therefore the only branch not covered by the preceding results is
\[
\boxed{
0\ne\alpha\in\pi_{n-1}(S^m),
\qquad
\alpha\otimes\mathbb Q=0,
\qquad
n\ge m+2.
}
\]
Equivalently: the genuinely remaining two-cell problem is the nonzero torsion-attaching branch.

---

## 5. First torsion-attaching core

The smallest clean case is
\[
m=3,\qquad n=5,
\qquad
\alpha=\eta_3\in\pi_4(S^3)\cong\mathbb Z/2.
\]
Then
\[
Z_\eta=S^3\cup_{\eta_3}e^5\simeq\Sigma\mathbb CP^2.
\]
Hence the new core problem is
\[
\boxed{
SNT(\Omega\Sigma\mathbb CP^2)=*\ ?
}
\]

McGibbon--Møller's H-space criterion turns this into
\[
\boxed{
[\operatorname{Aut}(P_rX):
\operatorname{Im}(\operatorname{Aut}X\to\operatorname{Aut}(P_rX))]
<\infty
\quad\forall r,
}
\]
for \(X=\Omega\Sigma\mathbb CP^2\).

---

## 6. First Postnikov calculation for the core case

From the cofibration
\[
S^4\xrightarrow{\eta_3}S^3\to\Sigma\mathbb CP^2\to S^5
\]
and the low homotopy groups of spheres,
\[
\pi_3(\Sigma\mathbb CP^2)\cong\mathbb Z,
\qquad
\pi_4(\Sigma\mathbb CP^2)=0,
\qquad
\pi_5(\Sigma\mathbb CP^2)\cong\mathbb Z.
\]
Thus for \(X=\Omega\Sigma\mathbb CP^2\),
\[
\pi_2X\cong\mathbb Z,
\qquad
\pi_3X=0,
\qquad
\pi_4X\cong\mathbb Z.
\]
The first possible \(k\)-invariant lies in
\[
H^5(K(\mathbb Z,2);\mathbb Z)=0,
\]
so
\[
\boxed{
P_4X\simeq K(\mathbb Z,2)\times K(\mathbb Z,4).
}
\]
Consequently
\[
\operatorname{Aut}(P_4X)
\cong
\mathbb Z\rtimes(C_2\times C_2)
\]
(up to the evident sign action), where the \(\mathbb Z\)-coordinate is the shear
\[
(u,v)\longmapsto(\pm u,\pm v+c\,u^2).
\]

The first concrete lifting question is therefore:

> Which integers \(c\) occur as the shear coordinate of a self-equivalence of \(\Omega\Sigma\mathbb CP^2\), and how does the allowable subgroup of \(\mathbb Z\) shrink as one asks for lifting through higher Postnikov stages?

If the allowable shear subgroups stabilize, the SNT tower is Mittag--Leffler. If they form a strictly decreasing divisibility tower, SNT is nontrivial (and, by countability, uncountable).

---

## 7. Current status

### Proved/reduced

1. Wilkerson/Mittag--Leffler reduction.
2. Finite-factor criterion.
3. Loop-space SNT rigidity for every finite wedge of spheres of dimensions at least 3.
4. Complete reduction of the two-cell problem to nonzero torsion attaching maps.
5. Identification of \(\Omega\Sigma\mathbb CP^2\) as the first clean torsion-attaching core.
6. The first nontrivial Postnikov automorphism problem is an integral shear-lifting problem at \(P_4\).

### Still open in this project

The full tower
\[
\operatorname{Aut}(P_r\Omega\Sigma\mathbb CP^2)
\]
and the stabilization of its image in \(\operatorname{Aut}(P_4X)\).

The next attack should be 2-primary: the attaching map \(\eta_3\) is 2-torsion, while away from 2 the two-cell complex splits locally as a wedge.  One must nevertheless not infer global SNT from primewise splitting without an additional local-to-global theorem, because SNT is not naively local.
