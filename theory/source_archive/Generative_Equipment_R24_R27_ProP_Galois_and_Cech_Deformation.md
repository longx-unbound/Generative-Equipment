# R24–R27：pro-\(p\)/Galois 与 Čech/deformation 跨域验证

**状态：** Candidate Extension Layer v0.3；不修改 Frozen v1.0。  
**日期：** 2026-09-29（Asia/Shanghai）。  
**依赖：** R16–R23，特别是 R19 的 split support-excision / support-cost。  
**目标：** 在两个独立自然领域中产生对象级的新 reduction theorem、no-go 与尖锐成本定理，而非仅改写 Dwyer 或 Maurer–Cartan 语言。

---

## 0. 结论摘要

本轮得到四个定理。

1. **R24（Factorwise Dwyer–Massey Excision）**：有限自由 pro-\(p\) 积上的 unitriangular defining spaces 与 lifting spaces 精确分解为各自由因子的乘积。因此，一个给定 \(n\)-tuple 的 Massey 可定义性与含 \(0\) 性都逐因子判定。
2. **R25（Mixed-Block No-Go / Grushko Cost）**：若每个输入类纯支撑于一个自由因子，而这些输入跨越至少两个因子，则任何已定义的高阶 Massey 乘积必含 \(0\)。非平凡纯块乘积只能存在于一个非自由 Grushko 块中，并得到 arity 上界。
3. **R26（Čech–Artin Split Excision）**：Čech–Thom–Whitney 控制 \(L_\infty\)-代数在 squarefree Artin 参数环上具有 Boolean support 分级；删除无关参数给出 split \(L_\infty\) retract，局部参数块的 obstruction tower 不受外部参数影响。
4. **R27（Punctured Artin Cube Obstruction）**：一族彼此相容的 proper-face deformation data 能否同时填充 full Artin cube，由唯一的 full-support \(H^2\) 类精确控制；一个 \(r\)-ary 原始耦合至少需要 \(r\) 个独立 square-zero 参数，等号时强迫 singleton partition。

这使同一 doctrine 在三个彼此独立的自然生态中产生对象级定理：

- moment-angle / toric topology；
- pro-\(p\) / Galois cohomology；
- Čech / deformation theory。

三领域阈值现在**初步达到**。但按 Frozen v1.0 的治理规则，新 sector theorems 默认属于派生层；没有反例、内部矛盾或良定义失败，因此核心仍不修改。

---

## 1. pro-\(p\)/Galois sector

### 1.1 Dwyer representation fibers

固定素数 \(p\)。令 \(U_{n+1}=U_{n+1}(\mathbb F_p)\) 为上三角幺幺矩阵群，中心

\[
Z=\{I+aE_{1,n+1}:a\in\mathbb F_p\},
\qquad \bar U_{n+1}=U_{n+1}/Z.
\]

对 pro-\(p\) 群 \(G\) 及 \(\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_n)\in H^1(G,\mathbb F_p)^n\)，定义

\[
\operatorname{Def}_n(G;\boldsymbol\alpha)
=\left\{\bar\rho:G\to\bar U_{n+1}
\mid \bar\rho_{i,i+1}=\alpha_i\right\},
\tag{1.1}
\]

\[
\operatorname{Lift}_n(G;\boldsymbol\alpha)
=\left\{\rho:G\to U_{n+1}
\mid \rho_{i,i+1}=\alpha_i\right\}.
\tag{1.2}
\]

所有同态均连续。Dwyer 判据给出

\[
\langle\boldsymbol\alpha\rangle\ne\varnothing
\iff \operatorname{Def}_n(G;\boldsymbol\alpha)\ne\varnothing,
\tag{1.3}
\]

\[
0\in\langle\boldsymbol\alpha\rangle
\iff \operatorname{Lift}_n(G;\boldsymbol\alpha)\ne\varnothing.
\tag{1.4}
\]

### 定理 R24（Factorwise Dwyer–Massey Excision）

设

\[
G=G_1\amalg_pG_2\amalg_p\cdots\amalg_pG_r
\tag{1.5}
\]

是有限自由 pro-\(p\) 积。记 \(\alpha_i^{(\lambda)}=\alpha_i|_{G_\lambda}\)，\(\boldsymbol\alpha^{(\lambda)}=(\alpha_1^{(\lambda)},\ldots,\alpha_n^{(\lambda)})\)。则存在自然双射

\[
\operatorname{Def}_n(G;\boldsymbol\alpha)
\cong
\prod_{\lambda=1}^r
\operatorname{Def}_n(G_\lambda;\boldsymbol\alpha^{(\lambda)}),
\tag{1.6}
\]

\[
\operatorname{Lift}_n(G;\boldsymbol\alpha)
\cong
\prod_{\lambda=1}^r
\operatorname{Lift}_n(G_\lambda;\boldsymbol\alpha^{(\lambda)}).
\tag{1.7}
\]

因此

\[
\langle\boldsymbol\alpha\rangle_G\text{ 可定义}
\iff
\forall\lambda,
\ \langle\boldsymbol\alpha^{(\lambda)}\rangle_{G_\lambda}
\text{ 可定义},
\tag{1.8}
\]

且

\[
0\in\langle\boldsymbol\alpha\rangle_G
\iff
\forall\lambda,
\ 0\in\langle\boldsymbol\alpha^{(\lambda)}\rangle_{G_\lambda}.
\tag{1.9}
\]

#### 证明

自由 pro-\(p\) 积的泛性质对任意有限 pro-\(p\) 群 \(Q\) 给出

\[
\operatorname{Hom}_{\mathrm{cont}}(G,Q)
\cong
\prod_{\lambda=1}^r
\operatorname{Hom}_{\mathrm{cont}}(G_\lambda,Q).
\tag{1.10}
\]

分别取 \(Q=\bar U_{n+1}\) 与 \(Q=U_{n+1}\)。超对角坐标约束在限制到各因子时逐项分解，故 (1.10) 限制为 (1.6) 与 (1.7)。再用 (1.3)–(1.4) 即得 (1.8)–(1.9)。证毕。

### 1.2 纯块支撑

由

\[
H^1(G,\mathbb F_p)\cong
\bigoplus_{\lambda=1}^rH^1(G_\lambda,\mathbb F_p),
\tag{1.11}
\]

称 \(0\ne\alpha\in H^1(G,\mathbb F_p)\) **纯支撑于** \(G_\lambda\)，若它的其他因子分量全为零。

### 定理 R25（Mixed-Block No-Go 与 Grushko Support-Cost）

设 \(n\ge3\)，每个 \(\alpha_i\) 都纯支撑于某个自由因子。若至少有两个不同因子被这些输入使用，则

\[
\langle\alpha_1,\ldots,\alpha_n\rangle_G\ne\varnothing
\Longrightarrow
0\in\langle\alpha_1,\ldots,\alpha_n\rangle_G.
\tag{1.12}
\]

于是，非平凡的已定义纯块 Massey 乘积必须把所有输入集中在同一因子。

再设 \(G\) 有有限 Grushko 分解

\[
G=G_1\amalg_p\cdots\amalg_pG_r\amalg_pF_s,
\tag{1.13}
\]

其中 \(G_\lambda\) 非平凡、非自由且 freely indecomposable，\(F_s\) 为秩 \(s\) 的自由 pro-\(p\) 群。定义

\[
b_M(G)=\max_{1\le\lambda\le r}d(G_\lambda),
\qquad d(H)=\dim_{\mathbb F_p}H^1(H,\mathbb F_p).
\tag{1.14}
\]

若一个非平凡已定义的 \(n\)-fold Massey 乘积具有纯块输入，且这些输入在相应最小生成元基下具有两两不交的非空支撑，则

\[
n\le b_M(G).
\tag{1.15}
\]

#### 证明

若输入跨越至少两个因子，则对每个固定 \(G_\lambda\)，至少有一个输入限制为零。全局可定义性由 R24 推出每个因子上的限制乘积可定义。定义的 Massey 乘积只要有一个零输入就含 \(0\)，所以每个因子限制乘积都含 \(0\)；R24 再推出全局乘积含 \(0\)，得到 (1.12)。

自由因子 \(F_s\) 的 \(H^2\) 为零，不能承载非平凡值。因此所有输入必须集中在某个非自由 \(G_\lambda\)。两两不交的非空生成元支撑至少各消耗一个最小生成元，故 \(n\le d(G_\lambda)\le b_M(G)\)。证毕。

### 1.3 Galois 解释

若一个 maximal pro-\(p\) Galois group \(G_F(p)\) 具有自由 pro-\(p\) 积分解，则 R24 把任意指定 tuple 的 Dwyer lifting problem 精确降到各 Galois block；R25 说明纯 valuation/Demuškin block 的非平凡 Massey 证书不能跨块形成。

这对 Elementary Type 研究有直接意义：该猜想的算术形式正预测大量有限生成 \(G_F(p)\) 可分解为自由 pro-\(p\) 积的 valuation-type blocks；此外，文献中已经构造/刻画了可作为 absolute Galois group 的 Demuškin 自由积。

### 1.4 新颖性边界

文献已知：

- Dwyer 把 definedness/vanishing 翻译为 \(\bar U_{n+1}/U_{n+1}\) 表示；
- 强 Massey vanishing property 对自由 pro-\(p\) 积保持。

R24–R25 的新增量是：对**固定输入 tuple** 给出 defining/lifting spaces 的精确因子化，并从中导出 mixed-block no-go 与 Grushko block-cost。它们是已知工具的新局部化后果，不应宣称 Dwyer 理论或自由积保持性本身为新发现。

限制：这里只证明有限自由积。无限自由 pro-\(p\) 积需要加入趋于单位的连续性条件，不能直接把 (1.6) 写成无约束直积。

---

## 2. Čech/deformation sector

### 2.1 Čech–Thom–Whitney 控制代数

设 \(k\) 为特征零域，\(\mathcal U=\{U_i\}\) 是空间或代数簇 \(X\) 的开覆盖，\(\mathfrak g\) 是控制某一变形问题的 DGLA sheaf。Čech semicosimplicial DGLA 为

\[
\prod_i\mathfrak g(U_i)
\Longrightarrow
\prod_{i<j}\mathfrak g(U_{ij})
\Longrightarrow
\prod_{i<j<k}\mathfrak g(U_{ijk})
\Longrightarrow\cdots.
\tag{2.1}
\]

令

\[
L=\operatorname{Tot}_{TW}(\mathfrak g(\mathcal U))
\tag{2.2}
\]

或其 transferred complete \(L_\infty\)-model。对 coherent sheaf \(F\)，可取 \(\mathfrak g=\operatorname{End}^*(E^\bullet)\)，其中 \(E^\bullet\to F\) 是局部自由解消；在标准 acyclicity 条件下

\[
H^1(L)\cong\operatorname{Ext}^1(F,F),
\qquad
H^2(L)\cong\operatorname{Ext}^2(F,F).
\tag{2.3}
\]

固定一个 base Maurer–Cartan 元后，以 twist 后的 \(L_\infty\)-代数工作，仍记结构映射为 \(\ell_r\)，并令 \(\ell_1=d\)。

### 2.2 Squarefree Artin cube

定义局部 Artin 环

\[
B_m=k[\varepsilon_1,\ldots,\varepsilon_m]/(\varepsilon_1^2,\ldots,\varepsilon_m^2),
\tag{2.4}
\]

其极大理想记为 \(\mathfrak m_m\)。对 \(S\subseteq[m]\)，写

\[
\varepsilon_S=\prod_{i\in S}\varepsilon_i.
\]

则

\[
B_m=\bigoplus_{S\subseteq[m]}k\varepsilon_S,
\qquad
\varepsilon_S\varepsilon_T=
\begin{cases}
\varepsilon_{S\cup T},&S\cap T=\varnothing,\\
0,&S\cap T\ne\varnothing.
\end{cases}
\tag{2.5}
\]

因此 \(L\widehat\otimes\mathfrak m_m\) 是 Boolean-support \(L_\infty\)-代数：微分保持参数支撑，而每个 \(r\)-bracket 把互不相交支撑送到其并集；有重叠时系数乘积为零。

### 定理 R26（Čech–Artin Split Support-Excision）

对 \(J\subseteq[m]\)，令

\[
B_J=k[\varepsilon_j:j\in J]/(\varepsilon_j^2:j\in J).
\]

包含 \(B_J\hookrightarrow B_m\) 与杀掉 \(J\) 外参数的投影 \(B_m\twoheadrightarrow B_J\) 诱导 split \(L_\infty\) retract

\[
L\widehat\otimes\mathfrak m_J
\longrightarrow
L\widehat\otimes\mathfrak m_m
\longrightarrow
L\widehat\otimes\mathfrak m_J.
\tag{2.6}
\]

因此，一个仅使用参数集合 \(J\) 的 Maurer–Cartan coefficient system，其：

1. proper coefficients 是否满足 MC equations；
2. maximal coefficient是否存在；
3. maximal obstruction class 是否为零；

在 \(B_J\) 中计算与在完整 \(B_m\) 中计算完全等价。任意 \(J\) 外参数及其 coefficients 都不能改变支撑包含于 \(J\) 的方程。

#### 证明

环包含与投影均保持乘法、微分与增广，且复合为恒等。张量后得到 split \(L_\infty\) maps。一个含有 \(J\) 外参数的 monomial 不可能通过乘法产生支撑包含于 \(J\) 的 monomial，因此投影与每个 \(\ell_r\) 相容。逐支撑读取 MC 方程即得结论。证毕。

### 2.3 Punctured Artin cube

给定一族 degree-one coefficients

\[
x_S\in L^1,
\qquad \varnothing\ne S\subsetneq J,
\tag{2.7}
\]

令

\[
x_{<J}=\sum_{\varnothing\ne S\subsetneq J}x_S\varepsilon_S.
\]

称其为一个 **compatible punctured \(J\)-cube**，若 Maurer–Cartan curvature

\[
\mathcal F(x)=\sum_{r\ge1}\frac1{r!}\ell_r(x,\ldots,x)
\tag{2.8}
\]

在每个 proper support \(T\subsetneq J\) 上的 coefficient 都为零。

注意：“每个 proper face 各自有某个 deformation”不够；这些数据必须在公共子面上一致，从而组合成同一个 punctured coefficient system。

定义 full-support curvature

\[
\Omega_J=
\sum_{r\ge2}\frac1{r!}
\sum_{\substack{S_1\sqcup\cdots\sqcup S_r=J\\S_a\ne\varnothing}}
\pm\ell_r(x_{S_1},\ldots,x_{S_r}),
\tag{2.9}
\]

其中内和遍历有序的不交非空分拆，符号为标准 Koszul 符号。

### 定理 R27（Punctured Artin Cube Obstruction and Sharp Cost）

对 compatible punctured \(J\)-cube：

1. \(d\Omega_J=0\)，故定义

   \[
   o_J(x)=[\Omega_J]\in H^2(L,d).
   \tag{2.10}
   \]

2. 存在 \(x_J\in L^1\) 使

   \[
   x_{\le J}=x_{<J}+x_J\varepsilon_J
   \]

   成为 full Maurer–Cartan solution，当且仅当

   \[
   o_J(x)=0.
   \tag{2.11}
   \]

3. 一个 \(r\)-ary bracket 对 \(\Omega_J\) 有贡献，必须满足

   \[
   r\le |J|.
   \tag{2.12}
   \]

4. 若 \(r=|J|\)，则所有 \(S_a\) 都被强迫为 singleton；因此最高 arity 的等号项正是 full polarization

   \[
   \pm\ell_{|J|}(x_{\{j_1\}},\ldots,x_{\{j_{|J|}\}}).
   \tag{2.13}
   \]

#### 证明

\(L_\infty\) Bianchi identity为

\[
\sum_{r\ge0}\frac1{r!}
\ell_{r+1}(x^{\otimes r},\mathcal F(x))=0.
\tag{2.14}
\]

读取 \(\varepsilon_J\)-coefficient。所有包含 proper-support curvature 的项因 compatibility 为零，剩下 \(d\Omega_J=0\)。加入 \(x_J\varepsilon_J\) 后，任何同时含该项与另一个正支撑 coefficient 的高阶 bracket 都带有重复参数，因 \(\varepsilon_J\varepsilon_S=0\) 而消失。因此新的 full-support equation 恰为

\[
dx_J+\Omega_J=0,
\tag{2.15}
\]

得到 (2.11)。式 (2.9) 的每个非零项要求 \(J\) 被分成 \(r\) 个非空块，所以 \(r\le|J|\)；等号时每块大小均为一。证毕。

### 2.4 Coherent-sheaf corollary

在 (2.3) 的条件下，R27 给出

\[
o_J(x)\in\operatorname{Ext}^2(F,F).
\tag{2.16}
\]

它精确检测：一族在所有 proper Artin coordinate faces 上彼此相容的 coherent-sheaf deformations，能否同时扩张到 full squarefree Artin cube。

若 \(o_J(x)\ne0\)，则每个 proper 参数子族都可实现，但所有 \(|J|\) 个一阶方向不能同时实现；这是真正的 simultaneous-effectivity defect，而不只是“存在一个二阶 obstruction”。

### 2.5 尖锐性与适用边界

若 minimal transferred \(L_\infty\)-model 上存在

\[
\ell_m(v_1,\ldots,v_m)=w\ne0,
\qquad [w]\ne0,
\]

且相关低支撑方程为零，则 \(B_m\) 上所有 proper faces 可填，而 full obstruction 为 \([w]\varepsilon_{[m]}\ne0\)。所以 (2.12) 的等号可达到。

该成本是 **squarefree independent-parameter cost**。它不声称在所有 Artin 环中至少需要 \(m\) 个变量；例如 \(k[t]/(t^{m+1})\) 的单一非 square-zero 参数可记录 \(m\) 次项。

---

## 3. 两个 sector 与 R19 的严格对应

| 结构位置 | pro-\(p\)/Galois | Čech/deformation |
|---|---|---|
| support 原子 | 自由 pro-\(p\) 因子 / Grushko block | square-zero Artin 参数 |
| proper defining object | \(G\to\bar U_{n+1}\) | punctured MC coefficient system |
| maximal filler | lift \(G\to U_{n+1}\) | full coefficient \(x_J\) |
| top obstruction | 中心扩张的 \(H^2(G,\mathbb F_p)\) 类 | \([\Omega_J]\in H^2(L)\) |
| excision 机制 | 自由积的 coproduct 泛性质 | 参数环的 split retract |
| no-go / cost | mixed-block 必消失；\(n\le b_M(G)\) | \(r\le|J|\)，等号强迫 singleton partition |

共同机制不是词汇相似，而是同一个可检验结构：

\[
\text{support decomposition}
\Longrightarrow
\text{resolved defining space factorization}
\Longrightarrow
\text{maximal filler obstruction}
\Longrightarrow
\text{sharp support cost}.
\]

---

## 4. 严格现实意义审计

### 4.1 pro-\(p\)/Galois

现实对象不是人为构造的 DGA，而是：

- maximal pro-\(p\) Galois groups；
- Elementary Type 猜想中的 valuation/Demuškin blocks；
- 文献已实现为 absolute Galois groups 的 Demuškin 自由积；
- Galois embedding problems \(G\to\bar U_{n+1}\leftarrow U_{n+1}\)。

R24 将一个全局 nonabelian embedding problem 化为独立 block problems；R25 排除了跨自由块产生纯支撑非平凡 Massey obstruction 的可能。这既能缩小搜索空间，也能说明某个候选非平凡类必须来自哪个 valuation block。

### 4.2 Čech/deformation

现实对象包括 coherent sheaves、vector bundles、complex structures，以及其他由 sheaf DGLA / semicosimplicial DGLA 控制的局部—整体变形问题。R27 检测的不是抽象方程，而是：

> 多个一阶变形方向分别及任意 proper 子族都能相容实现，但全体方向不能同时实现。

在 coherent-sheaf 情形，该失败由一个明确的 \(\operatorname{Ext}^2(F,F)\) 类证实，并可从 Čech 局部数据计算。

### 4.3 新颖性评级

| 定理 | 数学新增量 | 评级 |
|---|---|---:|
| R24 | 固定 tuple 的 defining/lift fibers 精确自由积分解 | 强 reduction theorem |
| R25 | mixed-block 非平凡性 no-go 与 Grushko arity bound | 新对象级推论 |
| R26 | TW 控制代数上的参数 support split-excision | 结构定理；证明短但非空泛 |
| R27 | compatible punctured Artin cube 的唯一 full-support \(H^2\) obstruction 与尖锐 arity cost | 强 reduction theorem |

R26 单独看接近形式性；R27 的 compatible-face hypothesis、唯一 full-support obstruction 和 equality rigidity 才是满足项目验收标准的实质部分。

---

## 5. 核心推广审计更新

R23 的三领域阈值现在从“未达到”更新为：

\[
\boxed{\text{三个独立自然 sector 已初步达到对象级非平凡定理阈值。}}
\tag{5.1}
\]

然而这不触发 Frozen v1.0 修改，因为：

1. R24–R27 与 Frozen core 相容，没有给出反例或内部矛盾；
2. 它们是由既有 primitive 导出的 sector theorems；
3. Frozen 治理规则明确规定 sector theorem 默认进入派生层。

因此正式状态为

\[
\boxed{
\begin{gathered}
\text{CORE PASS + Candidate Extension Layer v0.3}\\
\text{(Cross-Sector Validated).}
\end{gathered}}
\tag{5.2}
\]

下一次可能的“promotion”不应是增加核心公理，而应把以下模式冻结为一个稳定派生 theorem schema：

> 当 defining/filler problem 由 split support decomposition 控制时，resolved solution spaces 局部化，并产生可加支撑成本与等号刚性。

在正式冻结该 schema 前，还应压力测试两个非 split 情形：amalgamated pro-\(p\) products 与没有参数环 section 的小扩张。它们最可能揭示真正的 correction term。

---

## 6. 首轮文献监测基线

### pro-\(p\)/Galois

1. S. Blumer, A. Cassella, C. Quadrelli, *Groups of p-absolute Galois type that are not absolute Galois groups*, arXiv:2112.06744。包含 Dwyer 判据、RAAG strong Massey vanishing、自由 pro-\(p\) 积保持性。
2. I. Efrat, *The Elementary Type Conjecture for Maximal Pro-p Galois groups*, arXiv:2509.10168。2025 年综述并推进 valuation/free-product 构造与猜想。
3. T. Bar-On, *Free product of Demushkin groups as absolute Galois group*, arXiv:2408.13875。给出自由积确实出现为 absolute Galois group 的自然对象类。

### Čech/deformation

1. D. Fiorenza, D. Iacono, E. Martinengo, *Differential graded Lie algebras controlling infinitesimal deformations of coherent sheaves*, arXiv:0904.1301。建立 Čech–Thom–Whitney 控制 DGLA 与 \(\operatorname{Ext}^{1,2}\) 解释。
2. J. P. Pridham, *Derived deformation functors, Koszul duality, and Maurer-Cartan spaces*, arXiv:2503.05307。更新 derived Schlessinger / Maurer–Cartan 等价链。
3. M. Corrêa, S. Noja, *Formal moduli and the splitting theory of supermanifolds*, arXiv:2605.03166。2026 年实例显示 filtered MC tower 与 higher \(L_\infty\) Kuranishi relations 正在实际几何中出现。

---

## 7. 当前结论

本轮两个跨域测试均通过，而且通过方式不同：

- pro-\(p\) 线通过 coproduct 的非交换表示空间因子化得到 no-go；
- Čech/deformation 线通过 Artin 参数的 Boolean monomial 分级得到 simultaneous-effectivity obstruction。

它们不是 toric topology 的变体，因此项目首次获得真正的三领域独立验证。最值得继续攻击的问题已经从“还能不能找到第三领域”变为：

\[
\boxed{
\text{split support theorem 在 non-split gluing 中的 correction term 是什么？}}
\]

候选答案分别是 amalgamation holonomy 与小扩张的 transgression / higher bracket；这将是下一阶段的关键问题。
