# 数学内生生成性理论

## 全主线发展试验 R1

日期：2026-09-24  
基础版本：Strict Space-Valued Core v0.2 Candidate  
基础版本 SHA-256：`3ef6d885a8bd39bf4661e459774bc2389e5c2c268907f709682e3476dca7a448`  
研究原则：不修改 Frozen v1.0；本文件中的新结果先作为 derived/sector
theorems，只有发现核心反例时才修改冻结核心。

---

## 0. 本轮总结果

本轮同时试验七条主线。状态分为：

- **PROVED**：本文件给出完整证明；
- **CONDITIONAL**：在明确标准假设或已知背景定理下完成；
- **PARTIAL**：得到严格的可行部分及明确阻碍；
- **BLOCKED**：当前定义不足以继续。

| 主线 | 状态 | 本轮最强结果 |
|---|---|---|
| Simultaneous effectivity | **PROVED** | fiber-limit theorem；任意正则 \(\kappa\) 的同时效性检验秩例子 |
| Coherent objectification | **PROVED** | 逐点可余表示自动相干组装为 \(F:\mathcal A\to\mathcal B\) |
| Prof dynamics | **PROVED/PARTIAL** | right-representable reduction；得到 pseudofunctor，不能无条件得到 on-the-nose strict functor |
| Saturation calculus | **PROVED/CONDITIONAL** | Kan 复合律、pointwise Beck–Chevalley 判据、semantic descent criterion |
| Doctrine 内生化 | **CONDITIONAL/PARTIAL** | 小生成语义方程产生最小 accessible localization；bare \(P\) 仍不能唯一决定 doctrine |
| Small probes/coprobes | **PROVED** | reflective localization 保持小稠密 probes；任意 accessible \(\infty\)-category 有小稠密子范畴 |
| Enriched v0.3 | **PARTIAL** | saturation/Yoneda/Prof 可形式提升；elements、effectivity、novelty 不能自动提升 |

本轮最有实质性的新增定理是：

\[
\boxed{
\text{No Universal Bounded Simultaneous-Effectivity Test Rank}
}
\]

精确版本见定理 A.3。

---

## 1. 公共环境

令 \(I\) 为小 \(\infty\)-范畴。考虑箭头范畴中的图

\[
C_\bullet:I\longrightarrow
\Fun(\Delta^1,\Cat_\infty).
\]

逐点写成

\[
C_i:\mathsf{Act}_i\longrightarrow\mathsf{Formal}_i.
\]

其极限箭头记为

\[
C:\mathsf{Act}\longrightarrow\mathsf{Formal},
\qquad
\mathsf{Act}=\lim_i\mathsf{Act}_i,
\quad
\mathsf{Formal}=\lim_i\mathsf{Formal}_i.
\]

给定 \(\xi\in\mathsf{Formal}\)，其分量记为 \(\xi_i\)。定义

\[
\operatorname{EffFib}_{C}(\xi)
=
\mathsf{Act}^\simeq
\times_{\mathsf{Formal}^\simeq}
\{\xi\}.
\]

---

## 2. 主线 A：Simultaneous effectivity

### 定理 A.1（fiber-limit theorem）

存在自然等价

\[
\boxed{
\operatorname{EffFib}_{C}(\xi)
\simeq
\operatorname*{holim}_{i\in I}
\operatorname{EffFib}_{C_i}(\xi_i).
}
\]

#### 证明

core functor

\[
(-)^\simeq:\Cat_\infty\longrightarrow\mathcal S
\]

是空间嵌入 \(\mathcal S\hookrightarrow\Cat_\infty\) 的右伴随，故保持
所有极限。因此

\[
\mathsf{Act}^\simeq
\simeq
\lim_i\mathsf{Act}_i^\simeq,
\qquad
\mathsf{Formal}^\simeq
\simeq
\lim_i\mathsf{Formal}_i^\simeq.
\]

对象 \(\xi\) 给出相容的 points \(\{\xi_i\}\to
\mathsf{Formal}_i^\simeq\)。空间范畴中的小极限彼此交换，故

\[
\begin{aligned}
\operatorname{EffFib}_{C}(\xi)
&=
\left(\lim_i\mathsf{Act}_i^\simeq\right)
\times_{\lim_i\mathsf{Formal}_i^\simeq}
*\\
&\simeq
\lim_i
\left(
\mathsf{Act}_i^\simeq
\times_{\mathsf{Formal}_i^\simeq}
\{\xi_i\}
\right).
\end{aligned}
\]

右侧正是所需 homotopy limit。证毕。

### 推论 A.2（三层 simultaneous decomposition）

若每个 \(C_i=\Phi_iR_i\)，且 \(R_i,\Phi_i\) 构成相容图，则

\[
\operatorname{EffFib}_{C}(\xi)
\simeq
\operatorname*{holim}_{i\in I}
\left(
\mathsf{Act}_i^\simeq
\times_{\mathfrak G_i^\simeq}
\operatorname{FormFib}_{\Phi_i}(\xi_i)
\right).
\]

#### 证明

逐 \(i\) 使用 v0.2 的 two-stage pullback theorem，再使用定理 A.1。
证毕。

### 负例 A.2.1（逐阶段有效不推出同时有效）

即使每个

\[
\operatorname{EffFib}_{C_i}(\xi_i)\neq\varnothing,
\]

其 homotopy limit 仍可为空。最小有限例是 equalizer shape：令
\(X=*\)、\(Y=\{0,1\}\)，两箭头 \(X\rightrightarrows Y\) 分别取值
0 与 1。图中每个空间非空，但其极限为空。

所以 simultaneous effectivity 不是 objectwise effectivity 的逻辑推论。

### 定义 A.3（simultaneous-effectivity test rank）

设 \(X:I\to\mathcal S\) 是一图，\(\lim_I X=\varnothing\)。定义

\[
\rho_{\mathrm{sim}}(X)
=
\min
\left\{
|J|:
J\subseteq I\text{ 为 full subcategory 且 }
\lim_JX|_J=\varnothing
\right\},
\]

只在该最小基数存在时使用此记号。对 effectivity system，取
\(X_i=\operatorname{EffFib}_{C_i}(\xi_i)\)。

### 定理 A.4（超限 simultaneous-effectivity rank）

对每个落在工作宇宙内的无限正则基数 \(\kappa\)，存在一个离散空间值 effectivity
system \(X^\kappa:\kappa^{op}\to\mathcal S\)，满足：

1. 每个 \(X^\kappa_\alpha\) 非空；
2. 对任意对象数小于 \(\kappa\) 的 full subcategory
   \(J\subseteq\kappa^{op}\)，有
   \[
   \lim_JX^\kappa|_J\neq\varnothing;
   \]
3. 但
   \[
   \lim_{\alpha<\kappa}X^\kappa_\alpha=\varnothing;
   \]
4. 因而
   \[
   \rho_{\mathrm{sim}}(X^\kappa)=\kappa.
   \]

#### 构造与证明

对 \(\alpha<\kappa\)，令离散空间

\[
T_\alpha=[\alpha,\kappa)
=\{\beta<\kappa:\alpha\leq\beta\}.
\]

对 \(\alpha\leq\beta\)，以包含映射

\[
T_\beta\hookrightarrow T_\alpha
\]

定义逆系统。每个 \(T_\alpha\) 显然非空。

令 \(J\subseteq\kappa\) 且 \(|J|<\kappa\)。由 \(\kappa\) 的正则性，

\[
\gamma=\sup J<\kappa.
\]

元素 \(\gamma\) 同时属于每个 \(T_\alpha\)（\(\alpha\in J\)），并给出
相容族，故限制极限非空。

若整个系统有相容族，则其所有分量在包含映射下必须是同一个
\(\beta<\kappa\)，而该 \(\beta\) 必须满足

\[
\beta\geq\alpha
\qquad
\text{对所有 }\alpha<\kappa,
\]

不可能。因此全极限为空，最小失败基数正是 \(\kappa\)。

最后令

\[
C_\alpha:T_\alpha\longrightarrow *
\]

即可把该空间图实现为 effectivity fibers。证毕。

### 推论 A.5（无统一有界检验秩）

在固定 Grothendieck 宇宙内部，不存在一个 \(\mathbb U_0\)-小正则基数
\(\kappa_0\)，使所有 simultaneous-effectivity
问题都能通过检查少于 \(\kappa_0\) 个阶段的子系统判定。

#### 证明

把定理 A.4 应用于任意正则 \(\kappa>\kappa_0\)。证毕。

### A.6 Derived-limit obstruction：本轮状态

对 pointed tower，在通常 fibrancy、连通性与收敛条件下，可使用
Bousfield–Kan/Milnor 型 derived-limit machinery：

\[
E_2^{s,t}
=
\lim\nolimits^s\pi_tX_i
\Longrightarrow
\pi_{t-s}\operatorname*{holim}_iX_i.
\]

本轮没有把该谱序列无条件纳入核心，因为：

1. 非空性本身是未带基点的问题；
2. \(\pi_0\) 与低维项可能是非阿贝尔对象；
3. 一般 indexing category 需要明确收敛假设。

因此 A.1–A.5 是本文件中的完整 derived results；这里不主张其基础构造
在既有数学文献中从未出现。谱序列只是下一轮的 sector engine。

---

## 3. 主线 B：Coherent objectification

### 定理 B.1（逐点可余表示自动相干化）

令

\[
P:\mathcal A^{op}\times\mathcal B\to\mathcal S.
\]

若对每个 \(a\in\mathcal A\)，函子 \(P(a,-)\) 可余表示，则存在函子

\[
F:\mathcal A\to\mathcal B
\]

以及自然等价

\[
\boxed{
P(a,b)\simeq\Map_{\mathcal B}(F(a),b).
}
\]

这样的 pair \((F,P\simeq\Map(F(-),-))\) 的空间若非空则可缩。

#### 证明

柯里化得到

\[
\overline P:
\mathcal A^{op}\longrightarrow
\Fun(\mathcal B,\mathcal S).
\]

co-Yoneda embedding

\[
j:\mathcal B^{op}\hookrightarrow
\Fun(\mathcal B,\mathcal S),
\qquad
b\longmapsto\Map_{\mathcal B}(b,-)
\]

fully faithful。假设说明 \(\overline P\) 的每个对象都落在 \(j\) 的
本质像中。由于该本质像是 full replete subcategory，\(\overline P\)
整体因子化为

\[
\mathcal A^{op}\longrightarrow\mathcal B^{op}
\xrightarrow{j}\Fun(\mathcal B,\mathcal S).
\]

取 opposite 得到 \(F:\mathcal A\to\mathcal B\)。fully faithful
因子化的选择空间是可缩的，因此 \(F\) 与表示等价在 contractible
choice 意义下唯一。证毕。

### 推论 B.2（v0.2 的全局 objectification）

若对所有 \(a^\sharp\in\mathcal A^\sharp\)，possibility category
\(\mathfrak G(a^\sharp)\) 有初始对象，则这些初始对象自动组装成

\[
F:\mathcal A^\sharp\to\mathcal B^\sharp
\]

并给出

\[
P^\sharp(a^\sharp,b^\sharp)
\simeq
\Map_{\mathcal B^\sharp}(F(a^\sharp),b^\sharp).
\]

因此不需要额外假设“能够相干地选择逐点 universal objects”。

### 评价

该定理是 Yoneda fully faithfulness 的全局应用，数学机制是标准的；但它
补齐了 v0.2 从 pointwise representability 到 functorial
objectification 的一个真实证明义务。

---

## 4. 主线 C：Prof dynamics 的表示性与严格化

### 定义 C.1（right-representable profunctors）

对 \(F:\mathcal A\to\mathcal B\)，记

\[
F_*:\mathcal A\nrightarrow\mathcal B,
\qquad
F_*(a,b)=\Map_{\mathcal B}(F(a),b).
\]

称等价于某个 \(F_*\) 的 profunctor 为 right-representable。

### 命题 C.2（2-cell 方向）

若 \(F,G:\mathcal A\to\mathcal B\)，则

\[
\Map_{\operatorname{Prof}(\mathcal A,\mathcal B)}(F_*,G_*)
\simeq
\Map_{\Fun(\mathcal A,\mathcal B)}(G,F).
\]

特别地，right-representable profunctors 的 hom \(\infty\)-category
等价于 \(\Fun(\mathcal A,\mathcal B)^{op}\)，而不是未经取 opposite 的
functor category。

#### 证明

逐 \(a\) 使用 co-Yoneda：

\[
\operatorname{Nat}
\bigl(
\Map(Fa,-),\Map(Ga,-)
\bigr)
\simeq
\Map(Ga,Fa).
\]

再对 \(a\) 施加自然性条件，得到从 \(G\) 到 \(F\) 的自然变换空间。
证毕。

### 命题 C.3（right-representables 对合成封闭）

对

\[
\mathcal A\xrightarrow F\mathcal B\xrightarrow G\mathcal C,
\]

有自然等价

\[
G_*\odot F_*\simeq(GF)_*.
\]

#### 证明

\[
\begin{aligned}
(G_*\odot F_*)(a,c)
&=
\int^{b\in\mathcal B}
\Map_{\mathcal B}(Fa,b)
\times
\Map_{\mathcal C}(Gb,c)\\
&\simeq
\Map_{\mathcal C}(GFa,c)
\end{aligned}
\]

由 co-Yoneda 得到。证毕。

### 定理 C.4（representable reduction theorem）

设

\[
\mathbb T:\mathsf D\to\operatorname{Prof}_{\mathcal S}
\]

是 v0.2 意义下的 lax dynamics，并假设每个
\(\mathbb T_u\) right-representable。则：

1. 可在 contractible choice 意义下选择
   \[
   T_u:\mathsf E_d\to\mathsf E_{d'}
   \]
   表示 \(\mathbb T_u\)；
2. compositor
   \[
   \mathbb T_v\odot\mathbb T_u\to\mathbb T_{vu}
   \]
   对应于方向相反的自然变换
   \[
   T_{vu}\longrightarrow T_vT_u;
   \]
3. unit map 对应于
   \[
   T_{\id_d}\longrightarrow\id_{\mathsf E_d};
   \]
4. Prof 中的全部高阶相干转化为上述 oplax compositor 的全部高阶相干；
5. 若所有 compositor 与 unit cells 都是等价，则得到一个
   homotopy-coherent pseudofunctor，其合成等价为
   \[
   T_vT_u\simeq T_{vu}.
   \]

#### 证明

逐 transition 的表示函子由定理 B.1 组装。命题 C.3 说明 compositor
的 source 由 \(T_vT_u\) 表示；命题 C.2 把 Prof 2-cell 转成方向反转的
自然变换。由于这个对应来自 fully faithful 的 co-Yoneda embedding，
所有 associativity、unit 和 higher coherence 原样传递。若 cells 均为
等价，方向可以反转，得到 pseudofunctorial composition。证毕。

### 严格化边界 C.5

定理 C.4 **不**无条件给出逐等式满足

\[
T_{vu}=T_vT_u
\]

的 on-the-nose strict functor。它给出的是在 \(\infty\)-categorical
意义下正确的 homotopy-coherent functor/pseudofunctor。若要求某一具体
模型中的严格等式，还需要单独的 rectification theorem。

### 三层 obstruction

本轮得到自然的三层检查：

1. **Representability obstruction**：某个
   \(\mathbb T_u(x,-)\) 不可余表示；
2. **Composition obstruction**：所有 transitions 可表示，但某个
   \(\mu_{v,u}\) 不是等价；
3. **Rectification obstruction**：已得到 pseudofunctor，但所选严格模型
   不允许无损 on-the-nose strictification。

前两项已被 v0.2 严格检测；第三项依赖具体高阶范畴模型。

---

## 5. 主线 D：Saturation calculus

### 定理 D.1（Kan saturation 的复合律）

给定

\[
\mathcal C\xrightarrow{\lambda}\mathcal D
\xrightarrow{\mu}\mathcal E
\]

以及 \(P:\mathcal C\to\mathcal S\)，若相关 Kan extensions 存在，则

\[
\boxed{
\operatorname{Lan}_{\mu\lambda}P
\simeq
\operatorname{Lan}_{\mu}
\operatorname{Lan}_{\lambda}P.
}
\]

#### 证明

对任意 \(Q:\mathcal E\to\mathcal S\)，

\[
\begin{aligned}
\Map(\operatorname{Lan}_{\mu}\operatorname{Lan}_{\lambda}P,Q)
&\simeq
\Map(\operatorname{Lan}_{\lambda}P,\mu^*Q)\\
&\simeq
\Map(P,\lambda^*\mu^*Q)\\
&=
\Map(P,(\mu\lambda)^*Q)\\
&\simeq
\Map(\operatorname{Lan}_{\mu\lambda}P,Q).
\end{aligned}
\]

Yoneda 给出所需自然等价。证毕。

该定理逐变量应用后，直接给出 v0.2 domain-changing saturation 的复合律。

### 定理 D.2（pointwise Beck–Chevalley 判据）

考虑同伦可交换方块

\[
\begin{matrix}
\mathcal C'&\xrightarrow{u}&\mathcal C\\
\downarrow f'&&\downarrow f\\
\mathcal D'&\xrightarrow{v}&\mathcal D.
\end{matrix}
\]

对每个 \(d'\in\mathcal D'\)，该方块诱导 indexing-category functor

\[
\Theta_{d'}:
(f'\downarrow d')
\longrightarrow
(f\downarrow v(d')).
\]

若每个 \(\Theta_{d'}\) final，则对每个
\(P:\mathcal C\to\mathcal S\)，base-change mate

\[
\operatorname{Lan}_{f'}u^*P
\longrightarrow
v^*\operatorname{Lan}_{f}P
\]

是等价。

#### 证明

在 \(d'\) 处，两边分别由 pointwise Kan-extension 公式写为

\[
\operatorname*{colim}_{(c',f'c'\to d')}
P(uc')
\]

与

\[
\operatorname*{colim}_{(c,fc\to v d')}P(c).
\]

比较映射由 \(\Theta_{d'}\) 诱导。finality 保证两余极限等价。逐
\(d'\) 即得结论。证毕。

这给出一个可检查的充分条件；没有 finality 时 Beck–Chevalley 一般失败。

一个最小负控制是取

\[
\mathcal C'=\varnothing,
\qquad
\mathcal C=\mathcal D'=\mathcal D=*,
\]

并令其余 functors 为唯一可能的 functors。对非初始空间 \(P(*)\)，比较的
左侧是空图的余极限 \(\varnothing\)，右侧是 \(P(*)\)，故不等价；此时
\(\Theta_*:\varnothing\to*\) 确实不 final。

### 定理 D.3（semantic localization descent）

令 \(\mathcal X,\mathcal Y\) 为 presentable \(\infty\)-categories，令

\[
L_{\mathcal X}:\mathcal X\to\mathcal X_{loc},
\qquad
L_{\mathcal Y}:\mathcal Y\to\mathcal Y_{loc}
\]

为 reflective localizations，且 \(F:\mathcal X\to\mathcal Y\) 为
cocontinuous functor。若 \(F\) 把每个 \(L_{\mathcal X}\)-equivalence
送到 \(L_{\mathcal Y}\)-equivalence，则存在本质唯一的

\[
\overline F:\mathcal X_{loc}\to\mathcal Y_{loc}
\]

满足

\[
\boxed{
\overline F L_{\mathcal X}
\simeq
L_{\mathcal Y}F.
}
\]

#### 证明

复合 \(L_{\mathcal Y}F\) 反演所有
\(L_{\mathcal X}\)-equivalences。由 reflective localization 的泛性质，
它唯一地因子化通过 \(L_{\mathcal X}\)。证毕。

### 推论 D.4（真正的交换条件）

在定理 D.3 的假设下，记两个 localization 的 fully faithful 右伴随为
\(i_{\mathcal X},i_{\mathcal Y}\)。若 \(F i_{\mathcal X}\) 落在
\(i_{\mathcal Y}\) 的本质像中，因而给出
\(F_{loc}:\mathcal X_{loc}\to\mathcal Y_{loc}\)，

则在 \(\mathcal Y_{loc}\) 中存在自然等价

\[
L_{\mathcal Y}F
\simeq
F_{loc}L_{\mathcal X}.
\]

#### 证明

对 \(x\in\mathcal X\)，箭头

\[
F(x)\longrightarrow F(i_{\mathcal X}L_{\mathcal X}x)
\]

由定理 D.3 的假设是 \(L_{\mathcal Y}\)-equivalence，而其 target 由
新增假设是 \(\mathcal Y\)-local。故该 target 具有 \(F(x)\) 的
\(L_{\mathcal Y}\)-localization 的泛性质，从而自然等价于
\(i_{\mathcal Y}L_{\mathcal Y}F(x)\)。在
\(\mathcal Y_{loc}\) 中 corestrict 即得结论。证毕。

因此“domain saturation 与 semantic saturation 交换”不是形式恒等式，
而是需要上述 compatibility/distributive-law 条件的定理。

### 本线结论

复合律已经无条件解决；base change 有精确 finality 判据；semantic
interchange 只有在兼容条件下成立。下一轮应为常见 localizations 建立
可复用的 Beck–Chevalley sufficient packages。

---

## 6. 主线 E：Doctrine 的内生化

### 定理 E.1（小生成的最小 semantic doctrine）

令 \(\mathcal D\) 为 presentable \(\infty\)-category，令
\(S\) 为 \(\mathcal D\) 中一小族 morphisms。则存在 accessible
reflective localization

\[
L_S:\mathcal D\longrightarrow\mathcal D[S^{-1}]_{loc},
\]

其 local objects 恰为满足

\[
\Map(t,X)\longrightarrow\Map(s,X)
\]

对每个 \((s\to t)\in S\) 都是等价的对象。并且它在反演 \(S\) 的
cocontinuous functors 中具有泛性质。

特别地，当 \(\mathcal A,\mathcal B\) 小时，

\[
\mathcal D
=
\Fun(\mathcal A^{op}\times\mathcal B,\mathcal S)
\]

presentable，所以任何一小族明确的 semantic equations 都生成一个最小
accessible \(L^{sem}\)。

#### 证明依据

diagram category 的 presentability 与由小族 maps 生成 Bousfield
localization 的存在性是 presentable \(\infty\)-categories 的标准定理。
其泛性质说明该 localization 是相对于生成族 \(S\) 的最小 doctrine。

### 定义 E.2（generated doctrine datum）

把 doctrine 输入从一个任意 reflector

\[
L^{sem}
\]

缩减为一小族可审计的 semantic equations

\[
S(P)\subseteq
\operatorname{Mor}
\Fun(\mathcal A^{op}\times\mathcal B,\mathcal S),
\]

并定义

\[
L^{sem}_P:=L_{S(P)}.
\]

这样 doctrine 至少由有限或小规模证书生成，而不再以整个 reflector
作为黑箱输入。

### 命题 E.3（bare problem 的 doctrine underdetermination）

仅由 bare data

\[
(\mathcal A,\mathcal B,P)
\]

和 v0.2 当前公理，不能证明 \(L^{sem}\) 唯一。

#### 证明

取 \(\mathcal A=\mathcal B=*\) 且 \(P(*,*)=S^0\)，则 problem
category 是 \(\mathcal S\)。至少存在下列不同的 accessible reflective
localizations：

\[
\id_{\mathcal S},
\qquad
\tau_{\leq-1},
\qquad
\mathcal S\to\{*\}.
\]

它们都满足“reflective、accessible、idempotent”等当前形式要求；其中
identity 保留 \(S^0\)，而后两者把这个非空空间送到 \(*\)。bare \(P\)
中没有额外谓词指定应保留普通同伦型、
只保留真值，还是全部压到终对象。因此当前公理不蕴含唯一 doctrine。
证毕。

该命题不是说不存在某个人为约定的 functorial rule；它说明该 rule 不会
由现有 bare data 的泛性质唯一强迫出来。

### 本线结论

本轮实现了“相对于一小族语义方程的内生生成”，但没有实现“从 bare
problem 无附加原则地产生唯一语义”。下一步真正的问题变为：寻找自然、
target-independent 的生成规则

\[
P\longmapsto S(P),
\]

而不是继续直接指定任意 reflector。

---

## 7. 主线 F：Small probes/coprobes 与 observation

### 定理 F.1（representable observation 中 density = adequacy）

对小函子 \(i:\mathsf K\to\mathsf E\)，定义 restricted nerve

\[
N_i(e)(k)=\Map_{\mathsf E}(i(k),e).
\]

若 observation law 取 representable 形式

\[
\mathbb O(k,e)=\Map_{\mathsf E}(i(k),e),
\]

则 \(i\) dense 当且仅当

\[
N_i:\mathsf E\to\mathcal P(\mathsf K)
\]

fully faithful。因此在 representable-observation sector 中，v0.2 的
fully faithful observation condition 正是 density。对一般任意
profunctor \(\mathbb O\)，不能把 adequacy 自动改写成某个 probe functor
的 density。

### 定理 F.2（reflective localization 保持小稠密 probes）

设

\[
L:\mathsf E\rightleftarrows\mathsf E_{loc}:j,
\qquad L\dashv j,
\]

且 \(j\) fully faithful。若

\[
i:\mathsf K\to\mathsf E
\]

是小 dense functor，则

\[
Li:\mathsf K\to\mathsf E_{loc}
\]

仍 dense。

#### 证明

对 \(x\in\mathsf E_{loc}\)，

\[
\begin{aligned}
N_{Li}(x)(k)
&=
\Map_{\mathsf E_{loc}}(Li(k),x)\\
&\simeq
\Map_{\mathsf E}(i(k),j(x))\\
&=N_i(jx)(k).
\end{aligned}
\]

所以

\[
N_{Li}\simeq N_i j.
\]

\(N_i\) 与 \(j\) 均 fully faithful，故 \(N_{Li}\) fully faithful。
由 density criterion，\(Li\) dense。证毕。

### 推论 F.3（accessible event categories 有小充分观察装置）

若 \(\mathsf E\) accessible，则存在 essentially small dense full
subcategory \(\mathsf K\subseteq\mathsf E\)；可以取某个足够大的正则
基数 \(\kappa\) 下的 \(\kappa\)-compact objects 的小骨架。因此
accessible event category 至少存在一种小 fully faithful observation
nerve。

若再作 accessible reflective localization，则定理 F.2 给出局部化后的
小 adequate probes。

### 警告 F.4（density 不具有一般传递性）

不能仅凭

\[
\mathcal C\to\mathcal D\text{ dense},
\qquad
\mathcal D\to\mathcal E\text{ dense}
\]

推出 composite dense。标准反例为

\[
\mathbf\Delta_{\leq1}
\longrightarrow
\mathbf\Delta
\longrightarrow
\mathbf{Cat}:
\]

前两步分别 dense，但 \(\mathbf\Delta_{\leq1}\to\mathbf{Cat}\) 不
dense。因此，不能使用“两个 functors 分别 dense”这一论证推出
composite dense。对一般 categorical localization 后原 probes 的像是否
dense，本轮没有给出无附加条件的结论；reflective localization 的结论
成立，是因为有右伴随 \(j\) 的额外结构。

### Coprobes 状态

上述论证对 codensity 可形式对偶化，但 presentable/accessibility 本身不
自动保证小 codense subcategory；对偶范畴通常不再 accessible。因此本轮
只完整解决 probes 方向，coprobes 仍应单独研究。

---

## 8. 主线 G：统一 enriched v0.3 试验

### 假设 G.1

固定 presentably closed symmetric monoidal \(\infty\)-category
\((\mathcal V,\otimes,\mathbb 1)\)，并假设 \(\otimes\) 在每个变量中保持
小余极限。再固定一个满足 enriched Yoneda、enriched Kan extension 与
coend calculus 的小 \(\mathcal V\)-enriched \(\infty\)-category 模型。

### 条件化定理 G.2（formal enriched lifting）

在假设 G.1 下，下列 v0.2 模块可形式提升：

1. \(\mathcal V\)-profunctor
   \[
   P:\mathcal A^{op}\otimes\mathcal B\to\mathcal V;
   \]
2. enriched left Kan domain saturation；
3. enriched Yoneda/corepresentability；
4. coend composition
   \[
   (Q\odot P)(a,c)
   =
   \int^{b}P(a,b)\otimes Q(b,c);
   \]
5. right-representable transitions 与命题 C.3 的 enriched 版本；
6. 由一小族 morphisms 生成的 presentable semantic localization。

#### 理由

这些证明只使用 enriched Yoneda、Kan-extension adjunction、余极限和
coend Fubini；假设 G.1 正好保证所需运算存在并与 tensor 相容。

### 不能自动提升的模块

| v0.2 模块 | 是否自动提升 | 原因 |
|---|:---:|---|
| domain saturation | 是 | enriched Lan 即可 |
| representability | 是 | enriched Yoneda |
| Prof dynamics | 是 | enriched coend composition |
| category of elements | 否 | 一般 \(\mathcal V\) 没有 space-valued unstraightening |
| initial-object moduli | 否 | 需要 enriched weighted-initial notion |
| nonempty effectivity fiber | 否 | “非空”不是一般 \(\mathcal V\) 的内在谓词 |
| core 与 isotropy space | 否 | 需要指定 underlying-space 或 maximal-groupoid construction |
| novelty/OldMatch | 否 | 需要 \(\mathcal V\)-等价和 observation truth notion |

若简单应用

\[
U=\Map_{\mathcal V}(\mathbb 1,-):\mathcal V\to\mathcal S,
\]

可以得到空间值 shadow，但除非 \(U\) conservative 且保留相关
limits/colimits，这不构成对原 enriched 结构的保守替代。

### 各边界案例的第一次判定

| 方向 | Prof/representability | effectivity/novelty | 本轮判定 |
|---|---|---|---|
| Lawvere metric | quantale-enriched 部分可做 | 距离值不能化约为非空性 | PARTIAL |
| dg/chain complexes | \(\operatorname{Ch}_R\)-enriched coend 可做 | realization 需要 derived/enriched fiber | PARTIAL |
| \(\Cat_\infty\)-enriched | 可表达非可逆 2-cells | core-based effectivity 会丢 2-cells | PARTIAL |
| Banach | 需要选择 Ind-Banach/bornological 等良好基类 | 普通 Banach category 不直接满足全部假设 | BLOCKED BY BASE CHOICE |

### 本线结论

v0.3 不应只是把 \(\mathcal S\) 替换成符号 \(\mathcal V\)。正确结构应
至少分成：

1. **enriched equipment layer**：本轮已给出统一可行条件；
2. **enriched realization layer**：尚需定义 weighted elements 与
   enriched effectivity；
3. **underlying-space shadow**：只能作为比较函子，不能冒充原结构。

---

## 9. 横向主线：Anti-tautology 与可审计预测

数学结构只能规定依赖顺序，不能从内部证明某位研究者在历史上没有看到
目标答案。因此本轮不把“历史独立性”伪装成数学定理，而是给出一个最小
外部证书格式。

### 定义 H.1（pre-target configuration certificate）

证书至少包含：

1. 完整配置 \(\Xi\) 的内容哈希；
2. admissible class 与所有 doctrine generators \(S(P)\)；
3. observation law \(\mathbb O\)；
4. target-independent evaluation rule；
5. 生成时间或外部不可变版本记录；
6. 从输入到结论的依赖 DAG。

只有在证书冻结后得到的目标结果，才允许计入 prediction test。该协议不能
数学证明历史事实，但能把事后调参变成可审计的外部违规。

### 本线状态

**PROCEDURAL PASS，INTERNALIZATION BLOCKED。** provenance certificate
可严格定义并机器验证；“研究者事实上独立”仍不是配置内部性质。

---

## 10. 本轮得到的定理资产

### 10.1 完整证明，可直接作为 derived theorems

1. A.1：simultaneous effectivity fiber 是各阶段 fibers 的 homotopy limit；
2. A.4：任意正则 \(\kappa\) 的精确 simultaneous-effectivity rank；
3. A.5：不存在统一有界 simultaneous-effectivity test rank；
4. B.1：pointwise corepresentability 自动相干化；
5. C.2–C.4：right-representable Prof reduction；
6. D.1：domain saturation 的复合律；
7. D.2：pointwise Beck–Chevalley finality criterion；
8. D.3–D.4：semantic localization descent 与 interchange criterion；
9. F.2：reflective localization 保持小稠密 probes。

### 10.2 标准背景定理在本理论中的新用途

1. 小族 maps 在 presentable \(\infty\)-category 中生成 accessible
   localization；
2. accessible \(\infty\)-category 具有 essentially small dense
   subcategory；
3. density 等价于 restricted Yoneda fully faithful；
4. Bousfield–Kan/Milnor machinery 可作为 simultaneous obstruction 的
   sector engine。

这些不应宣称为本理论原创；本轮贡献是把它们放到严格接口中并识别适用
条件。

### 10.3 新发现的负边界

1. objectwise effectivity 不推出 simultaneous effectivity；
2. representable Prof dynamics 不自动得到 on-the-nose strict functor；
3. semantic reflector 不自动与 domain Kan extension 交换；
4. bare \(P\) 不唯一决定 doctrine；
5. dense functors 的复合一般不 dense；
6. enriched Prof 可提升不等于 enriched effectivity 已解决。

---

## 11. 哪条主线最值得进入 R2

按“可能产生非平凡新数学”的优先级排序：

### 第一：Simultaneous-effectivity obstruction theory

下一步不是重复 A.1，而是为不同 indexing shapes 证明非空性判据：

- countable towers：fibration + \(\pi_0\)-sur射；
- compact Hausdorff fibers：surjective inverse systems；
- truncated/nilpotent fibers：derived-limit obstruction；
- transfinite towers：cofinality 与 \(\rho_{sim}\)；
- two-stage fibers：分别定位 formal-lift 与 realization obstruction。

目标是把 Postnikov、Grothendieck existence、Kolmogorov extension、局部—
整体等至少一组 B 案例升级为 A 类 sector theorem。

### 第二：Prof representability obstruction

把

\[
\mathbb T_u(x,-)
\]

的 accessible/limit-preservation criteria 与 Pro-objectification 结合，定义
transition 的 Pro-representability rank，并判断何时一个 relation-like
dynamics 可提升为真正 functorial dynamics。

### 第三：Generated doctrines

选择一类不依赖目标答案的原始结构规则，构造

\[
P\mapsto S(P),
\]

并验证 naturality、minimality、base-change stability。若这一步失败，应
证明一个更强的 underdetermination/no-go theorem。

### 第四：Enriched realization

先选 \(\mathcal V=\operatorname{Ch}_R\) 或稳定 presentable monoidal
category；不要先处理 Banach。目标是定义不丢失 hom-complex 的 enriched
effectivity，而不仅是 underlying-space fiber。

---

## 12. R1 总判定

所有主线都已获得非空结果，没有一条在第一步即完全失败。但成熟度不同：

\[
\boxed{
\begin{array}{c}
\text{A、B、D、F 已产生可证明定理；}\\
\text{C 已完成 representable reduction，但严格化受模型限制；}\\
\text{E 只能相对于 generators 内生；}\\
\text{G 只完成 equipment layer，尚未完成 enriched effectivity。}
\end{array}
}
\]

理论当前最合理的身份仍是：

> 一个经过审计的空间值生成性 equipment，加上一批正在形成的
> effectivity、dynamics 与 observation sector theorems。

它还不是统一 enriched 基础理论。但本轮已经从“压力测试框架”迈入了
“能够产生 derived theorems”的阶段。

---

## 13. 标准背景来源

以下来源只支撑本文件明确标为标准背景的部分：

1. Kerodon, [Existence of Bousfield Localizations](https://kerodon.net/tag/06VG)：
   presentable \(\infty\)-category 中由小族 morphisms 生成 localization。
2. Kerodon, [Dense Functors](https://kerodon.net/tag/03V8)：density、restricted
   Yoneda fully faithfulness，以及 density 非一般传递的反例。
3. Kerodon, [Accessible Functors](https://kerodon.net/tag/06KX)：accessible
   \(\infty\)-categories 的小 dense subcategory。
4. A. K. Bousfield and D. M. Kan,
   [Homotopy Limits, Completions and Localizations](https://doi.org/10.1007/978-3-540-38117-4)：
   towers、homotopy inverse limits 与相关 obstruction machinery。
