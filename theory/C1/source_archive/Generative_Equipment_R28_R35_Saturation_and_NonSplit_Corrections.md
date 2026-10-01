# Generative Equipment R28–R35
## Saturated Obstruction, Homogeneous Normalization, and Non-Split Correction Theory

**Date:** 2026-09-29  
**Status:** Candidate Extension Layer v0.4; derived theory only; **Frozen v1.0 unchanged**.  
**Direct inputs:** Frozen v1.0; R16–R27; independent audit of R22 and R27.  

---

# 0. Executive correction

Two earlier derived statements require correction.

1. The R22 ten-edge computation only controls **interval-homogeneous defining systems**.  It does not by itself control all ordinary fourfold Massey defining systems.  The ten-edge representative admits off-interval closed fillers whose quadratic interaction kills the restricted top obstruction.
2. R27 gives a correct obstruction for a **fixed compatible punctured Artin cube**, but a nonzero value for one punctured cube does not imply that the same first-order directions are intrinsically unrealizable after all higher proper-face choices are allowed to vary.

These are instances of one general mistake:

\[
\boxed{
\text{representative obstruction}
\neq
\text{choice-saturated intrinsic obstruction}.}
\]

The repair developed below is to replace single chosen obstruction values by a **resolved/saturated obstruction correspondence**, and to prove exact criteria under which a restricted defining-system model is complete.

---

# 1. R28 — Resolved Saturation Theorem

Let

\[
p:D\to H,\qquad \omega:D\to G,\qquad \nu:N\to G
\]

be spaces / \(\infty\)-groupoids.  Interpret:

- \(H\): external inputs / first-order directions / tuples;
- \(D_h\): **all** admissible defining systems over \(h\);
- \(G\): obstruction-value space;
- \(N\to G\): nullification/filler data.

Define the true solution space

\[
Z:=D\times_G^hN,
\qquad
V:=\operatorname{im}_{-1}(Z\to H).
\tag{1.1}
\]

Let \(j:D_0\to D\) be a restricted model (interval-homogeneous systems, a selected gauge, split supports, etc.), and set

\[
Z_0:=D_0\times_G^hN,
\qquad
V_0:=\operatorname{im}_{-1}(Z_0\to H).
\tag{1.2}
\]

## Theorem R28.1 (Restricted-to-intrinsic transfer)

Always

\[
V_0\subseteq V.
\tag{1.3}
\]

Moreover, the restricted model is **existence-complete** over every \(h\in H\), i.e.

\[
(Z_0)_h\neq\varnothing
\iff
Z_h\neq\varnothing,
\tag{1.4}
\]

if and only if

\[
Z_0\longrightarrow Z
\]

is fiberwise \((-1)\)-connected over \(H\).

### Proof

The inclusion (1.3) follows from functoriality of homotopy pullback.  For fixed \(h\), condition (1.4) says precisely that every nonempty fiber of \(Z\to H\) receives a point from the corresponding fiber of \(Z_0\to H\), which is the definition of fiberwise \((-1)\)-connectedness.  ∎

## Corollary R28.2 (Intrinsic obstruction set)

If \(G\) is group-like and \(N\to G\) is the zero/null locus, define

\[
\mathfrak O(h)
:=
\operatorname{im}\bigl(\pi_0D_h\to\pi_0G\bigr).
\tag{1.5}
\]

Then

\[
\boxed{
h\text{ is realizable}
\iff
0\in\mathfrak O(h).}
\tag{1.6}
\]

A chosen value \(\omega(d)\) is a complete obstruction for \(h\) only when one has separately proved that the relevant choice-saturation does not enlarge the nullifiable locus.

### Interpretation

R28 is the corrected form of the earlier Resolved Coupl doctrine:

\[
\boxed{
\text{input}
\to
\text{full defining-system fiber}
\to
\text{obstruction correspondence}
\to
\text{nullification fiber}.}
\]

A section \(s:H\to D\) may be useful computationally, but \(\omega\circ s\) is not intrinsically decisive unless a saturation/completeness theorem is proved.

---

# 2. R29 — Support-Saturation and Triangular Homogeneous Normalization

Let \(A\) be a DGA over \(\mathbb F_2\), equipped with a finite support grading

\[
A=\bigoplus_{S\subseteq J}A_S,
\qquad
d(A_S)\subseteq A_S,
\qquad
A_SA_T\subseteq A_{S\cup T}.
\tag{2.1}
\]

Fix pairwise disjoint support atoms

\[
J_1,\ldots,J_n\subseteq J
\]

and cocycle inputs

\[
a_i\in A_{J_i}^{q_i}.
\]

For an interval

\[
I=[i,j]\subseteq[1,n],
\qquad \ell(I)=j-i+1,
\]

write

\[
J_I:=\bigcup_{r=i}^jJ_r
\]

and let the defining-entry degree be

\[
r_I:=\sum_{r=i}^jq_r-(\ell(I)-1).
\tag{2.2}
\]

The interval-homogeneous model requires the entry at \(I\) to lie in \(A_{J_I}^{r_I}\).  The ordinary model allows all support components compatible with total degree.

Define the **off-interval complex**

\[
Q_I
:=
\bigoplus_{S\subseteq J,\ S\neq J_I}A_S.
\tag{2.3}
\]

and the **saturation cohomology group**

\[
\operatorname{Sat}_I^{r_I}(A)
:=H^{r_I}(Q_I).
\tag{2.4}
\]

## Lemma R29.1 (Triangular exact perturbation)

Represent an \(n\)-fold defining system as a punctured strictly upper-triangular connection matrix \(M\), with the top-right entry omitted.  Over \(\mathbb F_2\), its curvature is

\[
F(M)=dM+M^2,
\]

and all non-top entries of \(F(M)\) vanish.

Let \(H\) be a degree-zero strictly upper triangular matrix and \(U=1+H\).  Then

\[
M^U=U^{-1}MU+U^{-1}dU
\tag{2.5}
\]

satisfies

\[
F(M^U)=U^{-1}F(M)U.
\tag{2.6}
\]

If \(H\) has only one matrix entry of width \(m\), then all entries of width \(<m\) are unchanged, while the width-\(m\) entry changes by \(dh\) plus no width-\(m\) lower-order term.  Removing the possibly created top-right entry changes the top curvature only by a coboundary.

### Proof

Equation (2.6) is the usual gauge covariance calculation.  Matrix width is additive under multiplication, so commutator terms involving a width-\(m\) matrix entry have width \(>m\).  The top matrix unit is central in the strictly upper-triangular algebra; resetting the omitted top entry therefore alters only the top curvature by its differential. ∎

## Theorem R29.2 (Off-support acyclicity implies homogeneous completeness)

Assume

\[
\boxed{
\operatorname{Sat}_I^{r_I}(A)=0
\quad
\text{for every proper interval }I\subsetneq[1,n]
\text{ with }|I|\ge2.}
\tag{2.7}
\]

Then every ordinary defining system for the fixed inputs is triangular-gauge equivalent, relative to the inputs, to an interval-homogeneous defining system.  The top Massey cohomology class is preserved.

Consequently the ordinary and interval-homogeneous Massey value sets coincide:

\[
\boxed{
\langle\alpha_1,\ldots,\alpha_n\rangle_{\mathrm{ordinary}}
=
\langle\alpha_1,\ldots,\alpha_n\rangle_{\mathrm{interval}}.}
\tag{2.8}
\]

### Proof

Normalize by increasing matrix width.

Assume all entries of smaller width have already been normalized to expected support.  The defining equation for an entry \(M_I\) has right-hand side built only from products of lower-width entries.  By support multiplicativity that right-hand side lies in \(A_{J_I}\).  Therefore the off-support projection of \(M_I\) is a cocycle in \(Q_I^{r_I}\).

By (2.7) it is exact, say equal to \(dh_I\).  Apply Lemma R29.1 with a width-\(|I|\) gauge parameter \(h_I\) to remove it.  This does not alter previously normalized smaller widths.  Repeating over all intervals of that width and then increasing width produces an interval-homogeneous defining system.

The gauge calculation shows that the omitted top-right curvature changes only by a coboundary, hence its cohomology class is unchanged.  Every homogeneous system is already ordinary, so (2.8) follows. ∎

## Definition R29.3 (Saturation defect rank)

When the groups are finite-dimensional, define

\[
\operatorname{SatRank}
:=
\sum_{I\subsetneq[1,n],\ |I|\ge2}
\dim\operatorname{Sat}_I^{r_I}(A).
\tag{2.9}
\]

This is **not** itself the final indeterminacy: nonzero saturation directions can interact nonlinearly.  But

\[
\operatorname{SatRank}=0
\]

is an exact sufficient criterion for restricted support calculations to be complete.

---

# 3. R30 — Saturated Hochster–Maurer–Cartan System

Now specialize to support-minimal degree-three inputs in a moment-angle DGA.  Thus

\[
|J_i|=2,
\qquad
\alpha_i\in H^3(\mathcal Z_K),
\]

and each input corresponds to a nonzero class in

\[
\widetilde H^0(K_{J_i}).
\]

For an interval \(I\) of length \(\ell\), the defining entry has total DGA degree

\[
r_I=3\ell-(\ell-1)=2\ell+1.
\tag{3.1}
\]

The Hochster multigrading gives, on support \(S\subseteq J\),

\[
A_S^{2\ell+1}
\cong
\widetilde C^{\,2\ell-|S|}(K_S)
\tag{3.2}
\]

(up to the standard Hochster/Baskakov identification).

Hence a **fully saturated** defining entry is

\[
a_I
=
\sum_{S\subseteq J}
a_{I,S},
\qquad
 a_{I,S}\in
\widetilde C^{\,2\ell-|S|}(K_S).
\tag{3.3}
\]

Only supports with \(|S|\le2\ell\) contribute for nonempty induced complexes.

## Theorem R30.1 (Exact saturated support equations)

The ordinary support-minimal Massey defining problem is equivalent to the finite multigraded Maurer–Cartan system obtained by substituting (3.3) into the defining equations and reading each support component separately.

The interval-homogeneous graph model is exactly the sub-system

\[
S=J_I,
\qquad |S|=2\ell,
\qquad
\widetilde C^0(K_{J_I}).
\tag{3.4}
\]

All other \((I,S)\) components are **saturation modes** omitted by the graph-only interval model.

### Consequence

The ordinary problem is generally **not** one-skeleton determined.  Smaller support components in (3.3) live in positive simplicial degree and can depend on higher-dimensional faces.

## Corollary R30.2 (Moment-angle saturation-vanishing criterion)

If for every proper interval \(I\) of length \(\ell\) and every \(S\neq J_I\),

\[
\boxed{
\widetilde H^{\,2\ell-|S|}(K_S;\Bbbk)=0,}
\tag{3.5}
\]

then the ordinary and interval-homogeneous Massey value sets coincide.

This is the precise hypothesis missing from the old R22 extrapolation.

---

# 4. R30B — Fourfold Saturation Variation Formula and the R22 diagnosis

Let a fourfold defining system over \(\mathbb F_2\) be

\[
(b_{12},b_{23},b_{34};c_{123},c_{234})
\]

with

\[
\begin{aligned}
db_{12}&=a_1a_2,\\
db_{23}&=a_2a_3,\\
db_{34}&=a_3a_4,\\
dc_{123}&=a_1b_{23}+b_{12}a_3,\\
dc_{234}&=a_2b_{34}+b_{23}a_4.
\end{aligned}
\tag{4.1}
\]

Its top curvature is

\[
\Omega
=a_1c_{234}+b_{12}b_{34}+c_{123}a_4.
\tag{4.2}
\]

Let

\[
b'_{ij}=b_{ij}+z_{ij},
\qquad dz_{ij}=0,
\]

and choose \(y_{123},y_{234}\) satisfying

\[
\begin{aligned}
dy_{123}&=a_1z_{23}+z_{12}a_3,\\
dy_{234}&=a_2z_{34}+z_{23}a_4.
\end{aligned}
\tag{4.3}
\]

Set

\[
c'_{123}=c_{123}+y_{123},
\qquad
c'_{234}=c_{234}+y_{234}.
\]

## Theorem R30.3 (Fourfold saturation variation)

The top curvature changes by

\[
\boxed{
\Delta\Omega
=
 a_1y_{234}
 +z_{12}b_{34}
 +b_{12}z_{34}
 +z_{12}z_{34}
 +y_{123}a_4.}
\tag{4.4}
\]

### Proof

Expand

\[
\Omega'-\Omega
=
a_1y_{234}
+(b_{12}+z_{12})(b_{34}+z_{34})-b_{12}b_{34}
+y_{123}a_4
\]

and use characteristic two. ∎

### Pure quadratic saturation

If

\[
z_{23}=0,
\qquad
z_{12}a_3=0,
\qquad
a_2z_{34}=0,
\]

we may take \(y_{123}=y_{234}=0\).  If in addition

\[
z_{12}b_{34}=0,
\qquad
b_{12}z_{34}=0,
\]

then

\[
\boxed{
\Delta\Omega=z_{12}z_{34}.}
\tag{4.5}
\]

This is exactly the mechanism in the audited R22 ten-edge graph: the two off-interval degree-five classes \(z\) and \(t\) satisfy

\[
zt=\Omega,
\]

so the restricted nonzero obstruction is killed in the ordinary defining space.

Thus the old R22 statement must be replaced by:

> **R22-restricted:** the ten-edge pattern is extremal for the interval-homogeneous graph MC system.  It is not an ordinary fourfold Massey nontriviality certificate.

---

# 5. R31 — Intrinsic First-Order Direction Obstruction for a 3-Cube

Let \(L\) be a DGLA over a characteristic-zero field and consider

\[
B_3=k[\varepsilon_1,\varepsilon_2,\varepsilon_3]/(\varepsilon_i^2).
\]

Fix closed first-order directions

\[
v_1,v_2,v_3\in Z^1(L).
\]

Assume the pair equations are solvable, i.e. choose

\[
x_{ij}\in L^1
\]

with

\[
dx_{ij}+[v_i,v_j]=0.
\tag{5.1}
\]

Define the cubic full-support curvature

\[
\Omega_3
:=[v_1,x_{23}]+[v_2,x_{13}]+[v_3,x_{12}]
\in Z^2(L).
\tag{5.2}
\]

For \([v]\in H^1(L)\), the induced bracket gives

\[
\operatorname{ad}_{[v]}:H^1(L)\to H^2(L).
\]

Set

\[
I(v_1,v_2,v_3)
:=
\operatorname{ad}_{[v_1]}H^1(L)
+
\operatorname{ad}_{[v_2]}H^1(L)
+
\operatorname{ad}_{[v_3]}H^1(L).
\tag{5.3}
\]

## Theorem R31.1 (Choice-independent cubic direction obstruction)

The class

\[
\boxed{
\bar o_3(v_1,v_2,v_3)
:=[\Omega_3]
\in
H^2(L)/I(v_1,v_2,v_3)}
\tag{5.4}
\]

is independent of the chosen pair fillers \(x_{ij}\).

Moreover,

\[
\boxed{
\bar o_3(v_1,v_2,v_3)=0
\iff
\text{there exists a full MC element over }B_3
\text{ with singleton coefficients }v_i.}
\tag{5.5}
\]

### Proof

Any two choices of pair fillers differ by cycles:

\[
x'_{ij}=x_{ij}+z_{ij},
\qquad dz_{ij}=0.
\]

Then

\[
[\Omega'_3]-[\Omega_3]
=
[v_1,z_{23}]+[v_2,z_{13}]+[v_3,z_{12}],
\]

which lies in \(I(v_1,v_2,v_3)\).  Exact changes of \(z_{ij}\) give exact changes of the brackets because \(d\) is a derivation, so (5.4) is well-defined.

If a full MC element exists, its pair coefficients differ from the chosen \(x_{ij}\) by cycles and its top coefficient makes the corresponding \(\Omega_3\) exact, so (5.4) vanishes.

Conversely, if (5.4) vanishes, choose cycle representatives \(z_{ij}\) whose bracket contribution cancels \([\Omega_3]\).  Replacing \(x_{ij}\) by \(x_{ij}+z_{ij}\) makes the new top curvature exact; choose \(x_{123}\in L^1\) with

\[
dx_{123}+\Omega'_3=0.
\]

This gives a full MC element. ∎

## Significance

R31 is the corrected direction-level version of R27 in the first nontrivial case.  A single chosen \([\Omega_3]\in H^2\) is not intrinsic; the intrinsic class is the quotient class (5.4).

---

# 6. R32 — The 2+2 Nonlinear Saturation Threshold

Consider a DGLA Boolean cube with fixed singleton coefficients \(v_i\) and proper coefficients \(x_S\in L^1\).  The support equations have the form

\[
dx_S
+
\frac12
\sum_{A\sqcup B=S}[x_A,x_B]
=0.
\tag{6.1}
\]

For \(|S|=3\), the top obstruction contains only \(1+2\) partitions:

\[
\Omega_3
=
[v_1,x_{23}]+[v_2,x_{13}]+[v_3,x_{12}],
\]

so the dependence on pair-filler variations is affine-linear.  This is why R31 collapses to a quotient group.

For \(|S|=4\), the top obstruction is

\[
\begin{aligned}
\Omega_4={}&
[v_1,x_{234}]+[v_2,x_{134}]+[v_3,x_{124}]+[v_4,x_{123}]\\
&+[x_{12},x_{34}]+[x_{13},x_{24}]+[x_{14},x_{23}].
\end{aligned}
\tag{6.2}
\]

Let pair fillers vary by cycles \(z_{ij}\), and let triple fillers vary by \(y_{ijk}\) so that the proper equations remain satisfied.

## Theorem R32.1 (First nonlinear indeterminacy)

The variation of the 4-support obstruction contains the unavoidable quadratic terms

\[
\boxed{
[z_{12},z_{34}]
+[z_{13},z_{24}]
+[z_{14},z_{23}].}
\tag{6.3}
\]

No analogous quadratic filler-variation term can occur at arity \(3\).

Hence, for quadratic Maurer–Cartan theories,

\[
\boxed{
4\text{ is the first arity at which saturation indeterminacy can be intrinsically nonlinear}.}
\tag{6.4}
\]

### Proof

For three labels there is no partition into two nonsingleton proper blocks.  Every contribution to top support therefore pairs one fixed singleton with one pair filler, so varying the fillers is linear.

For four labels the partitions

\[
12|34,\qquad13|24,\qquad14|23
\]

occur in (6.2).  Substituting \(x_{ij}+z_{ij}\) produces the three quadratic terms (6.3). ∎

## Cross-sector interpretation

The R22 counterexample is the associative-DGA analogue of (6.3):

\[
z_{12}z_{34}
\]

is the first nonlinear saturation term.  Thus the same **2+2 partition mechanism** appears in ordinary Massey and deformation MC problems.

---

# 7. R33 — Non-Split Small-Extension Correction Formula

Let \(L\) be a DGLA over a characteristic-zero field.  Let

\[
0\longrightarrow I
\longrightarrow B'
\xrightarrow{\pi}B
\longrightarrow0
\tag{7.1}
\]

be a small extension of local Artin algebras, meaning

\[
\mathfrak m_{B'}I=0.
\tag{7.2}
\]

Let

\[
x\in MC(L\otimes\mathfrak m_B).
\]

Choose a \(k\)-linear section

\[
s:\mathfrak m_B\to\mathfrak m_{B'}
\]

of \(\pi\), not assumed multiplicative.  Its multiplicative defect is

\[
\mu_s(b,c)
:=s(b)s(c)-s(bc)
\in I.
\tag{7.3}
\]

Write

\[
x=\sum_a x_a\otimes b_a
\]

and define the linear lift

\[
\widetilde x_s:=\sum_a x_a\otimes s(b_a).
\]

## Theorem R33.1 (Section-defect curvature formula)

The curvature of the lifted element lies in \(L^2\otimes I\) and is

\[
\boxed{
F(\widetilde x_s)
=
\frac12
\sum_{a,b}
[x_a,x_b]
\otimes
\mu_s(b_a,b_b).}
\tag{7.4}
\]

It is \(d\)-closed, and its class

\[
\boxed{
o_{B'/B}(x)
:=[F(\widetilde x_s)]
\in H^2(L)\otimes I}
\tag{7.5}
\]

is independent of the linear section and of the chosen lift.

Moreover,

\[
\boxed{
o_{B'/B}(x)=0
\iff
x\text{ lifts to }MC(L\otimes\mathfrak m_{B'}).}
\tag{7.6}
\]

### Proof

Because \(x\) is Maurer–Cartan in \(B\), applying \(s\) linearly to

\[
dx+\frac12[x,x]=0
\]

and subtracting from the actual curvature of \(\widetilde x_s\) gives exactly (7.4).

The curvature is \(I\)-valued.  The Bianchi identity gives

\[
dF(\widetilde x_s)+[\widetilde x_s,F(\widetilde x_s)]=0.
\]

The bracket term vanishes by \(\mathfrak m_{B'}I=0\), hence the curvature is closed.

Any other lift is \(\widetilde x_s+\eta\) with \(\eta\in L^1\otimes I\).  Again (7.2) kills all bracket terms involving \(\eta\), so

\[
F(\widetilde x_s+\eta)
=F(\widetilde x_s)+d\eta.
\]

Thus (7.5) is independent of choices and vanishes exactly when a correction \(\eta\) makes the curvature zero. ∎

## Theorem R33.3 (Full $L_\infty$ small-extension correction)

The preceding theorem extends without changing the logic to a complete nilpotent $L_\infty$-algebra $L$ with brackets $\ell_r$ of cohomological degree $2-r$.  For a linear section $s$ define the $r$-fold multiplicative defect

\[
\mu_s^{(r)}(b_1,\ldots,b_r)
:=
\prod_{j=1}^r s(b_j)-s\left(\prod_{j=1}^r b_j\right)
\in I.
\tag{7.7}
\]

If

\[
x=\sum_a x_a\otimes b_a
\in MC(L\widehat\otimes\mathfrak m_B),
\]

then the curvature of its linear lift is

\[
\boxed{
\mathcal F(\widetilde x_s)
=
\sum_{r\ge2}\frac1{r!}
\sum_{a_1,\ldots,a_r}
\ell_r(x_{a_1},\ldots,x_{a_r})
\otimes
\mu_s^{(r)}(b_{a_1},\ldots,b_{a_r}).}
\tag{7.8}
\]

It is $\ell_1$-closed, its class in $H^2(L)\otimes I$ is independent of $s$ and of the lift, and it vanishes if and only if the Maurer--Cartan element lifts to $B'$.

### Proof

Subtract the linear-section image of the Maurer--Cartan equation in $B$ from the actual curvature in $B'$.  The difference in each $r$-ary coefficient is exactly $\mu_s^{(r)}$, giving (7.8).  The $L_\infty$ Bianchi identity has terms with one curvature input and further inputs from $\widetilde x_s$; every such coefficient contains $I\mathfrak m_{B'}$ and vanishes, so only $\ell_1\mathcal F=0$ remains.  If the lift is changed by $\eta\in L^1\otimes I$, every nonlinear term containing $\eta$ has coefficient in $I\mathfrak m_{B'}$ or $I^2$ and vanishes; therefore the curvature changes only by $\ell_1\eta$.  The vanishing criterion follows. ∎

This closes the first $L_\infty$ non-split extension left open after R27: higher brackets do not create a new logical obstruction, but they couple to the corresponding higher multiplicative defects of the chosen linear section.

## Corollary R33.2 (Split case)

If the extension admits a multiplicative section, then

\[
\mu_s=0,
\qquad
o_{B'/B}(x)=0
\]

for every MC element \(x\).  Thus R26 is exactly the zero-correction split case.

## Interpretation

The non-split correction asked for after R27 is therefore explicit:

\[
\boxed{
\text{non-split Artin correction}
=
\text{quadratic MC bracket contracted with the multiplication defect }\mu_s.}
\]

This is a specialization of standard small-extension obstruction theory; the useful new project-level point is that it identifies the correction term relative to the previous split-support theorem.

---

# 8. R34 — Amalgamated Central-Lift Correction and Dwyer Application

Let

\[
G=G_1\amalg_H G_2
\tag{8.1}
\]

be a proper amalgamated free product in groups or pro-\(p\) groups.  Let

\[
1\longrightarrow A
\longrightarrow Q
\xrightarrow{\pi}\bar Q
\longrightarrow1
\tag{8.2}
\]

be a central extension, with \(A\) written additively.  Fix

\[
\bar\rho:G\to\bar Q
\]

and suppose both restrictions admit lifts

\[
\rho_i:G_i\to Q.
\]

On the overlap define

\[
\delta(h)
:=
ho_1(h)\rho_2(h)^{-1}\in A.
\tag{8.3}
\]

## Theorem R34.1 (Amalgamation mismatch class)

The map \(\delta:H\to A\) is a (continuous, in the pro-\(p\) case) homomorphism.  Changing the local lifts changes \(\delta\) by

\[
\delta
\mapsto
\delta+
\operatorname{res}_H^{G_1}\chi_1
-
\operatorname{res}_H^{G_2}\chi_2,
\]

where \(\chi_i\in H^1(G_i;A)\).  Hence the class

\[
\boxed{
\eta(\bar\rho)
\in
\frac{H^1(H;A)}
{\operatorname{res}H^1(G_1;A)+\operatorname{res}H^1(G_2;A)}}
\tag{8.4}
\]

is independent of local lift choices.

Furthermore,

\[
\boxed{
\eta(\bar\rho)=0
\iff
\bar\rho\text{ admits a global lift }G\to Q.}
\tag{8.5}
\]

### Proof

Centrality gives

\[
\delta(hk)
=
\rho_1(hk)\rho_2(hk)^{-1}
=
\delta(h)+\delta(k),
\]

so \(\delta\) is a homomorphism.  Two lifts of the same \(\bar\rho|_{G_i}\) differ by an \(A\)-valued character \(\chi_i\), giving the stated transformation rule.

If \(\eta(\bar\rho)=0\), adjust the local lifts by \(\chi_i\) so their restrictions agree on \(H\).  The universal property of the amalgamated product then gives a global homomorphism \(G\to Q\).  The converse follows by restricting any global lift. ∎

## Corollary R34.2 (Mayer–Vietoris transgression)

The usual cohomological Mayer–Vietoris sequence contains

\[
H^1(G_1;A)\oplus H^1(G_2;A)
\to H^1(H;A)
\xrightarrow{\partial}
H^2(G;A)
\to
H^2(G_1;A)\oplus H^2(G_2;A).
\tag{8.6}
\]

The local-lift mismatch class (8.4) transgresses to the global pullback extension obstruction in \(H^2(G;A)\).

Thus the free-product case \(H=1\) has zero overlap correction and recovers R24's factorwise lifting.

## Corollary R34.3 (Amalgamated Dwyer correction)

Take

\[
Q=U_{n+1}(\mathbb F_p),
\qquad
\bar Q=U_{n+1}/Z,
\qquad
A=Z\cong\mathbb F_p.
\]

For a fixed Dwyer defining representation

\[
\bar\rho\in\operatorname{Def}_n(G;\boldsymbol\alpha)
\]

whose restrictions lift on \(G_1,G_2\), the obstruction to a global lift is exactly

\[
\eta_n(\bar\rho)
\in
\frac{H^1(H;\mathbb F_p)}
{\operatorname{res}H^1(G_1;\mathbb F_p)
+
\operatorname{res}H^1(G_2;\mathbb F_p)}.
\tag{8.7}
\]

For the underlying tuple \(\boldsymbol\alpha\), one must still saturate over all admissible defining representations \(\bar\rho\).  Therefore

\[
0\in\langle\boldsymbol\alpha\rangle_G
\]

is equivalent to the existence of a defining representation with vanishing overlap class, not to the vanishing of an arbitrarily chosen representative's class.

---

# 9. R35 — Section-Defect Transgression Schema

R33 and R34 prove the same pattern in two genuinely different settings.

## Proved instance A: Artin extension

A nonmultiplicative linear section produces

\[
\mu_s(b,c)
=s(b)s(c)-s(bc),
\]

and the global obstruction is its contraction with the quadratic MC bracket.

## Proved instance B: amalgamated product

Local lifts produce an overlap mismatch

\[
\delta:H\to A,
\]

and the global obstruction is its Mayer–Vietoris transgression.

These support the following **derived theorem schema**:

\[
\boxed{
\text{chosen local/linear section}
\longrightarrow
\text{section defect cocycle}
\longrightarrow
\text{transgression}
\longrightarrow
\text{global effectivity obstruction}.}
\tag{9.1}
\]

This schema is **not** promoted to a new Frozen-core axiom.  It is a candidate stable derived principle whose abstract hypotheses still need to be formalized.

---

# 10. New conceptual synthesis: Saturation before transgression

The repaired theory now separates two logically different failure modes.

## Layer I — saturation defect

A chosen representative may fail even though another defining system succeeds:

\[
\boxed{
\text{representative failure}
\not\Rightarrow
\text{intrinsic failure}.}
\]

This is what broke R22 and the strong reading of R27.

## Layer II — gluing/transgression defect

Even after all local/defining choices have been saturated, compatible local solutions may fail to glue because the ambient decomposition is non-split:

\[
\boxed{
\text{local effectivity}
\not\Rightarrow
\text{global effectivity}.}
\]

R33 and R34 identify the first non-split correction in two sectors.

Therefore the corrected derived pipeline is

\[
\boxed{
\begin{array}{c}
\text{input / first-order datum}
\\ \Downarrow
\text{full defining-system saturation}
\\ \Downarrow
\text{intrinsic obstruction correspondence}
\\ \Downarrow
\text{local nullification}
\\ \Downarrow
\text{non-split section/overlap defect}
\\ \Downarrow
\text{transgression}
\\ \Downarrow
\text{global effectivity}.
\end{array}}
\tag{10.1}
\]

This is strictly stronger and safer than the old split-support slogan.

---

# 11. Consequences for the old theorem ledger

## Keep

- Frozen v1.0 core.
- R16 Resolved Coupl principle.
- R17/R19/R20 whole-support retract and support-cost results.
- R24 fixed-representation factorization for finite free pro-\(p\) products.
- R26 split Artin support retraction.
- R27 fixed-punctured-boundary obstruction theorem.

## Replace / restrict

- R22 ordinary fourfold Massey nontriviality claim is replaced by the restricted interval-homogeneous statement plus R29–R30 saturation criterion.
- R27's direction-level reading is replaced by the saturated obstruction set; for 3 directions R31 gives an exact quotient class.
- Any tuple-level Galois obstruction in an amalgamated product must saturate over defining representations, even though R34 gives a canonical class for each fixed defining representation.

---

# 12. New research invariants

The repaired theory suggests three derived invariants.

## 12.1 Saturation rank

\[
\operatorname{SatRank}
=
\sum_I\dim H^{r_I}(Q_I).
\]

Zero implies restricted defining systems are complete.

## 12.2 Saturation interaction

At arity four, pair-level saturation classes can interact quadratically:

\[
(z_{12},z_{34})\longmapsto[z_{12}z_{34}]
\]

or in DGLA form

\[
(z_{12},z_{34})\longmapsto[z_{12},z_{34}].
\]

This is the first nonlinear indeterminacy layer.

## 12.3 Section-defect class

For non-split gluing, the first correction is represented either by

\[
[\mu_s]
\]

(algebra extension) or

\[
[\delta]
\]

(overlap gluing), followed by the relevant transgression.

---

# 13. What is now genuinely improved

The project no longer needs to guess the two non-split correction terms proposed after R27:

1. **small Artin extension:** the correction is explicitly (7.4);
2. **amalgamated central lift:** the correction is explicitly (8.4), with global transgression (8.6).

More importantly, the project now has a general safeguard against the R22/R27 quantifier error:

\[
\boxed{
\text{no intrinsic obstruction claim before saturation over all admissible defining choices}.}
\]

This is not a new Frozen-core primitive; it is the correct derived implementation of the existing saturation/gauge discipline.

---

# 14. Next hard problems

After R28–R35, the first genuinely open project-level problems are:

1. **Ordinary extremal fourfold classification.**  Classify support-minimal fourfold moment-angle Massey products using the fully saturated Hochster-MC system, not the interval graph subsystem.
2. **Higher saturation geometry.**  Describe the image
   \[
   \mathfrak O_J(v)\subseteq H^2(L)
   \]
   for \(|J|\ge4\); from R32 it need not be a coset of a subgroup.
3. **Noncentral amalgamation.**  Replace the central overlap class by a genuinely nonabelian torsor/groupoid obstruction.
4. **\(L_\infty\) non-split Artin formula.**  Extend R33 from the DGLA quadratic bracket to all higher brackets via higher multiplicative defects of a linear section.
5. **Complexity under a fixed encoding.**  Only after choosing a concrete finite input model should one ask whether saturation-aware localization outperforms direct obstruction evaluation.

---

# 15. Status

The mathematically defensible status after repair is

\[
\boxed{
\begin{gathered}
\text{Frozen v1.0: unchanged},\\
\text{Candidate Extension Layer v0.4: Saturation / Non-Split Correction},\\
\text{R22 overclaim: repaired},\\
\text{R27 direction-level overclaim: repaired},\\
\text{first non-split corrections: proved in DGLA and central-amalgam sectors}.
\end{gathered}}
\]

No claim of literature-level originality is made for standard gauge invariance, small-extension \(H^2\) obstruction theory, or Mayer–Vietoris transgression.  The project-specific contribution of this package is their integration into an exact saturation-vs-gluing doctrine and the support-normalization criterion that repairs the previous interval-homogeneous extrapolation.
