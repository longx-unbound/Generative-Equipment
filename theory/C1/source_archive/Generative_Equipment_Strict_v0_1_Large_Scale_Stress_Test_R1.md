# 数学内生生成性理论

## Strict Space-Valued v0.1 大规模压力测试 R1

日期：2026-09-24  
被测试版本：Generative_Equipment_Strict_Space_Valued_v0_1.md  
被测试文件 SHA-256：55d19e853a88790515a1505f7f2c0c23ea270af50e751c78cfc8a4660dbc74bf  
案例数：72  
覆盖方向：范畴论与高阶范畴、代数、代数几何与下降、同伦论、分析、概率与测度、逻辑与组合、算术与局部整体、enriched/高阶边界。

---

## 0. 测试结论

本轮结论为：

\[
\boxed{
\text{INTERNAL CORE PASS AS AN }\mathcal S\text{-VALUED SECTOR}
}
\]

同时：

\[
\boxed{
\text{FAIL AS A CONSERVATIVE REPLACEMENT OF THE FULL FROZEN v1.0 SCOPE}
}
\]

72 个案例中没有发现 v0.1 内部定理的反例，也没有发现新的方差矛盾。但测试发现两个结构性缺口：

1. **domain-changing saturation gap**：v0.1 的
   \[
   L:\Fun(\mathcal A^{op}\times\mathcal B,\mathcal S)
   \to
   \Fun(\mathcal A^{op}\times\mathcal B,\mathcal S)
   \]
   固定 \(\mathcal A,\mathcal B\)。Gabriel–Zisman、Dwyer–Kan、Morita 等局部化会改变 candidate category 或其映射对象，一般不能证明其 derived mapping profunctor 是原 hom-profunctor 在这个固定函子范畴中的反射像。

2. **formal-comparison collapse gap**：v0.1 规定
   \[
   \mathsf{Formal}(a)=\mathfrak G(a).
   \]
   对 Grothendieck existence、Postnikov convergence、formal moduli comparison 等问题，只有取
   \[
   \mathcal A=*,\quad
   \mathcal B=\mathsf{Formal},\quad
   P(*,\xi)=*
   \]
   才能普遍编码。此时
   \[
   \mathfrak G(*)\simeq\mathsf{Formal},
   \]
   但 problem layer 没有产生 formal geometry，只是把它重新装入元素范畴。

因此 v0.1 是严格且自洽的 sector，但若要成为整个理论的新正式核心，至少需要一个 v0.2 修正：允许 problem/candidate categories 发生局部化，并恢复独立的 formal category，同时增加连接函子。

---

## 1. 压力测试标准

每个例子依次接受五项检查。

### S1：类型检查

能否明确给出

\[
\mathcal A,\quad
\mathcal B,\quad
P,\quad
P^\sharp,\quad
\mathsf{Act},\quad
C,\quad
\mathsf K,\quad
\mathbb O
\]

中实际需要的数据，并使所有函子方差一致？

### S2：非退化性检查

是否必须使用恒点函子

\[
P(*,\xi)=*
\]

并预先把整个 formal category 作为 \(\mathcal B\) 输入？若是，则只能证明 comparison layer 能容纳该例，不能证明 problem doctrine 生成了 formal geometry。

### S3：推导检查

是否有 v0.1 的某个定理真正参与推导，例如：

- initial object \(\Longleftrightarrow\) corepresentability；
- product preservation \(\Longleftrightarrow\) Pro-effectivity；
- effectivity fiber \(\Longleftrightarrow\) 本质满射；
- observation adequacy；
- horizon monotonicity；
- saturation invariance？

### S4：区分检查

模型能否区分一个相邻正例和反例，例如：

- effective 与 ineffective；
- unique type 与 contractible realization；
- objectwise effectivity 与 categorical reconstruction；
- local solvability 与 global effectivity；
- pointwise observation 与自然相容的 observation？

### S5：新增内容检查

是否得到一个不依赖本理论术语、可以由领域专家独立验证的新结论？

---

## 2. 判定标签

| 标签 | 含义 |
|---|---|
| **A — STRICT PASS** | 存在非退化严格配置，且 v0.1 的核心定理实际参与推导 |
| **B — CONDITIONAL PASS** | 配置忠实且有区分力，但主要数学结论仍由领域定理输入 |
| **C — COMPARISON ONLY** | 只能稳定地通过恒点函子或预装 formal category 编码 |
| **X — EXTENSION REQUIRED** | 若保留原问题的天然结构，需要 domain-changing、enriched、Prof-valued 或 \((\infty,2)\)-扩展 |
| **F — CORE FAIL** | 与 v0.1 的明确定理矛盾，或出现无法修正的内部类型错误 |

A 与 B 才计作非退化通过。C 只证明框架能记录已给定 comparison。X 是严格 sector 的边界，不自动构成内部反例。F 才触发直接否定。

---

## 3. 五种标准配置模板

### 模板 R：representability

给定

\[
U:\mathcal B\to\mathcal A,
\]

取

\[
P(a,b)=\Map_{\mathcal A}(a,U(b)),\qquad L=\id.
\]

则

\[
\mathfrak G(a)\simeq(a\downarrow U).
\]

初始对象等价于 \(P(a,-)\) 可余表示；若逐 \(a\) 成立，则得到

\[
F\dashv U.
\]

该模板是最稳定的 A 类来源。

### 模板 O：observation/probe

给定小 context category \(\mathsf K\) 及事件范畴 \(\mathsf E\)，取

\[
\mathbb O(k,e)=\Map_{\mathsf E}(i(k),e).
\]

则

\[
N_{\mathbb O}:\mathsf E\to\mathcal P(\mathsf K)
\]

是 restricted Yoneda。它 fully faithful 当且仅当 \(i(\mathsf K)\) 是 dense probing subcategory。

### 模板 E：effectivity

给定本来就存在的 comparison

\[
C:\mathsf{Actual}\to\mathsf{Formal},
\]

若另有非退化 problem geometry \(\mathfrak G\simeq\mathsf{Formal}\)，则 effectivity fiber 精确记录 actualizations。

### 模板 C：constant encoding

对任意 comparison，可取

\[
\mathcal A=*,\qquad
\mathcal B=\mathsf{Formal},\qquad
P(*,\xi)=*.
\]

于是

\[
\mathfrak G(*)\simeq\mathsf{Formal}.
\]

这个构造总是存在，所以只获得 C 判定。若允许它自动算作成功，则任何 comparison 都会无条件 PASS，压力测试将失去区分力。

### 模板 L：fixed-domain saturation

给定

\[
P\in\Fun(\mathcal A^{op}\times\mathcal B,\mathcal S)
\]

及该函子范畴上的反射局部化 \(L\)，取

\[
P^\sharp=L(P).
\]

该模板适合 descent condition、对象值等价闭包等固定 domain 的语义条件。若饱和过程改变 \(\mathcal A\) 或 \(\mathcal B\)，模板 L 一般不足。

---

## 4. 代表性详细测试

### 4.1 Free group

取

\[
\mathcal A=\mathbf{Set},\qquad
\mathcal B=\mathbf{Grp},\qquad
U:\mathbf{Grp}\to\mathbf{Set},
\]

以及

\[
P(S,G)=\operatorname{Hom}_{\mathbf{Set}}(S,U(G)).
\]

则

\[
\mathfrak G(S)\simeq(S\downarrow U).
\]

其初始对象为

\[
(F(S),\eta_S),
\]

故定理 4.1 恢复

\[
F\dashv U.
\]

整个 possibility category 仍包含所有带函数 \(S\to U(G)\) 的群，不会因初始对象存在而坍缩。

判定：**A — STRICT PASS**。

### 4.2 Gabriel–Zisman localization

给定 \((\mathcal C,W)\)，目标是

\[
\lambda:\mathcal C\to\mathcal C[W^{-1}]
\]

及 derived mapping spaces

\[
\Map_{\mathcal C[W^{-1}]}(\lambda x,\lambda y).
\]

若直接把

\[
\mathcal B=\mathcal C[W^{-1}]
\]

作为输入并令 \(L=\id\)，可以编码最终结果，但没有表达 raw-to-saturated 过程。

若保持 \(\mathcal A=\mathcal B=\mathcal C\)，v0.1 需要证明存在函子范畴反射

\[
L:\Fun(\mathcal C^{op}\times\mathcal C,\mathcal S)\to
\Fun(\mathcal C^{op}\times\mathcal C,\mathcal S)
\]

满足

\[
L(\Map_{\mathcal C}(-,-))
\simeq
\Map_{\mathcal C[W^{-1}]}(\lambda-,\lambda-).
\]

任意 \((\mathcal C,W)\) 下，这不是 Gabriel–Zisman 局部化泛性质的直接推论；反射 hom-bifunctor 与局部化整个范畴是不同层级的构造。

判定：**X — DOMAIN-CHANGING SATURATION REQUIRED**。

这是本轮最重要的结构边界。

### 4.3 Karoubi completion

在 world level 取：

\[
\mathcal A=\Cat_\infty,\qquad
\mathcal B=\Cat_\infty^{idem},
\]

\(U\) 为幂等完备 \(\infty\)-范畴的包含。令

\[
P(\mathcal C,\mathcal D)
=
\Map_{\Cat_\infty}(\mathcal C,U\mathcal D).
\]

Karoubi completion \(\operatorname{Idem}(\mathcal C)\) 余表示该函子：

\[
\Map_{\Cat_\infty^{idem}}
(\operatorname{Idem}(\mathcal C),\mathcal D)
\simeq
\Map_{\Cat_\infty}(\mathcal C,U\mathcal D).
\]

这是 scale polymorphism 的非退化严格实例。

判定：**A — STRICT PASS**。

### 4.4 Small dense probes

给定小满子范畴

\[
i:\mathsf K\hookrightarrow\mathsf E,
\]

取

\[
\mathbb O(k,e)=\Map_{\mathsf E}(i(k),e).
\]

persistent nerve 即 restricted Yoneda：

\[
N_i(e)=\Map_{\mathsf E}(i(-),e).
\]

按照定义 7.1：

\[
N_i\text{ adequate}
\quad\Longleftrightarrow\quad
N_i\text{ fully faithful}
\quad\Longleftrightarrow\quad
i(\mathsf K)\text{ dense}.
\]

这与 small probes 问题精确吻合。理论没有自动证明这样的小 \(\mathsf K\) 存在，但一旦给定候选，它准确表达充分性和重构缺口。

判定：**A — STRICT PASS**。

### 4.5 Algebraic closure

固定域 \(k\)。令 \(\mathfrak G(k)\) 的对象为 \(k\) 的代数闭包，态射为 \(k\)-嵌入。所有对象同构，所以

\[
\pi_0\mathcal M(k)=*.
\]

但一般存在非平凡的

\[
\operatorname{Aut}_k(\overline k),
\]

故

\[
\mathcal M(k)\simeq
B\operatorname{Aut}_k(\overline k)
\]

在选定基点后通常不可缩。

不存在初始对象，因为从一个代数闭包到另一个代数闭包的嵌入空间通常不是可缩单点。严格版本因此区分：

\[
\text{unique equivalence type}
\neq
\text{universal rigid solution}.
\]

判定：**A — STRICT PASS**。

### 4.6 Grothendieck existence

对适当形式完备情形，comparison 具有形状

\[
C:\operatorname{Coh}(X)
\longrightarrow
\varprojlim_n\operatorname{Coh}(X_n).
\]

effectivity 问题是 \(C\) 是否本质满射；完整重构是 \(C\) 是否等价。定义 5.1 与定理 5.2 正确区分这两个问题。

然而在 v0.1 中，要令 formal category 等于 possibility category，最普遍做法是：

\[
\mathcal A=*,\quad
\mathcal B=
\varprojlim_n\operatorname{Coh}(X_n),\quad
P(*,\xi)=*.
\]

这预先输入了整个 formal geometry。框架准确记录 Grothendieck existence 的结论，却没有从 problem doctrine 推出它。

判定：**C — COMPARISON ONLY**。

### 4.7 Banded gerbe

令 \(\mathsf{Formal}\) 为局部对象及其 descent data 的 \(\infty\)-范畴，\(\mathsf{Actual}\) 为全局对象范畴。comparison

\[
C:\mathsf{Actual}\to\mathsf{Formal}
\]

的效性纤维可以：

- 为空：gerbe 不 neutral；
- 非空连通但不可缩：存在全局对象并带非平凡 automorphisms；
- 可缩：刚性下降。

\(H^2\) obstruction 并非由抽象 effectivity fiber 自动产生；它来自具体 gerbe 的上同调理论。但 strict core 正确规定了 obstruction 应检测的目标。

判定：**B — CONDITIONAL PASS**。

### 4.8 Postnikov convergence

对具有 truncation 的 \(\infty\)-范畴 \(\mathcal C\)，取

\[
C_{\mathrm{Post}}:
\mathcal C\to
\varprojlim_n\mathcal C_{\le n},
\qquad
X\mapsto(\tau_{\le n}X)_n.
\]

则：

- 每个 compatible tower 是否在 \(C_{\mathrm{Post}}\) 的本质像中，是 effectivity；
- \(X\) 是否由全部 truncations 重构，是 \(C_{\mathrm{Post}}\) 的 fully faithfulness；
- left completeness 是 comparison equivalence。

严格版本成功区分这三层，但通常仍需模板 C 才把 tower category 作为 \(\mathfrak G(*)\) 输入。left-completeness theorem 来自具体 \(t\)-structure，而不是抽象核心。

判定：**C — COMPARISON ONLY**。

### 4.9 Phantom maps

令 \(\mathsf K\) 是 finite/compact probes，并取

\[
N_{\mathsf K}(X)
=
\Map(i(-),X).
\]

phantom map 给出一个非零态射

\[
f:X\to Y
\]

却对所有 compact probes \(k\) 诱导零映射。于是 restricted nerve 对态射不 faithful。

严格版本把失败精确定位为：

\[
N_{\mathsf K}\text{ 不 fully faithful}.
\]

扩大 context family 可以恢复区分力，且与定理 7.4 的 horizon 单调性一致。

判定：**B — CONDITIONAL PASS**。

### 4.10 Banach completion

令 \(\mathbf{Norm}\) 为赋范空间及线性收缩映射的范畴，\(\mathbf{Ban}\) 为 Banach 空间满子范畴，\(U\) 为包含。取

\[
P(V,B)=\operatorname{Hom}_{\mathbf{Norm}}(V,U(B)).
\]

完备化 \(\widehat V\) 满足

\[
\operatorname{Hom}_{\mathbf{Ban}}(\widehat V,B)
\cong
\operatorname{Hom}_{\mathbf{Norm}}(V,U(B)).
\]

故它是模板 R 的严格实例。范数信息通过对象和允许的收缩态射保存，不必在此例中使用 Ban-enriched mapping object。

但若研究 weighted enriched limits、算子范数的连续变化或 metric enrichment 本身，空间值核心只能看到底层映射空间。

判定：**A — STRICT PASS FOR THE REFLECTIVE UNIVERSAL PROPERTY**。

### 4.11 Lax–Milgram

固定 Hilbert 空间 \(H\)、连续 coercive 双线性形式 \(a\) 和线性泛函 \(f\)。令 possibility space 为

\[
\{u\in H:
a(u,v)=f(v)\ \forall v\in H\}.
\]

Lax–Milgram 定理说明该空间恰有一个点。它可以作为某个

\[
P^\sharp(\text{data},H)
\]

的纤维，或作为 effectivity fiber。

严格版本正确表达：

\[
\text{existence}+\text{uniqueness}
\Longleftrightarrow
\operatorname{EffFib}\simeq *.
\]

但 coercivity 如何迫使该纤维可缩，全部来自分析定理；抽象核心没有导出这一 implication。

判定：**B — CONDITIONAL PASS**。

### 4.12 Kolmogorov extension

设 \(I\) 为指标集。令

\[
\mathsf{Formal}
\]

为所有有限维分布组成的 compatible projective systems，令

\[
\mathsf{Actual}
\]

为 \(X^I\) 上的概率测度，并令 \(C\) 取全部有限维边缘分布。

Kolmogorov extension 是 \(C\) 的对象效性定理；在标准 Borel 等适当条件下还获得相应唯一性。

effectivity fiber 精确记录具有指定边缘族的全部全局测度。但 formal category 仍需独立输入，且紧性、可测性等条件来自概率论。

判定：**B — CONDITIONAL PASS**。

### 4.13 First-order compactness

固定语言 \(L\)。formal data 可取有限子理论的 compatible model/consistency data，actual object 为整个理论的模型。

紧致性定理提供：

\[
\forall T_0\subseteq_{\mathrm{fin}}T,\
\operatorname{Mod}(T_0)\neq\varnothing
\quad\Longrightarrow\quad
\operatorname{Mod}(T)\neq\varnothing.
\]

strict core 可以把右侧理解为全局 effectivity，并把有限子理论作为 contexts。它还能与 \(L_{\omega_1,\omega}\) 的紧致性失败形成相邻反例。

紧致性本身仍是 sector promotion theorem。

判定：**B — CONDITIONAL PASS**。

### 4.14 Tate–Shafarevich obstruction

对数域上的交换簇 \(A\)，局部可解 torsor 形成 local/formal data；全局 torsor 是 actual object。局部平凡但全局非平凡的类由

\[
\Sha(A)
\]

检测。

strict core 正确预言的只是：

\[
\text{所有局部效性纤维非空}
\not\Rightarrow
\text{全局效性纤维非空}.
\]

\(\Sha(A)\) 作为具体 obstruction group 来自算术几何。它是 core 所允许的 derived obstruction，而不是 core 自动构造出的对象。

判定：**B — CONDITIONAL PASS**。

### 4.15 Lawvere metric enrichment

在 \([0,\infty]\)-enriched category 中，hom-object 是距离值而不是空间。加权极限、Cauchy completion 和 Isbell completion 依赖 quantale enrichment。

若只取底层普通范畴或离散 mapping spaces，不同距离可能给出同一个空间值 profunctor；因此不能从 v0.1 的 \(\mathcal S\)-值数据恢复原 enriched universal property。

可以人工把距离作为对象标签编码，但这不等价于保留 enriched composition：

\[
d(x,z)\le d(x,y)+d(y,z).
\]

判定：**X — ENRICHED EXTENSION REQUIRED**。

### 4.16 Spectral-sequence revision dynamics

一个 \(E_r\)-page 的类未必给出下一页的类。一般只有

\[
Z_r\hookrightarrow E_r
\quad\text{和}\quad
Z_r\twoheadrightarrow E_{r+1}
\]

组成的 span，而没有定义在全部 \(E_r\) 上的单值输运

\[
E_r\to E_{r+1}.
\]

固定 context category \(\mathsf K\) 可以记录各页信息，但若要追踪“某个 witness 如何存活、死亡或分裂”，自然 dynamics 是 relation/profunctor-valued，而非 functor-valued。

判定：**X — PROF-VALUED DYNAMICS REQUIRED**。

---

## 5. 72 例总表

下表中的“锚点”给出该例进入严格理论的主要数学对象；它不是用新术语替换原定理。

### 5.1 范畴论与高阶范畴

| # | 例子 | 严格锚点 | 主要检验 | 判定 |
|---:|---|---|---|---|
| 1 | free group | \((S\downarrow U_{\mathbf{Grp}})\) 的初始对象 | representability、whole moduli | A |
| 2 | presheaf free cocompletion | \(\mathcal C\to\mathcal P(\mathcal C)\) 的 Kan-extension 泛性质 | world-level objectification | A |
| 3 | accessible reflective localization | \(L\dashv i:\mathcal C_{\rm loc}\hookrightarrow\mathcal C\) | reduct sector | A |
| 4 | Gabriel–Zisman localization | \(\mathcal C\to\mathcal C[W^{-1}]\) | fixed-domain saturation | X |
| 5 | Karoubi completion | \(\operatorname{Idem}\dashv U\) | scale polymorphism | A |
| 6 | restricted Yoneda/density | \(N_i(e)=\Map(i(-),e)\) | observation adequacy | A |
| 7 | Barr–Beck monadicity | comparison \(\mathcal B\to\operatorname{Alg}_{UF}(\mathcal A)\) | reconstruction | B |
| 8 | Isbell duality | observation profunctor诱导的 Isbell adjunction | variance、双重表示 | B |

### 5.2 代数与表示论

| # | 例子 | 严格锚点 | 主要检验 | 判定 |
|---:|---|---|---|---|
| 9 | free commutative algebra | \(\operatorname{Sym}\dashv U\) | functorial objectification | A |
| 10 | group completion | \((M\downarrow U_{\mathbf{Grp}})\) 初始对象 | reflector 可改变对象 | A |
| 11 | universal enveloping algebra | \(U(\mathfrak g)\dashv(-)_{\rm Lie}\) | carrier-changing generation | A |
| 12 | algebraic closure | connected noncontractible moduli | unique type 与 isotropy | A |
| 13 | injective hull | essential extensions 的 minimal locus | weak universality、automorphism | B |
| 14 | universal central extension | effectivity obstruction \(H_2(G)\) | obstruction extraction | B |
| 15 | minimal free resolution | resolutions modulo chain equivalence | provenance/gauge | B |
| 16 | profinite completion | \(\widehat{(-)}\dashv U_{\rm profinite}\) | completion 的 universal sector | A |

### 5.3 代数几何、下降与形变

| # | 例子 | 严格锚点 | 主要检验 | 判定 |
|---:|---|---|---|---|
| 17 | sheafification | \(a:\operatorname{PSh}\leftrightarrows\operatorname{Sh}:i\) | reflective objectification | A |
| 18 | stackification/hyperdescent | higher descent localization | saturation 与高阶相干 | B |
| 19 | Hilbert scheme | Hilbert moduli functor 的 representability | possibility functor | A |
| 20 | Picard stack | groupoid-valued descent data | isotropy、stack saturation | B |
| 21 | Grothendieck existence | \(\operatorname{Coh}(X)\to\lim_n\operatorname{Coh}(X_n)\) | effectivity/reconstruction | C |
| 22 | Artin approximation | formal solution到近似 actual solution | approximation 与 realization | C |
| 23 | formal moduli / dg Lie | controller 与 formal problems 的 equivalence | coordinatization | C |
| 24 | banded gerbe | global objects \(\to\) descent data | empty/noncontractible fibers | B |

### 5.4 同伦论与稳定范畴

| # | 例子 | 严格锚点 | 主要检验 | 判定 |
|---:|---|---|---|---|
| 25 | Bousfield localization | \(L:\mathcal C\leftrightarrows\mathcal C_L:i\) | reflective homotopy localization | A |
| 26 | Postnikov convergence | \(\mathcal C\to\lim_n\mathcal C_{\le n}\) | tower effectivity | C |
| 27 | non-left-complete \(t\)-structure | 上述 comparison 非等价 | formal tower 不重构 actual | C |
| 28 | plus construction | 指定同调与 \(\pi_1\) 约束的 localization | observation-relative novelty | A |
| 29 | stabilization | \(\operatorname{Sp}(\mathcal C)\) 的 universal property | world-level generation | A |
| 30 | Brown representability | cohomological functor的 representability | 定理 9.1 | A |
| 31 | phantom maps | compact restricted nerve 不 faithful | observation inadequacy | B |
| 32 | Dwyer–Kan/hammock localization | mapping spaces随 category localization 产生 | domain-changing saturation | X |

### 5.5 分析、泛函分析与 PDE

| # | 例子 | 严格锚点 | 主要检验 | 判定 |
|---:|---|---|---|---|
| 33 | Banach completion | \(\widehat{(-)}\dashv U:\mathbf{Ban}\to\mathbf{Norm}\) | ordinary universal property | A |
| 34 | Lax–Milgram | solution effectivity fiber | coercivity engine | B |
| 35 | Fredholm alternative | kernel/cokernel obstruction | scalar之外的 obstruction | B |
| 36 | GNS construction | cyclic representation的 universal pair | quotient、completion、gauge | A |
| 37 | Stinespring dilation | minimal dilation universal locus | minimality与 unitary gauge | A |
| 38 | Michael selection theorem | sections 的 possibility space | existence without rigidity | B |
| 39 | Arzelà–Ascoli | precompact family \(\to\) convergent subnet | extraction 而非 object effectivity | C |
| 40 | weak PDE solutions + Rellich | approximate sequence \(\to\) limit solution | compact extraction、closure | C |

### 5.6 概率与测度

| # | 例子 | 严格锚点 | 主要检验 | 判定 |
|---:|---|---|---|---|
| 41 | Carathéodory extension | measure extensions 的 fiber | existence/uniqueness hypotheses | B |
| 42 | Kolmogorov extension | global measure \(\to\) finite marginals | inverse-system effectivity | B |
| 43 | regular conditional probability | conditional kernels modulo a.s. equality | gauge 与非唯一版本 | B |
| 44 | Radon–Nikodym | densities modulo a.e. equality | quotient 后的刚性 | B |
| 45 | moment problem | measures \(\to\) moment sequences | determinate/indeterminate fibers | B |
| 46 | Prokhorov theorem | tight family \(\to\) convergent subnet | extraction promotion | C |
| 47 | martingale convergence | stage system \(\to\) a.s./\(L^p\) limit | topology依赖的 completion | C |
| 48 | Egorov theorem | a.e. convergence \(\to\) almost uniform | exceptional-budget promotion | C |

### 5.7 逻辑、模型论与组合

| # | 例子 | 严格锚点 | 主要检验 | 判定 |
|---:|---|---|---|---|
| 49 | first-order compactness | finite contexts \(\to\) global model | local-to-global promotion | B |
| 50 | Henkin construction | proof-relevant branch choices | procedure 与 semantic outcome | B |
| 51 | Fraïssé limit | finite amalgamation data \(\to\) limit | universality与 homogeneity | B |
| 52 | Rado graph | extension property的 rigid countable type | moduli与 framing | B |
| 53 | de Bruijn–Erdős coloring | finite colorability \(\to\) global coloring | compactness engine | B |
| 54 | Helly theorem | \((d+1)\)-subfamilies \(\to\) global intersection | bounded test rank | B |
| 55 | Aronszajn tree | 所有低层非空但无 cofinal branch | transfinite effectivity failure | B |
| 56 | spectral-sequence revision | \(Z_r\hookrightarrow E_r\), \(Z_r\twoheadrightarrow E_{r+1}\) | nonfunctorial witness transport | X |

### 5.8 算术与局部整体

| # | 例子 | 严格锚点 | 主要检验 | 判定 |
|---:|---|---|---|---|
| 57 | Hasse–Minkowski | rational solutions \(\to\) all local solutions | adequate local contexts | B |
| 58 | Tate–Shafarevich group | local triviality vs global torsor | explicit obstruction | B |
| 59 | Grunwald–Wang | prescribed local extensions | exceptional obstruction | B |
| 60 | infinite CRT | integer \(\to\) compatible profinite residues | completion vs realization | B |
| 61 | torsor descent | global torsor \(\to\) local descent data | nonabelian effectivity | B |
| 62 | banded \(H^2\)-gerbes | neutral objects \(\to\) cocycles | higher obstruction | B |
| 63 | finite étale descent | finite covers \(\to\) descent systems | comparison equivalence | B |
| 64 | adelic vs rational points | \(X(K)\to X(\mathbb A_K)\) | local observations不充分 | B |

### 5.9 Enriched、高阶与量化边界

| # | 例子 | 严格锚点 | 主要检验 | 判定 |
|---:|---|---|---|---|
| 65 | Lawvere metric spaces | \([0,\infty]\)-enriched hom | quantale enrichment | X |
| 66 | Banach-enriched adjunction | Banach mapping objects | norm-enriched representability | X |
| 67 | dg-enriched Morita localization | dg hom-complexes、bimodules | enriched/domain-changing localization | X |
| 68 | \((\infty,2)\)-categorical moduli | 非可逆 2-morphisms | space值 profunctor不足 | X |
| 69 | derived stacks | space值 functor of points + descent | higher moduli、effectivity | B |
| 70 | operator spaces/cb-norm | matrix norms 与 completely bounded maps | quantitative enrichment | X |
| 71 | stochastic path-space realization | finite-dimensional laws \(\to\) path law | topology与 measurability | B |
| 72 | quantitative PDE estimates | solution + stability constants | enriched error profiles | X |

---

## 6. 统计

本轮 72 例的主判定为：

| 判定 | 数量 | 比例 |
|---|---:|---:|
| A — STRICT PASS | 19 | 26.4% |
| B — CONDITIONAL PASS | 34 | 47.2% |
| C — COMPARISON ONLY | 10 | 13.9% |
| X — EXTENSION REQUIRED | 9 | 12.5% |
| F — CORE FAIL | 0 | 0% |
| **合计** | **72** | **100%** |

非退化通过数为

\[
19+34=53,
\]

即

\[
\frac{53}{72}\approx73.6\%.
\]

这不是理论正确率或预测成功率。它只表示：在 72 个选择案例中，53 个可以在不使用恒点退化编码、也不丢失主要语义类型的情况下进入严格核心。

真正由 v0.1 本身产生的新领域独立结论，当前仍主要是：

\[
\text{任意正则 }\kappa\text{ 上的 product effectivity rank 构造}.
\]

其余 A 类多数是严格恢复已有 universal property；B 类主要依靠领域定理。

---

## 7. 各核心模块的压力结果

### 7.1 Pre-target problem 与 representability：最强模块

free group、free commutative algebra、universal enveloping algebra、group completion、Karoubi completion、Banach completion、Bousfield localization、stabilization、Hilbert scheme 等均可由非退化

\[
P:\mathcal A^{op}\times\mathcal B\to\mathcal S
\]

表示。

这些案例一致验证：

\[
\mathfrak G(a)\text{ 有初始对象}
\quad\Longleftrightarrow\quad
P(a,-)\text{ 可余表示}.
\]

没有发现定理 4.1 或 functorial objectification 的反例。

但这些案例多数来自已知 universal property。核心在这里提供统一且正确的组织语言，不自动产生新的 universal object。

### 7.2 Generative moduli：区分力稳定

algebraic closure、Picard stack、gerbe、minimal resolutions、Stinespring dilation 等表明，下列四种情况必须分开：

\[
\varnothing,\qquad
|\pi_0|\ge2,\qquad
\text{connected noncontractible},\qquad
\simeq *.
\]

尤其 algebraic closure 提供清楚的负控制：

\[
\text{唯一等价类型}
\not\Rightarrow
\text{存在初始对象}.
\]

whole-moduli 与 universal-locus 的区分通过测试。

### 7.3 Effectivity fiber：定义正确，来源外在

gerbe descent、Kolmogorov extension、moment problem、Lax–Milgram、Hasse failures、Grothendieck existence 都能由

\[
\operatorname{EffFib}(\xi)
\]

区分：

- 不存在 actualization；
- 多个 actualizations；
- 唯一对象类型但有 automorphisms；
- object-rigid effectivity。

定理 5.2 通过所有正负控制。主要限制是：core 规定了 obstruction 要检测什么，却一般不构造 \(H^2\)、\(\Sha\)、kernel/cokernel、coercivity estimate 等 sector obstruction。

### 7.4 Reconstruction：fully faithful 条件不可删除

以下例子共同表明：

- Grothendieck existence 要区分本质满射与 equivalence；
- Postnikov towers 要区分 tower 可实现与 actual category 可重构；
- phantom maps 表明对象探测不能代替态射探测；
- formal moduli equivalence 需要 mapping spaces 级相容。

因此

\[
\text{所有 effectivity fibers 非空}
\]

不能推出

\[
C:\mathsf{Actual}\to\mathsf{Formal}
\text{ 是等价}.
\]

这一核心边界通过压力测试。

### 7.5 Persistent observation：对 probes 有效

restricted Yoneda、compact probes、adelic observations 与 finite truncations 表明：

\[
N_{\mathbb O}\text{ fully faithful}
\]

是一个正确而有力的 adequacy 标准。

负控制包括：

- phantom maps：finite probes 不检测全部态射；
- homotopy groups：逐群同构不等于包含全部 \(k\)-invariants 的重构数据；
- adelic points：局部点不充分检测有理点；
- pointwise isomorphism：不保证 presheaf 自然等价。

定理 7.4 的 horizon 单调性没有失败，但其假设

\[
N_0=r^*N_1
\]

是必要的。若扩大 horizon 时同时改变 gauge 或 observation law，则不能套用该定理。

### 7.6 Saturation：适用性最弱

定理 8.1 本身是正确的：

\[
L(P)\simeq L(Q)
\Longrightarrow
\mathfrak G_P\simeq\mathfrak G_Q.
\]

压力问题发生在它的输入端：是否存在所需的固定-domain reflector \(L\)。

在大多数 A/B 例中，实际做法是：

- 直接把已经局部化的 category 当作 \(\mathcal B\)；
- 把局部化写成另一个 adjunction；
- 把 gauge 放入 provenance localization \(q\)；
- 或令 \(L=\id\)。

这意味着 nontrivial \(L\) 在本轮并未得到与其他模块同等强度的验证。它目前更像一个合法接口，而不是已证明足以覆盖主要 saturation mechanisms 的统一构造。

### 7.7 Provenance：可记录，但不能内生选择 gauge

Henkin constructions、minimal resolutions、GNS、Stinespring 及不同证明路径都可放入

\[
\widetilde{\mathsf E}\xrightarrow q\mathsf E^{GM}
\xrightarrow{\overline p}\mathsf E^{sem}.
\]

这个结构正确表达：

\[
\text{same semantics}
\not\Rightarrow
\text{same normalized provenance}.
\]

但哪些态射属于 \(W\) 仍是外部 doctrine。strict core 没有从 bare event category 推出规范的 \(W\)。

### 7.8 Anti-tautology：研究纪律有效，尚非内部性质

量词顺序

\[
\forall\Xi\,\forall x
\]

确实排除了显式的

\[
\forall x\,\exists\Xi_x.
\]

但一份最终写出的配置本身不能证明研究者在历史上没有利用目标答案来选择 \(P,L,\mathbb O\)。若需要机器可审计的 pre-target 性质，必须增加：

- 依赖图；
- 版本时间戳；
- 允许输入的形式签名；
- proof-relevant provenance certificate。

因此 anti-tautology 目前是严格的协议条件，还不是配置内部可判定的同伦不变量。

---

## 8. 四组关键负控制

### 8.1 唯一性负控制

| 正例 | 负例 | core 区分 |
|---|---|---|
| free object 的 universal locus 可缩 | algebraic closure 只有唯一类型但有 isotropy | initiality vs connected moduli |
| Lax–Milgram 唯一解 | moment problem 可有多个测度 | contractible vs noncontractible fiber |

### 8.2 局部整体负控制

| 正例 | 负例 | core 区分 |
|---|---|---|
| Hasse–Minkowski 的完整 local tests | \(\Sha\neq0\) 的 torsors | adequate vs inadequate contexts |
| finite étale descent | non-neutral gerbe | comparison equivalence vs empty fiber |
| first-order compactness | Aronszajn tree | promotion hypothesis成立与失败 |

### 8.3 重构负控制

| 正例 | 负例 | core 区分 |
|---|---|---|
| dense restricted Yoneda | phantom maps | fully faithful nerve vs nonfaithful nerve |
| left-complete \(t\)-structure | non-left-complete \(t\)-structure | comparison equivalence vs failure |
| determinate moment problem | indeterminate moment problem | rigid vs branching fiber |

### 8.4 饱和负控制

| 可由 v0.1 严格处理 | 需要扩展 |
|---|---|
| 已知 reflector \(L\dashv i\) | arbitrary Gabriel–Zisman localization |
| Bousfield reflective localization | Dwyer–Kan hammock mapping spaces |
| sheafification reflector | dg Morita localization |
| event provenance localization \(q\) | candidate category 本身发生变化的 saturation |

这些负控制说明本轮不是“所有例子都可以事后解释”的兼容性列表。

---

## 9. 对 v0.1 各定理的审计判决

| v0.1 结果 | 压力测试判决 | 说明 |
|---|---|---|
| 定理 4.1：initiality \(\Leftrightarrow\) corepresentability | PASS | 多个代数、几何、分析 universal properties |
| 推论 4.2：pointwise representability 组装为 functor | PASS | free constructions 与 completions |
| 定理 5.2：effectivity/reconstruction | PASS | 正负 comparison 案例均吻合 |
| 命题 6.1：provenance localization factorization | PASS | 局部化泛性质直接保证 |
| 定理 7.3：adequate observation 下的 novelty | PASS | restricted Yoneda sector |
| 定理 7.4：horizon monotonicity | PASS WITH HYPOTHESIS | 仅在 restriction-compatible horizons 下 |
| 定理 8.1：saturation invariance | INTERNAL PASS | 定理正确，输入 \(L\) 的覆盖力不足 |
| 定理 9.1：accessible representability | PASS | Brown/Pro sectors |
| 定理 9.2：Pro-objectification | PASS | left-exact accessible functors |
| 定理 10.1：超限 product rank | PASS | 证明中未发现集合论或量词缺口 |
| 命题 12.1：doctrine symmetry no-go | PASS | 结论范围经过收窄后正确 |

---

## 10. 是否触发 core modification

### 对“空间值严格 sector”本身

没有发现：

- 内部矛盾；
- 类型不一致；
- 某个明确 theorem 被反例否定。

因此：

\[
\boxed{\text{NO INTERNAL CORE FAIL}}
\]

### 对“替代 Frozen v1.0 全部范围”的主张

发现了明确的覆盖失败：

1. 一般 domain-changing localization 不能由 fixed-domain \(L\) 保证；
2. formal comparison 常被迫使用 constant encoding；
3. genuine \(\mathbf{Met}\)、\(\mathbf{Ban}\)、dg、\((\infty,2)\) enrichment 不能无损恢复；
4. nonfunctorial witness dynamics 需要 profunctor/span。

所以：

\[
\boxed{
\text{v0.1 不能以“保守等价”的方式直接替代全部 Frozen v1.0}
}
\]

这与“v0.1 可以作为较窄但严格的正式核心”并不矛盾。

---

## 11. v0.2 的最小修正方案

### 修正 A：允许 domain-changing saturation

把单一 endofunctor

\[
L:\Fun(\mathcal A^{op}\times\mathcal B,\mathcal S)
\to
\Fun(\mathcal A^{op}\times\mathcal B,\mathcal S)
\]

推广为：

\[
\lambda_{\mathcal A}:\mathcal A\to\mathcal A^\sharp,
\qquad
\lambda_{\mathcal B}:\mathcal B\to\mathcal B^\sharp,
\]

以及 saturated profunctor

\[
P^\sharp:
(\mathcal A^\sharp)^{op}\times\mathcal B^\sharp
\to\mathcal S
\]

和比较 2-cell

\[
\eta:
P
\longrightarrow
(\lambda_{\mathcal A}^{op}\times\lambda_{\mathcal B})^*P^\sharp.
\]

要求 \((P^\sharp,\eta)\) 对发送指定 weak equivalences 为等价的 profunctors 满足泛性质。

fixed-domain reflective localization 是特殊情形：

\[
\mathcal A^\sharp=\mathcal A,\qquad
\mathcal B^\sharp=\mathcal B.
\]

这一修正直接覆盖 Gabriel–Zisman、Dwyer–Kan 和 Morita 型 saturation。

### 修正 B：恢复独立 Formal，并强制连接

保留：

\[
\mathfrak G:\mathcal A^{op}\to\Cat_\infty
\]

作为 possibility geometry，另给：

\[
\mathsf{Formal}:\mathcal A^{op}\to\Cat_\infty.
\]

增加自然变换：

\[
R:\mathsf{Act}\to\mathfrak G,
\qquad
\Phi:\mathfrak G\to\mathsf{Formal},
\qquad
C:\mathsf{Act}\to\mathsf{Formal},
\]

以及指定自然等价

\[
C\simeq\Phi R.
\]

于是：

- \(R\) 说明 actual object 是哪个 possibility；
- \(\Phi\) 说明 possibility 如何产生 formal datum；
- \(C\) 是 effectivity comparison；
- v0.1 是
  \[
  \mathsf{Formal}=\mathfrak G,\quad
  \Phi=\id,\quad
  C=R
  \]
  的特殊情形。

Grothendieck existence 和 Postnikov convergence 不再需要 constant encoding：actual objects 先进入可能性几何，再由 completion/truncation functor \(\Phi\) 进入 formal towers。

### 修正 C：把 dynamics 分层

保留 functorial sector：

\[
T:\mathsf D\to\Cat_\infty.
\]

另允许 relational sector：

\[
\mathbb T:
\mathsf D^{op}\times\mathsf D
\to\operatorname{Prof}_{\mathcal S}
\]

或以 span/correspondence 表示 witness transport。

只有在这些 proarrows 可表示时，才退化为普通 functor dynamics。这可覆盖 spectral sequences、非唯一 lifting 与 branch-changing procedures。

### 修正 D：enrichment 作为扩展接口

核心继续以 \(\mathcal S\) 为默认基础，但定义一个明确的 extension schema：

\[
\mathcal V\text{-Prof},
\qquad
\mathcal V\in
\{\mathbf{Met},\mathbf{Ban},\mathbf{Ch},\Cat_\infty,\ldots\}.
\]

每个 \(\mathcal V\)-扩展必须单独证明：

1. Grothendieck construction 或其替代物存在；
2. saturation 与 weighted limits 良定义；
3. 到 \(\mathcal S\)-核心的 forgetful functor 保留哪些结论；
4. 哪些 quantitative/enriched 信息会丢失。

---

## 12. 最终研究判定

严格版本成功解决了原理论最明显的良定义问题。尤其：

- profunctor 方差已经统一；
- possibility geometry 有确定构造；
- effectivity fiber 不再含糊；
- observation-relative novelty 有精确判据；
- Pro-sector 具有真正的超限测试秩定理。

大规模测试同时表明，v0.1 仍把两个本应独立的层压在一起：

\[
\text{possibility geometry}
\quad\text{与}\quad
\text{formal/local geometry}.
\]

并且它把 saturation 限制在固定 domain 的 functor category 中。

因此当前最合理的版本治理是：

\[
\boxed{
\begin{array}{c}
\text{Strict v0.1: audited stable sector}\\[2mm]
\text{Strict v0.2: replacement candidate after repairs A+B}\\[2mm]
\text{Enriched modules: separate extensions}
\end{array}
}
\]

若只研究空间值 representability、effectivity 和 observation，v0.1 已可继续使用。若目标是替代 Frozen v1.0 成为完整正式核心，则不应冻结 v0.1；应先完成修正 A 与 B，再重新运行本报告中的 72 个测试。
