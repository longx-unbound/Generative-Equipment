# Generative Equipment — ENDO-3
## Grammar Genesis, Universal Repair, and Defect-Driven Doctrine Dynamics

**Date:** 2026-09-29  
**Status:** ENDO grammar-generation branch v1.0 (relative-complete semantic theory)  
**Logical status:** derived theory over Frozen v1.0; **Frozen v1.0 unchanged**  
**Direct predecessors:** ENDO-1, ENDO-2, R28–R35  
**Scope:** grammar presentations living in a locally presentable category or presentable \(\infty\)-category; small/finitary defect languages; explicit preservation contracts.  
**Not claimed:** a unique grammar determined by a bare mathematical structure, a general effective algorithm, or an automatic ranking of research importance.

---

# 0. Executive result

ENDO-1 made *problems* endogenous relative to a structural signature. ENDO-2 made the *closure dynamics* endogenous relative to a fixed grammar. ENDO-3 addresses the missing layer:

\[
\boxed{\text{When the current grammar itself fails, how is the next grammar generated?}}
\]

The main answer is not “choose a better doctrine”. A genuine intrinsic defect generates a **repair category / repair moduli space**.

For a current grammar \(\Sigma\), an intrinsic defect \(\delta\), and a preservation contract \(K\), let

\[
\operatorname{Rep}_K(\Sigma,\delta)
\]

be the category or \(\infty\)-category of all admissible repairs of \(\delta\) that preserve \(K\).

There are exactly three logical outcomes:

\[
\boxed{
\begin{array}{rcl}
\operatorname{Rep}_K(\Sigma,\delta)\text{ has an initial object}
&\Rightarrow&
\text{universal grammar mutation},\\[1mm]
\operatorname{Rep}_K(\Sigma,\delta)\neq\varnothing
\text{ but has no initial object}
&\Rightarrow&
\text{intrinsic grammar branching},\\[1mm]
\operatorname{Rep}_K(\Sigma,\delta)=\varnothing
&\Rightarrow&
\text{the preservation contract is incompatible with repair.}
\end{array}}
\]

The theory therefore does **not** force a single next grammar when mathematics does not supply one.

Three natural test cases realize the three branches:

1. **Universal repair:** splitting idempotents gives the Karoubi completion.
2. **Branching/no canonical unpointed repair:** a \(\mathbb Q\)-algebra “having some square root of \(2\)” has no initial repair, while adjoining a **chosen** root has the universal repair \(\mathbb Q[t]/(t^2-2)\).
3. **Impossible strict repair:** the tensor-exactness defect for finitely generated abelian groups cannot be repaired while simultaneously preserving all of faithfulness, exactness, the ordinary tensor product, and nonzero torsion objects.

The central positive existence theorem is the **Walking Repair Theorem**:

If a defect occurrence is encoded by

\[
A\xrightarrow{u}B,\qquad A\xrightarrow{a}\Sigma,
\]

then the pushout

\[
\Sigma[u,a]=\Sigma\amalg_A B
\]

is the universal repair **with a chosen witness** for that occurrence.

For a small family of repair schemata in a locally presentable setting, algebraic small-object machinery gives functorial coherent filler-completion; unique/equivalence-type laws are instead handled by orthogonality/localization; missing weighted constructions are handled by free weighted cocompletion.

Finally, if defect generation itself is functorial and monotone, grammar mutation defines a closure operator on the doctrine lattice. Transfinite iteration reaches the least stable doctrine. Thus ENDO-3 closes the loop

\[
\boxed{
\text{structure}
\to
\text{problem}
\to
\text{intrinsic defect}
\to
\text{repair moduli}
\to
\text{grammar mutation}
\to
\text{new structure}.
}
\]

This is a **relative** completeness theorem: completeness is relative to the declared structural signature, defect language, preservation contract, and semantic universe.

---

# 1. Why ENDO-3 is necessary

ENDO-2 has the form

\[
(\mathcal C,\operatorname{Rel},\mathcal O,\mathcal M)
\longrightarrow
\text{generated closure}.
\]

Its main pressure-test boundary is that \(\mathcal O\) itself is fixed in advance.

For example, if ordinary tensor loses exactness after new objects appear, several mathematically legitimate responses exist:

- restrict to flat/projective objects;
- pass to a derived/stable semantics;
- localize away offending objects;
- weaken the preservation contract;
- retain the defect as an obstruction rather than eliminate it.

Therefore

\[
\boxed{
\text{defect alone}
\not\Rightarrow
\text{unique next grammar}.
}
\]

The missing mathematical object is not another scalar invariant. It is the **space of admissible grammar repairs**.

---

# 2. Grammar states

Fix a grammar universe \(\mathbf{Gram}\). In the strongest existence results below, \(\mathbf{Gram}\) is assumed locally presentable; the homotopical analogue uses a presentable \(\infty\)-category.

A grammar state is

\[
\Sigma
=
(G_\Sigma,\mathsf{Sem}_\Sigma,\mathsf{Law}_\Sigma,
K_\Sigma,N_\Sigma^\infty,\operatorname{Prov}_\Sigma),
\]

with:

1. \(G_\Sigma\in\mathbf{Gram}\): the grammar presentation;
2. \(\mathsf{Sem}_\Sigma\): its semantic interpretation;
3. \(\mathsf{Law}_\Sigma\): the currently active law / defect language;
4. \(K_\Sigma\): a preservation contract specifying which old semantics must survive a mutation;
5. \(N_\Sigma^\infty\): observation doctrine;
6. \(\operatorname{Prov}_\Sigma\): provenance.

The repair theory below acts primarily on \(G_\Sigma\), but a repair is admissible only when the semantic and preservation clauses are verified.

## Definition 2.1 — Relative endogeneity

A grammar mutation rule is **relative-endogenous** if:

- it uses only the current grammar state and a predeclared law compiler;
- it is invariant under the declared equivalence notion;
- it does not inspect a desired final theorem or target object;
- it preserves provenance of the defect occurrence;
- it performs R28-style saturation before declaring a defect intrinsic.

ENDO-3 does **not** claim absolute endogeneity from a bare category with no marked structure.

---

# 3. Walking defects

The basic syntax of grammar mutation is an extension problem.

A **walking repair schema** is a morphism

\[
u_\lambda:A_\lambda\longrightarrow B_\lambda
\]

in \(\mathbf{Gram}\).

Interpretation:

- \(A_\lambda\): a minimal incomplete pattern;
- \(B_\lambda\): the same pattern equipped with the desired witness / completion / law.

An occurrence in \(G\) is a map

\[
a:A_\lambda\longrightarrow G.
\]

In an \(\infty\)-categorical grammar universe define its filler space

\[
\operatorname{Fill}_{u_\lambda}(a;G)
=
\operatorname{hofib}_{a}
\left(
\operatorname{Map}(B_\lambda,G)
\to
\operatorname{Map}(A_\lambda,G)
\right).
\]

This distinguishes three law types.

### Existence law

The occurrence is solved if

\[
\operatorname{Fill}_{u_\lambda}(a;G)\neq\varnothing.
\]

### Rigid law

The occurrence is solved if

\[
\operatorname{Fill}_{u_\lambda}(a;G)\simeq *.
\]

### Structured-witness law

The filler itself is retained as part of the semantic data.

The last form is essential whenever different fillers are not canonically equivalent.

---

# 4. Saturation before mutation

A raw representative failure is not automatically a grammar defect.

Suppose an occurrence depends on internal defining choices \(d\in D_h\). ENDO-3 inherits the R28–R35 rule:

\[
\boxed{
\text{No grammar mutation before saturation over all admissible internal choices.}
}
\]

An **intrinsic defect** is a failure that survives the current semantic/gauge saturation.

This prevents the old R22/R27 error from reappearing at the grammar level.

---

# 5. Repair categories and repair moduli

Fix an intrinsic defect \(\delta\) in \(\Sigma\).

A preservation contract \(K\) specifies which mutations are admissible. Typical clauses include:

- the old semantic world embeds fully faithfully;
- specified relations remain valid;
- specified operations are preserved strongly;
- specified objects remain nonzero/distinct;
- observation equivalence is reflected;
- provenance maps commute.

## Definition 5.1 — Pointed repair

For a defect occurrence

\[
A\xrightarrow{u}B,\qquad A\xrightarrow{a}G_\Sigma,
\]

a pointed repair is a pair

\[
(r,b)
\]

with

\[
r:G_\Sigma\to G',
\qquad
b:B\to G',
\]

such that

\[
bu=ra,
\]

and \(r\) satisfies \(K\).

Morphisms of pointed repairs commute with \(r\) and the chosen witness \(b\).

Write

\[
\operatorname{Rep}^{\mathrm{pt}}_K(\Sigma,\delta).
\]

## Definition 5.2 — Unpointed repair

An unpointed repair remembers \(r:G_\Sigma\to G'\) and requires only that an admissible witness exists. The witness is not part of the structure.

Write

\[
\operatorname{Rep}^{\exists}_K(\Sigma,\delta).
\]

These two repair categories can behave very differently.

## Definition 5.3 — Universal repair

A universal repair is an initial object in the relevant repair category.

Its space of choices, when nonempty, is contractible.

---

# 6. The Walking Repair Theorem

## Theorem E3.1 — One-occurrence universal repair

Assume \(\mathbf{Gram}\) has pushouts.

For

\[
A\xrightarrow{u}B,
\qquad
A\xrightarrow{a}G,
\]

form

\[
G[u,a]
=
G\amalg_A B.
\]

Then \(G\to G[u,a]\), with its canonical map \(B\to G[u,a]\), is initial among **unconstrained pointed repairs** of this occurrence.

More precisely, for every \(r:G\to X\),

\[
\operatorname{Map}_{G/\mathbf{Gram}}
(G[u,a],X)
\simeq
\operatorname{Fill}_{u}(ra;X).
\]

### Proof

This is the mapping-space universal property of the pushout:

\[
\operatorname{Map}(G\amalg_A B,X)
\simeq
\operatorname{Map}(G,X)
\times_{\operatorname{Map}(A,X)}
\operatorname{Map}(B,X).
\]

Taking the fiber over \(r\) gives the formula. \(\square\)

## Corollary E3.2 — Preservation-contract version

If the pushout repair lies in the admissible preservation subcategory \(K\), then it is initial in the corresponding \(K\)-admissible pointed repair category.

Thus “minimal repair” is not a numerical optimization. It is a universal property.

---

# 7. Simultaneous repair and independent interchange

Let

\[
\{A_i\xrightarrow{u_i}B_i,\;A_i\xrightarrow{a_i}G\}_{i\in I}
\]

be a set of current defect occurrences.

If \(\mathbf{Gram}\) has the needed coproducts and pushouts, define

\[
G'
=
G
\amalg_{\coprod_i A_i}
\coprod_i B_i.
\]

Then \(G'\) is universal among grammars under \(G\) equipped with chosen fillers for all the **currently listed** occurrences.

If two repair occurrences are already present in the original grammar and neither is generated by the other, the two iterated pushouts canonically agree with the simultaneous pushout.

Hence

\[
\boxed{
\text{independent walking repairs commute up to canonical equivalence.}
}
\]

Newly created occurrences require a further generation stage.

---

# 8. Saturated filler completion

Let

\[
U=\{u_\lambda:A_\lambda\to B_\lambda\}_{\lambda\in\Lambda}
\]

be a small family of walking repair schemata.

A grammar \(G\) is **\(U\)-injective** if every map \(A_\lambda\to G\) extends along \(u_\lambda\).

It is **algebraically \(U\)-injective** if such extensions are chosen coherently as structure.

## Theorem E3.3 — Algebraic filler completion

In a locally presentable grammar universe, a small family \(U\) admits a functorial algebraic filler-completion by accessible algebraic weak-factorization/small-object machinery.

This is the universal repair engine when the law is **existence with retained witness data**.

### Source boundary

This theorem uses standard algebraic small-object / accessible AWFS theory. It is not a new theorem of Generative Equipment.

The project contribution is the identification

\[
\boxed{
\text{grammar defect with witness}
\longleftrightarrow
\text{algebraic injective completion}.
}
\]

---

# 9. Rigid repairs as localization / orthogonality

Existence and uniqueness are different doctrines.

If the law requires

\[
\operatorname{Map}(B,G)
\to
\operatorname{Map}(A,G)
\]

to be an equivalence, the relevant notion is orthogonality rather than mere injectivity.

For a presentable \(\infty\)-category and a small set \(S\) of morphisms, the \(S\)-local objects form an accessible reflective localization under the standard hypotheses.

Thus

\[
\boxed{
\text{equational / equivalence repair}
\longrightarrow
\text{localization repair}.
}
\]

Localization is idempotent, unlike a generic chosen-filler algebraic structure.

---

# 10. Missing-construction repairs

A different defect is not “an equation fails” but “a construction is absent”.

Let \(\Phi\) be a declared class of weights. The free \(\Phi\)-cocompletion

\[
\Phi(\mathcal A)
\]

is universal among \(\Phi\)-cocomplete targets receiving a functor from \(\mathcal A\).

Thus

\[
\boxed{
\text{missing weighted construction}
\longrightarrow
\text{free cocompletion repair}.
}
\]

Cauchy/Karoubi completion is obtained from absolute weights.

---

# 11. The three repair engines

Within the declared ENDO-3 mutation language, the principal semantic repair engines are

\[
\boxed{
\begin{array}{rcl}
\text{chosen existence}
&\rightsquigarrow&
\text{cell attachment / algebraic injectivity},\\[1mm]
\text{unique law / equivalence}
&\rightsquigarrow&
\text{orthogonality / localization},\\[1mm]
\text{missing construction}
&\rightsquigarrow&
\text{free weighted cocompletion}.
\end{array}}
\]

A general grammar repair may combine these.

This table is **not** claimed to classify every possible form of mathematical creativity. It classifies the repair language adopted by ENDO-3.

---

# 12. Deterministic example — splitting idempotents

Let \(E\) be the walking idempotent and \(E'\) the walking split idempotent.

The inclusion

\[
E\hookrightarrow E'
\]

is a walking repair schema.

An occurrence \(E\to\mathcal C\) is an idempotent in \(\mathcal C\).

Saturating these repairs freely produces

\[
\operatorname{Kar}(\mathcal C).
\]

Thus idempotent completion is an ENDO-3 **universal deterministic grammar repair**.

---

# 13. Unpointed existence can destroy universality

Let \(\mathcal R\) be the full category of commutative \(\mathbb Q\)-algebras \(B\) such that

\[
\exists b\in B,\qquad b^2=2.
\]

## Theorem E3.4 — No universal unpointed square-root repair

\(\mathcal R\) is nonempty but has no initial object.

### Proof

Assume \(A\) were initial. Since \(A\in\mathcal R\), choose \(a\in A\) with \(a^2=2\).

Take

\[
B=\mathbb Q[t]/(t^2-2)\cong\mathbb Q(\sqrt2).
\]

Initiality gives a unique \(\mathbb Q\)-algebra map

\[
f:A\to B.
\]

Let

\[
\sigma:B\to B,\qquad t\mapsto -t
\]

be the nontrivial \(\mathbb Q\)-automorphism.

Both \(f\) and \(\sigma f\) are maps \(A\to B\), hence initiality forces

\[
\sigma f=f.
\]

Thus \(f(a)\) lies in the fixed subring \(B^\sigma=\mathbb Q\). But

\[
f(a)^2=2,
\]

and \(\mathbb Q\) has no square root of \(2\), contradiction. \(\square\)

Now retain a chosen root as structure. The category of pairs \((B,b)\) with \(b^2=2\), and morphisms preserving \(b\), has initial object

\[
\boxed{(\mathbb Q[t]/(t^2-2),t).}
\]

Therefore

\[
\boxed{
\text{unpointed existence may have no universal repair,}
\quad
\text{while chosen-witness repair is universal.}
}
\]

---

# 14. Symmetry no-choice theorem

Let a group \(G\) act on the repair moduli

\[
\mathfrak R
=
\operatorname{Rep}_K(\Sigma,\delta)^\simeq.
\]

If every component lies in a nontrivial \(G\)-orbit and no component is \(G\)-fixed, then no \(G\)-equivariant single-valued repair selector exists.

### Proof

A \(G\)-equivariant selected component would be a fixed point of the induced action on \(\pi_0\mathfrak R\), contradicting the hypothesis. \(\square\)

Hence the endogenous output must sometimes be the entire repair moduli.

---

# 15. Impossible repairs and preservation contracts

ENDO-2 gives a natural impossible strict repair.

There is no faithful exact strong monoidal embedding

\[
J:\mathbf{Ab}_{fg}\to\mathcal B
\]

into an abelian monoidal category whose tensor is exact in each variable, while simultaneously preserving the ordinary tensor product and keeping \(\mathbb Z/n\neq0\).

Indeed, tensoring

\[
n:\mathbb Z\hookrightarrow\mathbb Z
\]

with \(\mathbb Z/n\) gives the zero endomorphism of \(\mathbb Z/n\), which cannot remain monic unless the torsion object becomes zero.

Therefore a repair of tensor exactness must relax at least one preservation clause.

---

# 16. Relaxation frontiers

Let a finite preservation contract be

\[
K=\{k_1,\ldots,k_m\}.
\]

For \(J\subseteq K\), call \(J\) **feasible** if

\[
\operatorname{Rep}_{J}(\Sigma,\delta)\neq\varnothing.
\]

Feasibility is downward closed.

## Definition 16.1 — Relaxation frontier

The **relaxation frontier** is the antichain of maximal feasible subcontracts.

Equivalently, it records inclusion-minimal sets of clauses that must be dropped.

## Theorem E3.5 — Finite frontier theorem

If \(K\) is finite and at least one repair exists after relaxing some clauses, then the relaxation frontier is nonempty.

If it has one member, the preservation loss is structurally forced.

If it has several members, grammar mutation branches already at the level of preservation policy.

### Proof

The feasible subsets form a nonempty finite down-set in \(2^K\), hence possess maximal elements. \(\square\)

---

# 17. The ENDO-3 repair trichotomy

## Theorem E3.6 — Repair trichotomy

For every intrinsic defect \(\delta\) and fixed preservation contract \(K\), exactly one of the following occurs:

### I. Universal repair

\[
\operatorname{Rep}_K(\Sigma,\delta)
\]

has an initial object. Grammar mutation is determined up to contractible choice.

### II. Branching repair

The repair category is nonempty but has no initial object. Any single repair requires extra non-endogenous data or symmetry breaking. The canonical output is the repair moduli itself.

### III. Infeasible repair

The repair category is empty. Then \(\delta\) and \(K\) are jointly inconsistent. If \(K\) is finite, the relaxation frontier records minimal preservation losses.

The three natural examples above realize I, II and III respectively.

---

# 18. Defect compilers

## Definition 18.1 — Defect compiler

A defect compiler \(\mathscr C\) assigns to each grammar state \(\Sigma\):

1. a small family of walking repair schemata
   \[
   U(\Sigma)=\{A_\lambda\to B_\lambda\};
   \]
2. the corresponding saturated occurrence spaces;
3. a preservation contract for each defect species.

It must satisfy:

### (N) Naturality
Equivalent grammar states induce equivalent defect families.

### (S) Saturation invariance
Gauge/representation-equivalent raw occurrences determine the same intrinsic defect.

### (A) Anti-tautology
The compiler uses only current structure and predeclared law tokens, not the desired solution.

### (Sm) Smallness
The generated defect family is set-sized in the chosen universe.

### (P) Provenance
Each defect retains a map to the structural configuration that generated it.

A compiler satisfying these conditions is an **endogenous compiler relative to its structural signature**.

---

# 19. One-step doctrine mutation

Given an endogenous compiler \(\mathscr C\), define the one-step mutation operator

\[
\mathbb T(\Sigma)
\]

by applying the repair trichotomy to all intrinsic defect species:

- universal repairs are attached;
- branching repairs are retained as a repair-moduli family;
- infeasible repairs generate relaxation frontiers.

A **deterministic sector** is a sector in which every active repair has an initial object and the preservation contracts are feasible.

There \(\mathbb T\) is an honest endofunctor up to coherent equivalence.

Outside the deterministic sector, the correct object is a correspondence/profunctor of grammar states rather than an ordinary function.

---

# 20. Doctrine lattices and least fixed points

Fix a semantic universe and a set-sized collection of admissible law tokens. Let \(L\) be the complete lattice of saturated subdoctrines ordered by inclusion.

Suppose the compiler/repair process induces

\[
T:L\to L
\]

with

\[
x\le T(x)
\]

and \(T\) monotone.

Starting from \(x_0\), define

\[
x_{\alpha+1}=T(x_\alpha),
\]

and at limit ordinals

\[
x_\lambda=\bigvee_{\beta<\lambda}x_\beta.
\]

## Theorem E3.7 — Least grammar fixed point

There exists a least \(T\)-fixed doctrine above \(x_0\).

If the lattice is set-sized, the transfinite chain stabilizes before \(|L|^+\).

### Proof

Knaster–Tarski gives the least fixed point of a monotone self-map of a complete lattice. For the explicit iteration, the chain is increasing; a set-sized poset cannot support a strictly increasing chain through every ordinal below \(|L|^+\). Once \(x_\alpha=x_{\alpha+1}\), the point is fixed. Any fixed \(y\ge x_0\) dominates the chain by transfinite induction, proving leastness. \(\square\)

## Corollary E3.8 — \(\omega\)-continuous sector

If \(T\) preserves suprema of increasing \(\omega\)-chains, then

\[
x_\omega=\bigvee_{n<\omega}T^n(x_0)
\]

is already fixed.

This recovers ENDO-2 finite-tree/\(\omega\)-closure as a special case.

---

# 21. Grammar closure ordinal

## Definition 21.1

The least ordinal

\[
\theta_T(\Sigma)
\]

at which the doctrine chain stabilizes is the **grammar closure ordinal relative to \(T\)**.

It is not an absolute invariant of the mathematical structure.

Changing the grammar primitives can change \(\theta_T\), exactly as ENDO-2's “three rounds” depends on the declared atomic syntax.

---

# 22. The forced core of a branching mutation

Suppose repairs are represented in the doctrine lattice \(L\), and let

\[
\mathcal R_K(\Sigma,\delta)\subseteq L
\]

be the nonempty family of feasible repair doctrines.

Define

\[
\operatorname{Force}_K(\Sigma,\delta)
=
\bigwedge_{\rho\in\mathcal R_K(\Sigma,\delta)}\rho.
\]

This is the **forced repair core**: the largest doctrine fragment shared by every admissible repair.

## Theorem E3.9

A doctrine token belongs to the forced core iff it is contained in every admissible repair.

If a least/universal repair \(\rho_0\) exists in the doctrine order, then

\[
\operatorname{Force}_K(\Sigma,\delta)=\rho_0.
\]

Thus branching does not erase all endogenous content: common consequences can still be separated from branch-dependent choices.

---

# 23. Provenance and path dependence

Two repair paths may reach equivalent final semantic worlds but represent different generative histories.

ENDO-3 therefore retains a repair path

\[
\Sigma_0\to\Sigma_1\to\cdots\to\Sigma_n
\]

as provenance data.

Semantic quotient may identify endpoints, but provenance is not discarded unless the current gauge declares the difference zero-cost.

---

# 24. Re-reading ENDO-2's regular/singular split

ENDO-2 found that for a nonregular Noetherian ring, standard truncation pushes the stable finite world outside \(\operatorname{Perf}(R)\), and later derived tensor detects unbounded Tor.

ENDO-3 changes the interpretation.

The intrinsic output is **not**

> therefore choose \(D(R)\).

Instead the failure generates a repair moduli problem.

Depending on the preservation contract, possible policies include:

- enlarge the carrier from \(\operatorname{Perf}(R)\);
- weaken or remove truncation closure;
- change observation/equivalence doctrine;
- retain the defect as a singularity invariant;
- move to a derived/stable completion with altered operation semantics.

Without a preservation contract these are not canonically ordered.

---

# 25. No bare-structure compiler theorem

A bare additive category does not determine its exact grammar.

The same underlying additive category can carry the split exact structure or a larger exact structure. ENDO-2 showed that the associated saturation and problem generation differ.

Hence

\[
\boxed{
\text{there is no compiler depending only on the bare additive category
that can simultaneously recover both marked exact semantics.}
}
\]

More generally, any structure that the theory promises to preserve must occur in the grammar input, or be recoverable by a separately proved invariant construction.

---

# 26. Semantic versus effective grammar generation

All preceding theorems are semantic unless an effective presentation is supplied.

A semantic grammar repair may use:

- all mapping objects;
- an accessible localization;
- a transfinite small-object construction;
- a derived tensor object represented by an infinite resolution.

Therefore

\[
\boxed{
\text{finite repair depth}
\not\Rightarrow
\text{finite computational cost}.
}
\]

Define:

### Semantic ENDO-3
Repair exists in the mathematical semantic universe.

### Effective ENDO-3
Defect detection, repair construction, equivalence testing, and observation admit specified algorithms with a declared cost model.

No general theorem upgrades the former to the latter.

---

# 27. Relative Grammar-Genesis Completeness Theorem

## Theorem E3.10 — Relative completeness

Fix:

1. a locally presentable grammar universe, or a presentable \(\infty\)-categorical analogue;
2. a structural signature;
3. a natural, saturation-invariant, anti-tautological, small defect compiler;
4. explicit preservation contracts;
5. a repair language generated by walking attachments, orthogonality/localization, and weighted completion;
6. a semantic observation/provenance doctrine.

Then every intrinsic defect receives a mathematically well-defined ENDO-3 output:

- a universal repair, when an initial admissible repair exists;
- otherwise a nonempty branching repair moduli;
- otherwise an infeasible-contract certificate, and for finite contracts a nonempty relaxation frontier whenever some relaxation is feasible.

In deterministic sectors, repeated mutation has a least stable doctrine on the complete-lattice shadow.

In branching sectors, the forced core records what is common to every admissible future grammar.

### Meaning

This closes the **grammar-generation logic** inside the declared defect language.

### Non-meaning

It does not prove:

- that the structural signature itself is uniquely forced by a bare object;
- that every mathematical construction is expressible by the chosen repair language;
- that repairs are computable;
- that generated questions are important or literature-original.

---

# 28. ENDO-1 / ENDO-2 / ENDO-3 synthesis

## ENDO-1 — Problem genesis

\[
\boxed{
\text{existing structure}
\to
\text{uniformly generated problems}.
}
\]

## ENDO-2 — Structural closure

\[
\boxed{
\text{generated objects}
\to
\text{new relations/operations}
\to
\text{closure or structural defect}.
}
\]

## ENDO-3 — Grammar genesis

\[
\boxed{
\text{intrinsic defect}
\to
\text{repair moduli}
\to
\text{universal repair / branching / relaxation frontier}.
}
\]

Together:

\[
\boxed{
\begin{array}{c}
\text{structure}\\
\Downarrow\\
\text{problem generation}\\
\Downarrow\\
\text{saturation}\\
\Downarrow\\
\text{object / relation generation}\\
\Downarrow\\
\text{structural compatibility test}\\
\Downarrow\\
\text{intrinsic defect}\\
\Downarrow\\
\text{grammar repair moduli}\\
\Downarrow\\
\text{new grammar}\\
\Downarrow\\
\text{repeat}.
\end{array}}
\]

This is the first version of the project in which **objects, problems, and grammar mutations** all belong to one formal generative loop.

---

# 29. Pressure-test ledger for ENDO-3

| Attack | Result |
|---|---|
| Representative failure mistaken for intrinsic defect | blocked by saturation-before-mutation |
| Minimal repair defined by arbitrary scalar cost | blocked; minimality uses initiality/factorization |
| Symmetry forces arbitrary choice | blocked; output repair moduli |
| Strict preservation impossible | detected by empty repair category |
| Repair requires dropping a law | handled by relaxation frontier |
| One attachment creates new defects | handled by saturated filler completion |
| Two independent repairs order-dependent | pushout interchange gives canonical agreement |
| Raw depth mistaken for intrinsic invariant | grammar-relative closure ordinal |
| Semantic repair mistaken for algorithm | semantic/effective split |
| Same final grammar treated as same history | provenance retained |
| Bare category claimed to determine all doctrine | explicitly ruled out |

---

# 30. Research status

## Closed inside ENDO-3's declared scope

- grammar defects as saturated extension/filler failures;
- pointed repair categories;
- universal one-cell repair;
- simultaneous independent repair;
- coherent filler saturation under smallness/accessibility hypotheses;
- localization repair for rigid/equivalence laws;
- free weighted completion repair;
- universal / branching / infeasible trichotomy;
- symmetry no-choice mechanism;
- finite preservation relaxation frontier;
- monotone doctrine fixed-point theory;
- forced core of branching repairs;
- semantic/effective distinction.

## Still outside the theory

- a unique structural signature generated from a completely bare mathematical object;
- automatic mathematical importance or originality ranking;
- universal computability;
- proof that all real mathematical creativity is captured by the adopted repair language.

These are boundaries, not hidden assumptions.

---

# 31. Main mathematical references

1. J. Lurie, *Higher Topos Theory*, §§5.2.7, 5.5.4 — localizations of presentable \(\infty\)-categories.
2. Richard Garner, *Understanding the small object argument*, arXiv:0712.0724 — algebraic refinement of the small object argument.
3. John Bourke and Richard Garner, *Algebraic weak factorisation systems I: accessible AWFS*, arXiv:1412.6559.
4. G. M. Kelly and V. Schmitt, *Notes on enriched categories with colimits of some class*, arXiv:math/0509102 — free \(\Phi\)-cocompletion and Cauchy completion.
5. J. Adámek and J. Rosický, *Locally Presentable and Accessible Categories* — orthogonality/injectivity classes and sketchable semantics.
6. A. Tarski, fixed-point theorem for complete lattices.
7. J. Lurie, *Higher Algebra* — stable/presentable universal constructions.

---

# 32. Final compressed form

The stable ENDO-3 core is

\[
\boxed{
\begin{array}{c}
\text{current structured grammar }\Sigma\\
\Downarrow\\
\text{uniform problem generation}\\
\Downarrow\\
\text{saturation of internal choices}\\
\Downarrow\\
\text{intrinsic defect }\delta\\
\Downarrow\\
\operatorname{Rep}_K(\Sigma,\delta)\\
\Downarrow\\
\begin{cases}
\text{initial object} &\Rightarrow \text{universal mutation},\\
\text{nonempty, no initial} &\Rightarrow \text{repair branching},\\
\varnothing &\Rightarrow \text{preservation relaxation frontier}
\end{cases}\\
\Downarrow\\
\text{new structured grammar}\\
\Downarrow\\
\text{repeat to least stable doctrine when fixed-point hypotheses hold.}
\end{array}}
\]

The main conceptual change is

\[
\boxed{
\text{ENDO-3 does not identify “internal generation” with a unique next theory.}
}
\]

Instead,

\[
\boxed{
\text{the endogenous mathematical output is the universal repair when one exists,
and otherwise the entire structured space of admissible futures.}
}
\]

This is the grammar-level analogue of the Frozen v1.0 possibility-geometry principle.
