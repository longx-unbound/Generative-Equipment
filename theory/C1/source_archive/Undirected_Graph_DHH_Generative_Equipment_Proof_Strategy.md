# Undirected Graph DHH — Generative Equipment Proof Strategy

## 0. Status and discipline

This document is a **derived proof strategy** for the problem:

> Let \(\mathsf{Gra}\) be the category of undirected graphs and let \(W_A\) be the class of \(A\)-weak homotopy equivalences. Is the \(\infty\)-categorical localization
> \[
> \mathcal G_\infty:=\mathsf{Gra}[W_A^{-1}]
> \]
> equivalent to the \(\infty\)-category of all Kan complexes / spaces
> \[
> \mathsf{Spc}?
> \]

The strategy is developed relative to **Generative Equipment / 数学内生生成性理论 — Frozen v1.0**.

### Frozen-core rule

Nothing below modifies the Frozen v1.0 primitive core.

All new notions in this document — including:

- Global Effectivity Principle,
- Simultaneous Object Effectivity,
- Mapping/Coherence Completeness,
- Relative Cubical Transversality as an effectivity engine,
- tower-comparison criteria,

are treated as **derived sector structure**.

A core revision is allowed only if one finds:

1. a mathematically explicit counterexample to a frozen statement;
2. an internal contradiction;
3. a genuine well-definedness failure.

---

# 1. Target theorem

Let

\[
\mathcal G_\infty:=\mathsf{Gra}[W_A^{-1}]
\]

and let

\[
N:\mathcal G_\infty\longrightarrow \mathsf{Spc}
\]

be the functor induced by the cubical nerve / \(A\)-homotopy realization mechanism.

The target is:

\[
\boxed{
N:\mathcal G_\infty \simeq \mathsf{Spc}.
}
\]

Equivalently, prove that \(N\) is

1. essentially surjective;
2. fully faithful.

The central principle of this strategy is:

> Do **not** try to prove the equivalence directly from raw graph colimits.  
> Instead, pass through the tower of finite \(n\)-type localizations and prove that every formally compatible tower is simultaneously effective in the actual graph localization.

---

# 2. Known finite-stage input

For each \(n\ge 0\), let

\[
\mathcal G_n
\]

denote the \(\infty\)-categorical localization of undirected graphs at the corresponding \(n\)-equivalences.

The finite-stage theorem gives equivalences

\[
E_n:\mathcal G_n \xrightarrow{\sim} \mathsf{Spc}_{\le n}.
\]

We also require the transition functors

\[
q_{n+1,n}:\mathcal G_{n+1}\to\mathcal G_n
\]

to correspond, under \(E_n\), to Postnikov truncation

\[
\tau_{\le n}:\mathsf{Spc}_{\le n+1}\to\mathsf{Spc}_{\le n}.
\]

Thus the finite-stage systems should fit into a homotopy-commutative diagram

\[
\begin{array}{ccc}
\mathcal G_{n+1} & \xrightarrow{E_{n+1}} & \mathsf{Spc}_{\le n+1} \\
\downarrow q_{n+1,n} && \downarrow \tau_{\le n} \\
\mathcal G_n & \xrightarrow{E_n} & \mathsf{Spc}_{\le n}.
\end{array}
\]

This compatibility is not merely bookkeeping: it is the bridge that identifies the formal inverse limit of graph stages with the Postnikov-complete \(\infty\)-category of spaces.

---

# 3. First reduction: construct the formal target

Define

\[
\mathsf{Formal}
:=
\varprojlim_n \mathcal G_n.
\]

Using the equivalences \(E_n\) and their compatibility with truncation, prove

\[
\mathsf{Formal}
\simeq
\varprojlim_n \mathsf{Spc}_{\le n}.
\]

By Postnikov completeness of spaces,

\[
\varprojlim_n \mathsf{Spc}_{\le n}
\simeq
\mathsf{Spc}.
\]

Hence obtain a canonical equivalence

\[
\boxed{
\mathsf{Formal}\simeq\mathsf{Spc}.
}
\]

This is the formal side of the Frozen v1.0 actual/formal comparison.

---

# 4. Canonical comparison functor

Each graph-localization object has all of its finite truncations, giving a canonical functor

\[
C:
\mathcal G_\infty
\longrightarrow
\varprojlim_n \mathcal G_n.
\]

Under the identification

\[
\varprojlim_n\mathcal G_n\simeq\mathsf{Spc},
\]

the original discrete homotopy hypothesis is reduced to:

\[
\boxed{
C \text{ is an equivalence.}
}
\]

Thus the proof splits into exactly two tasks:

\[
\boxed{
\text{(A) Essential surjectivity of } C
}
\]

and

\[
\boxed{
\text{(B) Full faithfulness of } C.
}
\]

These are the two main proof programs below.

---

# 5. Sector theorem to prove

## Theorem A — Global Effectivity Principle

Assume:

1. the finite-stage equivalences
   \[
   \mathcal G_n\simeq\mathsf{Spc}_{\le n};
   \]

2. compatibility of the transition functors with Postnikov truncation;

3. every compatible formal tower in
   \[
   \varprojlim_n\mathcal G_n
   \]
   is simultaneously realizable by an object of \(\mathcal G_\infty\);

4. for every \(G,H\in\mathcal G_\infty\),
   \[
   \operatorname{Map}_{\mathcal G_\infty}(G,H)
   \longrightarrow
   \varprojlim_n
   \operatorname{Map}_{\mathcal G_n}(q_nG,q_nH)
   \]
   is an equivalence.

Then

\[
\mathcal G_\infty\simeq\mathsf{Spc}.
\]

### Proof shape

Conditions (1) and (2) identify the formal limit with \(\mathsf{Spc}\).

Condition (3) gives essential surjectivity of \(C\).

Condition (4) gives full faithfulness of \(C\).

Therefore \(C\) is an equivalence.

---

# 6. Main Program I: Simultaneous Object Effectivity

The finite-stage theorem provides, morally,

\[
\forall n\ \exists G_n
\]

such that

\[
E_n(G_n)\simeq\tau_{\le n}X
\]

for a given space \(X\).

The full theorem requires:

\[
\exists G\ \forall n
\]

such that

\[
q_nG\simeq G_n.
\]

This is the precise infinitary uniformization problem.

## 6.1 Formal tower associated to a space

For \(X\in\mathsf{Spc}\), define

\[
\xi_X
=
\left(
E_n^{-1}(\tau_{\le n}X)
\right)_{n\ge0}
\in
\varprojlim_n \mathcal G_n.
\]

The object-level problem becomes:

> Show that \(\xi_X\) lies in the essential image of
> \[
> C:\mathcal G_\infty\to\varprojlim_n\mathcal G_n.
> \]

Equivalently, prove nonemptiness of the effectivity fiber

\[
\operatorname{EffFib}(X)
:=
\mathcal G_\infty
\times_{\varprojlim_n\mathcal G_n}
\{\xi_X\}.
\]

The desired statement is

\[
\boxed{
\operatorname{EffFib}(X)\neq\varnothing
\quad
\forall X\in\mathsf{Spc}.
}
\]

A stronger and highly desirable form is

\[
\boxed{
\operatorname{EffFib}(X)\text{ is contractible.}
}
\]

Contractibility would later simplify full faithfulness and uniqueness.

---

# 7. Construction route for object effectivity

The preferred construction is inductive but must be upgraded from finite realizability to a single actual object.

## Step O1 — choose compatible finite graph models

For every \(n\), choose

\[
G_n\in\mathcal G_n
\]

representing \(\tau_{\le n}X\).

Then construct equivalences

\[
q_{n+1,n}(G_{n+1})\simeq G_n.
\]

The goal is not merely existence level-by-level, but a coherent object of the inverse limit.

## Step O2 — strictify the tower

Replace the weakly compatible tower by a model in which the transition data are represented by actual graph maps whenever possible.

Desired output:

\[
\widetilde G_0
\leftarrow
\widetilde G_1
\leftarrow
\widetilde G_2
\leftarrow \cdots
\]

together with comparison maps realizing the Postnikov transitions.

This is where relative cubical transversality enters.

## Step O3 — build a single graph realization

Construct a candidate graph \(G_X\) from the compatible tower.

Possible engines:

### Engine O3.a — telescopic realization

Construct a graph-theoretic telescope

\[
G_X
=
\operatorname{Tel}(\widetilde G_0\leftarrow\widetilde G_1\leftarrow\cdots)
\]

with controlled cubical nerve.

Required theorem:

\[
\tau_{\le n}N(G_X)\simeq N(\widetilde G_n)
\]

for every \(n\).

### Engine O3.b — filtered attachment realization

Start from \(G_0\) and inductively attach graph cells / gadgets killing or creating the required homotopy data.

Construct

\[
G^{(0)}
\to
G^{(1)}
\to
G^{(2)}
\to
\cdots
\]

so that

\[
\tau_{\le n}N(G^{(m)})
\]

stabilizes for \(m\ge n\).

Then define a suitable homotopy colimit candidate \(G_X\).

This route requires strong control of newly generated nondegenerate cubes.

### Engine O3.c — pro-object effectivity

Construct a formal/pro graph object

\[
\widehat G_X
\]

representing all finite stages, and prove an effectivity theorem saying that the relevant class of pro-objects comes from actual graph-localization objects.

This is the cleanest route conceptually if a suitable compactness/effectivity theorem can be proved.

---

# 8. Relative Cubical Transversality

This is the most important local technical theorem suggested by the theory.

## Desired theorem

Let

\[
i:\partial\square^r\hookrightarrow\square^r
\]

be a cubical boundary inclusion.

Suppose one has:

1. a formal cubical filling in the target homotopy type;
2. an actual graph realization of the boundary;
3. compatibility of the two after applying the graph nerve.

Then one wants an actual graph filling, possibly after controlled \(A\)-weak modification.

Schematically:

\[
\begin{array}{ccc}
\partial\square^r & \longrightarrow & N(G) \\
\downarrow && \downarrow \\
\square^r & \longrightarrow & X
\end{array}
\]

should admit an actual graph refinement

\[
\square^r\longrightarrow N(G')
\]

with

\[
G'\simeq_A G
\]

relative to the boundary.

## Strong form

The space of such relative lifts should be contractible.

## Why this theorem matters

It converts a formal coherence condition into an actual graph-theoretic coherence condition.

In Frozen v1.0 language, it proves vanishing of a relative shape residue

\[
\mathbf{ShRes}
\left(
\partial\square^r\hookrightarrow\square^r;
\sigma,\widetilde\sigma_{\partial}
\right).
\]

This theorem can simultaneously drive:

- strictification of Postnikov towers;
- realization of higher coherences;
- compatibility of graph models;
- mapping-space reconstruction.

---

# 9. Main Program II: Mapping/Coherence Completeness

Even perfect object realization does not imply an equivalence of \(\infty\)-categories.

We must prove that, for every \(G,H\in\mathcal G_\infty\),

\[
\boxed{
\operatorname{Map}_{\mathcal G_\infty}(G,H)
\simeq
\varprojlim_n
\operatorname{Map}_{\mathcal G_n}(q_nG,q_nH).
}
\]

This is the mapping-space completeness theorem.

---

# 10. Postnikov analysis of mapping spaces

Under finite-stage equivalences,

\[
\operatorname{Map}_{\mathcal G_n}(q_nG,q_nH)
\]

corresponds to a finite Postnikov approximation of

\[
\operatorname{Map}_{\mathsf{Spc}}(N(G),N(H)).
\]

Thus the desired theorem should follow if one proves:

1. the graph-localized mapping space is Postnikov complete;
2. its \(n\)-truncation agrees with the finite-stage mapping space.

The precise local statement to target is:

\[
\boxed{
\tau_{\le n}
\operatorname{Map}_{\mathcal G_\infty}(G,H)
\simeq
\operatorname{Map}_{\mathcal G_n}(q_nG,q_nH).
}
\]

If true for every \(n\), then Postnikov completeness gives

\[
\operatorname{Map}_{\mathcal G_\infty}(G,H)
\simeq
\varprojlim_n
\operatorname{Map}_{\mathcal G_n}(q_nG,q_nH).
\]

So the full-faithfulness problem is reduced to a family of finite mapping-truncation theorems plus convergence.

---

# 11. Avoiding phantom phenomena

The main danger is that two maps may agree at every finite stage but differ globally.

Thus one must rule out a graph-theoretic analogue of phantom maps.

## Phantom obstruction

Define a potential kernel

\[
\operatorname{Ph}(G,H)
:=
\operatorname{hofib}
\left[
\operatorname{Map}_{\mathcal G_\infty}(G,H)
\to
\varprojlim_n
\operatorname{Map}_{\mathcal G_n}(q_nG,q_nH)
\right].
\]

The desired statement is

\[
\boxed{
\operatorname{Ph}(G,H)\simeq *.
}
\]

A weaker first step is

\[
\pi_0\operatorname{Ph}(G,H)=0.
\]

Then prove inductively

\[
\pi_k\operatorname{Ph}(G,H)=0
\qquad
\forall k\ge0.
\]

If a nontrivial phantom class exists, the original DHH fails even though every finite \(n\)-type theorem remains true.

This makes phantom analysis an explicit falsification test.

---

# 12. A possible Milnor-\(\lim^1\) attack

If the tower of mapping spaces satisfies suitable fibrancy conditions, one expects Milnor-type exact sequences

\[
0
\to
\lim\nolimits^1
\pi_{k+1}M_n
\to
\pi_k(\holim_n M_n)
\to
\lim_n\pi_k(M_n)
\to0,
\]

where

\[
M_n
=
\operatorname{Map}_{\mathcal G_n}(q_nG,q_nH).
\]

Hence a concrete sufficient condition for mapping completeness is:

\[
\boxed{
\lim\nolimits^1_n \pi_{k+1}M_n=0
\quad
\forall k.
}
\]

Possible ways to force this:

- eventual constancy;
- Mittag-Leffler conditions;
- surjectivity of transition maps on homotopy groups;
- finite generation plus stabilization;
- a graph-specific lifting theorem implying tower fibrancy.

This gives a sharply testable route to full faithfulness.

---

# 13. Alternative representability route

There is a second route, conceptually closer to the representability sector.

For \(X\in\mathsf{Spc}\), define

\[
H_X(G)
:=
\operatorname{Map}_{\mathsf{Spc}}(X,N(G)).
\]

If one can construct an object \(R_X\in\mathcal G_\infty\) such that

\[
H_X(G)
\simeq
\operatorname{Map}_{\mathcal G_\infty}(R_X,G)
\]

naturally in \(G\), then one obtains a left adjoint

\[
R:\mathsf{Spc}\rightleftarrows\mathcal G_\infty:N.
\]

Then it is enough to prove that unit and counit are equivalences.

The finite-stage models provide formal representing objects

\[
R_{X,n}
\]

for the truncated functors.

The key theorem again becomes:

> a compatible family of finite-stage representing objects is simultaneously effective.

So this route does not remove the global difficulty; it re-expresses it as representability effectivity.

---

# 14. Why the accessible-localization shortcut should not be used as the main engine

Do not assume that raw graph pushouts compute homotopy pushouts after localization.

The dangerous inference is:

\[
\text{ordinary graph pushout}
\Rightarrow
\text{correct localized pushout}.
\]

Known counterexamples to naive pushout stability show that this step is not valid in general.

Therefore the following route should **not** be used without an independent theorem:

\[
\text{accessible localization}
\Rightarrow
\text{presentability}
\Rightarrow
\text{raw graph colimits compute localized colimits}.
\]

A future theorem could still prove presentability or cocompleteness of \(\mathcal G_\infty\), but it must be derived from genuinely homotopical constructions, not assumed from raw graph combinatorics.

---

# 15. Proof dependency graph

The recommended dependency order is:

\[
\boxed{
\text{Finite-stage equivalences}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{Tower compatibility}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\varprojlim_n\mathcal G_n\simeq\mathsf{Spc}
}
\]

then split:

\[
\begin{array}{ccc}
\text{Simultaneous Object Effectivity}
&&
\text{Mapping/Coherence Completeness}
\\[4pt]
\Downarrow
&&
\Downarrow
\\
\text{essential surjectivity of }C
&&
\text{full faithfulness of }C
\end{array}
\]

and finally

\[
\boxed{
C:\mathcal G_\infty
\xrightarrow{\sim}
\varprojlim_n\mathcal G_n
\simeq
\mathsf{Spc}.
}
\]

---

# 16. Concrete lemma checklist

The proof should be organized around the following lemmas.

## L1. Finite-stage compatibility lemma

Construct equivalences

\[
E_n:\mathcal G_n\simeq\mathsf{Spc}_{\le n}
\]

compatible with truncation.

### Pass criterion

The transition square commutes up to specified coherent equivalence.

---

## L2. Formal-limit lemma

Prove

\[
\varprojlim_n\mathcal G_n\simeq\mathsf{Spc}.
\]

### Pass criterion

This must be an equivalence of \(\infty\)-categories, not merely a bijection of equivalence classes of objects.

---

## L3. Relative realization lemma

Prove a relative cubical filling theorem sufficient to lift compatible finite coherence data to graph data.

### Pass criterion

The theorem is relative to an already fixed boundary and stable under \(A\)-weak replacement.

---

## L4. Tower strictification lemma

Every formal compatible tower in the \(\mathcal G_n\) admits a sufficiently strict graph representative tower.

### Depends on

L3.

---

## L5. Simultaneous Effectivity Theorem

Every compatible formal tower is represented by one object

\[
G\in\mathcal G_\infty.
\]

### Equivalent target

\[
C
\]

is essentially surjective.

---

## L6. Mapping truncation lemma

For all \(G,H\),

\[
\tau_{\le n}
\operatorname{Map}_{\mathcal G_\infty}(G,H)
\simeq
\operatorname{Map}_{\mathcal G_n}(q_nG,q_nH).
\]

---

## L7. No-phantom / convergence lemma

Prove Postnikov completeness of graph-localized mapping spaces, or directly show

\[
\operatorname{Map}_{\mathcal G_\infty}(G,H)
\simeq
\holim_n
\operatorname{Map}_{\mathcal G_n}(q_nG,q_nH).
\]

### Possible sufficient criterion

All relevant \(\lim^1\)-obstructions vanish.

---

## L8. Full faithfulness theorem

Deduce

\[
C
\]

is fully faithful.

---

## L9. Final equivalence theorem

Combine L5 and L8:

\[
\mathcal G_\infty
\simeq
\varprojlim_n\mathcal G_n
\simeq
\mathsf{Spc}.
\]

---

# 17. Recommended attack order

The optimal research order is **not** L1 through L9 mechanically.

Instead:

## Phase I — lock the formal reduction

Prove L1 and L2 completely.

This isolates all genuinely new mathematics inside L3–L7.

## Phase II — attack local relative effectivity

Focus on L3.

Test first on:

- \(r=1\);
- \(r=2\);
- horns / partial cubes;
- collars;
- mixed cubes generated by pushout constructions.

The purpose is to identify the exact mechanism by which new nondegenerate cubes appear.

## Phase III — derive strictification

Use L3 to prove L4.

Do not attempt the infinite tower yet.

## Phase IV — prove simultaneous object effectivity

Use L4 plus one of the engines O3.a–O3.c to prove L5.

## Phase V — separately attack mapping completeness

Do not assume L5 implies full faithfulness.

Prove L6 and L7 independently.

## Phase VI — conclude

Only after L5 and L8 are proved should the final equivalence be claimed.

---

# 18. Falsification program

The strategy is deliberately designed so that failure produces mathematically meaningful information.

## F1. Object-effectivity failure

Find a compatible tower

\[
\xi\in\varprojlim_n\mathcal G_n
\]

such that

\[
\operatorname{EffFib}(\xi)=\varnothing.
\]

Then the full DHH is false.

This would be a genuine infinitary counterexample invisible at every finite stage.

---

## F2. Nonuniqueness defect

Find a tower \(\xi\) with

\[
\operatorname{EffFib}(\xi)
\]

noncontractible.

This may indicate that object realization exists but carries extra graph-localized moduli not seen by spaces.

---

## F3. Phantom-map failure

Find \(G,H\) such that

\[
\operatorname{Ph}(G,H)\not\simeq *.
\]

Then full faithfulness fails.

---

## F4. Relative transversality failure

Find a formally fillable cubical boundary that admits no actual relative graph filling even after \(A\)-weak replacement.

This would identify a concrete local obstruction to the current proof engine.

It would not automatically disprove DHH, but it would kill this particular effectivity route.

---

# 19. Anti-tautology checks

The following are forbidden in the proof.

1. Defining a class of “good towers” to mean “towers that come from actual graphs” and then proving good towers are effective.

2. Choosing obstruction groups only after seeing whether realization succeeds.

3. Building \(P_\Xi\), test objects, or lifting classes so that the desired equivalence is true by definition.

4. Replacing the global theorem with an equivalent statement whose proof already assumes the desired equivalence.

5. Using presentability of \(\mathcal G_\infty\) unless it has been established independently.

Every diagnostic introduced must be independently computable or independently characterized before the final theorem is known.

---

# 20. What would count as a decisive intermediate theorem?

The following would each be major progress.

## Milestone M1

A fully coherent equivalence

\[
\varprojlim_n\mathcal G_n\simeq\mathsf{Spc}.
\]

This completely isolates the problem as effectivity.

## Milestone M2

A Relative Cubical Transversality Theorem strong enough to strictify arbitrary finite coherence diagrams.

This would supply the missing local engine.

## Milestone M3

A Simultaneous Effectivity Theorem for Postnikov towers of graph models.

This proves essential surjectivity of

\[
C.
\]

## Milestone M4

A no-phantom theorem

\[
\operatorname{Map}_{\mathcal G_\infty}(G,H)
\simeq
\holim_n
\operatorname{Map}_{\mathcal G_n}(q_nG,q_nH).
\]

This proves full faithfulness.

## Milestone M5

Combine M3 and M4 to prove the full undirected graph DHH.

---

# 21. Strongest recommended formulation of the research target

Rather than working directly on

\[
\mathcal G_\infty\simeq\mathsf{Spc},
\]

the recommended central theorem is:

\[
\boxed{
\textbf{Graph Postnikov Effectivity Theorem}
}
\]

> The canonical functor
> \[
> C:
> \mathsf{Gra}[W_A^{-1}]
> \longrightarrow
> \varprojlim_n\mathcal G_n
> \]
> is an equivalence.

This formulation has several advantages:

1. it cleanly separates finite-stage knowledge from the genuinely infinite problem;
2. it matches the actual/formal architecture of Frozen v1.0;
3. it identifies counterexamples as infinitary effectivity defects;
4. it forces object and mapping-space issues to be handled separately;
5. once proved, the original DHH follows immediately from Postnikov completeness.

---

# 22. Final strategic summary

The recommended proof architecture is:

\[
\boxed{
\text{Finite \(n\)-type DHH}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{formal Postnikov tower category}
\simeq
\mathsf{Spc}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{prove actual/formal comparison is an equivalence}
}
\]

with two independent subproblems:

\[
\boxed{
\text{Simultaneous Object Effectivity}
}
\]

and

\[
\boxed{
\text{Mapping/Coherence Completeness}.
}
\]

The best local technical engine currently suggested by the theory is:

\[
\boxed{
\text{Relative Cubical Transversality}
}
\]

because it directly attacks the conversion

\[
\text{formal coherence}
\longrightarrow
\text{actual graph coherence}.
\]

The proof should therefore proceed in the following order:

\[
\boxed{
\text{formal reduction}
\to
\text{relative cubical lifting}
\to
\text{tower strictification}
\to
\text{simultaneous effectivity}
\to
\text{no-phantom convergence}
\to
\text{equivalence}.
}
\]

No modification of the Frozen v1.0 core is required by this strategy.
