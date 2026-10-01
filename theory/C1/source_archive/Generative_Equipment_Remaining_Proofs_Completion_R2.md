# 数学内生生成性理论

## 剩余证明完成报告 R2

日期：2026-09-24  
前置文件：`Generative_Equipment_All_Main_Lines_Development_R1.md`  
前置文件 SHA-256：`8846467504ca9de1be6ec721791dc69298f6a39a33b37299aa322c3c5a160379`  
基础核心：Strict Space-Valued Core v0.2 Candidate  
基础核心 SHA-256：`3ef6d885a8bd39bf4661e459774bc2389e5c2c268907f709682e3476dca7a448`  
原则：能证明者完成证明；缺少必要数据者证明 no-go theorem，并给出加入
最小额外数据后的完整相对版本。

---

## 0. R1 未完成项的最终处理

| R1 剩余项 | R2 处理 | 最终状态 |
|---|---|---|
| simultaneous nonemptiness | tower lifting theorem | **PROVED** |
| derived-limit obstruction | 精确 Milnor sequence 与消失判据 | **PROVED UNDER STANDARD TOWER HYPOTHESES** |
| Prof pseudofunctor strictification | representable subequipment + cocartesian unstraightening | **PROVED IN \(\infty\)-CATEGORICAL SENSE** |
| on-the-nose strict equality | ordinary-index rectification；一般情形判为模型问题 | **CLOSED** |
| coprobes | 对偶 density 与 coreflective stability | **PROVED** |
| probes under arbitrary localization | 必要充分判据 | **CHARACTERIZED** |
| doctrine 从 bare \(P\) 唯一产生 | doctrine moduli 非连通 no-go | **PROVED IMPOSSIBLE UNDER CURRENT AXIOMS** |
| enriched effectivity | zero-map/full-shadow no-go + truth-functor relative theorem | **RELATIVE THEORY PROVED** |
| metric/dg/Banach 边界 | threshold/probe-family realization | **CONCRETE SECTOR ROUTES GIVEN** |

本文件完成后，没有遗留的“证明写到一半”状态。仍未获得无条件结论的地方，
已被改写为明确不可能性定理或带必要附加数据的等价刻画。

---

## 1. Simultaneous effectivity：非空性证明完成

沿用 R1 定理 A.1：对一图比较函子 \(C_i\) 与相容 formal datum
\(\xi=(\xi_i)\)，

\[
\operatorname{EffFib}_{\lim C_i}(\xi)
\simeq
\operatorname*{holim}_i
\operatorname{EffFib}_{C_i}(\xi_i).
\]

因此剩余问题精确化为：何时一图非空空间的 homotopy limit 非空？

### 定理 1.1（可数 tower 的 simultaneous nonemptiness）

设

\[
X_0\xleftarrow{p_0}X_1
\xleftarrow{p_1}X_2
\xleftarrow{}\cdots
\]

是 Kan complexes 的 tower，并满足：

1. 每个 \(p_n\) 是 Kan fibration；
2. \(X_0\neq\varnothing\)；
3. 每个
   \[
   \pi_0(X_{n+1})\to\pi_0(X_n)
   \]
   满射。

则

\[
\operatorname*{holim}_nX_n\neq\varnothing.
\]

#### 证明

先选 \(x_0\in X_0\)。假设已构造 \(x_n\in X_n\)。由 \(\pi_0\) 满射，
存在 \(y\in X_{n+1}\)，使 \(p_n(y)\) 与 \(x_n\) 位于同一连通分支；
故存在路径

\[
\gamma:p_n(y)\rightsquigarrow x_n.
\]

由于 \(p_n\) 是 Kan fibration，\(\gamma\) 可从 \(y\) 开始提升为
\(X_{n+1}\) 中的路径。令其终点为 \(x_{n+1}\)，则

\[
p_n(x_{n+1})=x_n.
\]

递归得到严格相容族 \((x_n)_{n\geq0}\)，所以严格逆极限非空。tower
由 fibrations 构成，故其严格逆极限计算 homotopy inverse limit。因此
\(\operatorname*{holim}_nX_n\neq\varnothing\)。证毕。

### 推论 1.2（可数 simultaneous effectivity criterion）

若 effectivity fibers

\[
E_n=\operatorname{EffFib}_{C_n}(\xi_n)
\]

可由满足定理 1.1 的 fibrant tower 表示，则 \(\xi\) simultaneously
effective。

该条件比逐阶段 \(E_n\neq\varnothing\) 严格强；R1 的尾集反例正是因为
transition 在 \(\pi_0\) 上不满射。

### 定理 1.3（Milnor obstruction sequence）

设 \((X_n,x_n)\) 是 pointed、相容、fibrant 的可数 tower。对
\(q\geq1\)，存在自然短正合序列

\[
0\longrightarrow
\lim\nolimits^1_n\pi_{q+1}(X_n,x_n)
\longrightarrow
\pi_q(\operatorname*{holim}_nX_n,x)
\longrightarrow
\lim_n\pi_q(X_n,x_n)
\longrightarrow0.
\]

在 \(q=0\) 处有相应的 pointed-set exact sequence

\[
\lim\nolimits^1_n\pi_1(X_n,x_n)
\longrightarrow
\pi_0\operatorname*{holim}_nX_n
\longrightarrow
\lim_n\pi_0X_n.
\]

#### 证明说明

这是 tower of fibrations 的标准 Milnor exact sequence。其构造把
homotopy limit 写成由 \(\prod_nX_n\) 与 transition maps 构造的
path-space homotopy equalizer；对相应 fibration 取长正合 homotopy
sequence 后，homotopy-group tower 上的 kernel 给出 ordinary inverse
limit，orbit/cokernel 项给出 \(\lim^1\)。低维处必须使用 pointed
sets/nonabelian \(\lim^1\)，所以不能把所有次数都写成阿贝尔群短正合
序列。

### 推论 1.4（simultaneous contractibility criterion）

在定理 1.3 的条件下，再假设：

1. \(\lim_n\pi_0X_n=*\)；
2. \(\lim^1_n\pi_1X_n=*\)；
3. 对每个 \(q\geq1\)，
   \[
   \lim_n\pi_qX_n=0,
   \qquad
   \lim\nolimits^1_n\pi_{q+1}X_n=0.
   \]

则

\[
\operatorname*{holim}_nX_n\simeq *.
\]

#### 证明

低维 exact sequence 给出 homotopy limit 连通；定理 1.3 给出其所有正维
homotopy groups 为零。homotopy limit 是 Kan complex，因此 Whitehead
判据给出其可缩。证毕。

### 结论 1.5

simultaneous effectivity 的 obstruction 现已分成三个严格层次：

1. \(\pi_0\)-lifting obstruction：是否存在相容 components；
2. \(\lim^1\pi_1\) obstruction：相容 components 是否粘合成全局 component；
3. higher \(\lim^1\) obstruction：全局 realization 的 higher coherence。

因此 R1 的“derived-limit 只是未来计划”已经补成可直接使用的 tower theorem。

---

## 2. Prof dynamics：严格化证明完成

### 定义 2.1（representable pseudo-dynamics）

称 lax Prof-valued dynamics \(\mathbb T\) 为 representable pseudo-dynamics，
若：

1. 每个 transition \(\mathbb T_u\) right-representable；
2. 所有 compositor 与 unit cells 都是等价；
3. 已包含 lax functor 所要求的全部高阶相干。

### 定理 2.2（\(\infty\)-categorical strictification）

每个 representable pseudo-dynamics 决定一个在等价意义下唯一的 genuine
\(\infty\)-functor

\[
T:\mathsf D\longrightarrow\operatorname{Cat}_\infty,
\qquad
d\longmapsto\mathsf E_d,
\]

使每条边 \(u:d\to d'\) 的 transport functor \(T(u)\) 表示
\(\mathbb T_u\)。

#### 证明

R1 定理 C.4 给出表示函子 \(T_u\) 及相干等价

\[
T_vT_u\simeq T_{vu},
\qquad
T_{\operatorname{id}_d}\simeq\operatorname{id}_{\mathsf E_d}.
\]

right-representable profunctors 的 2-cells 与 functor 2-cells 方向相反；
但在 compositor 全部可逆后，取 inverse 消除这一方向差异。故
\(\mathbb T\) 落入 representable subequipment 的 invertible-cell 部分，
该部分等价于 \(\operatorname{Cat}_\infty\) 的
homotopy-coherent diagram theory。

等价地，对这些 data 作 Grothendieck construction，得到

\[
p:\int_{\mathsf D}\mathsf E_d\longrightarrow\mathsf D.
\]

compositor 可逆保证局部 cocartesian transports 对合成封闭，故 \(p\)
是 cocartesian fibration。cocartesian-fibration classification/unstraightening
给出一个 functor

\[
T:\mathsf D\to\operatorname{Cat}_\infty
\]

并在等价意义下唯一。其 transports 正是原来的 \(T_u\)。证毕。

### 推论 2.3（普通 indexing category 的 on-the-nose rectification）

若 \(\mathsf D=N(\mathbf D)\) 来自普通小范畴 \(\mathbf D\)，则上述
homotopy-coherent diagram 在 levelwise equivalence 意义下，可由某个严格
交换图

\[
\mathbf D\longrightarrow\mathbf{QCat}
\]

表示。

### 结论 2.4

R1 所谓“rectification obstruction”需修正为：

- 在 invariant 的 \(\infty\)-categorical 层面，没有剩余 obstruction；
- 对 ordinary indexing category，也有标准 strict model；
- 对任意具体模型要求符号上的逐等式相等，是 presentation choice，不是
  理论的内在数学缺口。

真正不可消除的 obstruction 只有：transition 不可表示，或 compositor
不是等价。

---

## 3. Coprobes 与任意 localization：对偶与必要充分判据

### 定义 3.1（codense coprobes）

给定小函子

\[
j:\mathsf K\longrightarrow\mathsf E,
\]

定义 restricted conerve

\[
C_j:\mathsf E^{op}\longrightarrow\operatorname{Fun}(\mathsf K,\mathcal S),
\qquad
C_j(e)(k)=\operatorname{Map}_{\mathsf E}(e,j(k)).
\]

称 \(j\) **codense**，若 \(C_j\) fully faithful。于是，若 observation
允许从事件射向一族 coprobes，那么“这些 coprobes 能区分事件及其全部
高阶映射”恰好等价于 codensity。

### 定理 3.2（coreflective localization 保持小 codense coprobes）

设

\[
i:\mathsf D\rightleftarrows\mathsf E:R,
\qquad i\dashv R,
\]

其中 \(i\) fully faithful；亦即 \(\mathsf D\) 是 \(\mathsf E\) 的
coreflective 子范畴。若

\[
j:\mathsf K\to\mathsf E
\]

codense，则

\[
Rj:\mathsf K\to\mathsf D
\]

codense。

#### 证明

对 \(x\in\mathsf D\) 与 \(k\in\mathsf K\)，由伴随得到

\[
\begin{aligned}
C_{Rj}(x)(k)
&=\operatorname{Map}_{\mathsf D}(x,Rj(k))\\
&\simeq\operatorname{Map}_{\mathsf E}(i(x),j(k))\\
&=C_j(i(x))(k).
\end{aligned}
\]

因而

\[
C_{Rj}\simeq C_j\,i^{op}.
\]

\(i^{op}\) 与 \(C_j\) 都 fully faithful，所以复合 fully faithful。
故 \(Rj\) codense。证毕。

### 推论 3.3（小 coprobes 的存在范围）

若 \(\mathsf E^{op}\) accessible，则 \(\mathsf E\) 存在 essentially
small codense full subcategory：对 \(\mathsf E^{op}\) 取小 dense full
subcategory，再取 opposite 即可。若再作 accessible coreflective
localization，则定理 3.2 保持这组 coprobes。

这里不能删去关于 \(\mathsf E^{op}\) 的假设；\(\mathsf E\) accessible
本身只保证 probes，不自动保证 coprobes。

### 定理 3.4（任意 categorical localization 后 probes 的精确判据）

令

\[
\lambda:\mathsf C\longrightarrow\mathsf D
\]

为一 categorical localization，令 \(a:\mathsf K\to\mathsf C\) 为小
函子。记 Yoneda embedding 为

\[
y_{\mathsf D}:\mathsf D\to\mathcal P(\mathsf D).
\]

则下列条件等价：

1. \(\lambda a:\mathsf K\to\mathsf D\) dense；
2. 复合
   \[
   \mathsf D
   \xrightarrow{y_{\mathsf D}}\mathcal P(\mathsf D)
   \xrightarrow{\lambda^*}\mathcal P(\mathsf C)
   \xrightarrow{a^*}\mathcal P(\mathsf K)
   \]
   fully faithful；
3. \(a^*\) 在 full subcategory
   \[
   \lambda^*y_{\mathsf D}(\mathsf D)
   \subseteq\mathcal P(\mathsf C)
   \]
   上 fully faithful。

#### 证明

对 \(d\in\mathsf D\) 和 \(k\in\mathsf K\)，上述复合的值为

\[
\bigl(a^*\lambda^*y_{\mathsf D}(d)\bigr)(k)
=\operatorname{Map}_{\mathsf D}(\lambda a(k),d),
\]

即 \(\lambda a\) 的 restricted nerve。density criterion 给出
\((1)\Longleftrightarrow(2)\)。

由于 \(\lambda\) 是 localization，restriction

\[
\lambda^*:\mathcal P(\mathsf D)\to\mathcal P(\mathsf C)
\]

fully faithful；Yoneda 也 fully faithful。因此复合是否 fully faithful，
恰好取决于 \(a^*\) 是否在
\(\lambda^*y_{\mathsf D}(\mathsf D)\) 上保持并反映全部 mapping spaces。
这给出 \((2)\Longleftrightarrow(3)\)。证毕。

### 结论 3.5

R1 的 coprobe 缺口现已关闭；一般 localization 后的 probe 问题也不再是
模糊的“也许保持”，而是定理 3.4 的必要充分条件。Reflective 情形之所以
自动成立，正是因为右伴随把该条件化为 R1 定理 F.2 中两个 fully faithful
函子的复合。

---

## 4. Doctrine：唯一性 no-go 与相对生成定理

### 定义 4.1（doctrine moduli）

对 fixed problem \(P\)，令

\[
\mathfrak{Doct}(P)
\]

为所有满足 v0.2 形式要求的 accessible reflective semantic
localizations 所成的 \(\infty\)-groupoid；态射取与 reflector 及其
fully faithful inclusion 相容的 localization-data 等价。所谓“doctrine
由 bare \(P\) 唯一决定”，至少要求
\(\mathfrak{Doct}(P)\) contractible，或要求另有一个泛性质选出其中的
contractible 子空间。

### 定理 4.2（bare doctrine 的非唯一性 no-go）

v0.2 当前公理不能从 bare

\[
(\mathcal A,\mathcal B,P)
\]

唯一确定 semantic doctrine。更强地，存在 \(P\) 使
\(\mathfrak{Doct}(P)\) 不连通。

#### 证明

取

\[
\mathcal A=\mathcal B=*,
\qquad
P(*,*)=S^0.
\]

此时 semantic ambient category 是 \(\mathcal S\)。考虑两个 accessible
reflective localizations

\[
\operatorname{id}_{\mathcal S}
\quad\text{与}\quad
\tau_{\leq-1}:\mathcal S\to\mathcal S_{\leq-1}.
\]

记 \(i_{\leq-1}:\mathcal S_{\leq-1}\hookrightarrow\mathcal S\) 为
inclusion。若两个 localization data 在 doctrine moduli 中等价，则其
associated idempotent endofunctors

\[
\operatorname{id}_{\mathcal S}
\quad\text{与}\quad
i_{\leq-1}\tau_{\leq-1}
\]

必自然等价。可是作用在 \(S^0\) 上分别得到

\[
S^0
\quad\text{与}\quad
*,
\]

二者不等价。因此这两个 doctrine 位于不同连通分支，
\(\mathfrak{Doct}(P)\) 不连通，更不 contractible。证毕。

该结论排除的是“现有公理强迫唯一选择”，并不排除人为指定某个额外规则。

### 命题 4.3（只诉诸极值不会给出非平凡语义）

按“被反演 morphisms 的包含”排序，identity doctrine 是最小元，而把
所有对象送到终对象的 localization 是最大元。因此：

- 无约束地选最小 doctrine，只会得到 identity；
- 无约束地选最大 doctrine，会抹去所有非平凡语义。

所以任何非平凡、可审计的选择都必须提供位于两极之间的额外信息。

#### 证明

identity 只强制反演原本已是 equivalence 的 morphisms，故为最小。
若 \(\mathbb 1_{\mathcal D}\) 是终对象，则 singleton full subcategory
\(\{\mathbb 1_{\mathcal D}\}\hookrightarrow\mathcal D\) 有常值左伴随，
因为
\[
\operatorname{Map}_{\mathcal D}(X,\mathbb 1_{\mathcal D})\simeq *.
\]
其 reflector 反演所有 morphisms，故为最大。两条结论由排序定义得到。
证毕。

### 定理 4.4（由生成规则得到的完整相对 doctrine）

设 \(\mathcal A,\mathcal B\) 为小 \(\infty\)-categories，并令

\[
\mathcal D_P
=
\operatorname{Fun}(\mathcal A^{op}\times\mathcal B,\mathcal S)
\]

为 presentable problem category。额外给定一小族、target-independent
且可审计的 semantic equations

\[
S(P)\subseteq\operatorname{Mor}(\mathcal D_P).
\]

则存在 localization

\[
L_P=L_{S(P)}:\mathcal D_P\to(\mathcal D_P)_{S(P)\text{-loc}},
\]

并且它在所有反演 \(S(P)\) 的 accessible reflective localizations 中
最小，因而在这个相对问题中由 contractible choice 唯一。

若一 base-change functor

\[
F:\mathcal D_P\to\mathcal D_{P'}
\]

把 \(S(P)\) 的每个元素送为 \(L_{P'}\)-equivalence，则存在在等价意义下
唯一的下降函子

\[
\overline F:(\mathcal D_P)_{S(P)\text{-loc}}
\longrightarrow
(\mathcal D_{P'})_{S(P')\text{-loc}}
\]

以及自然等价

\[
\overline F\,L_P\simeq L_{P'}F.
\]

#### 证明

presentable \(\infty\)-category 中一小族 morphisms 生成 accessible
Bousfield localization；其 universal property 给出存在性与最小性。
第二部分中 \(L_{P'}F\) 反演 \(S(P)\)，故同一 universal property 迫使
它唯一因子化通过 \(L_P\)。证毕。

### 结论 4.5

因此 doctrine 主线的最终形式是：

\[
\boxed{
\text{bare }P\text{ 不足以唯一选择 doctrine；}
\quad
(P,S(P))\text{ 则唯一生成最小 doctrine。}
}
\]

以后要发展的对象不是“再猜一个 reflector”，而是证明具体规则
\(P\mapsto S(P)\) 的 naturality、base-change stability 与
anti-tautology certificate。

---

## 5. Enriched effectivity：零映射 no-go 与相对提升

R1 已经完成 \(\mathcal V\)-Prof、enriched Kan extension、coend composition
和 representability 的形式提升。剩余问题是：怎样从
\(\mathcal V\)-值对象读出非平凡的“实现了/未实现”？

### 定理 5.1（naive underlying-point effectivity 在 pointed base 上退化）

设 \((\mathcal V,\otimes,\mathbb 1)\) 是 pointed
\(\infty\)-category，并令

\[
U(X)=\operatorname{Map}_{\mathcal V}(\mathbb 1,X).
\]

则对每个 \(X\in\mathcal V\)，空间 \(U(X)\) 非空。因此谓词

\[
\operatorname{Eff}_{U}(X)
\quad:\Longleftrightarrow\quad
U(X)\neq\varnothing
\]

恒真，不能作为非平凡 enriched effectivity。

#### 证明

pointed 意味着存在零对象 \(0\)。复合

\[
\mathbb 1\longrightarrow0\longrightarrow X
\]

给出 \(\operatorname{Map}_{\mathcal V}(\mathbb 1,X)\) 的一个点，即零
morphism。故该 mapping space 对所有 \(X\) 非空。证毕。

### 推论 5.2（stable、dg 与 Banach 的非空性 no-go）

stable \(\infty\)-categories、derived/dg module categories 以及以有界线性
映射为 morphisms 的 Banach categories 都是 pointed；所以把 enriched
hom object 化成“存在一个 underlying element/morphism”只会检测到零
morphism，不能检测非零解、可逆解或满足约束的解。

同样，Lawvere metric enrichment 中任意对象对都有一个
\([0,\infty]\)-值距离；“有一个 hom-value”本身也恒真。必须加入阈值、
非零性、可逆性或一族 probes 中至少一种额外结构。

### 命题 5.2.1（pointed base 不存在全余极限空间值 shadow）

若 \(\mathcal V\) pointed，则不存在同时满足下列两项的函子：

\[
\varepsilon:(\mathcal V,\otimes,\mathbb 1)
\longrightarrow(\mathcal S,\times,*):
\]

1. \(\varepsilon\) strong unital monoidal；
2. \(\varepsilon\) 保持初对象。

特别地，不存在定义 5.3 所要求的、保持全部小余极限的 truth shadow。

#### 证明

记 \(\mathcal V\) 的零对象为 \(0\)。保持初对象迫使

\[
\varepsilon(0)\simeq\varnothing,
\]

而 strong unital monoidality 迫使

\[
\varepsilon(\mathbb 1)\simeq *.
\]

\(\mathcal V\) 中的零 morphism \(\mathbb 1\to0\) 经
\(\varepsilon\) 后必须给出空间之间的 map

\[
*\longrightarrow\varnothing,
\]

但这样的 map 不存在，矛盾。证毕。

所以 stable/dg/Banach sectors 若要保留全部 coend equipment，不能以
这种方式整体降到 cartesian spaces；必须改用 probe family、分级 truth
system，或把 shadow target 也换成合适的 pointed monoidal base。

### 定义 5.3（truth/effectivity shadow）

一个足以把完整 equipment 推到空间值理论的 **truth shadow** 是函子

\[
\varepsilon:
(\mathcal V,\otimes,\mathbb 1)
\longrightarrow
(\mathcal S,\times,*),
\]

满足：

1. \(\varepsilon\) strong symmetric monoidal；
2. \(\varepsilon\) 保持所用的小余极限；
3. 若要求反映 enriched equivalence，再要求 \(\varepsilon\) conservative；
4. 若要求把某类 enriched fibers 或 homotopy limits 逐项送到空间值
   fibers/limits，再额外要求它保持那些指定极限。

相对于所选 \(\varepsilon\)，定义

\[
\operatorname{Eff}_{\varepsilon}(X)
\quad:\Longleftrightarrow\quad
\varepsilon(X)\neq\varnothing,
\]

并把 v0.2 的 fiber、isotropy 与 simultaneous obstruction 施加在
\(\varepsilon\)-shadow 上。

这是一项额外 doctrine datum，不是一般 monoidal base 自动附带的结构。

### 定理 5.4（truth shadow 的相对提升定理）

在 R1 假设 G.1 下，给定满足定义 5.3 前两项的
\(\varepsilon\)，存在从 \(\mathcal V\)-enriched equipment 到
\(\mathcal S\)-valued equipment 的 change-of-base，作用为

\[
\mathcal A(a,a')
\longmapsto
\varepsilon\mathcal A(a,a'),
\qquad
P(a,b)\longmapsto\varepsilon P(a,b).
\]

它具有以下性质：

1. 保持 identity profunctors 与 Prof composition；
2. 保持由 coend 公式计算的 enriched left Kan saturation；
3. 把 enriched right-representable profunctor 送到
   right-representable space-valued profunctor；
4. 把 enriched pseudo-dynamics 送到 space-valued pseudo-dynamics。

若 \(\varepsilon\) conservative，则一条**已给定的** enriched comparison
map 是 equivalence，当且仅当其 shadow 是 equivalence。若再满足定义
5.3 第四项，则相应 fiber/limit effectivity obstruction 也可在 shadow
中计算。

#### 证明

strong monoidality 把 enriched composition

\[
\mathcal A(a',a'')\otimes\mathcal A(a,a')
\longrightarrow\mathcal A(a,a'')
\]

送为空间值 composition，并保持单位，故得到 change-of-base category
与 profunctor。对 Prof composition，

\[
\begin{aligned}
\varepsilon\bigl((Q\odot P)(a,c)\bigr)
&=
\varepsilon\left(\int^{b}P(a,b)\otimes Q(b,c)\right)\\
&\simeq
\int^{b}\varepsilon P(a,b)\times\varepsilon Q(b,c),
\end{aligned}
\]

其中用到 \(\varepsilon\) 保持余极限与 tensor。右端正是 space-valued
Prof composition。enriched left Kan extension 也由同型的 weighted
coend 公式给出，所以同理保持。

若

\[
P(a,b)\simeq\mathcal B(Fa,b),
\]

应用 \(\varepsilon\) 即得 shadow 中的 representability。compositors
与 units 逐项送出，故 pseudo-dynamics 也被保持。conservativity 给出
对指定 comparison map 的 equivalence 反映；指定极限的保持性给出最后
一项。证毕。

#### 重要边界

“shadow 中某 profunctor 碰巧可表示”一般不反推出原 enriched
profunctor 可表示；除非已给出原层候选与 comparison map，才能使用
conservativity。定义 5.3 的条件也很强，不能假定任意
\(\mathcal V\) 都存在这样的 \(\varepsilon\)。

### 定理 5.5（小 probe family 的保守检测版本）

设 \(\mathcal G\subseteq\mathcal V\) 是 essentially small dense full
subcategory。则 restricted nerve

\[
N_{\mathcal G}:\mathcal V
\longrightarrow
\operatorname{Fun}(\mathcal G^{op},\mathcal S),
\qquad
X\longmapsto
\bigl(g\mapsto\operatorname{Map}_{\mathcal V}(g,X)\bigr)
\]

fully faithful。因此整个 probe profile 检测对象、morphisms 与
equivalences。

#### 证明

这正是 density 与 restricted Yoneda fully faithfulness 的等价刻画。
证毕。

但 \(N_{\mathcal G}\) 通常不 strong monoidal，也不保持 coends；所以它
无条件给出的是**语义检测器**，不是定理 5.4 的 equipment
change-of-base。只有再验证 tensor/coend compatibility 后，才能把
probe profile 提升成完整 truth shadow。

### 5.6 四个边界 sector 的严格落点

| sector | 不能使用的 naive 判据 | 可用的附加结构 | 合成律/恢复力 |
|---|---|---|---|
| Lawvere metric | “距离值存在” | 全部阈值命题 \(d(x,y)\leq r\) | \(r,s\) 合成为 \(r+s\)；全体阈值恢复距离 |
| \(R\)-dg / \(\operatorname{Mod}_R\) | mapping space 非空 | probes \(\{\Sigma^nR\}_{n\in\mathbb Z}\) 的完整 mapping profiles | 检测各阶 homotopy/homology；生成假设下检测 equivalence |
| \(\operatorname{Cat}_\infty\)-enriched | 只取 hom-category 的 core | simplicial probes \([n]\) 与 \(\operatorname{Fun}([n],X)^\simeq\) | complete Segal profile 保留非可逆高阶合成 |
| Banach-enriched | hom-set/任意 norm-ball 非空 | ball-filtered morphisms \(B_r\operatorname{Hom}(X,Y)\) 及指定 tensor norm | \(B_r\circ B_s\subseteq B_{rs}\)；全部半径恢复 norm |

对 Lawvere metric，triangle inequality 正给出

\[
d(x,y)\leq r,\ d(y,z)\leq s
\Longrightarrow
d(x,z)\leq r+s.
\]

对 Banach-enriched sector，必须先选 projective、injective、bornological
或其他适当 completed tensor/base；这不是尚待证明的引理，而是不同理论
的输入选择。对任一固定选择，submultiplicativity

\[
\lVert g\circ f\rVert
\leq
\lVert g\rVert\,\lVert f\rVert
\]

给出表中的 radius-graded composition。

### 结论 5.7

enriched 主线现已得到一个完全闭合的分叉：

\[
\boxed{
\begin{array}{ll}
\text{仅有 monoidal base }\mathcal V:
&\text{equipment layer 可做，但 naive effectivity 在重要 sector 退化；}\\[2mm]
\text{pointed base:}
&\text{全余极限、强幺半的 cartesian-space shadow 不存在；}\\[2mm]
\text{再给 truth shadow }\varepsilon:
&\text{定理 5.4 给出完整的相对 space-valued 理论；}\\[2mm]
\text{只给 dense probes:}
&\text{定理 5.5 给出保守检测，是否保持 equipment 需另验兼容性。}
\end{array}
}
\]

因此 R1 的 “PARTIAL/BLOCKED” 已被替换为 no-go theorem 加最小附加数据
后的完整定理，而不是留下一个未证明的承诺。

---

## 6. 最终证明账本

| 主题 | R2 最终结果 | 仍需作为输入者 |
|---|---|---|
| 可数 simultaneous nonemptiness | 定理 1.1 | fibration 与 \(\pi_0\)-满射 |
| higher simultaneous obstruction | 定理 1.3、推论 1.4 | pointed fibrant tower；标准 Milnor theorem |
| representable Prof dynamics | 定理 2.2 | representability、invertible compositors、高阶相干 |
| ordinary-index strict model | 推论 2.3 | 允许 levelwise equivalence |
| coprobes | 定理 3.2、推论 3.3 | opposite accessibility/coreflectivity |
| probes after arbitrary localization | 定理 3.4 | local Yoneda image 上的 fully faithfulness |
| bare doctrine | 定理 4.2：不可能唯一 | 需额外生成规则 |
| generated doctrine | 定理 4.4 | 小族 \(S(P)\) 与 base-change compatibility |
| naive enriched effectivity | 定理 5.1、命题 5.2.1：恒真且无全结构空间 shadow | 需 probe/graded truth/新 target |
| enriched relative theory | 定理 5.4、5.5 | monoidal-colimit compatibility 或 dense probes |

这张表中没有“证明尚未完成”的条目。右栏列出的都是结论本身不可删去的
假设或新版本明确承认的 sector data。

---

## 7. 逻辑地位与不可过度宣称之处

1. 定理 1.3、cocartesian unstraightening、ordinary-index rectification、
   Bousfield localization existence 与 density criterion 是标准背景定理；
   本报告的贡献是把它们接入 v0.2 接口并推出对应结论，不宣称这些背景
   定理本身为新发现。
2. 定理 4.2、定理 5.1 与命题 5.2.1 是真正的模型边界：继续在原公理内
   “努力证明”不会得到所要求的唯一 doctrine、非平凡 nonempty
   effectivity 或 pointed-to-cartesian 的全余极限强幺半 shadow。
3. 定理 5.4 是相对 theorem，不是“所有 enrichment 自动统一”的 theorem。
4. on-the-nose equality 取决于模型 presentation；理论不应把它与
   invariant equivalence 混为一谈。

---

## 8. 标准背景来源

1. A. K. Bousfield and D. M. Kan,
   [Homotopy Limits, Completions and Localizations](https://doi.org/10.1007/978-3-540-38117-4)：
   tower homotopy limits 与 derived-limit obstruction。
2. Philip S. Hirschhorn,
   [The homotopy groups of the inverse limit of a tower of fibrations](https://www-math.mit.edu/~psh/notes/limfibrations.pdf)：
   tower of fibrations 的 Milnor theorem 及其 \(\lim^1\) kernel。
3. Kerodon,
   [The Universality Theorem](https://kerodon.net/tag/028K)：
   cocartesian fibrations 与 \(\infty\)-functors 的分类。
4. Kerodon,
   [Rectification of Homotopy Coherent Diagrams](https://kerodon.net/tag/028U)：
   普通 indexing category 上的 homotopy-coherent diagram strict model。
5. Kerodon,
   [Existence of Bousfield Localizations](https://kerodon.net/tag/06VG)：
   presentable \(\infty\)-category 中由小族 morphisms 生成 localization。
6. Kerodon,
   [Dense Functors](https://kerodon.net/tag/03V8)：
   density 与 restricted Yoneda fully faithfulness。
7. Kerodon,
   [Accessible Functors](https://kerodon.net/tag/06KX)：
   accessible \(\infty\)-category 具有 essentially small dense full
   subcategory。

---

## 9. R2 最终结论

原先的剩余项现在分成三类，并全部闭合：

\[
\boxed{
\begin{array}{rcl}
\text{可证明项}
&\longrightarrow&
\text{给出定理、假设与证明；}\\
\text{只在附加条件下成立项}
&\longrightarrow&
\text{给出必要充分判据或最小相对定理；}\\
\text{原公理不可能推出项}
&\longrightarrow&
\text{给出反例/no-go theorem。}
\end{array}
}
\]

所以 v0.2 当前已经不是“还有几段证明没补”的状态。下一阶段若继续发展，
应选择具体 sector，验证本报告右栏中的输入条件，并追求新的 sector
theorems；不应再把这些必要输入伪装成待补的形式证明。
