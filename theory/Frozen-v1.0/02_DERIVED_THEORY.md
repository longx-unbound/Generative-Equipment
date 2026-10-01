# 02 — Derived Theory

本文件记录从 Frozen Core 推出的主要结构。它们不是 primitive。

---

# 1. Exact Residue / Universal Residue / Co-universal Residue

给定

\[
U:\mathcal B\to\mathcal A,
\]

可导出：

\[
\operatorname{hofib}_a(U)
\]

作为 exact residue；

\[
(a\downarrow U)
\]

作为 universal residue；

\[
(U\downarrow a)
\]

作为 co-universal residue。

只有在 base groupoidal 时，fiber 与 comma 才可自然靠近。

冻结结论：

\[
\boxed{
\text{fiber theory is strictly weaker than comma theory in non-groupoidal semantics.}
}
\]

---

# 2. Horizontal Rigidification Criterion

若 \(\mathcal B\) 是 accessible 且 complete 的 \(\infty\)-category，且

\[
H_a(-):=P^\sharp(a,-):\mathcal B\to\mathcal S,
\]

则：

\[
H_a
\]

可 corepresent 当且仅当它：

\[
\boxed{
\text{accessible + preserves all small limits}.
}
\]

这把：

- Generative Compression；
- Coherence / Resolution Stability；

在该 sector 中变成完整的 representability criterion。

---

# 3. Pro-rigidification

若 \(\mathcal B\) accessible 且具有 finite limits，而

\[
H_a=P^\sharp(a,-)
\]

accessible 且 left exact，则可产生 canonical pro-generator：

\[
\boxed{
\widehat F(a)\in\operatorname{Pro}(\mathcal B).
}
\]

并满足：

\[
H_a(b)
\simeq
\Map_{\operatorname{Pro}(\mathcal B)}
(\widehat F(a),j(b)).
\]

实际 representability 等价于：

\[
\widehat F(a)
\]

落在

\[
j(\mathcal B)\subseteq\operatorname{Pro}(\mathcal B).
\]

因此：

\[
\boxed{
\text{pro-representability}
=
\text{formal objectification},
}
\]

而：

\[
\boxed{
\text{actual representability}
=
\text{effectivity of the pro-generator}.
}
\]

注意：这只适用于 pro-sector，不是 general effectivity 的定义。

---

# 4. Infinitary Uniformization

若

\[
\widehat F(a)\simeq\{x_j\},
\]

则

\[
H_a(b)
\simeq
\operatorname*{colim}_j\Map(x_j,b).
\]

对 family \((b_i)_{i\in I}\)，product comparison：

\[
\chi_{a,I}:
H_a\!\left(\prod_i b_i\right)
\to
\prod_i H_a(b_i)
\]

对应：

\[
\operatorname*{colim}_j\prod_i\Map(x_j,b_i)
\to
\prod_i\operatorname*{colim}_j\Map(x_j,b_i).
\]

逻辑上：

左侧要求

\[
\exists j\ \forall i,
\]

右侧允许

\[
\forall i\ \exists j_i.
\]

因此 pro-effectivity 的核心 obstruction 是：

\[
\boxed{
\forall i\,\exists j_i
\quad\Rightarrow\quad
\exists j\,\forall i.
}
\]

在已 left exact 时，actual representability 的剩余 obstruction 可压缩为 infinite product preservation。

这形成：

\[
\boxed{
\text{formal-to-actual}
=
\text{infinitary uniformization}
}
\]

的 sector theorem。

---

# 5. Effectivity Spectrum

在 pro-sector 中可定义第一失败 cardinal：

\[
\rho_{\mathrm{eff}}(\widehat F(a))
=
\inf\{|I|:\chi_{a,I}\text{ fails}\}.
\]

也可定义：

\[
\operatorname{EffSpec}(\widehat F(a))
=
\{\kappa:H_a\text{ preserves all }<\kappa\text{-small products}\}.
\]

冻结边界：

这不是完整 obstruction；derived phenomena 如 \(R^1\!\lim\)、phantom maps、gerbe classes 等表明完整 obstruction 必须可以是 enriched / derived object。

---

# 6. Shape Residue

给 coarse-graining

\[
Q:\mathcal X\to\mathcal Y
\]

与 diagram shape

\[
\sigma:K\to\mathcal Y,
\]

定义 lift category：

\[
\mathbf{Lift}_Q(\sigma)
=
\operatorname{Fun}(K,\mathcal X)
\times_{\operatorname{Fun}(K,\mathcal Y)}
\{\sigma\}.
\]

对 inclusion

\[
i:A\hookrightarrow K
\]

及 partial lift \(\widetilde\sigma_A\)，定义：

\[
\boxed{
\mathbf{ShRes}_Q(i;\sigma,\widetilde\sigma_A)
=
\operatorname{Fib}_{\widetilde\sigma_A}
\left(
\mathbf{Lift}_Q(\sigma)
\to
\mathbf{Lift}_Q(\sigma|_A)
\right).
}
\]

它统一：

- object realization；
- arrow lifting；
- factorization residue；
- descent；
- Postnikov extension；
- diagram extension。

---

# 7. Relative Generative Residue

对

\[
Q:\mathcal X\to\mathcal Y
\]

与 base arrow

\[
u:y\to y',
\]

定义：

\[
\Lambda_Q(u)(x,x')
=
\operatorname{hofib}_u
\left(
\Map_\mathcal X(x,x')
\to
\Map_\mathcal Y(y,y')
\right).
\]

得到 profunctor：

\[
\Lambda_Q(u):
\mathcal X_y\nrightarrow\mathcal X_{y'}.
\]

组合只一般给 lax map：

\[
\Lambda_Q(v)\odot\Lambda_Q(u)
\to
\Lambda_Q(vu).
\]

因此 residual composition defect 与 objectification/representability defect必须区分。

---

# 8. Two-Axis Residue

两个独立轴：

\[
\mathbf R:
\text{ residue 是否 representable},
\]

\[
\mathbf C:
\text{ composition comparison 是否 equivalence}.
\]

不能将其混为一个 defect。

---

# 9. Residual Twisting

一般 total residue 不分裂为：

\[
\text{vertical}\times\text{relative}.
\]

群扩张、2-cocycle 等说明 residual family 可以带 nontrivial twisting。

因此冻结：

\[
\boxed{
\text{total residue is generally a twisted family, not a product decomposition.}
}
\]

---

# 10. Generative Compression

给 event/context family，可定义：

\[
e\equiv_U f
\iff
\omega_c(e)\simeq\omega_c(f)\quad\forall c\in U.
\]

由此得到 closure：

\[
\operatorname{Cl}_{gen}(U).
\]

adequate context basis 不必有 inclusion-minimal basis。

horizon enlargement 一般使 adequacy 更难：

\[
\operatorname{Cl}^{H_1}_{gen}(U)
\subseteq
\operatorname{Cl}^{H_0}_{gen}(U).
\]

---

# 11. Persistent Observation

对 future context：

\[
\mathsf{FCtx}_\Xi
=
\int_{(u:\Xi\to\Xi')}
\mathsf C_{\Xi'}.
\]

定义：

\[
\mathbb O_\Xi^\infty(e;(u,c))
=
\mathbb O_{\Xi'}(T_u e,c).
\]

persistent nerve：

\[
N^\infty_\Xi(e)
=
\mathbb O^\infty_\Xi(e,-).
\]

在适当 coherence/path completeness 假设下：

\[
\ker N^\infty
=
\nu\Phi^{lim}.
\]

persistent observation 的正确 duality 是由 \(\mathbb O^\infty\) 诱导的 Isbell adjunction，而不是 Reach\(\dashv\)Obs。

---

# 12. Reconstruction / Completion / Realization Separation

必须严格区分：

\[
\boxed{
\text{reconstruction defect}
\neq
\text{completion defect}
\neq
\text{semantic realization defect}.
}
\]

对 nerve

\[
N:\mathsf E^{GM}\to[\mathsf{FCtx},\mathcal V]
\]

可因子化：

\[
\mathsf E^{GM}
\xrightarrow{q_N}
\mathsf R_N
\xrightarrow{j_N}
[\mathsf{FCtx},\mathcal V],
\]

其中 \(j_N\) fully faithful。

再做 \(\mathcal W\)-completion：

\[
\mathsf R_N
\to
\widehat{\mathsf R}_N^\mathcal W.
\]

image closure 与 actual semantic realization必须继续区分。

---

# 13. Detection Kernel / Resolution Logic

不再使用单一 scalar detection height 作为 general object。

对 witness \(w\) 与 stage \(i\)，应保留：

\[
\mathbb D(w,i)
\]

以及 enriched 情形的：

\[
\mathbb E(w,i)
\]

作为 detection/error profile。

区分：

\[
\forall w\exists i
\]

与：

\[
\exists i\forall w;
\]

以及：

\[
\forall w\forall\varepsilon\exists i
\]

与：

\[
\forall\varepsilon\exists i\forall w.
\]

Promotion theorem 应被理解为允许某种量词交换的 sector theorem，而不是 universal law。

---

# 14. Promotion Engines

已确认至少存在彼此不同的 promotion mechanisms：

- compactness；
- Baire category + algebraic propagation；
- truncation / orthogonality；
- measure continuity / exceptional-budget control；
- finite generation / lattice compactness；
- equicontinuity；
- saturation；
- descent；
- algebraization；
- compact extraction。

冻结原则：

\[
\boxed{
\text{same promotion conclusion does not determine a unique engine.}
}
\]

---

# 15. Doctrine Moduli

bare semantic object 一般不能 canonical 地选择一个 nontrivial doctrine。

因此合理对象是：

\[
\boxed{
\mathfrak{Doct}(\Xi)
}
\]

及其 symmetry action。

若无 invariant \(\pi_0\)-component，则甚至 homotopy fixed point也不存在。

history/provenance 可缩小 stabilizer，从而激活 latent branch。

一般 doctrine dynamics 是 Prof-valued，而不是必然 functor-valued。

---

# 16. Monadic Reconstruction — 仅限 reduct sector

如果 horizontal problem具有：

\[
P^\sharp(a,b)
\simeq
\Map_{\mathcal A}(a,U b),
\]

且 corepresenter给：

\[
F\dashv U,
\]

则产生：

\[
T=UF.
\]

只有在满足 Barr–Beck 型 conservativity 与 split-simplicial realization 条件时，才可重建：

\[
\mathcal B\simeq\operatorname{Alg}_T(\mathcal A).
\]

冻结：

\[
\boxed{
\text{monadic reconstruction is not on the main chain of general generativity.}
}
\]

---

# 17. Scale Polymorphism

generative problem 可以发生于不同层级：

- object；
- diagram；
- category；
- semantic world；
- doctrine。

Ind-completion、Pro-completion、exact completion、stabilization 等均为 world-level universal problems。

理论不能固定只在 object-level 工作。
