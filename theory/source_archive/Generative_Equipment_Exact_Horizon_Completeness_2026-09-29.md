# Generative Equipment — Exact Horizon Completeness Theorem
## Relative Horizon Completion, Object/Mapping Recognition, and Sector Engines

**Date:** 2026-09-29  
**Status:** derived theory over Frozen v1.0; resolves the abstract Horizon Completeness Problem.  
**Frozen core:** unchanged.

---

# 0. Executive theorem

Let

\[
C:\mathcal A\to\mathcal F
\]

be an actual/formal comparison. Suppose there are compatible horizon towers

\[
\{\mathcal A_n\}_{n\ge0},
\qquad
\{\mathcal F_n\}_{n\ge0},
\]

with comparison functors

\[
C_n:\mathcal A_n\to\mathcal F_n
\]

and compatible horizon maps from \(\mathcal A,\mathcal F\).

Set

\[
\widehat{\mathcal A}:=\lim_n\mathcal A_n,
\qquad
\widehat{\mathcal F}:=\lim_n\mathcal F_n,
\qquad
\widehat C:=\lim_n C_n.
\]

Let

\[
\alpha:\mathcal A\to\widehat{\mathcal A},
\qquad
\beta:\mathcal F\to\widehat{\mathcal F}
\]

be the canonical horizon maps, with

\[
\beta C\simeq \widehat C\,\alpha.
\]

Define the **relative horizon completion**

\[
\boxed{
\mathcal A_C^{\mathrm{hor}}
:=
\mathcal F\times_{\widehat{\mathcal F}}\widehat{\mathcal A}.
}
\]

There is a canonical comparison

\[
\boxed{
\delta_C:\mathcal A\to\mathcal A_C^{\mathrm{hor}}.
}
\]

The abstract Horizon Completeness Problem is exactly the problem of whether
\(\delta_C\) is an equivalence (for full semantic reconstruction), or whether
its maximal-groupoid fibers are equivalences (for object-level effectivity).

---

# 1. Horizon realization spaces

For \(\xi\in\mathcal F\), define

\[
\operatorname{Eff}_C(\xi)
=
\operatorname{hofib}_{\xi}
\left(
C^\simeq:\mathcal A^\simeq\to\mathcal F^\simeq
\right).
\]

At horizon \(n\), with image \(\xi_n\in\mathcal F_n\), define

\[
\mathcal R_n(\xi)
=
\operatorname{hofib}_{\xi_n}
\left(
C_n^\simeq:
\mathcal A_n^\simeq\to\mathcal F_n^\simeq
\right).
\]

The tower gives

\[
\eta_\xi:
\operatorname{Eff}_C(\xi)
\to
\operatorname*{holim}_n\mathcal R_n(\xi).
\]

---

# 2. Fiber–limit identity

## Theorem HC1 — Horizon Fiber Identity

There is a canonical equivalence

\[
\boxed{
\operatorname*{holim}_n\mathcal R_n(\xi)
\simeq
\operatorname{hofib}_{\beta(\xi)}
\left(
\widehat C^\simeq:
\widehat{\mathcal A}^{\simeq}
\to
\widehat{\mathcal F}^{\simeq}
\right).
}
\]

Equivalently,

\[
\boxed{
\operatorname*{holim}_n\mathcal R_n(\xi)
\simeq
\operatorname{hofib}_{\xi}
\left(
(\mathcal A_C^{\mathrm{hor}})^\simeq
\to
\mathcal F^\simeq
\right).
}
\]

### Proof

The maximal \(\infty\)-groupoid functor

\[
(-)^\simeq:\mathrm{Cat}_\infty\to\mathcal S
\]

is right adjoint to the inclusion of spaces into \(\mathrm{Cat}_\infty\), hence
preserves limits. Therefore

\[
\widehat{\mathcal A}^{\simeq}
\simeq
\lim_n\mathcal A_n^\simeq
\]

and similarly for \(\widehat{\mathcal F}\).

Homotopy fibers are pullbacks in spaces, and limits commute with limits.
Hence

\[
\lim_n
\left(
\mathcal A_n^\simeq
\times_{\mathcal F_n^\simeq}
\{\xi_n\}
\right)
\simeq
\widehat{\mathcal A}^{\simeq}
\times_{\widehat{\mathcal F}^{\simeq}}
\{\beta\xi\}.
\]

The second formula is the pullback definition of
\(\mathcal A_C^{\mathrm{hor}}\). \(\square\)

---

# 3. Exact object-level solution

## Theorem HC2 — Exact Object Horizon Completeness Criterion

For fixed \(\xi\), the map

\[
\eta_\xi:
\operatorname{Eff}_C(\xi)
\to
\operatorname*{holim}_n\mathcal R_n(\xi)
\]

is an equivalence iff the map

\[
\delta_C^\simeq:
\mathcal A^\simeq
\to
(\mathcal A_C^{\mathrm{hor}})^\simeq
\]

is an equivalence on the fiber over \(\xi\).

Consequently, the following are equivalent:

1. \(\eta_\xi\) is an equivalence for every \(\xi\in\mathcal F\);
2. the square of maximal groupoids
   \[
   \begin{CD}
   \mathcal A^\simeq @>>> \widehat{\mathcal A}^{\simeq}\\
   @VVV @VVV\\
   \mathcal F^\simeq @>>> \widehat{\mathcal F}^{\simeq}
   \end{CD}
   \]
   is homotopy cartesian;
3. \(\delta_C^\simeq\) is an equivalence.

This solves **object-level Horizon Completeness** exactly.

### Meaning

There is no extra hidden obstruction beyond relative horizon reconstruction:
the global effectivity fibers are exactly the finite-horizon homotopy limits
iff the actual/formal square is cartesian after passing to cores.

---

# 4. Full semantic solution

Object realization is weaker than semantic reconstruction.

## Theorem HC3 — Strong Horizon Completeness Criterion

The following are equivalent:

1. the square
   \[
   \begin{CD}
   \mathcal A @>{\alpha}>> \widehat{\mathcal A}\\
   @V{C}VV @VV{\widehat C}V\\
   \mathcal F @>{\beta}>> \widehat{\mathcal F}
   \end{CD}
   \]
   is a pullback square in \(\mathrm{Cat}_\infty\);
2. the canonical functor
   \[
   \boxed{
   \delta_C:
   \mathcal A
   \longrightarrow
   \mathcal F\times_{\widehat{\mathcal F}}\widehat{\mathcal A}
   }
   \]
   is an equivalence.

When these conditions hold, every effectivity fiber and every mapping-space
coherence datum are completely reconstructed from the horizon tower.

We call this **strong/semantic horizon completeness**.

---

# 5. Object plus mapping decomposition

The pullback mapping spaces satisfy

\[
\operatorname{Map}_{\mathcal A_C^{\mathrm{hor}}}
(\delta a,\delta b)
\simeq
\operatorname{Map}_{\mathcal F}(Ca,Cb)
\times_{
\operatorname{Map}_{\widehat{\mathcal F}}
(\beta Ca,\beta Cb)
}
\operatorname{Map}_{\widehat{\mathcal A}}
(\alpha a,\alpha b).
\]

Since mapping spaces in limits of \(\infty\)-categories are limits of the
mapping spaces,

\[
\operatorname{Map}_{\widehat{\mathcal A}}
(\alpha a,\alpha b)
\simeq
\operatorname*{holim}_n
\operatorname{Map}_{\mathcal A_n}(a_n,b_n)
\]

and similarly for \(\widehat{\mathcal F}\).

Hence:

## Theorem HC4 — Object/Mapping Recognition

Strong horizon completeness is equivalent to the conjunction of:

### (O) Simultaneous object effectivity

\[
\delta_C
\]

is essentially surjective.

Equivalently, every horizon-compatible actual/formal object has a global
actual representative.

### (M) Mapping/coherence completeness

For every \(a,b\in\mathcal A\),

\[
\boxed{
\operatorname{Map}_{\mathcal A}(a,b)
\simeq
\operatorname{Map}_{\mathcal F}(Ca,Cb)
\times_{
\operatorname*{holim}_n
\operatorname{Map}_{\mathcal F_n}(C_na_n,C_nb_n)
}
\operatorname*{holim}_n
\operatorname{Map}_{\mathcal A_n}(a_n,b_n).
}
\]

Thus the old distinction

\[
\text{simultaneous effectivity}
\quad+\quad
\text{no-phantom mapping reconstruction}
\]

is not accidental: they are precisely essential surjectivity and full
faithfulness of one canonical relative-completion functor.

---

# 6. Relative, not absolute, completeness

A major consequence is that horizon completeness is **relative**.

It is sufficient, but not necessary, that both

\[
\alpha:\mathcal A\to\widehat{\mathcal A}
\]

and

\[
\beta:\mathcal F\to\widehat{\mathcal F}
\]

be equivalences.

Indeed:

## Corollary HC5 — Bilateral Reconstruction

If both \(\alpha\) and \(\beta\) are equivalences, then \(\delta_C\) is an
equivalence and strong horizon completeness holds.

But the converse fails.

For example, if

\[
\mathcal A=\mathcal F,\qquad C=\operatorname{id},
\]

and the two horizon systems are identical, then the comparison square is
cartesian regardless of whether

\[
\mathcal A\to\widehat{\mathcal A}
\]

is itself an equivalence.

Therefore identical horizon blindness on both sides cancels in the relative
effectivity problem.

This is why “both categories are Postnikov complete” is a convenient engine,
not the definition of horizon completeness.

---

# 7. Formal-complete simplification

A particularly important case is when the formal category is *defined* as the
horizon limit:

\[
\mathcal F\simeq\widehat{\mathcal F}.
\]

Then

\[
\mathcal A_C^{\mathrm{hor}}
\simeq
\widehat{\mathcal A},
\]

and

\[
\delta_C\simeq\alpha.
\]

Hence:

## Corollary HC6

If the formal side is horizon-complete, then

\[
\boxed{
\text{strong horizon completeness}
\iff
\mathcal A\to\widehat{\mathcal A}
\text{ is an equivalence}.
}
\]

At object level the analogous statement holds after passing to maximal
groupoids.

Thus whenever Formal is literally the compatible finite-horizon tower, the
entire problem is an **actual-side reconstruction theorem**.

---

# 8. Stable t-structure recognition engine

Let \(\mathcal A,\mathcal F\) be stable \(\infty\)-categories with
left-complete t-structures, and suppose \(C\) is t-exact.

Take

\[
\mathcal A_n=\mathcal A_{\le n},
\qquad
\mathcal F_n=\mathcal F_{\le n}.
\]

Left completeness means precisely that the natural maps to the inverse limits
of truncation categories are equivalences.

Therefore:

## Theorem HC7 — Left-Complete t-Structure Engine

Under these hypotheses,

\[
\boxed{
\mathcal A
\simeq
\lim_n\mathcal A_{\le n},
\qquad
\mathcal F
\simeq
\lim_n\mathcal F_{\le n},
}
\]

and hence the comparison is strongly horizon-complete.

So every effectivity fiber is reconstructed from its truncation tower.

### Boundary

If one drops left completeness, the conclusion is not valid merely from the
existence of all truncations.

---

# 9. Postnikov-complete infinity-topos engine

Let \(\mathcal X\) be an \(\infty\)-topos.  Its Postnikov completion is

\[
\widehat{\mathcal X}
=
\lim_n\tau_{\le n}\mathcal X.
\]

If \(\mathcal X\) is Postnikov complete then

\[
\mathcal X\simeq\widehat{\mathcal X}.
\]

Therefore comparisons between Postnikov-complete \(\infty\)-topoi which
respect the truncation horizons satisfy the bilateral reconstruction engine.

A useful sharp boundary is:

\[
\boxed{
\text{Postnikov complete}
\Longrightarrow
\text{hypercomplete},
}
\]

but the converse need not hold.

So hypercompleteness alone is not enough to invoke HC5.

---

# 10. I-adic completion engine

Let \(A\) be Noetherian, \(I\subset A\), and \(A^\wedge\) the \(I\)-adic
completion.

For finite modules, the formal compatible tower

\[
\{M_n\},
\qquad
M_n=M_{n+1}/I^nM_{n+1},
\]

is recovered by

\[
M=\lim_nM_n,
\]

with

\[
M/I^nM\simeq M_n.
\]

In the affine Noetherian coherent setting, this gives an equivalence between
finite \(A^\wedge\)-modules and compatible finite \(A/I^n\)-module systems.

Thus the actual category is equivalent to its formal horizon category and
HC6 applies.

This supplies a non-topological positive sector of exact horizon completeness.

---

# 11. DHH consequence

Let

\[
\mathcal C=\mathsf{Gra}[W_A^{-1}]
\]

and let

\[
\mathcal F
=
\lim_n\mathcal C_n
\]

be the formal Postnikov category.

Here the formal side is horizon-complete by definition.  Therefore HC6 gives:

\[
\boxed{
\text{Graph horizon completeness}
\iff
\mathcal C
\to
\lim_n\mathcal C_n
\text{ is an equivalence}.
}
\]

By HC4 this splits exactly into:

### Object half

Every compatible formal finite-stage graph/Postnikov object is realized by a
single object of \(\mathcal C\).

This is the **Simultaneous Object Effectivity** problem.

### Mapping half

For all \(G,H\),

\[
\boxed{
\operatorname{Map}_{\mathcal C}(G,H)
\simeq
\operatorname*{holim}_n
\operatorname{Map}_{\mathcal C_n}(q_nG,q_nH).
}
\]

This is precisely the **No-Phantom / Mapping Completeness** problem.

Therefore the two long-standing DHH milestones are exactly the
essential-surjectivity and full-faithfulness halves of the general Horizon
Completeness theorem.

The abstract theory does not prove those graph-specific halves automatically;
it proves that there is no third hidden global condition.

---

# 12. Horizon residue

Define the **horizon residue** of a comparison to be the canonical relative
completion map

\[
\boxed{
\operatorname{HRes}(C)
:=
\delta_C:
\mathcal A\to
\mathcal F\times_{\widehat{\mathcal F}}\widehat{\mathcal A}.
}
\]

Then:

- object-level residue vanishes iff \(\delta_C^\simeq\) is an equivalence;
- semantic residue vanishes iff \(\delta_C\) is an equivalence;
- failure of essential surjectivity is an actualization residue;
- failure of full faithfulness is a phantom/coherence residue.

This is a derived diagnostic, not a new Frozen primitive.

---

# 13. Status of the Horizon Completeness Problem

The abstract problem

\[
\eta_\xi:
\operatorname{EffFib}(\xi)
\to
\operatorname*{holim}_n\mathcal R_n(\xi)
\stackrel{?}{\simeq}
\]

is now solved at the theorem level:

\[
\boxed{
\eta_\xi\text{ is an equivalence}
\iff
\delta_C^\simeq
\text{ is an equivalence on the fiber over }\xi.
}
\]

Uniformly in \(\xi\),

\[
\boxed{
\text{object horizon completeness}
\iff
\begin{CD}
\mathcal A^\simeq @>>> \widehat{\mathcal A}^\simeq\\
@VVV @VVV\\
\mathcal F^\simeq @>>> \widehat{\mathcal F}^\simeq
\end{CD}
\text{ is cartesian}.
}
\]

And at the full semantic level,

\[
\boxed{
\text{semantic horizon completeness}
\iff
\begin{CD}
\mathcal A @>>> \widehat{\mathcal A}\\
@VVV @VVV\\
\mathcal F @>>> \widehat{\mathcal F}
\end{CD}
\text{ is cartesian}.
}
\]

Hence the remaining work in any concrete sector is no longer to discover
what “horizon completeness” means.  It is to prove one of these exact
cartesianness conditions using sector-specific mathematics.

---

# 14. Research consequence

The hierarchy is now:

\[
\boxed{
\text{finite-horizon realizability}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{component ML / coherent branch}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\operatorname*{holim}\mathcal R_n
}
\]

\[
\Downarrow\quad
\text{relative horizon residue } \delta_C
\]

\[
\boxed{
\text{global actual effectivity}.
}
\]

The Milnor \(\lim^1\)-profile controls the internal homotopy type of the
horizon limit.  The new theorem identifies the separate obstruction to
whether that horizon limit is the **correct global effectivity fiber at all**:
it is exactly the relative horizon residue \(\delta_C\).

This resolves the conceptual gap left by the earlier
Coherence-at-Infinity theory.
