# 生成装备研究 R11：Nilpotent 系数的中心分层与三滤过障碍塔

## 0. 本轮结论

本报告把“nilpotent fiber”中真正可用于障碍计算的输入精确化为 **relative nilpotence**：实际出现在 section/Postnikov 障碍中的单值群作用必须是幂零的。

在此前提下，每个扭曲系数系统都有一个规范的有限过滤

\[
M=I^0M\supseteq IM\supseteq\cdots\supseteq I^cM=0,
\]

其相邻商上的 monodromy 完全平凡。因此一个扭曲 Postnikov 障碍可以细化成有限个常系数阿贝尔障碍；选择歧义由相邻长正合列控制。\(\pi_1\) 的非阿贝尔部分先由下中心列细化成中心扩张，其障碍落在 \(H^2\)，解集是 \(H^1\)-torsor；若这些中心商仍带外部 monodromy，还要再对它们作增广过滤，才能得到常系数层。

该中心过滤与 R3/Postnikov 双滤过结合后形成三维匹配图。R9 的高维边界在此立即生效：只验证三组两两交换方块不够，必须验证完整的三维 matching map。

本轮状态：

\[
\boxed{\text{PASS + DERIVED STRUCTURE}}
\]

---

## 1. 相对幂零作用

设 \(G\) 为群，\(M\) 为左 \(\mathbb Z[G]\)-模。令

\[
I_G:=\ker(\varepsilon:\mathbb Z[G]\to\mathbb Z)
\]

为增广理想。

### 定义 1.1

若存在 \(c\ge1\) 使

\[
I_G^cM=0,
\]

则称 \(G\) 在 \(M\) 上的作用幂零；最小这样的 \(c\) 称为作用的幂零长度。

对一个基空间 \(B\) 上的局部系统 \(\mathcal M\)，实际作用群是 monodromy 像

\[
G=\operatorname{im}
\bigl(\pi_1(B)\to\operatorname{Aut}(M)\bigr).
\]

“relative nilpotence”指这个实际作用满足 \(I_G^cM=0\)。

### 关键区分

纤维 \(F\) 作为空间是 nilpotent，通常只说明 \(\pi_1(F)\) 幂零且其对 \(\pi_k(F)\) 的内在作用幂零。一个纤维化

\[
F\to E\to B
\]

还可能有来自 \(\pi_1(B)\) 的外部 monodromy。内在 nilpotence 不自动约束这个外部作用。因此下文的结论需要 relative nilpotence，不能只写“纤维 nilpotent”。

---

## 2. 规范增广过滤

定义

\[
F^jM:=I_G^jM,
\qquad 0\le j\le c.
\]

### 定理 2（Canonical Trivial-Quotient Filtration）

若 \(I_G^cM=0\)，则

\[
M=F^0M\supseteq F^1M\supseteq\cdots\supseteq F^cM=0
\]

是一个规范、有限且对 \(G\)-等变映射自然的过滤。其相邻商

\[
A_j:=F^jM/F^{j+1}M
\]

上的 \(G\)-作用平凡。

#### 证明

每个 \(F^jM\) 由群环作用规范定义，故为 \(G\)-子模，并被等变映射保持。对 \(g\in G\)、\(x\in I_G^jM\)，

\[
gx-x=(g-1)x\in I_G^{j+1}M.
\]

所以 \(g\) 在商 \(A_j\) 上恒等。\(\square\)

### 推论 2.1（Local-system Form）

若 \(B\) 连通，且局部系统 \(\mathcal M\) 的 monodromy 作用幂零，则有规范局部子系统过滤

\[
\mathcal M=F^0\mathcal M\supseteq\cdots\supseteq F^c\mathcal M=0,
\]

而

\[
F^j\mathcal M/F^{j+1}\mathcal M
\]

是以 \(A_j\) 为纤维的常局部系统。

### 推论 2.2（Pullback Naturality）

对任意 \(f:B'\to B\)，原增广过滤的拉回仍是一个有限、相邻商常值的过滤。若以拉回后的实际 monodromy 像 \(G'\) 重新构造其规范增广过滤，则

\[
I_{G'}^jM\subseteq I_G^jM
\]

（把 \(G'\) 视为原作用像的子群），故拉回后的幂零长度不增。

一般不能断言 \(I_{G'}^jM=I_G^jM\)：限制 monodromy 可能使规范过滤严格变短。这里的自然性是包含意义下的 lax naturality，而不是无条件相等。

---

## 3. 幂零长度的稳定性估计

### 命题 3.1（Subquotients and Sums）

若 \(I^cM=0\)，则任何 \(G\)-子模与商模的幂零长度都不超过 \(c\)。若 \(M\) 与 \(N\) 的长度分别不超过 \(c,d\)，则

\[
\ell(M\oplus N)\le\max(c,d).
\]

### 命题 3.2（Extensions）

对 \(G\)-模短正合列

\[
0\to M'\to M\to M''\to0,
\]

若 \(I^{c'}M'=0\)、\(I^{c''}M''=0\)，则

\[
I^{c'+c''}M=0.
\]

#### 证明

\(I^{c''}M\) 在 \(M''\) 中像为零，故包含于 \(M'\)；再作用 \(I^{c'}\) 即为零。\(\square\)

### 命题 3.3（Tensor Bound）

给 \(M\otimes N\) 配置对角 \(G\)-作用。若 \(M,N\) 的幂零长度分别不超过 \(c,d\)，则

\[
I^{c+d-1}(M\otimes N)=0.
\]

#### 证明

用总过滤

\[
T^r=\sum_{p+q=r}I^pM\otimes I^qN.
\]

恒等式

\[
(g-1)(m\otimes n)
=(g-1)m\otimes gn+m\otimes(g-1)n
\]

表明 \(I\cdot T^r\subseteq T^{r+1}\)。当 \(r\ge c+d-1\) 时，每项都有 \(p\ge c\) 或 \(q\ge d\)，故 \(T^r=0\)。\(\square\)

这些估计允许从已知层构造出的 cup product、张量型系数或扩张系数获得显式的 nilpotence 上界。

---

## 4. 一个扭曲上同调类的有限中心细化

由第 2 节，对每个 \(j<c\) 有短正合列

\[
0\to F^{j+1}M
\longrightarrow F^jM
\longrightarrow A_j
\to0,
\]

其中 \(A_j\) 的作用平凡。

固定

\[
x_0=x\in H^n(B;M).
\]

### 定理 4（Central Coefficient Obstruction Refinement）

类 \(x\) 为零，当且仅当存在一条有限提升链

\[
x_j\in H^n(B;F^jM),
\qquad 0\le j\le c,
\]

满足：

1. \(x_0=x\)；
2. \(x_{j+1}\) 在 \(H^n(B;F^jM)\) 中的像为 \(x_j\)；
3. 每一步的常系数投影
   \[
   \bar x_j\in H^n(B;A_j)
   \]
   为零；
4. 终点 \(x_c=0\)，因为 \(F^cM=0\)。

#### 证明

长正合列的正合性给出：\(\bar x_j=0\) 当且仅当 \(x_j\) 来自某个 \(x_{j+1}\)。若存在完整链，则 \(x\) 来自 \(H^n(B;F^cM)=0\)，故 \(x=0\)。反之若 \(x=0\)，可取所有 \(x_j=0\)。\(\square\)

### 选择歧义

若 \(x_j\) 可提升，则其上同调类提升的集合是

\[
\ker\bigl(
H^n(B;F^{j+1}M)\to H^n(B;F^jM)
\bigr)
\]

的 torsor，而该核等于连接同态的像

\[
\operatorname{im}
\bigl(
H^{n-1}(B;A_j)\xrightarrow{\delta_j}
H^n(B;F^{j+1}M)
\bigr).
\]

在完整映射空间层面，提升纤维还记录更低次数上同调所给出的路径与高阶自同构。

### 分支警告

\(\bar x_j=0\) 后的提升通常不唯一；某个选择可能在后续失败，而另一个选择成功。因此正确对象仍是 R7 的精确可生存像，而不是“任选一个提升继续”。

---

## 5. 有限系数谱序列

### 定理 5（Nilpotent-Coefficient Spectral Sequence）

增广过滤诱导一个有限谱序列，其 \(E_1\)-层由常系数群

\[
H^*(B;A_j)
\]

组成，并收敛到 \(H^*(B;M)\) 的相应有限过滤的 associated graded。

#### 证明要点

过滤 \(F^\bullet M\) 给局部系数上链复形以有限过滤；相邻商是常系数复形 \(C^*(B;A_j)\)。有限过滤的标准 exact-couple 构造给出谱序列，且有限性保证不存在条件收敛问题。\(\square\)

### 解释

定理 4 是逐类、带选择的 obstruction 版本；定理 5 是同时组织全部类的线性化版本。谱序列微分编码相邻常系数层不能独立拼合的扩张信息。

---

## 6. \(\pi_1\) 的中心扩张细化

设 \(\Gamma\) 是幂零群，其下中心列为

\[
\gamma_1\Gamma=\Gamma,
\qquad
\gamma_{j+1}\Gamma=[\Gamma,\gamma_j\Gamma],
\qquad
\gamma_{c+1}\Gamma=1.
\]

每个

\[
A_j:=\gamma_j\Gamma/\gamma_{j+1}\Gamma
\]

都是阿贝尔群，并且有中心扩张

\[
1\to A_j
\to \Gamma/\gamma_{j+1}\Gamma
\to \Gamma/\gamma_j\Gamma
\to1.
\]

### 定理 6（Central \(\pi_1\)-Lifting Tower）

给定映射

\[
f:B\to B(\Gamma/\gamma_j\Gamma),
\]

把它提升到

\[
B(\Gamma/\gamma_{j+1}\Gamma)
\]

的障碍是拉回中心扩张类

\[
o_j(f)\in H^2(B;A_j).
\]

它消失当且仅当提升存在；若存在，提升的同伦类组成 \(H^1(B;A_j)\)-torsor，自同构由 \(H^0(B;A_j)\) 控制。

#### 证明要点

中心扩张由一个类

\[
e_j\in H^2(B(\Gamma/\gamma_j\Gamma);A_j)
\]

分类。提升存在当且仅当 \(f^*e_j=0\)。零化的选择差由 \(H^1\) 给出，而零化之间的自同构由 \(H^0\) 给出。\(\square\)

因此在固定 \(\Gamma\) 且没有额外外部 twisting 的情形，非阿贝尔
\(\pi_1\) 阶段能在有限步内细化为常系数阿贝尔障碍；其次数是 \(2\)，
而不是高阶 Postnikov 层通常出现的 \(k+1\)。一般局部群系统还需要下面的
外部 monodromy 修正。

### 局部群系统修正

若 \(\Gamma\) 是纤维群，而基空间 monodromy 通过 \(\operatorname{Aut}(\Gamma)\) 作用，则下中心列因其特征性而仍给出局部群系统过滤；但是

\[
A_j=\gamma_j\Gamma/\gamma_{j+1}\Gamma
\]

只在纤维内部是中心的，外部 monodromy 在 \(A_j\) 上未必平凡。此时定理 6 的障碍属于带该外部作用的 twisted \(H^2(B;A_j)\)，解集是 twisted \(H^1(B;A_j)\)-torsor。

只有再假设外部作用在每个 \(A_j\) 上幂零，并对 \(A_j\) 应用第 2 节的增广过滤，才能把这些层进一步细化为常系数障碍。故“\(\Gamma\) 幂零”本身不推出“下中心商是常局部系统”。

---

## 7. 截断相对幂零 Postnikov 塔的高度界

设纤维 \(F\) 为 \(N\)-截断，并假设：

1. \(\pi_1(F)=\Gamma\) 的幂零类不超过 \(s\)；
2. 对每个下中心商
   \[
   A_{1,j}:=\gamma_j\Gamma/\gamma_{j+1}\Gamma,
   \qquad 1\le j\le s,
   \]
   外部 monodromy 的幂零长度不超过 \(a_{1,j}\)；
3. 对每个 \(2\le k\le N\)，实际 monodromy 在 \(\pi_k(F)\) 上的幂零长度不超过 \(c_k\)。

### 定理 7（Finite Central-Abelian Refinement Bound）

经典 Postnikov obstruction tower 可细化为一个有限的中心—阿贝尔塔，其系数商均为常局部系统。所需中心/系数层数至多

\[
C_N:=
\sum_{j=1}^{s}a_{1,j}
+\sum_{k=2}^N c_k.
\]

#### 证明

\(\pi_1\) 阶段先用第 6 节的 \(s\) 个中心商，再把第 \(j\) 个可能扭曲的阿贝尔商用第 2 节细化为至多 \(a_{1,j}\) 个常系数层。每个高阶 \(\pi_k\)-局部系统同样细化为至多 \(c_k\) 层。按 Postnikov 次数依次拼接，得到总层数上界。\(\square\)

若所有 \(\pi_1\) 中心商上的外部 monodromy 已平凡，则 \(a_{1,j}=1\)，此时第一项退化为 \(s\)。

### 注意

该上界计算的是**细化层数**，不是解分支数，也不是算法复杂度。每层 torsor 可能无限，Coupl 也可能非仿射；R10 的不可判定边界仍然存在。

---

## 8. 自然性

### 定理 8（Functorial Central Refinement）

以下构造均为自然的：

1. 增广过滤 \(F^jM=I^jM\) 对等变模映射自然；
2. 下中心列 \(\gamma_j\Gamma\) 对群同态自然；
3. 局部系统过滤对基空间拉回具有第 2.2 节所述的包含型自然性，且拉回后长度不增；
4. 相邻商的上同调障碍与拉回相容；
5. 中心扩张类及其 \(H^2/H^1/H^0\) obstruction–torsor–automorphism 结构与拉回相容。

因此该 refinement 不依赖任选的中心列或模过滤；它给出 R3/Postnikov 比较中可使用的规范第三过滤。

---

## 9. 三滤过匹配定理

把三种有限阶段写成

\[
\mathcal T_{r,k,j},
\]

其中：

- \(r\) 是 cellular/R3 阶段；
- \(k\) 是 Postnikov 阶段；
- \(j\) 是中心或增广过滤阶段。

### 定理 9（Three-Axis Matching Descent）

在任意有限下闭三维区域中，若每个新格点的完整匹配映射

\[
\mathcal T_{r,k,j}
\longrightarrow
M_{r,k,j}\mathcal T
\]

是有效满射，则边界相容数据局部地延拓到整个区域；若所有匹配映射是等价，则全局填充空间可缩。

#### 证明

这是 R9 的 Finite Matching Descent 对三维有限偏序集的直接应用。\(\square\)

### 定理 9.1（Pairwise Beck–Chevalley Is Insufficient）

只验证 \((r,k)\)、\((r,j)\)、\((k,j)\) 三类二维交换方块为有效满射，不足以推出三维 simultaneous effectivity。

#### 证明

R9 的偶校验反例已给出一个集合值三立方体：顶点到三个两两边际的投影均满射，但到完整三重 matching object 的映射不满。因此任何只读取二维面的判据都会漏掉三重相关缺陷。\(\square\)

这给出本轮最重要的结构边界：加入中心 refinement 后，理论不能继续只画两两交换方块；必须显式保留三重 matching defect。

---

## 10. 与 R7–R10 的统一算法骨架

对一个有限截断、相对幂零的 section/lifting 问题，可使用以下严格流程：

1. 以 R7 的精确可生存像保留所有真正有完整未来的分支；
2. 以 R11 的下中心列和增广过滤，把扭曲系数细化为常系数商；对 \(\pi_1\) 的中心商也必须计入外部 monodromy；
3. 对每个局部 Coupl：
   - 仿射时用 R7 的 cofiber residual；
   - 多项式时用 R10 的 cross-effect jet；
4. 对 cellular 与 Postnikov 两方向，用 R8/R9 的比较映射；
5. 加入中心方向后，用完整三维 matching map，而不是只验 pairwise squares；
6. 在每个有限盒子内用 Finite Matching Descent 拼合；
7. 若要通过无限极限 actualize，另行验证收敛、超完备性与派生逆极限条件。

由此得到总的有限结构：

\[
\boxed{
\text{finite Postnikov height}
\times
\text{finite relative-nilpotence length}
\times
\text{finite cellular region}
}
\]

在每个有限盒子里，存在性与相干性都有精确 matching 判据。

---

## 11. 失效模式与 no-go

### 11.1 只有 intrinsic nilpotence

若只知道纤维本身 nilpotent，却不知道基空间 monodromy 的作用幂零，则 \(I^cM\) 可能永不为零，常系数商塔不存在。

### 11.2 无限幂零长度

若没有统一有限 \(c\)，则中心细化成为无限塔；有限阶段消失不自动 actualize。

### 11.3 常系数层不等于独立层

即使每个 \(A_j\) 常值，相邻层仍由连接同态与谱序列微分耦合。不能把总障碍简单写成 \(\prod_jH^*(B;A_j)\)。

### 11.4 Pairwise coherence 不等于 triple coherence

三滤过中，所有二维比较良好仍可能有纯三重缺陷；完整 matching object 不可省略。

### 11.5 有限高度不等于可判定

R10 表明某层 Coupl 即使次数有限，也可能包含不可判定的整数求零问题。有限 obstruction height 只保证结构终止，不保证存在统一算法。

---

## 12. 已知性与新颖性边界

以下输入是标准的：

- 群环增广理想与幂零模；
- nilpotent group 的下中心列；
- 中心扩张的 \(H^2\) 分类及 \(H^1\)-torsor；
- 过滤复形的谱序列；
- nilpotent spaces 与 Postnikov towers。

本项目中的派生结构是：

1. 把 relative nilpotence 明确为冻结装备可实际使用的假设；
2. 给出扭曲 Postnikov 障碍的规范常系数细化及包含 \(\pi_1\) 外部作用的总高度界；
3. 用 R7 的 viability 处理细化中的分支依赖；
4. 把中心过滤识别为 R3/Postnikov 双塔之外的第三轴；
5. 由 R9 严格推出 pairwise interchange 不足、完整三维 matching 必需。

这些结论是标准群论、局部系数障碍论和 matching descent 的组合派生，不主张未经全面文献核查的原创优先权。

参考背景：

- A. K. Bousfield and D. M. Kan, *Homotopy Limits, Completions and Localizations*, Lecture Notes in Mathematics 304, Springer, 1972.
- Wojciech Chachólski, Emmanuel Dror Farjoun, Ramón Flores, and Jérôme Scherer, *Homotopy Colimits of Nilpotent Spaces*, [arXiv:1401.3975](https://arxiv.org/abs/1401.3975).
- Samuel Eilenberg, the standard equivariant-chain description of (co)homology with local coefficients; a modern account is given in James F. Davis and Paul Kirk, *Lecture Notes in Algebraic Topology*.

---

## 13. 最终结论

对有限截断并满足 relative nilpotence 的纤维问题，扭曲 Postnikov obstruction tower 有一个规范有限中心细化：

\[
\boxed{
\text{twisted coefficients}
\rightsquigarrow
\text{finite augmentation filtration}
\rightsquigarrow
\text{constant abelian quotients}.
}
\]

连同 \(\pi_1\) 的下中心列，细化高度满足

\[
\boxed{
C_N\le
\sum_{j=1}^{s}a_{1,j}
+\sum_{k=2}^Nc_k.
}
\]

但中心过滤加入后形成真正的三滤过问题：

\[
\boxed{
\text{pairwise squares 不足；完整 3D matching map 才是正确局部判据。}
}
\]

这条路线已经闭合到有限层面；任何进一步的全局结论都必须明确添加无限收敛或特定 Coupl 可解性的额外输入。
