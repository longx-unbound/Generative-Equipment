# 生成装备研究 R17：Moment-Angle 支撑局部化、立方体普适性与最优支撑 Arity

日期：2026-09-29  
逻辑地位：Frozen v1.0 的派生 sector theorem；不修改冻结核心

## 0. 结论概览

设 \(K\) 是 \(m\) 个顶点上的有限 simplicial complex，\(\mathcal Z_K=(D^2,S^1)^K\)。对两两不交的顶点集 \(J_1,\ldots,J_n\)，取非零 Hochster classes

\[
\alpha_i\longleftrightarrow
\bar\alpha_i\in\widetilde H^{p_i}(K_{J_i};\Bbbk).
\]

本轮得到：

1. **Resolved Support-Excision**：这些输入的 Massey defining、top filler 与“\(0\) 是否属于 Massey product”完全收缩到 \(K_J\)，其中 \(J=\bigsqcup_iJ_i\)。改变 \(J\) 外的 simplices 不改变可解性。
2. **Interval Matching Localization**：规范 multihomogeneous defining system 的 \(a_{ik}\) 只生活在 \(K_{J_i\cup\cdots\cup J_k}\)；这正是 proper intervals 上的 punctured matching tower。
3. **最优支撑界**：若 \(P=\sum_i p_i\)，则
   \[
   \boxed{|J|\ge P+2n},\qquad
   \boxed{n\le\left\lfloor\frac{|J|}{2}\right\rfloor\le\left\lfloor\frac m2\right\rfloor}.
   \]
4. **等号刚性**：若 \(|J|=2n\)，则所有 \(p_i=0\)、\(|J_i|=2\)，输入全是 degree \(3\) classes，且每个 \(J_i\) 是 missing edge。
5. **立方体普适性**：等号情形强迫
   \[
   K_J\subseteq(S^0)^{*n}=\partial C_n^\diamond,
   \]
   即 \(n\)-维交叉多面体边界，也就是 \(n\)-cube 的对偶边界。
6. **Exact R3 Realization**：Limonchenko/Grbić--Linton 的 truncated-cube construction 对每个 proper interval \([i,k]\subsetneq[1,n]\) 做一次 truncation，唯独保留 maximal interval。它是 R3 punctured matching tower 的逐节点几何实现。

第 1、2 点建立于标准 Hochster--Baskakov 模型与 full-subcomplex retract；高阶 Massey 构造本身来自已有文献。第 3--5 点是由该模型推出的尖锐结构结论。在完成全面文献查重前，不宣称文献意义上的首创。

---

## 1. Hochster--Baskakov 模型

Hochster 分解为

\[
H^q(\mathcal Z_K;\Bbbk)
\cong
\bigoplus_{I\subseteq[m]}
\widetilde H^{q-|I|-1}(K_I;\Bbbk).
\tag{1.1}
\]

若 \(\bar\alpha_i\in\widetilde H^{p_i}(K_{J_i})\)，相应 moment-angle class 次数为

\[
q_i=p_i+|J_i|+1.
\tag{1.2}
\]

定义

\[
J_{ik}:=\bigsqcup_{r=i}^kJ_r,\qquad
P_{ik}:=\sum_{r=i}^kp_r.
\tag{1.3}
\]

一个 interval-homogeneous defining system 由

\[
a_{ik}\in\widetilde C^{P_{ik}}(K_{J_{ik}};\Bbbk),
\qquad(i,k)\ne(1,n),
\tag{1.4}
\]

组成，并满足

\[
d a_{ik}
=
\sum_{i\le r<k}\overline a_{ir}a_{r+1,k}.
\tag{1.5}
\]

顶端曲率为

\[
\Omega(A)
=
\sum_{1\le r<n}\overline a_{1r}a_{r+1,n}
\in\widetilde Z^{P_{1n}+1}(K_J;\Bbbk).
\tag{1.6}
\]

它对应的 moment-angle cohomology 次数为

\[
\sum_iq_i-(n-2)=P_{1n}+|J|+2.
\tag{1.7}
\]

---

## 2. Resolved Support-Excision Theorem

### 定理 2.1

令 \(J\subseteq[m]\)。把 \(J\) 外的坐标固定在 \(S^1\) 的基点，得到

\[
i_J:\mathcal Z_{K_J}\longrightarrow\mathcal Z_K.
\]

坐标投影给出

\[
r_J:\mathcal Z_K\longrightarrow\mathcal Z_{K_J},
\qquad r_Ji_J=\operatorname{id}.
\tag{2.1}
\]

对来自 \(H^*(\mathcal Z_{K_J})\) 的输入：

\[
\langle\alpha_1,\ldots,\alpha_n\rangle
\text{ 在 }\mathcal Z_{K_J}\text{ 中 defined}
\Longleftrightarrow
\langle r_J^*\alpha_1,\ldots,r_J^*\alpha_n\rangle
\text{ 在 }\mathcal Z_K\text{ 中 defined},
\tag{2.2}
\]

并且

\[
0\in\langle\alpha_1,\ldots,\alpha_n\rangle
\Longleftrightarrow
0\in\langle r_J^*\alpha_1,\ldots,r_J^*\alpha_n\rangle.
\tag{2.3}
\]

更强地，局部与全局的 resolved defining/filler spaces 之间有往返映射，局部到全局再返回局部为恒等。

### 证明

若 \(x\in\mathcal Z_K\) 位于由 \(\sigma\in K\) 给出的 cell，则其 \(J\)-坐标投影位于由 \(\sigma\cap J\in K_J\) 给出的 cell，故 \(r_J\) 良定义。在 cellular cochain DGA 上得到分裂

\[
C^*(\mathcal Z_{K_J})
\xrightarrow{r_J^*}
C^*(\mathcal Z_K)
\xrightarrow{i_J^*}
C^*(\mathcal Z_{K_J}),
\qquad i_J^*r_J^*=\operatorname{id}.
\tag{2.4}
\]

DGA maps 保持 defining equations、top curvature 与 fillers。局部解可推到全局，全局解可拉回局部，因此 partial systems 与 complete systems 的非空性分别等价。证毕。

### 推论 2.2（环境不变性）

若 \(K_J=L_J\)，则由 \(J\) 支撑的给定输入之定义性与平凡性，在 \(\mathcal Z_K\) 和 \(\mathcal Z_L\) 中相同。环境可能增加其他 Massey values，但不能把局部非平凡 product 变成包含 \(0\) 的 product。

---

## 3. Interval Matching Localization

### 定理 3.1

proper interval \([i,k]\subsetneq[1,n]\) 的 matching obstruction 是

\[
\Omega_{ik}
:=
\sum_{i\le r<k}\overline a_{ir}a_{r+1,k}
\in\widetilde Z^{P_{ik}+1}(K_{J_{ik}};\Bbbk).
\tag{3.1}
\]

该节点可填当且仅当

\[
[\Omega_{ik}]=0
\in\widetilde H^{P_{ik}+1}(K_{J_{ik}};\Bbbk).
\tag{3.2}
\]

全部 proper intervals 填入后，唯一遗漏的 maximal interval \([1,n]\) 的 defect 为 (1.6)。

### 证明

节点 \([i,k]\) 的方程就是 \(d a_{ik}=\Omega_{ik}\)。较短 intervals 的 Maurer--Cartan 方程与 Leibniz rule 给出 \(d\Omega_{ik}=0\)，故 filler 存在当且仅当其上同调类消失。递归完成所有 proper intervals 后只剩 maximal interval。证毕。

### 推论 3.2（cohomological corridor）

若对所有长度至少为 \(2\) 的 proper intervals 有

\[
\widetilde H^{P_{ik}+1}(K_{J_{ik}};\Bbbk)=0,
\tag{3.3}
\]

则可以按 interval 长度归纳构造 defining system。若进一步

\[
\widetilde H^{P_{1n}+1}(K_J;\Bbbk)=0,
\tag{3.4}
\]

则该 Massey product 包含 \(0\)。这是充分条件，不压缩 indeterminacy。

---

## 4. 最优顶点支撑界

### 引理 4.1

若有限 simplicial complex \(L\) 有 \(s\) 个顶点且

\[
\widetilde H^p(L;\Bbbk)\ne0,\qquad p\ge0,
\]

则 \(s\ge p+2\)。

### 证明

若 \(s\le p\)，则 \(\dim L<p\)。若 \(s=p+1\)，要有 \(p\)-cochains 必须包含全部顶点张成的 \(p\)-simplex；simplicial 闭包迫使 \(L\) 是完整 simplex，约化上同调仍为零。证毕。

### 定理 4.2（Sharp Vertex-Support Bound）

令 \(P=\sum_i p_i\) 与 \(s=|\bigsqcup_iJ_i|\)。则

\[
\boxed{s\ge P+2n}
\tag{4.1}
\]

以及

\[
\boxed{
n\le
\left\lfloor\frac{s-P}{2}\right\rfloor
\le
\left\lfloor\frac{s}{2}\right\rfloor
\le
\left\lfloor\frac m2\right\rfloor.}
\tag{4.2}
\]

### 证明

由引理，\(|J_i|\ge p_i+2\)。支撑不交，所以

\[
s=\sum_i|J_i|
\ge\sum_i(p_i+2)
=P+2n.
\]

证毕。

这是严格的组合资源界：高维输入每增加一个 simplicial degree，至少消耗一个额外支撑顶点。

---

## 5. 等号刚性与立方体普适性

### 定理 5.1（Support-Rigidity）

若达到绝对最小支撑

\[
s=2n,
\tag{5.1}
\]

则：

1. \(p_i=0\)；
2. \(|J_i|=2\)；
3. \(K_{J_i}=S^0\)，即 \(J_i=\{x_i,y_i\}\) 是 missing edge；
4. 每个输入在 \(\mathcal Z_K\) 中次数为 \(3\)；
5. 
   \[
   \boxed{
   K_J\subseteq
   S^0_1*\cdots*S^0_n
   =\partial C_n^\diamond.}
   \tag{5.2}
   \]

### 证明

\(2n=s\ge P+2n\) 强迫 \(P=0\)，故所有 \(p_i=0\)。每个 \(|J_i|\ge2\)，总和又为 \(2n\)，故全部等于 \(2\)。两顶点复形具有非零 \(\widetilde H^0\) 当且仅当两点不相连。

若某个 \(\sigma\in K_J\) 同时含 \(x_i,y_i\)，则 \(\{x_i,y_i\}\) 是 face，与 missing-edge 条件矛盾。因此每个 simplex 从每一对至多选择一个顶点；这正是 join \(S^0_1*\cdots*S^0_n\) 的 face 条件。证毕。

因为 \((S^0)^{*n}\) 是交叉多面体边界，其对偶为 \(n\)-cube，所以：

> 任意顶点支撑最优的 \(n\)-重 moment-angle Massey phenomenon，都被迫发生在立方体对偶边界的某个子复形中。

这说明 truncated cube 不是偶然选中的成功例子，而是最低支撑 sector 的普适 ambient geometry。

---

## 6. 相邻方形判据

### 定理 6.1

在 support-minimal sector 中，\(K_{J_i\cup J_{i+1}}\) 是四边形

\[
S^0_i*S^0_{i+1}=K_{2,2}
\]

的子复形。两个 degree \(3\) 输入的 cup product 非零，当且仅当四条 cross edges 全部存在。因此相邻 pair obstruction 可填的充要条件是至少缺一条 cross edge。

### 证明

两条 pair-internal edges 已经缺失，所以诱导子复形是 \(K_{2,2}\) 的子图。若四条 cross edges 全在，它是 \(S^1\)，Baskakov product

\[
\widetilde H^0(S^0_i)\otimes\widetilde H^0(S^0_{i+1})
\longrightarrow
\widetilde H^1(S^0_i*S^0_{i+1})
\]

给出生成元。若缺至少一边，子图是 forest，\(\widetilde H^1=0\)，故 product 为零。证毕。

所以任何 defined support-minimal \(n\)-Massey product 都要求每个相邻 pair 之间至少缺一条 cross edge。

---

## 7. Truncated Cube 的逐节点 R3 实现

proper intervals 集合

\[
\mathcal I_n^\circ
=
\{[i,k]\mid1\le i<k\le n,\ (i,k)\ne(1,n)\}
\]

有

\[
|\mathcal I_n^\circ|=\binom n2-1
\tag{7.1}
\]

个节点。

Limonchenko 的 family 从 \(n\)-cube 出发，对每个

\[
1\le i<k\le n,\qquad(i,k)\ne(1,n)
\]

截断 \(F_i\cap F'_k\)。在对偶 simplicial complex 上对应 edge \(\{x_i,y_k\}\) 的 stellar subdivision；限制到原来的 \(2n\) 个顶点，就是该 edge 的 star deletion。文献的 cochain construction 说明该 deletion 允许定义

\[
a_{ik},\qquad
d a_{ik}
=
\sum_{i\le r<k}\overline a_{ir}a_{r+1,k}.
\tag{7.2}
\]

| R3/Massey 数据 | truncated-cube 几何 |
|---|---|
| proper interval \([i,k]\) | face \(F_i\cap F'_k\) |
| filler \(a_{ik}\) | truncation / 对偶 edge deletion |
| 全部 proper intervals | \(\binom n2-1\) 个 truncations |
| maximal interval \([1,n]\) | 故意不截断的 pair |
| top curvature \(\Omega\) | 剩余全局 Massey obstruction |

### 定理 7.1（Exact Geometric Realization）

Limonchenko 的最低次数 \(n\)-Massey construction 是 interval-poset R3 punctured matching tower 的逐节点几何 realization：所有 proper nodes 由 truncations 产生 fillers，而 maximal node 无 filler；Grbić--Linton 的非平凡性定理说明 top defect 对所有 defining-system choices 都不为零。

### 证明

truncations 与 \(\mathcal I_n^\circ\) 的指标集合相同。Construction 3.5 的后续说明指出，对 \((i,k)\ne(1,n)\) 的 star deletion 允许 cochain \(a_{ik}\) trivialize lower product \(\langle\alpha_i,\ldots,\alpha_k\rangle\)。Proposition 3.12 构造全部 defining entries，Proposition 3.16 证明任意 defining system 的 top value 非零，Theorem 3.17 合并两者。与定理 3.1 比较即得。证毕。

---

## 8. 自然样本

### 8.1 六顶点 triple product

Grbić--Linton 的公开例子取

\[
J_1=\{1,2\},\quad J_2=\{3,4\},\quad J_3=\{5,6\}
\]

和

\[
\bar\alpha_1=[\chi_1]\in\widetilde H^0(K_{12}),\quad
\bar\alpha_2=[\chi_3]\in\widetilde H^0(K_{34}),\quad
\bar\alpha_3=[\chi_5]\in\widetilde H^0(K_{56}).
\]

这是 \(s=6=2n\) 的最小支撑。两个 proper interval 方程位于 \(K_{1234}\) 与 \(K_{3456}\)。文献参数化全部 pairwise fillers，并得到

\[
[\Omega]=[\chi_{15}+(c_1-c_2)\chi_{35}]\ne0
\]

对所有参数成立。因此 punctured defining space 非空且有 indeterminacy，但 top nullification fiber 恒为空。它是公开的自然 moment-angle example，不是我们设计的自由 DGA。

### 8.2 任意 \(n\) 的 support-optimal family

取 \(n\) 个 \(S^0\)，总支撑顶点数 \(2n\)，再按第 7 节删除 proper-interval edges。已有结果给出非平凡 \(n\)-Massey product，而定理 4.2 表明任何 disjoint-support \(n\)-Massey 输入至少需要 \(2n\) 个支撑顶点。因此该族达到绝对支撑最优：

\[
\boxed{\text{support size}=2n=\text{theoretical minimum}.}
\]

若把 support complex 嵌入 triangulated sphere 或 polytope dual 以得到闭 moment-angle manifold，环境可能增加顶点；最优性指 operation 的必需支撑，不是所有 manifold realizations 的总 facets 数。

---

## 9. 严格现实性审计

### 已确认

1. truncated cube 的每次 truncation 是一个 proper matching node 的几何 filler。
2. 唯独遗漏 \((1,n)\) 是因为它是 maximal interval；若也填掉，top obstruction 将被消去。
3. \(n\)-重 disjoint-support operation 至少消耗 \(P+2n\) 个顶点。
4. 最低支撑自动强迫 cube/crosspolytope ambient geometry。
5. 搜索 support-minimal examples 只需搜索
   \[
   K\subseteq(S^0)^{*n}
   \]
   及一个有序 missing-edge matching，而无需搜索任意 simplicial complex。
6. resolved formulation 正确区分“某个 value 非零”和“所有 defining systems 都无法得到零”。

### 不能夸大

1. Hochster decomposition、Baskakov product、full-subcomplex retract 与 star-deletion constructions 都是已有数学。
2. R3 matching identification 是结构解释，不等同于发现新的 moment-angle family。
3. 支撑界与等号刚性的证明短；价值在于把 cube family 刻画为 support-extremal。
4. 尚未获得 \(n\ge4\) 时全部 support-minimal complexes 的充要组合分类。

---

## 10. 当前精确开放边界

> **Extremal R3 Classification Problem.** 设
> \[
> K\subseteq(S^0)^{*n}
> \]
> 位于 \(2n\) 个顶点上，并以每个 \(S^0_i\) 的生成元给出 \(n\) 个 degree \(3\) classes。给出纯组合充要条件，使相应 \(n\)-Massey product defined 且不包含 \(0\)。

当前可严格得到：

- 每个相邻方形至少缺一条 cross edge；
- 所有 proper interval curvatures 必须依次为 boundaries；
- maximal curvature 必须对全部 defining systems 保持 non-exact；
- Limonchenko 的定向 deletion pattern 是一族充分条件；
- \(n=3\) 最低次数 sector 已有 obstruction-graph 分类；
- 当前资料中没有 \(n\ge4\) 的完整充要分类。

这是一个有限、自然、严格的组合分类问题。R3 已把问题定位到正确对象，但 Frozen v1.0 不能自动给出其分类。

---

## 11. 文献

1. J. Grbić and A. Linton, *Non-trivial higher Massey products in moment-angle complexes*, Adv. Math. 387 (2021), 107837.  
   https://arxiv.org/abs/1911.07083
2. G. Denham and A. I. Suciu, *Moment-angle complexes, monomial ideals, and Massey products*, Pure Appl. Math. Q. 3 (2007), 25--60.  
   https://arxiv.org/abs/math/0512497
3. V. Buchstaber and I. Limonchenko, *Embeddings of moment-angle manifolds and sequences of Massey products*.  
   https://arxiv.org/abs/1808.08851
4. V. Buchstaber and I. Limonchenko, *Massey products, toric topology and combinatorics of polytopes*.  
   https://arxiv.org/abs/1811.02221

## 最终判定

\[
\boxed{
\begin{array}{c}
\text{R16 抽象 Massey matching}
\\
\Downarrow
\\
\text{Hochster interval subcomplexes 上的 punctured matching}
\\
\Downarrow\quad\text{最低支撑}
\\
K_J\subseteq(S^0)^{*n}=\partial C_n^\diamond
\\
\Downarrow
\\
\text{truncated \(n\)-cube 逐节点实现 proper fillers，}
\\
\text{并保留 maximal defect。}
\end{array}}
\]

理论现已准确解释一个实际高阶数学构造为何从立方体开始、为何出现 \(\binom n2-1\) 个指定 truncations，以及为何必须遗漏唯一 maximal pair。
