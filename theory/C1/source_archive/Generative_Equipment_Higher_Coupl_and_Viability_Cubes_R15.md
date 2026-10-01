# 生成装备研究 R15：高阶 Coupl、原始性判据与可行性立方体

日期：2026-09-28  
逻辑地位：Frozen v1.0 的派生实验与 sector theorem；不修改冻结核心

## 0. 本轮突破

R14 只证明了二次 cup-square 会产生真实的非仿射 Postnikov Coupl。本轮得到三个更强结论。

1. **Universal Coupl-Jet Criterion**：一个由 universal class
   \(\kappa\in H^q(K(G,r);R)\) 给出的 Postnikov 修正规律，其 Eilenberg--Mac Lane 多项式次数，精确等于 \(\kappa\) 相对于加法 H-space 结构的有限差分次数。仿射性等价于 \(\kappa\) 是 primitive class。
2. **Two-Stage Unbounded Coupling Theorem**：对每个 \(d\ge2\)，存在一个 simply connected two-stage nilpotent \((2d-1)\)-type，其 Coupl 的精确次数为 \(d\)。因此：
   \[
   \boxed{\text{Postnikov 层数为 2、}\pi_1\text{ 及其作用都平凡，仍不能约束 Coupl 次数。}}
   \]
3. **Punctured Viability Cube Theorem**：对每个 \(d\ge2\)，存在一个自然的 \(d\)-维分支立方体，使全部 proper-subset branches 都可提升，而 total branch 不可提升；首个非零缺陷恰为 \(d\)-元 cross-effect。

这不是新算法，但它给出了一个严格的不可压缩边界：一般 R3/Postnikov 自然比较可以成立，然而任何与 fiber 无关的统一有限阶 Coupl 截断都不可能成立。

---

## 1. Universal Coupl classes

令

\[
A=K(G,r)
\]

带标准的加法 H-space 结构

\[
\mu:A\times A\longrightarrow A.
\]

固定系数环 \(R\) 及正次数 universal class

\[
\kappa\in \widetilde H^q(A;R).
\]

它给出自然上同调运算

\[
Q_\kappa:H^r(B;G)\longrightarrow H^q(B;R),
\qquad
Q_\kappa(a)=a^*\kappa.
\tag{1.1}
\]

对一个初始 branch \(a\) 与 correction \(h\)，定义

\[
C_a(h):=Q_\kappa(a+h)-Q_\kappa(a).
\tag{1.2}
\]

这正是相应 two-stage Postnikov lifting problem 中，改变第一阶段 branch 后的 obstruction variation。

对 \(j\ge1\)，在

\[
A^{j+1}=A_a\times A_{h_1}\times\cdots\times A_{h_j}
\]

上定义 universal action difference

\[
\Theta_j(\kappa)
:=
\sum_{S\subseteq\{1,\ldots,j\}}
(-1)^{j-|S|}\,
\mu_S^*\kappa,
\tag{1.3}
\]

其中

\[
\mu_S(a,h_1,\ldots,h_j)
=a+\sum_{i\in S}h_i.
\]

---

## 2. Universal Coupl-Jet Criterion

### 定理 2.1

对任意 CW complex \(B\) 及

\[
a,h_1,\ldots,h_j\in H^r(B;G),
\]

成立

\[
\operatorname{cr}_j C_a(h_1,\ldots,h_j)
=
(a,h_1,\ldots,h_j)^*\Theta_j(\kappa).
\tag{2.1}
\]

因此以下条件等价：

1. 对所有 \(B\) 与 \(a\)，\(C_a\) 的 Eilenberg--Mac Lane degree 至多为 \(D\)；
2. universal class 满足
   \[
   \Theta_{D+1}(\kappa)=0.
   \tag{2.2}
   \]

特别地，全部 Coupl 都是仿射的，当且仅当 \(\kappa\) 对 H-space coproduct 是 primitive：

\[
\boxed{
\mu^*\kappa
=
\operatorname{pr}_1^*\kappa
+
\operatorname{pr}_2^*\kappa.
}
\tag{2.3}
\]

### 证明

按 cross-effect 定义，

\[
\operatorname{cr}_j C_a(h_1,\ldots,h_j)
=
\sum_{S\subseteq[j]}
(-1)^{j-|S|}
C_a\!\left(\sum_{i\in S}h_i\right).
\]

代入 (1.2)。因为 \(j\ge1\)，所有常数项 \(-Q_\kappa(a)\) 的符号和为零，所得表达式正是 (1.3) 沿 \((a,h_1,\ldots,h_j):B\to A^{j+1}\) 的拉回。这证明 (2.1)。

若 (2.2) 成立，则所有拉回都为零，故 degree 至多 \(D\)。反之，取 universal tuple，即得到 \(\Theta_{D+1}(\kappa)=0\)。

若 \(\kappa\) primitive，则

\[
Q_\kappa(a+h)=Q_\kappa(a)+Q_\kappa(h),
\]

所以 \(C_a(h)=Q_\kappa(h)\) 且它关于 \(h\) 可加。反之，若所有 \(C_a\) 仿射，令 \(a=0\)、\(B=A\times A\)，并取两投影给出的 universal classes，就得到 (2.3)。证毕。

### 意义

R10 的“\(\operatorname{cr}_2=0\)”现在不再只是对每个实例逐一检查；它被提升为对 Postnikov \(k\)-invariant 的内在判据：

\[
\boxed{\text{affine Coupl}\iff\text{primitive }k\text{-invariant}.}
\]

---

## 3. 完整的 \(K(\mathbb Z,2)\) 单生成元 sector

令

\[
A=K(\mathbb Z,2)\simeq\mathbb{CP}^{\infty},
\qquad
H^*(A;\mathbb Z)=\mathbb Z[u],\quad |u|=2.
\]

对 \(d\ge1\) 与 \(c\in\mathbb Z\)，取

\[
\kappa_{c,d}=c\,u^d\in H^{2d}(A;\mathbb Z).
\tag{3.1}
\]

因为

\[
\mu^*u=u_1+u_2,
\]

有限差分直接给出

\[
\Theta_{d+1}(\kappa_{c,d})=0,
\tag{3.2}
\]

而

\[
\Theta_d(\kappa_{c,d})
=c\,d!\,u_{h_1}\cdots u_{h_d}.
\tag{3.3}
\]

当 \(c\ne0\) 时，(3.3) 在

\[
H^{2d}(A^{d+1};\mathbb Z)
\]

中非零。因此：

### 定理 3.1（单生成元次数分类）

映射

\[
K(\mathbb Z,2)\longrightarrow K(\mathbb Z,2d)
\]

由整数 \(c\) 分类。零类给出零 Coupl；每个非零类 \(c u^d\) 的 Coupl 精确具有 Eilenberg--Mac Lane degree \(d\)。

这完成了该自然 sector 的全部有限-degree 分类，而不只是给出若干例子。

---

## 4. Two-Stage Unbounded Coupling Theorem

对 \(d\ge2\)，令

\[
\kappa_d:K(\mathbb Z,2)\longrightarrow K(\mathbb Z,2d)
\]

表示 \(u^d\)，并定义

\[
F_d:=\operatorname{hofib}(\kappa_d).
\tag{4.1}
\]

### 定理 4.1

\(F_d\) 是 simply connected nilpotent two-stage \((2d-1)\)-type，并且

\[
\pi_i(F_d)\cong
\begin{cases}
\mathbb Z,&i=2,\\
\mathbb Z,&i=2d-1,\\
0,&\text{其余 }i.
\end{cases}
\tag{4.2}
\]

其唯一非平凡 \(k\)-invariant 是 \(u^d\)，相应 branch-Coupl 的精确次数为 \(d\)。

### 证明

由 (4.1) 的同伦长正合列，\(K(\mathbb Z,2)\) 提供 \(\pi_2\cong\mathbb Z\)，而目标的 \(\pi_{2d}\cong\mathbb Z\) 经 connecting morphism 给出

\[
\pi_{2d-1}(F_d)\cong\mathbb Z.
\]

其余次数均为零。特别地 \(F_d\) 单连通，故为 nilpotent。其 Postnikov fibration 为

\[
K(\mathbb Z,2d-1)\longrightarrow F_d
\longrightarrow K(\mathbb Z,2),
\]

分类类正是 \(u^d\)。Coupl 次数由定理 3.1 得到。证毕。

### 推论 4.2（无统一次数界）

不存在只依赖于下列数据的 Coupl-degree 上界：

1. 非零 Postnikov homotopy groups 的个数；
2. \(\pi_1\)-action 的幂零长度；
3. 是否 simply connected。

因为整个族 \(F_d\) 都只有两个非零同伦群，并且 \(\pi_1\) 与其作用恒平凡，但 Coupl degree 为任意大的 \(d\)。

若允许上界依赖 truncation degree \(N\)，则该族还给出必要下界

\[
D(N)\ge \frac{N+1}{2}
\qquad (N=2d-1).
\tag{4.3}
\]

---

## 5. \(\mathbb{CP}^d\) 上的完整 correction 实验

取有限底空间

\[
B=\mathbb{CP}^d,
\qquad
H^*(B;\mathbb Z)=\mathbb Z[u]/(u^{d+1}).
\]

一个 first-stage branch \(a=nu\) 提升到 \(F_d\) 当且仅当

\[
a^d=n^d u^d=0,
\]

亦即 \(n=0\)。从 \(a_0=u\) 出发，取 correction \(h=mu\)，则

\[
Q(a_0+h)=(1+m)^d u^d.
\tag{5.1}
\]

精确方程只有一个整数解

\[
m=-1.
\]

普通的一阶仿射截断则给出

\[
1+d\,m=0,
\tag{5.2}
\]

它对每个 \(d\ge2\) 都没有整数解。这里 (5.2) 只是对完整整数 Coupl 的非规范一阶近似；真正严格的结论不是“某个线性化总失败”，而是 (3.3) 已证明任何 degree \(<d\) 的自然模型都不可能在所有底空间上精确表示该 Coupl。

因此 R14 的 cup-square 反例不是孤立现象，而是一个任意高阶族的 \(d=2\) 首项。

---

## 6. Punctured Viability Cube Theorem

令

\[
B_d=(S^2)^d
\]

并记各因子的生成元为

\[
u_i\in H^2(B_d;\mathbb Z),
\qquad
u_i^2=0.
\]

对每个子集 \(S\subseteq[d]\)，定义 branch

\[
a_S:=\sum_{i\in S}u_i.
\tag{6.1}
\]

这些 branches 构成由逐个加入 correction \(u_i\) 生成的 \(d\)-维可行性立方体。

### 定理 6.1

相对于 two-stage Postnikov target \(F_d\)：

1. 每个 proper-subset branch \(a_S\)、\(S\subsetneq[d]\)，都可提升；
2. total branch \(a_{[d]}\) 不可提升；
3. 首个非零 coordinate interaction 是 \(d\)-元 cross-effect
   \[
   \operatorname{cr}_d Q(0;u_1,\ldots,u_d)
   =d!\,u_1\cdots u_d\ne0.
   \tag{6.2}
   \]

### 证明

若 \(|S|<d\)，展开

\[
a_S^d=\left(\sum_{i\in S}u_i\right)^d.
\]

每个次数 \(d\) 的 monomial 只使用少于 \(d\) 个变量，故至少一个变量重复；由 \(u_i^2=0\)，全部 monomials 消失。因此

\[
a_S^d=0.
\]

当 \(S=[d]\) 时，唯一存活的 monomials 各恰使用每个 \(u_i\) 一次，共有 \(d!\) 个排列，所以

\[
a_{[d]}^d=d!\,u_1\cdots u_d.
\]

该类生成 \(H^{2d}(B_d;\mathbb Z)\) 的一个非零倍数，故不为零。因为所有 proper-subset terms 均为零，有限差分公式立即给出 (6.2)。证毕。

### 严格解释

这是 **branch-viability cube**，并不自动提供 lift spaces 之间的 coherent cubical maps；不能把它误称为已经构造好的 Reedy punctured cube。它严格证明的是：

\[
\boxed{
\text{所有基于 proper coordinate subsets 的零基点 viability tests 都可通过，}
\quad
\text{但 }d\text{ 元总修正仍失败。}
}
\]

在 R3 的 cellular 语言中，失败定位在 \(B_d\) 的唯一 top product cell 上，其 local matching value 正是 \(d!u_1\cdots u_d\)。这给出了任意高 arity 的真实 Postnikov local defect。

---

## 7. Steenrod、Pontryagin square 与 Massey 边界

定理 2.1 给出统一分类接口。

| 操作类型 | universal class 的行为 | Coupl 结论 |
|---|---|---|
| 加性稳定上同调操作，包括各个 \(Sq^i\) | primitive | 精确仿射；单一线性 residual 在该层有效 |
| Pontryagin square | quadratic refinement，二阶差分由 \(2x\smile y\) 给出 | degree \(2\)；必须保留二阶 cross-effect |
| integral cup-power \(x\mapsto x^d\) | \(d\)-次非 primitive | degree 精确为 \(d\) |
| Massey-type operation | 通常只部分定义、依赖 defining system、可能多值 | 不是普通函数 \(H\to G\)；不能直接套用 R10 的单值 cross-effect formalism |

这里真正的分界不是简单的“stable/unstable”：

\[
\boxed{\text{primitive/non-primitive 才是 affine/non-affine 的精确分界。}}
\]

稳定操作必为加性，因而落在 primitive sector；但某些不稳定操作仍可能是加性的。

Massey sector 需要把 Coupl 从函数升级为 correspondence、space-valued operation 或 defining-system fibration。这是下一阶段的合理扩张点，但不是 Frozen v1.0 的修正。

---

## 8. 对 R5 与 R12 的影响

### 8.1 R5 自然比较保持成立

本轮没有反驳 R5。对 \(F_d\)，R3 top-cell matching cocycle 与 Postnikov obstruction 都是同一个类

\[
a^d\in H^{2d}(B;\mathbb Z).
\]

因此 stagewise obstruction identity 仍严格成立。

### 8.2 必须区分三个高度

本轮证明三个互不等价的复杂度参数：

1. **Postnikov length**：非零 homotopy groups 的个数；对 \(F_d\) 恒为 \(2\)；
2. **truncation height**：最高非零 homotopy degree；对 \(F_d\) 为 \(2d-1\)；
3. **Coupl arity/degree**：精确 cross-effect 次数；对 \(F_d\) 为 \(d\)。

所以不能从“two-stage”推出“quadratic”，也不能从“nilpotent class one”推出“affine”。

### 8.3 R12-F 得到严格加强

R12 已说明有限 degree 不给出一般整数 solver。本轮进一步证明：

\[
\boxed{
\text{甚至在最简单的 simply connected two-stage fibers 中，}
\text{所需 finite jet 的阶数也没有统一上界。}
}
\]

因此一般自然等价定理必须保留完整 \(k\)-invariant evaluation，或保留直到实际 degree 为止的全部 cross-effects；不能预先固定 affine、quadratic，或任何统一有限阶模板。

---

## 9. 现实意义审计

### 已获得的真实意义

1. **严格的不可压缩性**：不是依靠 Hilbert 第十问题的外部不可判定性，而是在 genuine two-stage Postnikov spaces 内部构造任意高 Coupl degree。
2. **可检查的内在判据**：仿射性可直接由 \(k\)-invariant 是否 primitive 判断，无需遍历所有底空间和 branches。
3. **自然高阶压力测试族**：\((F_d,B_d,a_S)\) 可系统测试任何声称只用低阶局部兼容性的算法。
4. **纠正复杂度直觉**：Postnikov stage 数少并不意味着 branch equation 简单。

### 尚未获得的意义

1. 没有给出比经典 Postnikov 方法更快的算法；
2. 没有证明求解这些实例计算困难，示例本身反而可显式求解；
3. 没有完成 Massey-type 的 space-valued Coupl 理论；
4. 没有完成 R11 优势实例或 R13 强加速基准 C。

已有 fixed-dimension Postnikov 计算算法与本结果并不冲突：本族的 top dimension \(2d\) 随 Coupl degree 一起增长。本报告给出的是 uniform compression no-go，而不是 fixed-dimension complexity lower bound。

---

## 10. 下一阶段

现在最值得推进的不是继续罗列操作，而是两条严格路线：

1. **Derived Coupl 路线**：把部分定义、多值的 Massey operation 表示为 defining-system fibration，建立 space-valued cross-effect 与 R3 matching obstruction 的比较；
2. **Complexity 路线**：固定 truncation degree \(N\)，研究 Coupl degree 的最佳上界，并寻找 R3 cellular localization 相对直接 \(k\)-invariant evaluation 的真实复杂度分离。

第一条扩张理论表达能力；第二条决定现实算法价值。

---

## 参考背景

- J. P. May and K. Ponto, *More Concise Algebraic Topology*, Chapter 3: nilpotent spaces、Postnikov towers、principal refinements 与作为 \(k\)-invariant homotopy fibers 的 stages。  
  https://www.math.uchicago.edu/~may/PAPERS/116.pdf
- Qimh Richey Xantcha, *Polynomial Maps of Modules*, Eilenberg--Mac Lane polynomial maps 与有限差分背景。  
  https://arxiv.org/abs/1112.0991
- M. Čadek et al., *Polynomial-time computation of homotopy groups and Postnikov systems in fixed dimension*，用于区分 fixed-dimension algorithms 与本报告的 uniform no-go。  
  https://arxiv.org/abs/1211.3093

## 最终判定

\[
\boxed{
\begin{array}{rcl}
\text{affine Coupl}
&\Longleftrightarrow&
\text{primitive }k\text{-invariant},\\
\text{Coupl degree}\le D
&\Longleftrightarrow&
\Theta_{D+1}(\kappa)=0,\\
\text{two-stage + simply connected + nilpotent}
&\centernot\Longrightarrow&
\text{bounded Coupl degree},\\
\text{all proper-subset branches viable}
&\centernot\Longrightarrow&
\text{total branch viable}.
\end{array}
}
\]

这是 R14 之后的决定性推进：R10 从“二次现象确实存在”升级为“任意高阶现象在最简单的两阶段 Postnikov 世界中已经不可避免”。
