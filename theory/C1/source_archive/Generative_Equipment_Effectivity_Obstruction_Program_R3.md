# 数学内生生成性理论

## 有限逆图同时有效化障碍机 R3

日期：2026-09-25  
逻辑地位：Frozen v1.0 的**导出层扩展**；不修改冻结核心  
直接前置：`Generative_Equipment_Remaining_Proofs_Completion_R2.md`  
前置文件 SHA-256：`12f39f5a7937f5aba43e5ef01cacaf8dbf9ec44f7ff6759808d4823f86c425c9`  
本报告目标：把 R2 的可数 tower 结论推广为有限逆图上的、可逐层计算的
同时有效化障碍机，并严格分开“是否存在”与“存在以后有多少高阶选择”。

---

## 0. 本轮得到的结论

本报告完成第一条后冻结主线：

\[
\boxed{
\text{comparison fiber theorem}
+\text{Reedy matching obstruction}
+\text{branch-relative derived-limit spectral sequence}
}
\]

其输出分为两个不能混淆的层：

| 层 | 问题 | 严格工具 | 输出 |
|---|---|---|---|
| 存在层 | 局部 realization 能否同时粘合 | matching fibers 的逐度提升 | 空 / 非空，以及首次失败位置 |
| 高阶层 | 已选全局 branch 有多少变形与自同构 | Bousfield--Kan 型谱序列 | \(R^s\!\lim\pi_t\)、差分、扩张 |

最重要的逻辑修正是：通常的带基点
\(R^s\!\lim\pi_t\) 谱序列**不能独立用来证明全局点存在**。它需要先选定
一个全局 branch，或加入足以定义相应局部系数的等价数据。存在性必须先由
unpointed matching obstruction 处理。

本轮的主定理是定理 3.2；有限终止定理是定理 4.2。

---

## 1. 预备约定与逻辑校正

### 1.1 空间模型

全文在 simplicial sets 的 Kan--Quillen 模型中陈述。所有“空间”均可由
Kan complex 表示；所有 homotopy limit 均取导出意义。

连通度约定为：

- \((-1)\)-connected 表示非空；
- \(0\)-connected 表示路径连通；
- \(c\geq 1\) 时，\(c\)-connected 表示路径连通且
  \(\pi_k=0\) 对 \(1\leq k\leq c\)；
- weakly contractible 表示非空且所有正维 homotopy groups 消失。

有限积的连通度是各因子连通度的下确界。

### 命题 1.2（带基点谱序列的存在性循环）

设 \(X:I\to\mathsf{sSet}\) 是一图。若要逐对象写出一个严格相容的带基点
homotopy-group 图

\[
i\longmapsto \pi_t(X_i,x_i),
\]

则所需的相容基点族 \((x_i)\) 正是严格极限 \(\lim_I X\) 的一个点。若
\(X\) 已是计算 homotopy limit 的 fibrant 图，则它也是
\(\operatorname{holim}_I X\) 的一个点。

因此，以某个全局点 \(x\) 为 abutment 基点的谱序列

\[
R^s\!\lim_I\pi_t(X_i,x_i)
\Longrightarrow
\pi_{t-s}(\operatorname{holim}_I X,x)
\]

是**branch-relative** 的：它分析一个已经存在的 branch，不能在不增加
unpointed/fringed obstruction data 的情况下，用作该 branch 存在的
非循环证明。

#### 证明

自然变换 \(*\Rightarrow X\) 的数据，就是对每个 \(i\) 选择
\(x_i\in X_i\)，并要求每条 \(i\to j\) 都满足
\(X(i\to j)(x_i)=x_j\)。这正是 \(\lim_I X\) 的点。反过来，极限点逐分量
给出这样的自然变换。带基点的 transition homomorphisms 要严格定义，便需要
这些等式；若只选择路径，则还必须加入路径之间的更高相干。故简单的 pointed
derived-limit 公式已经使用了它试图证明的全局 branch。证毕。

#### 注 1.3

命题 1.2 不否认完整的 unpointed obstruction theory、非阿贝尔
\(\lim^1\)、局部系数或 fringed spectral sequence。它只排除以下错误推理：
先假装已有相容基点图，再用由它产生的 pointed spectral sequence 证明相容
基点存在。

---

## 2. 有限逆图的 matching calculus

### 定义 2.1（有限逆范畴）

称小范畴 \(I\) 为维数至多 \(d\) 的有限逆范畴，若：

1. \(I\) 有有限多个对象与 morphisms；
2. 存在 degree 函数
   \[
   |-|:\operatorname{Ob}(I)\longrightarrow\{0,1,\ldots,d\};
   \]
3. 每个非恒等 morphism \(i\to j\) 都严格降 degree：\(|i|>|j|\)。

令 \(I_{<r}\)、\(I_{\leq r}\)、\(I_r\) 分别表示由 degree
\(<r\)、\(\leq r\)、\(=r\) 的对象张成的满子范畴。

逆性立即推出：同一 degree 的不同对象之间没有 morphism；任意非退化
composable chain 的长度至多为 \(d\)。

### 定义 2.2（matching object 与 Reedy fibrancy）

对图 \(X:I\to\mathsf{sSet}\) 及对象 \(i\)，令

\[
M_iX
:=
\lim_{(i\to j)\in\partial(i\downarrow I)}X_j,
\]

其中 \(\partial(i\downarrow I)\) 只保留从 \(i\) 出发的非恒等箭头。
由结构映射得到 matching map

\[
m_i:X_i\longrightarrow M_iX.
\]

若每个 \(m_i\) 都是 Kan fibration，则称 \(X\) Reedy fibrant。degree
为零时 matching category 为空，因而 \(M_iX=*\)。

### 引理 2.3（精确的逐度拉回公式）

令 \(X:I\to\mathsf{sSet}\)，并记

\[
L_{<r}:=\lim_{I_{<r}}X,
\qquad
L_{\leq r}:=\lim_{I_{\leq r}}X.
\]

每个 \(x\in L_{<r}\) 在对象 \(i\in I_r\) 处诱导 matching datum

\[
\mu_i(x)\in M_iX.
\]

存在自然拉回同构

\[
\boxed{
L_{\leq r}
\cong
L_{<r}
\times_{\prod_{i\in I_r}M_iX}
\prod_{i\in I_r}X_i.
}
\tag{2.3.1}
\]

若 \(X\) Reedy fibrant，则 restriction

\[
q_r:L_{\leq r}\longrightarrow L_{<r}
\]

是 Kan fibration，且其在 \(x\) 上的严格 fiber 同时也是 homotopy
fiber，并满足

\[
\boxed{
\operatorname{Ext}_r(x)
:=\operatorname{fib}_x(q_r)
\simeq
\prod_{i\in I_r}
\operatorname{hofib}_{\mu_i(x)}(m_i).
}
\tag{2.3.2}
\]

#### 证明

一个 \(I_{\leq r}\)-相容族由两部分组成：

1. 一个低于 \(r\) 的相容族 \(x\in L_{<r}\)；
2. 对每个 \(i\in I_r\)，一个 \(y_i\in X_i\)，其沿所有
   \(i\to j\) 的像恰好等于 \(x\) 所给出的 matching datum
   \(\mu_i(x)\)。

由于同 degree 对象间没有非恒等箭头，第二项之间没有额外兼容条件。这正是
(2.3.1) 的拉回泛性质。若 \(X\) Reedy fibrant，则有限积
\(\prod_i m_i\) 是 Kan fibration；其拉回 \(q_r\) 也是 Kan fibration。
fibration 的严格 fiber 计算 homotopy fiber，且拉回 fiber 是各 matching
fibers 的乘积，得到 (2.3.2)。证毕。

### 定义 2.4（component obstruction profile）

对 \(x\in L_{<r}\) 与 \(i\in I_r\)，定义二值障碍

\[
o_{r,i}(x)=0
\quad\Longleftrightarrow\quad
[\mu_i(x)]
\in
\operatorname{im}\!\left(
\pi_0X_i\xrightarrow{\pi_0m_i}\pi_0M_iX
\right).
\tag{2.4.1}
\]

这不是被强行阿贝尔化的“障碍群元素”，而是精确的 component-membership
condition。它在最一般的存在层比群值障碍更基本。

### 定理 2.5（有限逆图的精确存在性与统一充分判据）

令 \(I\) 为有限逆范畴，\(X:I\to\mathsf{sSet}\) 为 Reedy fibrant 图。

1. **逐步必要充分条件。** 对给定 \(x\in L_{<r}\)，以下条件等价：
   
   \[
   x\text{ 可延拓到 }L_{\leq r};
   \]
   
   \[
   \operatorname{Ext}_r(x)\neq\varnothing;
   \]
   
   \[
   o_{r,i}(x)=0\quad\text{对每个 }i\in I_r.
   \]

2. **全局必要充分递归。** \(\lim_I X\neq\varnothing\) 当且仅当存在一条
   逐度相容链
   \[
   x_{<0}=*,\ x_{\leq0},\ldots,x_{\leq d},
   \]
   使每一步的全部 component obstructions 都消失。

3. **统一充分条件。** 若每个 matching map 都在 \(\pi_0\) 上满射，
   \[
   \pi_0X_i\twoheadrightarrow\pi_0M_iX,
   \tag{2.5.1}
   \]
   则 \(\lim_I X\neq\varnothing\)。

4. **连通度传播。** 固定 \(c\geq-1\)。若对每个 \(i\) 和每个 vertex
   \(b\in M_iX\)，fiber
   \[
   F_{i,b}:=\operatorname{fib}_b(m_i)
   \]
   都是 \(c\)-connected，则 \(\lim_I X\) 也是 \(c\)-connected。

5. 特别地，所有 matching fibers 非空蕴含极限非空；全部路径连通蕴含
   极限路径连通；全部 weakly contractible 蕴含极限 weakly contractible。

#### 证明

由引理 2.3，\(x\) 的延拓空间正是 matching fibers 的有限积。该乘积非空
当且仅当每一 fiber 非空。对 Kan fibration \(m_i\)，给定
\(b=\mu_i(x)\)，fiber 非空当且仅当 \([b]\) 落在
\(\pi_0(m_i)\) 的像中：若只有某个 \(y\) 的像与 \(b\) 同 component，取一条
连接它们的路径并用 fibration path lifting，即可把 \(y\) 移到严格位于
\(b\) 上方的点。这证明第一项。

从空骨架 \(L_{<0}=*\) 开始，有限次使用第一项，得到第二项。条件 (2.5.1)
使任意已构造的 \(x\) 在下一层的所有障碍同时消失，有限归纳给出第三项。

对第四项，\(q_r:L_{\leq r}\to L_{<r}\) 是 fibration，其每个 fiber 是
若干个 \(c\)-connected spaces 的有限积，故仍为 \(c\)-connected。从
\(*\) 开始，对 fibration 的 homotopy long exact sequence 作有限归纳，
即得总空间为 \(c\)-connected。\(c=-1,0\) 分别按非空性与路径提升解释。
weak contractibility 情形对所有有限 \(c\) 应用同一结论，或直接使用长正合
序列。证毕。

### 推论 2.6（严格极限计算 homotopy limit）

在定理 2.5 的条件下，

\[
\lim_I X\simeq\operatorname*{holim}_I X.
\tag{2.6.1}
\]

#### 证明说明

有限逆范畴带有 inverse Reedy structure。Reedy fibrant 图上的 ordinary
limit 是 derived limit 的模型；等价地，引理 2.3 把极限写成有限列沿
fibrations 的拉回，而这些拉回同时是 homotopy pullbacks。

---

## 3. 一般同时有效化障碍定理

### 3.1 输入接口

设 \(I\) 为有限逆范畴，\((C_i)_{i\in I}\) 是相容的 comparison functors，
\(\xi=(\xi_i)\) 是相容 formal datum。记局部 effectivity spaces 为

\[
E_i:=\operatorname{EffFib}_{C_i}(\xi_i).
\]

沿用 R1--R2 已证明的 comparison-fiber/limit 接口：

\[
\operatorname{EffFib}_{\lim_I C_i}(\xi)
\simeq
\operatorname*{holim}_{i\in I}E_i.
\tag{3.1.1}
\]

取图 \(E:I\to\mathsf{sSet}\) 的一个 Reedy fibrant replacement
\(E\xrightarrow{\sim}X\)。

### 定理 3.2（General Simultaneous-Effectivity Obstruction Theorem）

在 3.1 的条件下：

1. 有自然弱等价
   \[
   \operatorname{EffFib}_{\lim_I C_i}(\xi)
   \simeq
   \lim_I X.
   \tag{3.2.1}
   \]

2. 对每一 degree \(r\) 及每个已经实现的低阶 branch
   \(x\in L_{<r}\)，其下一步同时有效化空间为
   \[
   \operatorname{Ext}^{\mathrm{eff}}_r(x)
   \simeq
   \prod_{i\in I_r}
   \operatorname{hofib}_{\mu_i(x)}
   \bigl(X_i\to M_iX\bigr).
   \tag{3.2.2}
   \]

3. formal datum \(\xi\) simultaneously effective，当且仅当存在一条从
   degree \(0\) 到 \(d\) 的 branch，使 (3.2.2) 在每一步都非空。

4. 若全部 matching maps
   \[
   X_i\longrightarrow M_iX
   \]
   在 \(\pi_0\) 上满射，则 \(\xi\) simultaneously effective。

5. 若全部 matching fibers 为 \(c\)-connected，则全局 effectivity space
   也是 \(c\)-connected。特别地，matching fibers 全部 weakly
   contractible 时，全局 realization 存在且在 coherent homotopy 意义下
   唯一。

#### 证明

由 (3.1.1)、Reedy replacement 的 homotopy-limit invariance 以及推论 2.6，
得到 (3.2.1)。其余各项分别由引理 2.3 与定理 2.5 直接得到。证毕。

### 注 3.3（“统一满射”不是必要条件）

定理 3.2(4) 是一个容易验证、对所有低阶 branch 都有效的**统一充分条件**，
不是全局非空的必要条件。真正的必要充分条件是 3.2(3)：只需存在一条成功
branch，不要求每个可能的 matching datum 都可提升。第 6.2 节给出最小反例。

### 注 3.4（模型依赖与不变量）

某个特定 Reedy replacement 的中间 matching objects 不是冻结核心中新添的
绝对对象。它们是计算装置。以下输出是 homotopy-invariant 的：

- 全局 effectivity space 的弱同伦型；
- 是否为空；
- 每个已选全局 component 的 homotopy groups；
- “存在 / 非唯一 / contractible”这类最终判定。

“首次失败在哪个 degree”依赖所选 filtration 与 fibrant model，但作为诊断
信息仍然有用。

---

## 4. 选定 branch 后的 derived-limit 层

### 定义 4.1（维数与简单性假设）

令 \(I\) 为有限逆范畴。以其 nerve 中非退化 simplices 的最高维数为
\(\dim N(I)=d\)。逆 degree 函数保证此数有限。

称连通 Kan complex \(Y\) simple，若 \(\pi_1Y\) 阿贝尔，且其对所有
\(\pi_tY\)、\(t\geq2\) 的作用平凡。该条件保证沿路径改变基点不会给
coefficient diagram 引入未记录的共轭或 monodromy 歧义。

### 定理 4.2（有限维、截断的 branch-relative obstruction spectral sequence）

设：

1. \(I\) 是 \(\dim N(I)=d<\infty\) 的有限逆范畴；
2. \(X:I\to\mathsf{sSet}\) Reedy fibrant；
3. 已由定理 2.5 或 3.2 选定一点
   \(x\in\lim_I X\simeq\operatorname{holim}_I X\)；
4. 每个 \(X_i\) 连通、simple 且 \(n\)-truncated。

则存在以 \(x\) 为 abutment branch 的 Bousfield--Kan 型 homotopy-limit
谱序列

\[
E_2^{s,t}
\cong
R^s\!\lim_I\pi_t(X_i,x_i)
\quad\Longrightarrow\quad
\pi_{t-s}(\operatorname*{holim}_I X,x),
\tag{4.2.1}
\]

其中正总次数 \(t-s\geq1\) 为群值收敛区，\(t-s=0\) 必须按标准
fringe/pointed-set 解释。并且：

\[
E_2^{s,t}=0
\quad\text{若 }s>d\text{ 或 }t>n.
\tag{4.2.2}
\]

所以所有可能项位于有限矩形

\[
0\leq s\leq d,
\qquad
1\leq t\leq n,
\]

谱序列至迟在

\[
E_{\max\{2,d+1\}}=E_\infty
\tag{4.2.3}
\]

稳定。换言之，在这个 sector 中高阶障碍计算是有限的，而不是无限等待的
形式过程。

#### 证明

对图 \(X\) 作标准 cosimplicial replacement：第 \(s\) 层由所有
\(s\)-重 composable chains 上的对象乘积构成。其 totalization 计算
\(\operatorname{holim}_I X\)。以全局点 \(x\) 为 compatible basepoint，
对 totalization tower 取 homotopy exact couples，得到 (4.2.1)。simple
假设使 coefficient systems 在此无扭曲版本中良定义，并控制低维 fringe。

对阿贝尔 coefficient diagram \(A:I\to\mathsf{Ab}\)，标准 normalized
cosimplicial cochain complex

\[
N^s(I;A)
\subseteq
\prod_{i_0\to i_1\to\cdots\to i_s}A(i_s)
\]

计算 \(R^s\!\lim_I A\)。当 \(s>d\) 时不存在非退化 \(s\)-chains，故
\(N^s(I;A)=0\)，从而 \(R^s\!\lim_I A=0\)。另一方面，
\(n\)-truncatedness 给出 \(\pi_tX_i=0\) 对所有 \(t>n\)。因此谱序列只占
有限矩形；不存在无限 filtration 或 Boardman 型无穷收敛问题。差分

\[
d_r:E_r^{s,t}\longrightarrow E_r^{s+r,t+r-1}
\]

在 \(r>d\) 时无目标；又因该谱序列从 \(E_2\) 页起，得到 (4.2.3)。证毕。

### 推论 4.3（维数一的 Milnor 型短正合序列）

在定理 4.2 的条件下，若 \(d\leq1\)，则没有可能的 \(d_r\)、\(r\geq2\)。
对每个 \(q\geq1\)，存在 filtration 所给出的自然短正合序列

\[
0\longrightarrow
R^1\!\lim_I\pi_{q+1}(X_i,x_i)
\longrightarrow
\pi_q(\operatorname*{holim}_I X,x)
\longrightarrow
\lim_I\pi_q(X_i,x_i)
\longrightarrow0.
\tag{4.3.1}
\]

低维 \(q=0\) 仍须使用 pointed-set/nonabelian fringe，不能无条件写成阿贝尔
群短正合序列。

### 推论 4.4（有限逆图的 rigidity 判据）

在定理 4.2 的条件下，再假设：

1. 定理 2.5 的 matching fibers 至少 \(0\)-connected，因而全局
   homotopy limit 路径连通；
2. 对所有满足 \(t-s\geq1\) 的 \((s,t)\)，
   \[
   R^s\!\lim_I\pi_t(X_i,x_i)=0.
   \]

则

\[
\operatorname*{holim}_I X\simeq *.
\]

#### 证明

第二条件使 (4.2.1) 在所有正总次数上的 \(E_2\) 项消失，故全局 branch 的
所有正维 homotopy groups 消失。第一条件给出路径连通性。Kan complex 的
Whitehead 判据给出 weak contractibility。证毕。

### 注 4.5（稳定版本）

若 effectivity deformation object 已提升到 spectra，则无需 unstable 的
simple/fringe 限制：同一 construction 给出稳定的

\[
E_2^{s,t}=R^s\!\lim_I\pi_tE_i
\Longrightarrow
\pi_{t-s}\operatorname*{holim}_I E_i.
\]

因此未来若某个 sector 天然具有 tangent spectrum，稳定版通常比直接处理
非阿贝尔低维数据更干净。

---

## 5. 可执行算法

对一个具体 finite inverse sector，计算流程如下。

### 阶段 A：存在性

1. 写出局部 fibers \(E_i=\operatorname{EffFib}_{C_i}(\xi_i)\)。
2. 取 Reedy fibrant model \(X\)。
3. 按 degree 计算 \(M_iX\) 与 \(m_i:X_i\to M_iX\)。
4. 从 \(L_{<0}=*\) 开始；对每个当前 branch \(x\)，检查
   \([\mu_i(x)]\in\operatorname{im}\pi_0(m_i)\)。
5. 若所有 branch 都在某层失败，则全局 effectivity fiber 为空；若至少一条
   branch 到达最高 degree，则 simultaneously effective。

### 阶段 B：高阶结构

6. 选定成功 branch \(x\)。
7. 计算 coefficient diagrams \(\pi_t(X_i,x_i)\)。
8. 用 normalized chain complex 计算 \(R^s\!\lim\)。
9. 运行至多到 \(E_{\max\{2,d+1\}}\)，并解决最后的 filtration
   extensions。

最终输出不再只是 yes/no，而是：

| 输出 | 数学含义 |
|---|---|
| empty | formal datum 不可同时实现 |
| nonempty, disconnected | 有多个本质不同 realization branches |
| connected, higher \(\pi_t\neq0\) | realization 唯一到 component，但有高阶 deformation/isotropy |
| contractible | coherent realization 存在且唯一 |

---

## 6. 压力测试

### 6.1 单对象图：恢复原始 effectivity

若 \(I=*\)，则唯一对象的 matching object 为 \(*\)，且

\[
\operatorname*{holim}_I X=X.
\]

定理 2.5 的第一层条件正好是 \(X\neq\varnothing\)，没有产生虚假的额外
障碍。通过。

### 6.2 单箭头图：检验“充分但非必要”

令 \(I=(1\to0)\)，图为 \(f:X_1\to X_0\)。严格极限自然同构于 \(X_1\)：

\[
\lim_I X\cong X_1.
\]

逐层算法先选 \(x_0\)，再问它是否落在 \(\pi_0f\) 的像中。存在一条成功
branch 等价于 \(X_1\neq\varnothing\)。

取离散图

\[
X_1=*,
\qquad
X_0=\{0,1\},
\qquad
f(*)=0.
\]

则极限非空，但 \(\pi_0f\) 不满射。这证明定理 3.2(4) 不能被误写为必要
条件；而 branchwise 条件 3.2(3) 仍是精确的。通过。

### 6.3 cospan：恢复 homotopy pullback 的相交障碍

令 indexing shape 为

\[
1\longrightarrow0\longleftarrow2.
\]

Reedy fibrant 图的极限为

\[
X_1\times_{X_0}X_2
\simeq
X_1\times^h_{X_0}X_2.
\]

先选 \(x_0\)，随后必须同时把它提升到 \(X_1\) 与 \(X_2\)。extension
space 正是

\[
\operatorname{fib}_{x_0}(X_1\to X_0)
\times
\operatorname{fib}_{x_0}(X_2\to X_0).
\]

若两个 matching maps 都在 \(\pi_0\) 上满射，则任意 \(x_0\) 都可同时
提升。该范畴的 nerve 维数为一，故高阶层退化为推论 4.3 的短正合序列。
通过。

### 6.4 可数 tower：恢复 R2 定理 1.1

对 tower

\[
X_0\longleftarrow X_1\longleftarrow X_2\longleftarrow\cdots,
\]

第 \(n\) 层 matching object 等价于 \(X_{n-1}\)，matching map 就是
transition map。因而条件变成

\[
\pi_0X_n\twoheadrightarrow\pi_0X_{n-1}.
\]

有限逆图证明在每一有限 stage 完成；加入 countable dependent choice 后，
递归选择得到严格相容无限族，恰好恢复 R2 定理 1.1。可数 tower 不再是新
理论的孤立特例，而是 matching machine 的一维无限版本。通过。

### 6.5 有限群作用：检验适用边界

令非平凡有限群 \(G\) 通过左平移作用在离散空间 \(G\) 上，并把它看成
\(BG\)-indexed diagram。唯一对象上的局部空间 \(G\) 非空，但

\[
\operatorname*{holim}_{BG}G
\simeq
G^{hG}
\simeq
\operatorname{Map}_G(EG,G)
=\varnothing.
\]

确实，\(EG\) 连通而 \(G\) 离散，所以任意 map \(EG\to G\) 为常值；但自由
左平移作用没有 \(G\)-固定常值，故不存在 equivariant map。

这说明“逐对象非空 \(\Rightarrow\) homotopy limit 非空”在一般 indexing
category 上为假。\(BG\) 也不是逆范畴：非恒等 automorphism 不可能严格降低
degree；其 nerve 还有任意长的非退化 chains。因此本报告没有偷偷把有限逆图
结论推广到群作用图。边界测试通过。

### 6.6 二维图：检验谱序列不会被过早压平

若 \(\dim N(I)=2\)，则

\[
R^s\!\lim=0\quad(s>2),
\]

但 \(R^2\!\lim\) 可以存在，且谱序列仍允许唯一可能的高阶差分类型

\[
d_2:E_2^{0,t}\longrightarrow E_2^{2,t+1}.
\]

所以不能把 R2 的 tower/Milnor 短正合序列机械推广到所有有限逆图。正确结论
是“维数一给短正合序列，维数二开始必须允许差分”。本机器保留了这一信息。
通过。

### 6.7 压力测试总表

| 测试族 | 期望行为 | 实际输出 | 结论 |
|---|---|---|---|
| 单对象 | 回到单个 fiber 非空性 | 完全恢复 | PASS |
| 单箭头 | 满射只能是统一充分条件 | 给出最小反例 | PASS |
| cospan | 同时提升等于 homotopy pullback | 精确恢复 | PASS |
| 可数 tower | 回到 R2 的 \(\pi_0\)-满射递归 | 精确恢复 | PASS |
| 自由有限群作用 | objectwise nonempty 仍可全局空 | 正确排除于假设外 | PASS |
| nerve 维数二 | 允许 \(R^2\lim\) 与 \(d_2\) | 未误写成 Milnor 序列 | PASS |

---

## 7. 证明账本与新颖性边界

### 7.1 本报告内证明的部分

1. finite inverse diagram 的逐度 pullback decomposition；
2. extension space 的 matching-fiber 公式；
3. branchwise 必要充分条件；
4. matching \(\pi_0\)-满射的统一充分条件；
5. matching-fiber 连通度向全局极限的传播；
6. 与 R2 comparison-fiber theorem 组合后的 simultaneous-effectivity theorem；
7. 带基点谱序列不能非循环地承担一般存在性证明的逻辑校正；
8. finite cohomological dimension 与 truncatedness 给出的有限终止结论。

### 7.2 明确引用的标准背景

以下工具本身不宣称为本理论新发现：

- inverse Reedy model structure 与 fibrant diagram 的 strict-limit model；
- cosimplicial replacement 对 homotopy limit 的计算；
- Bousfield--Kan homotopy-limit spectral sequence；
- derived limits 由 normalized cosimplicial cochains 计算；
- fibration long exact sequence 与 Whitehead criterion。

本报告的理论贡献是把这些标准工具接到冻结核心的 effectivity-fiber 接口上，
并给出“unpointed existence first, pointed deformation second”的严格分层。

### 7.3 没有声称的结论

本报告没有声称：

1. 任意 indexing category 上 objectwise nonempty 都蕴含全局 nonempty；
2. matching \(\pi_0\)-满射是全局非空的必要条件；
3. 不选全局 branch 就能无条件写出普通阿贝尔群值 obstruction spectral
   sequence；
4. 所有 sector 的 coefficient systems 都自动 simple 或 untwisted；
5. 标准 Reedy/Bousfield--Kan machinery 本身是本理论首创。

---

## 8. 对冻结版本的影响

R3 没有发现 Frozen v1.0 或 R2 的反例，也不要求修改核心定义。它增加的是
一个 derived bridge theorem：

\[
\boxed{
\begin{array}{c}
\text{local effectivity fibers}\\
\Downarrow\\
\text{matching existence profile}\\
\Downarrow\ \text{choose a branch}\\
R^s\!\lim\pi_t\text{ deformation profile}
\end{array}
}
\]

这也使 R2 的三层描述更精确：在一般有限逆图上，首先是逐层
component-membership obstruction；只有选出 coherent branch 后，才进入
derived-limit 高阶层。

---

## 9. 下一项精确任务

理论发展的下一步不应继续只抽象推广 indexing shapes，而应把本机器投入一个
可完全计算的 sector。建议优先顺序为：

1. **有限 posets 与二维 nerves**：给出显式 \(R^2\lim\) 和非零 \(d_2\)
   样例，验证二维 coherence obstruction；
2. **低 Postnikov spaces**：把 matching fibers 写成 Eilenberg--Mac Lane
   fibers，使 obstruction 变成普通 cohomology classes；
3. **有限 simplicial diagrams**：寻找由本理论接口导出的、而非重新表述标准
   Reedy theorem 的独立结论；
4. 再考察含 automorphisms 的 indexing categories，此时必须引入 equivariant
   fixed-point obstruction 或完整 unpointed descent machinery。

下一份报告的合格目标应是：至少产生一个事先未知、可证伪、且不以定义为真的
sector theorem。

---

## 10. 标准背景来源

1. A. K. Bousfield and D. M. Kan,
   [Homotopy Limits, Completions and Localizations](https://doi.org/10.1007/978-3-540-38117-4)，
   尤其是 homotopy inverse limits、cosimplicial replacement、derived limits
   与 homotopy spectral sequence。
2. A. K. Bousfield,
   [Cosimplicial resolutions and homotopy spectral sequences in model categories](https://doi.org/10.2140/agt.2003.3.109)，
   *Algebraic & Geometric Topology* 3 (2003), 109--141。
3. Daniel Dugger,
   [A Primer on Homotopy Colimits](https://pages.uoregon.edu/ddugger/hocolim.pdf)，
   §§17--18：category cohomology/derived limits、homotopy-limit spectral
   sequence、低维 fringe 与 tower/Milnor 情形。
4. Emily Riehl and Dominic Verity,
   [The theory and practice of Reedy categories](https://arxiv.org/abs/1304.6871)，
   Reedy diagrams、matching objects 与 homotopy limits 的模型化背景。

---

## 11. R3 最终判定

\[
\boxed{
\begin{array}{rcl}
\text{finite inverse simultaneous existence}
&=&\text{SOLVED EXACTLY BY MATCHING FIBERS},\\[1mm]
\text{uniform practical criterion}
&=&\pi_0\text{-SURJECTIVE MATCHING MAPS},\\[1mm]
\text{higher deformation after a branch}
&=&R^s\!\lim\pi_t\text{ SPECTRAL SEQUENCE},\\[1mm]
\text{finite }d\text{ and }n\text{-truncated input}
&=&\text{FINITE TERMINATION AT }E_{\max\{2,d+1\}},\\[1mm]
\text{frozen core}
&=&\text{UNCHANGED}.
\end{array}
}
\]

因此，“下一步”已经从路线建议转化为一个可执行的定理机器。它既能给出
simultaneous effectivity 的严格充分条件，也能在失败时定位到具体 matching
stage；而在成功以后，它用有限 derived-limit 计算区分唯一性、变形与高阶
isotropy。
