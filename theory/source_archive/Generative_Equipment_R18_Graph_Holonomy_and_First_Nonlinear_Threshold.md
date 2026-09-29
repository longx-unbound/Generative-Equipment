# 生成装备研究 R18：极值 Moment-Angle Massey 的图 Holonomy 判据与首个非线性阈值

日期：2026-09-29  
逻辑地位：R17 的继续；Frozen v1.0 的派生 sector theorem，不修改冻结核心

## 0. 本轮突破

R17 把顶点支撑最优的 \(n\)-重 Massey 问题压缩到

\[
K\subseteq(S^0)^{*n}
\]

及 \(n\) 对 missing edges

\[
J_i=\{x_i,y_i\}.
\]

R18 进一步证明：

1. 在这一 sector 中，所有 defining entries \(a_{ik}\) 都是 simplicial \(0\)-cochains；
2. 所有 matching curvatures 都是 \(1\)-cochains；
3. 因而 defining、top filling 与非平凡性完全由诱导图
   \[
   G=K^{(1)}
   \]
   上的 incidence、cycle space 与 edgewise Baskakov product 决定；
4. proper filler 存在，当且仅当相应 curvature 在每条 graph cycle 上的 holonomy 为零；
5. \(0\) 属于最终 Massey product，当且仅当 punctured graph Maurer--Cartan system 可以补上 maximal vertex-potential；
6. 该判据可编码为 \(O(n^3)\) 个变量、\(O(n^4)\) 个二次方程；
7. \(n=4\) 是第一个真正非线性的阈值：top obstruction 首次出现两个独立低阶 fillers 的乘积
   \[
   a_{12}a_{34}.
   \]

这给出了 extremal sector 的完整图代数充要判据。仍未解决的是把该判据进一步压缩成有限 forbidden-subgraph list。

为避免无关符号，正文先在 \(\mathbb F_2\) 上陈述；对一般域只需加入标准 Koszul 与 oriented-incidence signs。

---

## 1. 极值 sector 中的次数塌缩

令

\[
J_i=\{x_i,y_i\},\qquad
\alpha_i\leftrightarrow
\bar\alpha_i\in\widetilde H^0(K_{J_i};\mathbb F_2),
\]

其中 \(K_{J_i}=S^0\)。取代表

\[
a_i=\chi_{x_i}\in\widetilde C^0(K_{J_i};\mathbb F_2).
\]

对 interval \(I=[i,k]\)，记

\[
J_I=J_i\sqcup\cdots\sqcup J_k.
\]

由 Hochster grading，任意标准 multihomogeneous defining entry 满足

\[
a_{ik}\in C^0(K_{J_I};\mathbb F_2)
\tag{1.1}
\]

而不是随 interval 长度增长到更高 simplicial degree。其 curvature 为

\[
\Omega_{ik}
=
\sum_{i\le r<k}a_{ir}\star a_{r+1,k}
\in C^1(K_{J_I};\mathbb F_2),
\tag{1.2}
\]

其中 \(\star\) 是 Hochster--Baskakov cochain product。

因此所有 proper equations 都是

\[
\delta a_{ik}=\Omega_{ik}
\tag{1.3}
\]

形式的“vertex potential 的 gradient 等于 edge curvature”。

---

## 2. 1-Skeleton Determinacy

### 定理 2.1

固定有序 missing-edge pairs \(J_1,\ldots,J_n\)。在 support-minimal、multihomogeneous sector 中：

1. defining-system space；
2. 完整 top-filler space；
3. Massey product 是否 defined；
4. \(0\) 是否属于该 Massey product；
5. 每个 top curvature 是否 exact；

都只依赖于诱导图

\[
G=K_J^{(1)}
\]

及其顶点的 block ordering，不依赖于 \(K_J\) 的二维或更高 simplices。

### 证明

每个 \(a_{ik}\) 是 \(0\)-cochain，所以：

- \(\delta a_{ik}\) 只使用 graph incidence \(C^0(G_I)\to C^1(G_I)\)；
- 两个 \(0\)-cochains 的 Baskakov product 是 \(1\)-cochain，其在一条 edge 上的值只由两个端点值、支撑 blocks 与顶点顺序决定；
- 因而 (1.2)--(1.3) 的全部方程只使用 \(G_I\)。

若 proper equations 成立，formal Maurer--Cartan/Bianchi cancellation 保证 top curvature 在 \(K_J\) 中为 cocycle。它是否 exact 只问是否属于

\[
\operatorname{im}\bigl(\delta:C^0(G)\to C^1(G)\bigr),
\]

同样只依赖 \(G\)。证毕。

### 推论 2.2（Flagification Invariance）

令

\[
\operatorname{Flag}(G)
\]

为图 \(G\) 的 clique complex。把 \(K_J\) 替换为 \(\operatorname{Flag}(K_J^{(1)})\)，不改变上述 extremal Massey matching problem 的 defined/trivial/nontrivial 状态。

因此极值分类可以严格限制在 flag complexes，亦即有限图。

### 边界说明

该结论针对 R17 的最低支撑、multihomogeneous sector。对高 simplicial-degree 输入，\(a_{ik}\) 不再全部位于 degree \(0\)，高维 faces 会重新进入 obstruction equations，不能使用本定理。

---

## 3. Graph Maurer--Cartan Criterion

令

\[
G_I:=G[J_I]
\]

为 interval \(I=[i,k]\) 上的诱导子图。记

\[
B_I:C^0(G_I;\mathbb F_2)\longrightarrow C^1(G_I;\mathbb F_2)
\]

为 incidence/coboundary map。

### 定义 3.1

一个 punctured graph MC system 是一族 vertex functions

\[
\phi_{ik}\in C^0(G_{[i,k]};\mathbb F_2),
\qquad
(i,k)\ne(1,n),
\]

满足

\[
\phi_{ii}=a_i
\]

和

\[
B_{[i,k]}\phi_{ik}
=
\sum_{i\le r<k}
\phi_{ir}\star\phi_{r+1,k}
\tag{3.1}
\]

对所有 proper intervals 成立。

若再存在 \(\phi_{1n}\) 使 (3.1) 对 maximal interval 成立，则称其为 full graph MC system。

### 定理 3.2（完整充要判据）

在 support-minimal sector：

\[
\boxed{
\langle\alpha_1,\ldots,\alpha_n\rangle
\text{ defined}
\Longleftrightarrow
\text{punctured graph MC system 存在}.}
\tag{3.2}
\]

\[
\boxed{
0\in\langle\alpha_1,\ldots,\alpha_n\rangle
\Longleftrightarrow
\text{full graph MC system 存在}.}
\tag{3.3}
\]

所以

\[
\boxed{
\text{Massey product 非平凡}
\Longleftrightarrow
\mathfrak D^\circ(G)\ne\varnothing
\ \text{且}\
\mathfrak D(G)=\varnothing,}
\tag{3.4}
\]

其中 \(\mathfrak D^\circ(G)\) 与 \(\mathfrak D(G)\) 分别是 punctured 与 full solution sets。

### 证明

由 (1.1)，标准 defining entries 与 graph vertex functions 相同；由 (1.2)，所有 defining equations 与 (3.1) 相同。缺失 maximal entry 正是 Massey defining system，加入它正是要求 top curvature 为 coboundary。因此三式均成立。证毕。

这不是仅有充分性的构造法，而是一个精确的有限图充要判据。

---

## 4. Cycle-Holonomy Criterion

给定 oriented graph \(H\) 与 \(c\in C^1(H;\Bbbk)\)，对 graph cycle \(z\in Z_1(H;\Bbbk)\) 定义

\[
\operatorname{Hol}_z(c):=\langle c,z\rangle.
\tag{4.1}
\]

在 \(\mathbb F_2\) 上就是沿 cycle 对 edge coefficients 求和。

### 引理 4.1

\[
c\in\operatorname{im}
\bigl(\delta:C^0(H;\Bbbk)\to C^1(H;\Bbbk)\bigr)
\]

当且仅当

\[
\operatorname{Hol}_z(c)=0
\qquad
\text{对所有 }z\in Z_1(H;\Bbbk).
\tag{4.2}
\]

### 证明

gradient 沿 closed cycle 的 telescoping sum 为零，所以必要性成立。反之，在每个连通分支选基点，沿路径积分定义 vertex potential；所有 cycle holonomies 为零保证该定义与路径选择无关，于是 \(c\) 是该 potential 的 gradient。证毕。

### 定理 4.2（R3 Graph-Holonomy）

给定所有更短 intervals 的 fillers，节点 \([i,k]\) 可填，当且仅当

\[
\operatorname{Hol}_z(\Omega_{ik})=0
\quad
\text{对每个 }z\in Z_1(G_{[i,k]};\Bbbk).
\tag{4.3}
\]

一个 punctured system 的 top value 非零，当且仅当存在

\[
z\in Z_1(G;\Bbbk)
\]

使

\[
\operatorname{Hol}_z(\Omega_{1n})\ne0.
\tag{4.4}
\]

整个 Massey product不包含 \(0\)，当且仅当对每个 punctured graph MC system，至少存在一条 cycle 满足 (4.4)。

### 意义

Grbić--Linton 用显式 cycle 检测所有 defining systems 的非零 top value；在 R18 中，这被识别为一般的 graph-holonomy certificate，而非个别例子的技巧。

---

## 5. 有限二次方程编码

对每个 proper interval \([i,k]\) 和每个 \(v\in J_{ik}\)，引入变量

\[
X_{ik,v}:=\phi_{ik}(v).
\]

对 \(G_{ik}\) 的每条 oriented edge \(e=(u,v)\)，方程 (3.1) 给出

\[
X_{ik,v}-X_{ik,u}
=
\sum_{i\le r<k}
\bigl(\phi_{ir}\star\phi_{r+1,k}\bigr)(e).
\tag{5.1}
\]

右端对变量至多二次。

### 定理 5.1（Polynomial-Size Quadratic Encoding）

punctured defining problem可编码为一个二次方程系统，其中：

- vertex-potential variables 数为
  \[
  2\sum_{\ell=2}^{n-1}(n-\ell+1)\ell
  =
  \frac{n(n+5)(n-2)}{3}
  =
  O(n^3);
  \tag{5.2}
  \]
- edge equations 数最多为
  \[
  \sum_{\ell=2}^{n-1}
  (n-\ell+1)\,2\ell(\ell-1)
  =
  O(n^4).
  \tag{5.3}
  \]

测试 \(0\) 是否属于 Massey product，只需再加入 maximal potential 的 \(2n\) 个变量和 \(O(n^2)\) 个 edge equations。

### 推论 5.2

对固定有限域 \(\mathbb F_q\)，definedness 与 \(0\)-membership 都具有 polynomial-size certificates，可在给定 certificate 后以多项式时间验证。

这不意味着问题已有多项式时间算法：寻找二次系统的解仍可能困难。R18 给出的是真正良定义的有限计算模型，避免了 R16 中 presentation-independent complexity 命题不良定义的问题。

---

## 6. \(n=4\) 是首个非线性阈值

### \(n=3\)

proper equations 为

\[
\delta a_{12}=a_1a_2,\qquad
\delta a_{23}=a_2a_3.
\]

top curvature 是

\[
\Omega_{13}=a_1a_{23}+a_{12}a_3.
\tag{6.1}
\]

它对 variable fillers \(a_{12},a_{23}\) 是 affine-linear 的。这与最低次数 triple products 可以由有限 obstruction graphs 分类相协调。

### \(n=4\)

proper equations 是

\[
\begin{aligned}
\delta a_{12}&=a_1a_2,\\
\delta a_{23}&=a_2a_3,\\
\delta a_{34}&=a_3a_4,\\
\delta a_{13}&=a_1a_{23}+a_{12}a_3,\\
\delta a_{24}&=a_2a_{34}+a_{23}a_4.
\end{aligned}
\tag{6.2}
\]

top curvature 为

\[
\boxed{
\Omega_{14}
=
a_1a_{24}
+a_{12}a_{34}
+a_{13}a_4.}
\tag{6.3}
\]

中间项

\[
a_{12}a_{34}
\tag{6.4}
\]

耦合两个彼此独立的低阶 filler choices。

### 定理 6.1（First Nonlinear Threshold）

在最低支撑 sector：

1. triple top-obstruction map 对 proper filler variables 是 affine-linear；
2. fourfold top-obstruction map 含有普适 bilinear cross-term \(a_{12}a_{34}\)；
3. 除非该 Baskakov pairing 因图结构退化为零，fourfold obstruction map 不是 affine；
4. 因而 \(n=4\) 是 resolved defining-system choices 首次发生不可忽略的非线性耦合的 arity。

### 证明

式 (6.1) 每项只有一个 variable filler 与一个固定 input。式 (6.3) 的中间项同时含两个 variable fillers，二阶交叉差分等于相应 Baskakov pairing，通常非零。证毕。

### 解释

这给出了 triple obstruction-graph classification 难以直接推广到 \(n\ge4\) 的结构原因：

> 难点不是图的数量突然增多，而是 maximal obstruction 从 affine matching 变成了 genuinely coupled matching。

这正是 Frozen v1.0 中 Coupl 所要检测的现象。

---

## 7. 对 truncated-cube family 的重新解释

Limonchenko pattern 删除

\[
\{x_i,y_k\},
\qquad
i<k,\quad(i,k)\ne(1,n).
\]

在 graph-holonomy 语言中：

1. adjacent deletions 先使 pair curvatures 的 cycle holonomies 消失；
2. non-adjacent proper deletions继续消去 longer-interval holonomies；
3. maximal pair \((1,n)\) 被保留，使 top graph curvature具有不可消去的 cycle holonomy；
4. Grbić--Linton 的 detecting cycle 正是一个 top-holonomy witness。

所以该 family 是一个显式的“逐层消 holonomy、最终保留 maximal holonomy”的生成算法。

---

## 8. 严格评估

### 已推进

1. R17 的 extremal classification problem 已从 simplicial-complex 问题严格降为 graph problem。
2. 得到了 definedness、triviality 与 nontriviality 的完整 graph-MC 充要判据。
3. 得到了 cycle-holonomy 版本，提供可验证 certificate。
4. 得到了一个标准有限计算模型：\(O(n^3)\) variables、\(O(n^4)\) quadratic equations。
5. 找到了 \(n=4\) 分类困难的第一结构性来源：\(a_{12}a_{34}\) choice-coupling。

### 文献新颖性限制

1. Hochster cochain degrees与 defining-system equations来自标准模型；
2. 最低次数 triple products 的 graph classification 已知；
3. Grbić--Linton 已经使用 cycles 检测其构造的非平凡性；
4. R18 的贡献是把这些事实提升为任意 \(n\) 的 exact graph-MC/holonomy theorem，并给出统一二次编码与 nonlinear-threshold 解释；
5. 尚未完成足以断言“此前无人陈述”的全面查重。

---

## 9. 当前不能闭合的问题

R18 后剩下三个精确问题。

### A. Fourfold forbidden-pattern classification

把 (6.2)--(6.3) 消元，给出有限或结构化的 graph pattern 列表，精确刻画

\[
\mathfrak D^\circ(G)\ne\varnothing,
\qquad
\mathfrak D(G)=\varnothing.
\]

当前 bilinear term \(a_{12}a_{34}\) 阻止把 triple obstruction-graph 论证直接线性推广。

### B. Complexity

对固定有限域，判定 full graph MC system 是否存在的复杂度是 P、NP-complete，还是属于更特殊的 graph-quadratic class，目前没有证明。

### C. Universality of the Limonchenko pattern

未知每个 support-minimal nontrivial \(n\)-Massey graph 是否都包含、收缩到或可由某种局部变换化为 Limonchenko 的 directed-deletion pattern。R18 只证明该 pattern 是尖锐且充分的，不证明其分类普适性。

这些问题均已良定义，但不能仅由 Frozen v1.0 或现有形式恒等式自动解决。

---

## 10. 文献依据

1. J. Grbić and A. Linton, *Non-trivial higher Massey products in moment-angle complexes*, Adv. Math. 387 (2021), 107837.  
   https://arxiv.org/abs/1911.07083
2. J. Grbić and A. Linton, *Lowest-degree triple Massey products in moment-angle complexes*.  
   https://arxiv.org/abs/1908.02222
3. G. Denham and A. I. Suciu, *Moment-angle complexes, monomial ideals, and Massey products*.  
   https://arxiv.org/abs/math/0512497
4. V. Buchstaber and I. Limonchenko, *Massey products, toric topology and combinatorics of polytopes*.  
   https://arxiv.org/abs/1811.02221

## 最终结论

\[
\boxed{
\begin{array}{c}
\text{support-minimal moment-angle Massey}
\\
\Downarrow
\\
\text{vertex potentials on }K^{(1)}
\\
\Downarrow
\\
\text{proper cycle holonomies vanish}
\\
\Downarrow
\\
\text{maximal holonomy survives}
\end{array}}
\]

R17 证明 cube geometry 被支撑极值强迫；R18 证明在该 geometry 内，R3 matching tower 就是一个有限图上的 nonlinear holonomy problem。
