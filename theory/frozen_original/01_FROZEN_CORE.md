# 01 — Frozen Core

## 0. 版本状态

版本：**Frozen v1.0**  
冻结日期：**2026-09-23**

本文件只记录当前理论的**primitive core**与必须保持的语义边界。  
所有额外 theorem、rank、obstruction group、sector-specific criterion 都放在派生理论中。

---

# 1. 基本环境

固定一个适当的 enriched / higher-categorical 语义环境。核心不要求唯一指定一种模型，但需要能够表达：

- objects / semantic worlds；
- vertical arrows；
- horizontal proarrows / profunctors / correspondences；
- 2-cells / higher coherence；
- companions / conjoints；
- admissible weighted limits、colimits、representability；
- 必要时的 \(\mathcal V\)-enrichment。

记其为

\[
\mathbb E_{\mathcal V}.
\]

\(\mathcal V\) 可以按 sector 取：

\[
\mathbf{Set},\ \mathcal S,\ \mathbf{Cat}_\infty,\ \mathbf{Top},\ \mathbf{Met},\ \mathbf{Ban},\ldots
\]

理论不把具体 \(\mathcal V\) 当作绝对固定数据。

---

# 2. Configuration

一个 generative configuration 记为

\[
\Xi=(S,\Omega,\mathrm{Prov},\ldots),
\]

其中至少包含：

- 当前 semantic state \(S\)；
- 当前有效 law / admissibility / active structure \(\Omega\)；
- provenance / history 数据；
- 用于决定 admissible problem、gauge、observation 的必要 doctrine。

旧版本中的

\[
S=(R,A\hookrightarrow R,K)
\]

已经被吸收到更一般的 configuration picture 中。

若需要保留 capacity sector，则推荐使用：

\[
S=(R,A\hookrightarrow R,\iota_S:\mathsf{Cap}_S\hookrightarrow\mathsf{Sch}_S),
\]

其中 \(K\) 若存在，应从 reflective/capacity structure 导出，而不是默认 primitive。

---

# 3. Pre-target Problem Doctrine

核心的第一个 primitive 不是 generator、functor 或 adjunction，而是**预目标问题 doctrine**。

对每个 configuration \(\Xi\)，给出 admissible horizontal problems：

\[
P_\Xi:
\mathcal A_\Xi^{op}\otimes\mathcal B_\Xi
\to
\mathcal V.
\]

解释：

\[
P_\Xi(a,b)
\]

表示从 datum/problem \(a\) 到 candidate \(b\) 的 admissible realization / extension / compatibility / solution ways。

核心要求：

1. \(P_\Xi\) 必须在目标答案出现之前由 configuration、law、provenance、admissibility 决定；
2. 不允许为了得到指定答案而事后选择 \(P_\Xi\)；
3. problem doctrine 可以来自：
   - reduct/forgetful interface；
   - localization constraints；
   - quotient constraints；
   - gluing/descent；
   - extension/lifting；
   - deformation problem；
   - universal mapping problem；
   - 其他预先定义的 horizontal relation。

因此：

\[
\boxed{
\text{generativity is horizontal first.}
}
\]

---

# 4. Saturation / Gauge

raw problem 不直接视为真正的 generative problem。

必须先根据 configuration 中已经预先固定的语义 doctrine，进行：

\[
\boxed{
P_\Xi
\longrightarrow
P_\Xi^\sharp.
}
\]

其中 \((-)^\sharp\) 表示必要的 saturation / semantic normalization / gauge quotient。

它可能包括：

- descent / sheafification；
- homotopy localization；
- Morita / Cauchy normalization；
- a.e. quotient；
- provenance gauge；
- equivalence closure；
- admissible completion；
- 其他 sector-specific semantic saturation。

冻结原则：

\[
\boxed{
\text{Raw representatives do not define genuine branching before saturation.}
}
\]

例如 null-set 差异、weak-equivalent cofibrant replacements、Morita-equivalent presentations 等，不应自动计入 generative novelty。

---

# 5. Possibility Geometry

固定 \(a\in\mathcal A_\Xi\)。

从饱和后的 problem

\[
P_\Xi^\sharp(a,-)
\]

形成 possibility category / \(\infty\)-category：

\[
\boxed{
\mathfrak G_\Xi(a)
=
\int_{\mathcal B_\Xi}
P_\Xi^\sharp(a,-).
}
\]

其 maximal \(\infty\)-groupoid：

\[
\boxed{
\mathcal M_\Xi(a)
=
\mathfrak G_\Xi(a)^\simeq
}
\]

称为 **generative moduli**。

这是理论的基本输出之一。

必须区分：

\[
\mathcal M_\Xi(a)=\varnothing
\]

表示无 admissible candidate；

\[
\pi_0\mathcal M_\Xi(a)>1
\]

表示 genuine branching；

\[
\mathcal M_\Xi(a)\ \text{connected but noncontractible}
\]

表示 object type 唯一但存在 isotropy / automorphism / higher coherence；

\[
\mathcal M_\Xi(a)\simeq *
\]

是最强的 groupoidal rigidity，但并不等同于整个 possibility category 只有一个 object。

---

# 6. Distinguished / Universal Loci

理论允许从 \(\mathfrak G_\Xi(a)\) 派生 distinguished loci，例如：

- universal locus；
- minimal / maximal locus；
- extremal locus；
- framed locus；
- stable locus；
- provenance-compatible locus。

但它们不是 primitive。

特别地，若 \(\mathfrak G_\Xi(a)\) 有 initial object，则所有 initial objects 构成的空间：

\[
\boxed{
\mathcal U_\Xi(a)
=
\left(\mathfrak G_\Xi(a)^{\mathrm{init}}\right)^\simeq
}
\]

若非空则必 contractible。

冻结修正：

\[
\boxed{
\text{Representability does not collapse all generative moduli;}
}
\]

它只在 possibility geometry 内部产生一个 contractible universal locus。

---

# 7. Oriented Representability

若存在 \(F(a)\in\mathcal B_\Xi\) 使

\[
\boxed{
P_\Xi^\sharp(a,b)
\simeq
\Map_{\mathcal B_\Xi}(F(a),b)
}
\]

自然于 \(b\)，则称该 problem 在 \(a\) 处发生 **oriented objectification / corepresentability**。

如果这些对象自然组装成

\[
F:\mathcal A_\Xi\to\mathcal B_\Xi,
\]

则得到 functorial objectification。

冻结原则：

\[
\boxed{
\text{Representability is a special rigid sector of generativity, not generativity itself.}
}
\]

若 problem 特别来自

\[
P_U(a,b)
=
\Map_{\mathcal A}(a,U b),
\]

则 oriented representability 等价于

\[
F\dashv U.
\]

因此 adjunction 是重要 sector，而不是 general definition。

---

# 8. Actual / Formal Comparison

一般 effectivity 的核心 primitive 是一个比较函子：

\[
\boxed{
C_\Xi:
\mathsf{Actual}_\Xi
\longrightarrow
\mathsf{Formal}_\Xi.
}
\]

\(\mathsf{Formal}_\Xi\) 按 sector 可以表示：

- pro-data；
- descent data；
- formal completion；
- local data；
- infinitesimal data；
- truncated towers；
- compatible finite data；
- deformation data；
- 其他 formal/local possibility geometry。

\(\mathsf{Actual}_\Xi\) 表示该 sector 中真正的 actual mathematical objects。

核心不规定唯一的 formalization doctrine；它必须由 configuration 预先确定。

---

# 9. Effectivity Fiber

对 formal datum

\[
\xi\in\mathsf{Formal}_\Xi
\]

定义：

\[
\boxed{
\operatorname{EffFib}_\Xi(\xi)
=
\operatorname{hofib}_\xi(C_\Xi).
}
\]

解释：

\[
\operatorname{EffFib}_\Xi(\xi)=\varnothing
\]

表示 formal datum 不可 actualize；

\[
\operatorname{EffFib}_\Xi(\xi)\neq\varnothing
\]

表示至少存在 actual realization；

非 contractible fiber 可以记录 branching / isotropy；

\[
\operatorname{EffFib}_\Xi(\xi)\simeq *
\]

表示 rigid object-level effectivity。

对象级 effectivity 不是完整 semantic reconstruction；完整 reconstruction 由 \(C_\Xi\) 本身是否为 equivalence 决定。

---

# 10. Persistent Observation / Novelty

actualization 是否构成真正的新生成，不能由以下任何一个条件单独决定：

- object 改变；
- unit 非同构；
- functoriality；
- universal property；
- completion；
- representability；
- adjunction。

必须使用独立的、预先固定的 persistent observation doctrine。

记未来 context category 为

\[
\mathsf{FCtx}_\Xi,
\]

persistent observation profunctor：

\[
\mathbb O_\Xi^\infty:
\mathsf E_\Xi^{GM}
\nrightarrow_{\mathcal V}
\mathsf{FCtx}_\Xi,
\]

以及 persistent nerve：

\[
\boxed{
N_\Xi^\infty(e)
=
\mathbb O_\Xi^\infty(e,-).
}
\]

persistent equivalence由未来所有 admissible contexts 中不可区分来定义。

因此 novelty 必须相对于 \(N^\infty\) 判断。

冻结原则：

\[
\boxed{
\text{universal objectification}
\not\Rightarrow
\text{generative novelty}.
}
\]

Karoubi completion、Stone duality、sobrification、plus construction 等都表明 observation doctrine 不同，novelty 判定可以不同。

---

# 11. Provenance

语义事件之外必须允许 proof-relevant provenance lift：

\[
p_\Omega:
\widetilde{\mathbb E}_\Omega
\to
\mathbb E.
\]

同一个 semantic event 可以具有不同 derivation/provenance histories。

冻结原则：

\[
\boxed{
\text{same final semantics}
\neq
\text{same generative history}.
}
\]

GM normalization 允许 quotient 掉：

- Cauchy/Morita gauge；
- definitional macro；
- 其他预先宣布为 zero-cost 的表示差异。

但不能自动删除 genuinely different provenance。

---

# 12. Frozen Core — 最简压缩形式

整个核心最终冻结为：

\[
\boxed{
\begin{array}{c}
\text{Configuration }\Xi
\\
\Downarrow\\
\text{Pre-target horizontal problem }P_\Xi
\\
\Downarrow\\
\text{Saturation / gauge }P_\Xi^\sharp
\\
\Downarrow\\
\text{Possibility geometry }\mathfrak G_\Xi(a),\ \mathcal M_\Xi(a)
\\
\Downarrow\\
\text{Formal/actual comparison }
C_\Xi:\mathsf{Actual}_\Xi\to\mathsf{Formal}_\Xi
\\
\Downarrow\\
\text{Effectivity / realization}
\\
\Downarrow\\
\text{Persistent observation }N_\Xi^\infty
\\
\Downarrow\\
\text{Genuine novelty}.
\end{array}
}
\]

任何 representability、adjunction、monad、pro-object、obstruction group、resolution rank、promotion spectrum 等，默认均为从该核心导出的 sector structure。
