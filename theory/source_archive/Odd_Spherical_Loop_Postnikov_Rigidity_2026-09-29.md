# Same-n-Type Rigidity for Loop Spaces of Finite Wedges of Odd Spheres

**Date:** 2026-09-29  
**Status:** theorem draft; proof complete modulo standard Hilton–Milnor and McGibbon–Møller inputs; targeted novelty search performed, not an exhaustive priority certification.

## 1. Main theorem

Let
\[
W=\bigvee_{i=1}^r S^{2d_i+1},\qquad d_i\ge 1,
\]
be a finite wedge of simply connected odd-dimensional spheres. Then
\[
\boxed{\operatorname{SNT}(\Omega W)=\{[\Omega W]\}.}
\]
Equivalently, if a connected CW-space \(Y\) satisfies
\[
P_nY\simeq P_n\Omega W\qquad\text{for every }n,
\]
then
\[
Y\simeq\Omega W.
\]

A localized version holds as well: for a set of primes \(P\),
\[
\boxed{\operatorname{SNT}(\Omega W_P)=*.}
\]
using the standard localized Hilton–Milnor decomposition for nilpotent spaces.

## 2. Classical inputs

We use two results of McGibbon–Møller (Topology 31 (1992), 177–201).

### MM criterion
If \(X\) is a 1-connected rational H-space (their \(H_0\)-space) of finite type, then
\[
\operatorname{SNT}(X)=*
\]
if and only if, for every \(n\),
\[
\operatorname{im}\bigl(\operatorname{Aut}(X)\to\operatorname{Aut}(P_nX)\bigr)
\]
has finite index in \(\operatorname{Aut}(P_nX)\).

### MM finite rational-H delooping theorem
If \(K\) is a 1-connected finite CW complex which is a rational H-space, then
\[
\operatorname{SNT}(\Omega K_P)=*
\]
for every set of primes \(P\).

McGibbon–Møller then conjectured that \(\operatorname{SNT}(\Omega K)=*\) for every 1-connected finite CW complex \(K\).

We also use the classical Hilton–Milnor decomposition. If
\[
W=\bigvee_i \Sigma X_i,
\]
then
\[
\Omega W\simeq \prod_{w\in\mathcal B}'\Omega\Sigma w(X_1,\ldots,X_r),
\]
where \(\mathcal B\) is a Hall/basic-word basis and the product has weak topology with respect to finite subproducts.

For \(X_i=S^{2d_i}\), every factor is an odd sphere:
\[
\Sigma w(X_1,\ldots,X_r)\simeq S^{N(w)},
\qquad
N(w)=1+\sum_i m_i(w)\,2d_i,
\]
so \(N(w)\) is odd.

## 3. Finite-visibility rigidity lemma

### Lemma 3.1
Let \(X\) be a 1-connected \(H_0\)-space of finite type. Assume that for every \(n\) there is a homotopy splitting
\[
X\simeq Y_n\times Z_n
\]
such that
\[
P_nZ_n\simeq *
\]
and
\[
\operatorname{im}\bigl(\operatorname{Aut}(Y_n)\to\operatorname{Aut}(P_nY_n)\bigr)
\]
has finite index. Then
\[
\operatorname{SNT}(X)=*.
\]

### Proof
The splitting gives
\[
P_nX\simeq P_nY_n.
\]
Every \(f\in\operatorname{Aut}(Y_n)\) extends to
\[
f\times\operatorname{id}_{Z_n}\in\operatorname{Aut}(X).
\]
Hence, under the identification \(P_nX\simeq P_nY_n\),
\[
\operatorname{im}\bigl(\operatorname{Aut}(Y_n)\to\operatorname{Aut}(P_nY_n)\bigr)
\subseteq
\operatorname{im}\bigl(\operatorname{Aut}(X)\to\operatorname{Aut}(P_nX)\bigr).
\]
The latter therefore also has finite index for every \(n\). McGibbon–Møller's criterion implies \(\operatorname{SNT}(X)=*\). \(\square\)

## 4. Proof of the main theorem

Set
\[
X=\Omega W.
\]
By Hilton–Milnor,
\[
X\simeq \prod_{w\in\mathcal B}'\Omega S^{N(w)},
\]
with every \(N(w)\) odd.

Fix \(n\). There are only finitely many basic words with
\[
N(w)\le n+1,
\]
because the alphabet is finite and every letter has strictly positive weight \(2d_i\).

Let
\[
\mathcal B_{\le n}=\{w:N(w)\le n+1\}.
\]
Write
\[
Y_n=\prod_{w\in\mathcal B_{\le n}}\Omega S^{N(w)},
\qquad
Z_n=\prod_{w\notin\mathcal B_{\le n}}'\Omega S^{N(w)}.
\]
Since a weak product splits off any finite set of factors,
\[
X\simeq Y_n\times Z_n.
\]

For every factor in \(Z_n\),
\[
N(w)\ge n+2,
\]
so \(\Omega S^{N(w)}\) is at least \(n\)-connected. Therefore
\[
P_nZ_n\simeq *
\]
and
\[
P_nX\simeq P_nY_n.
\]

Now define the finite complex
\[
K_n=\prod_{w\in\mathcal B_{\le n}}S^{N(w)}.
\]
It is a finite product of odd-dimensional spheres, hence is 1-connected and a rational H-space. Moreover
\[
Y_n\simeq\Omega K_n.
\]
By McGibbon–Møller's finite rational-H delooping theorem,
\[
\operatorname{SNT}(Y_n)=*.
\]
Applying their finite-index criterion to \(Y_n\), the image
\[
\operatorname{Aut}(Y_n)\to\operatorname{Aut}(P_nY_n)
\]
has finite index.

Thus Lemma 3.1 applies to \(X\), proving
\[
\boxed{\operatorname{SNT}(\Omega W)=*.}
\]
\(\square\)

## 5. Why this is outside the old Theorem 5

If \(r\ge2\), the finite wedge
\[
W=\bigvee_{i=1}^r S^{2d_i+1}
\]
is not, in general, a rational H-space. Indeed its rational cohomology has zero products between distinct positive-degree generators, whereas the rational cohomology algebra of a connected finite rational H-space is a free graded-commutative Hopf algebra; for two or more odd generators this contains nonzero exterior products.

Thus the main theorem is not obtained simply by substituting \(K=W\) into McGibbon–Møller Theorem 5. The proof instead uses a new finite-visibility step: each fixed Postnikov stage sees only finitely many Hilton–Milnor factors, and those visible factors jointly deloop to a finite rational H-space.

## 6. Torsion two-cell corollary

Let
\[
K_\alpha=S^{2a+1}\cup_\alpha e^{2b+1}
\]
where \(\alpha\) has finite order \(N\). If a prime \(p\nmid N\), then
\[
(K_\alpha)_{(p)}\simeq S^{2a+1}_{(p)}\vee S^{2b+1}_{(p)}.
\]
The localized version of the main theorem therefore gives
\[
\boxed{\operatorname{SNT}(\Omega(K_\alpha)_{(p)})=*.}
\]
for every \(p\nmid N\).

Hence all possible local non-rigidity is supported at primes dividing the attaching-map order.

### Example: \(\Sigma\mathbb{CP}^2\)
Since
\[
\Sigma\mathbb{CP}^2\simeq S^3\cup_{\eta_3}e^5,
\qquad |\eta_3|=2,
\]
we obtain
\[
\boxed{
\operatorname{SNT}\bigl(\Omega(\Sigma\mathbb{CP}^2)_{(p)}\bigr)=*
\quad(p\text{ odd}).
}
\]
Thus the first torsion two-cell case reduces completely to its 2-primary Postnikov automorphism tower.

This does not by itself imply integral rigidity: SNT is not a naive product of its localizations.

## 7. Novelty boundary

Classical ingredients:
- Hilton–Milnor decomposition;
- Wilkerson's \(\lim^1\) classification of SNT;
- McGibbon–Møller finite-index criterion;
- McGibbon–Møller rigidity for loops on finite rational H-spaces.

Candidate new contribution:
- the finite-visibility rigidity lemma as a systematic reduction principle;
- its application proving SNT-rigidity of loops on arbitrary finite wedges of simply connected odd spheres;
- the resulting prime-support reduction for torsion odd-dimensional two-cell complexes.

A targeted literature search using combinations of “same n-type”, “SNT”, “loop space”, “wedge/bouquet of odd spheres”, and “Hilton–Milnor” did not locate an explicit prior statement of the main theorem. This is not an exhaustive MathSciNet/Zentralblatt priority certification, so novelty should be stated as a candidate pending specialist literature review.

## 8. Relation to Generative Equipment

The theorem is ordinary algebraic topology and does not require Generative Equipment in its statement or proof.

The project contribution was problem selection and reduction:
\[
\text{actual/formal Postnikov frontier}
\to
\text{finite-visibility criterion}
\to
\text{Hilton–Milnor sector}
\to
\text{odd-spherical rigidity theorem}.
\]

The next genuinely hard target is the remaining 2-primary case
\[
\operatorname{SNT}(\Omega\Sigma\mathbb{CP}^2),
\]
where the low Postnikov stage already contains an integral shear direction and higher 2-primary \(k\)-invariants must determine whether that shear tower satisfies Mittag–Leffler.

## References

1. C. A. McGibbon and J. M. Møller, *On spaces with the same n-type for all n*, Topology 31 (1992), 177–201.
2. P. J. Hilton, *On the homotopy groups of the union of spheres*, J. London Math. Soc. 30 (1955), 154–172.
3. J. Milnor, classical generalization of the Hilton decomposition to wedges of suspensions.
4. C. Wilkerson, *Classification of spaces of the same n-type for all n*, Proc. Amer. Math. Soc. 60 (1976), 279–285.
