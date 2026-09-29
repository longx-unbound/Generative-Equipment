# 生成装备研究 R12：有限相对幂零主定理与最大有效边界

## 0. 总结

R5–R11 现在可以压缩为一个完整的有限主定理：

> 对有限维底空间上的 connected truncated fiber，R3 matching obstruction theory 与 fiberwise Moore–Postnikov obstruction theory 自然等价；若实际 monodromy 满足统一的 relative nilpotence，则该共同障碍塔有一个规范的有限常系数中心细化。有限二维交换由小方格匹配映射完全控制；加入中心过滤后的三维问题则必须使用完整的高阶 matching map。局部 Coupl 在仿射、二次、有理多项式及一般整数多项式层分别具有不同且严格的可压缩程度。

这个定理是结构有限性定理，不是无条件的统一算法定理，也不是无限塔 actualization 定理。

本轮状态：

\[
\boxed{\text{PASS + DERIVED STRUCTURE}}
\]

Frozen Generative Equipment v1.0 保持不变；本报告只整理并加强其 derived layer。

---

## 1. 工作假设

设

\[
p:E\to B=|K|
\]

为有限 simplicial complex \(K\) 上的 fibration，且

\[
\dim B=d.
\]

假设每个 fiber 连通且为 \(N\)-type。令

\[
E_k=P_k^BE=\tau_{\le k}^BE
\]

为 fiberwise Postnikov stage，并定义共同双滤过

\[
\mathcal S_{r,k}
:=
\Gamma(B^{(r)},E_k|_{B^{(r)}}).
\]

令

\[
m:=\min\{N,d-1\}.
\]

只有 \(1\le k\le m\) 的 Postnikov obstruction 可能非平凡。

### 相对幂零附加假设

自然比较本身不需要下面的附加假设。只有当我们要求把 twisted coefficients 进一步细化成常系数层时，才假设：

1. fiber \(\pi_1=\Gamma\) 的 nilpotency class 至多为 \(s\)；
2. 对每个下中心商
   \[
   A_{1,j}=\gamma_j\Gamma/\gamma_{j+1}\Gamma,
   \qquad 1\le j\le s,
   \]
   基空间外部 monodromy 的幂零长度在所有 viable branches 上统一不超过 \(a_{1,j}\)；
3. 对 \(2\le k\le m\)，实际 local system
   \[
   \Pi_k(s_{k-1})=s_{k-1}^*\pi_k(E/B)
   \]
   的 monodromy 幂零长度在所有 viable branches 上统一不超过 \(c_k\)。

若某层 homotopy group 为零，相应长度记为零。

---

## 2. 有限相对幂零主定理

### 定理 2（Finite Relative-Nilpotent Master Theorem）

在第 1 节假设下，成立：

#### A. 自然比较

R3 matching obstruction tower 与 fiberwise Moore–Postnikov obstruction tower 在以下意义下自然等价：

1. complete branch \(\infty\)-groupoids 均自然等价于
   \[
   \Gamma(B,E);
   \]
2. 第一非阿贝尔 matching class 等于 banded Postnikov \(H^2\)-class；
3. 对每个 \(2\le k\le m\)，R3 cellular matching cocycle 表示同一个类
   \[
   s_{k-1}^*\kappa_{k+1}
   \in
   H^{k+1}(B;\Pi_k(s_{k-1}));
   \]
4. 两边的 vanishing criterion、lift torsor、deformation groups 与高阶 lift homotopy groups 一致；
5. 该比较对 fibration maps 与基空间 pullback 自然。

这里不声称两个原始 tower 的 stage spaces 逐项等价。

#### B. 有限终止

全局 section 存在，当且仅当存在一条 successive branch，使 \(1\le k\le m\) 的全部依赖型障碍依次消失。不存在维数 \(>d\) 或 fiber degree \(>N\) 的额外有限障碍。

#### C. 规范常系数中心细化

在 relative-nilpotence 附加假设下，共同 obstruction tower 可细化为常系数阿贝尔层。其总细化高度至多

\[
L_{d,N}
:=
\mathbf 1_{\{m\ge1\}}
\sum_{j=1}^{s}a_{1,j}
+
\sum_{k=2}^{m}c_k.
\]

第一项的指示符只表示：当 \(d<2\) 或 \(N<1\) 时，不出现 degree-\(2\) 的 \(\pi_1\) obstruction。

#### D. 精确分支有效性

对任何有限 refinement tower

\[
\mathcal B_L\to\cdots\to\mathcal B_0,
\]

第 \(j\) 层真正可延拓到底的分支由

\[
V_j^{(L)}
=
\operatorname{im}_{-1}
(\mathcal B_L\to\mathcal B_j)
\]

给出。它与逐层消元顺序无关，并满足 R7 的反向递归。

#### E. 有限匹配下降

对 cellular、Postnikov 及中心 refinement 组成的任意有限下闭指标区域 \(A\subseteq P\)，若所有新节点的完整 matching maps 为有效满射，则

\[
\lim_P\mathcal T\to\lim_A\mathcal T
\]

为有效满射；若所有 matching maps 为等价，则该限制映射为等价。

在原始二维 \((r,k)\)-双塔中，完整 matching map 就是 R8 的小方格比较映射 \(\chi_{r,k}\)。加入中心轴后，完整 matching object 是 punctured \(3\)-cube 的同伦极限，不能只看三个 pairwise squares。

#### F. 局部 Coupl 分层

设某个局部修正对象是阿贝尔群 \(H\)，障碍值在阿贝尔群 \(G\)，且 Coupl

\[
q:H\to G
\]

具有有限 Eilenberg–Mac Lane degree。

1. \(\operatorname{cr}_2q=0\) 当且仅当 \(q\) 为仿射，此时有单一 cofiber residual；
2. degree \(2\) 且 \(2\) 在 \(G\) 上可逆时，
   \[
   q(h)=q(0)+\ell(h)+\frac12B(h,h)
   \]
   唯一；
3. \(G\) 为 \(\mathbb Q\)-向量空间时，
   \[
   q(h)=q(0)+\sum_{r=1}^{D}\frac1{r!}B_r(h,\ldots,h)
   \]
   唯一；
4. 一般整数情形只有未分裂的有限 cross-effect jet，不存在由 degree 假设单独推出的线性求解塔。

#### G. 自然性与长度单调性

上述 obstruction classes、matching maps、viability images、cross-effects 与中心过滤均在适当映射下自然。基空间拉回会把 monodromy 限制到子群，因此 relative-nilpotence 长度不增；但拉回后的规范增广过滤可能严格变短，不应声称逐层相等。

---

## 3. 主定理证明

### A 的证明

R5 构造共同双滤过 \(\mathcal S_{r,k}\)。对 fixed \(k\)，R3 matching cocycle 是 fiberwise \(k\)-invariant 在每个 simplex 边界上的 cellular representative；把这些局部值拼合，正得到

\[
s_{k-1}^*\kappa_{k+1}.
\]

relative truncation、restriction 与同伦拉回的 functoriality 给出自然性。第一层用 banded nonabelian descent，后续层用 twisted Eilenberg–Mac Lane torsor。故 obstruction、lift spaces 与全部高阶变形一致。

### B 的证明

fiber 在 \(N\) 后无 homotopy groups；有限 \(d\)-complex 上任意 local system 的 \(H^q\) 在 \(q>d\) 时为零。第 \(k\) 阶障碍位于 degree \(k+1\)，故仅 \(k\le\min(N,d-1)\) 可能出现。

### C 的证明

\(\pi_1\) 先按 characteristic lower central series 分成 \(s\) 个 twisted abelian quotients。第 \(j\) 个商的外部 monodromy 再按

\[
I^0A_{1,j}\supseteq I^1A_{1,j}
\supseteq\cdots\supseteq I^{a_{1,j}}A_{1,j}=0
\]

细化；每个 associated quotient 的作用平凡。对 \(k\ge2\) 的 \(\Pi_k\) 同理使用长度 \(c_k\) 的增广过滤。逐层计数得到 \(L_{d,N}\)。

### D 的证明

一个第 \(j\) 层分支可延拓到底，当且仅当它落在复合

\[
\mathcal B_L\to\mathcal B_j
\]

的 \((-1)\)-像中。像的结合律给出顺序无关；逐层取像给出 R7 的反向递归。

### E 的证明

沿 \(P\setminus A\) 的偏序线性扩张逐点附加。每一步

\[
\lim_{A\cup\{v\}}\mathcal T
\longrightarrow
\lim_A\mathcal T
\]

是 matching map

\[
\mathcal T_v\to M_v\mathcal T
\]

的基变换。有效满射、等价与连通映射均在基变换及有限复合下稳定。二维 matching object 退化为一个 homotopy pullback；三维 matching object 则是完整 punctured cube。

### F 的证明

这是 R10 的有限差分恒等式、最高 cross-effect 多加性、仿射判据及有理极化分解。一般整数求零包含丢番图方程求解，故不存在统一 solver。

### G 的证明

各构造均由 functorial truncation、同伦极限、像、群环增广理想与差分算子定义。若拉回后 monodromy 像为 \(G'\subseteq G\)，则

\[
I_{G'}^jM\subseteq I_G^jM,
\]

从而长度不增，但可能严格下降。

\(\square\)

---

## 4. 直接推论

### 推论 4.1（Untwisted Height Bound）

若所有外部 monodromy 都平凡，则每个非零阿贝尔层长度为 \(1\)。因此

\[
L_{d,N}
\le
\mathbf 1_{\{m\ge1\}}s
+
\#\{k\mid 2\le k\le m,\ \pi_k(F)\ne0\}.
\]

若 fiber 还 simply connected，则第一项消失。

### 推论 4.2（Contractible Choice Criterion）

若从 canonical initial branch 开始，主定理 E 中所有所需 matching maps 都是等价，则完整 section/lift 空间可缩。

若它们仅为有效满射，只能推出存在性；lift 空间仍可能有非平凡 components、路径和自同构。

### 推论 4.3（Connectivity Propagation）

若第 \(v\) 个 matching map 是 \(c_v\)-连通的，则有限全局限制映射至少为

\[
\min_v c_v
\]

连通。故局部唯一性或高阶变形控制能以最弱局部连通度传播到全局。

### 推论 4.4（Global Filler as Iterated Torsor）

固定边界数据后，全局填充空间是局部 matching fibers 的有限迭代同伦纤维。若每个局部纤维是某群对象作用下的 torsor，则全局填充空间是有限迭代 torsor。

一般不能把它压成群对象的直积；只有作用平凡或存在相容分裂时才可如此。

### 推论 4.5（Gauge Quotient First）

对任意局部 Coupl \(q:H\to G\)，平移稳定子

\[
K_q=\{h\mid q(a+h)=q(a)\ \forall a\}
\]

是规范子群。零点问题先下降到

\[
\bar q:H/K_q\to G
\]

不会丢失信息，并去除所有纯 gauge 方向。

### 推论 4.6（Globally Affine Sector）

若一个有限 sector 中：

1. 所有修正对象和障碍对象可在固定阿贝尔群对象中同时表示；
2. 所有 Coupl 均仿射；
3. 所有系数运输与相干映射均线性；

则全部局部方程可组装为一个有限仿射系统

\[
Q(h)=o+Dh.
\]

其存在性由单一总 residual

\[
[o]\in\pi_0\operatorname{cofib}(D)
\]

判定，解空间是 \(\operatorname{fib}(D)\)-torsor。

若任一条件失败，尤其系数随 branch 改变或存在非零 \(\operatorname{cr}_2\)，则不能使用这一总线性压缩。

---

## 5. 必要假设的反例审计

### 5.1 Raw towers 不逐项等价

一个方向截断底空间，另一个方向截断 fiber。即使二者总极限和 obstruction data 相同，固定中间 stage 仍可看到不同的高阶同伦信息。因此主定理只断言 obstruction-theoretic natural equivalence。

### 5.2 Intrinsic nilpotence 不推出 relative nilpotence

取 fiber

\[
K(\mathbb Z^2,n),
\]

它是阿贝尔因而 nilpotent。令 \(B=S^1\)，monodromy 取双曲矩阵

\[
A=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix}.
\]

则

\[
A-I=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}
\]

在 \(\mathbb Z^2\) 上可逆，所以

\[
I^j\mathbb Z^2=\mathbb Z^2
\]

对所有 \(j\ge1\) 成立。故 fiber 本身 nilpotent，但外部作用没有有限增广过滤。

### 5.3 二维 pairwise 数据不控制三重相关

令

\[
Q=\{(a,b,c)\in\{0,1\}^3\mid a+b+c=0\pmod2\}.
\]

三个两两投影 \(Q\to\{0,1\}^2\) 都满射，但

\[
Q\to\{0,1\}^3
\]

不满射。这证明三滤过中 pairwise Beck–Chevalley 条件不充分。

### 5.4 Degree 不自动下降

\[
q(n)=n^2
\]

限制到任意非零子群 \(m\mathbb Z\) 后仍为二次。有限差分 jet 不是逐分支自动线性化算法。

### 5.5 有限层数不推出可判定

任意整数多项式

\[
p:\mathbb Z^r\to\mathbb Z
\]

都是有限差分次数的 Coupl。若有限 degree 自动给出统一求零算法，就会解出 Hilbert 第十问题，矛盾。

### 5.6 有限非空不推出无限 actualization

考虑集合逆系统

\[
X_n=\{m\in\mathbb N\mid m\ge n\},
\qquad
X_{n+1}\hookrightarrow X_n.
\]

每个有限 stage 非空，但

\[
\lim_nX_n=\bigcap_nX_n=\varnothing.
\]

因此任何无限塔结论都必须另行控制 inverse limit、\(\lim^1\)、完备性或 ML 条件。

---

## 6. “一般 truncated nilpotent fiber”应如何准确表述

原问题中的“一般”必须分成三层：

| 层次 | 所需假设 | 可得结论 |
|---|---|---|
| R3/Postnikov 自然比较 | connected truncated fiber；有限 base | obstruction data、branch spaces、torsors 自然等价 |
| nilpotent central refinement | fiber \(\pi_1\) 幂零 | first fringe 分成有限 twisted central extensions |
| 常系数有限 refinement | 额外 relative nilpotence，且沿 viable branches 有统一长度界 | 全部 twisted 层细化为有限常系数层，并有显式高度界 |

因此，最强而正确的表述是：

\[
\boxed{
\begin{aligned}
&\text{R3/Postnikov comparison：一般 connected truncated 情形成立；}\\
&\text{finite constant-coefficient refinement：仅在 relative-nilpotent 情形成立。}
\end{aligned}
}
\]

把第二行只从“fiber nilpotent”推出，是不正确的。

---

## 7. 已知性与项目派生结构

标准输入：

- cellular obstruction theory 与 Moore–Postnikov towers；
- twisted cohomology 和 banded nonabelian \(H^2\)；
- Reedy matching objects 与有限 homotopy limits；
- nilpotent groups、augmentation ideals 和 filtered complexes；
- Eilenberg–Mac Lane polynomial maps 与 cross-effects；
- Hilbert 第十问题的不可判定性。

本项目形成的统一派生结构：

1. R3 matching tower 被识别为 Postnikov obstruction tower 的 cellular/Reedy resolution；
2. exact viability image 替代逐层“选一个 lift”的不充分递归；
3. obstruction Fubini 与 finite matching descent 控制多个截断方向；
4. polynomial Coupl 的可压缩程度由 \(\operatorname{cr}_2\)、极化和系数环精确分层；
5. relative nilpotence 把 twisted coefficients 规范细化为常系数层；
6. 中心轴把二维交换升级为真正三维 matching 问题；
7. 有限结构终止、算法可判定与无限 actualization 被严格分开。

参考：

- Emily Riehl and Dominic Verity, *The Theory and Practice of Reedy Categories*, [arXiv:1304.6871](https://arxiv.org/abs/1304.6871).
- Qimh Richey Xantcha, *Polynomial Maps of Modules*, [arXiv:1112.0991](https://arxiv.org/abs/1112.0991).
- Yu. V. Matiyasevich, *Diophantine Representation of Enumerable Predicates*, Math. USSR-Izvestija 5 (1971), 1–28.
- A. K. Bousfield and D. M. Kan, *Homotopy Limits, Completions and Localizations*, LNM 304.
- J. P. May and K. Ponto, *More Concise Algebraic Topology*.

---

## 8. 最终判定

\[
\boxed{
\begin{array}{rcl}
\text{raw termwise tower equivalence}
&=&\text{false in general},\\
\text{obstruction-theoretic natural equivalence}
&=&\text{proved},\\
\text{finite 2D coherent descent}
&=&\text{proved},\\
\text{3D pairwise descent}
&=&\text{false; full matching required},\\
\text{relative-nilpotent constant refinement}
&=&\text{proved with height bound},\\
\text{affine single-cofiber compression}
&\Longleftrightarrow&\operatorname{cr}_2=0,\\
\text{finite polynomial jet}
&=&\text{proved},\\
\text{universal integer zero solver}
&=&\text{impossible},\\
\text{unconditional infinite actualization}
&=&\text{not claimed}.
\end{array}
}
\]

这给出当前假设下能够无条件推出的最大有限定理包。进一步推进只能沿三类额外输入进行：特定可计算的 Postnikov 数据、特定可解的 Coupl 子类、或明确的无限收敛条件；不能再从“truncated + nilpotent”这几个词本身推出更强的一般结论。
