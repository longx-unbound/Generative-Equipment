# 生成装备研究 R16：最优 Arity 界、Resolved Coupl 与 Massey Matching

日期：2026-09-29  
逻辑地位：Frozen v1.0 的派生 sector theorem 与边界报告；不修改冻结核心

## 0. 结论概览

本轮没有停在 R15 的任意高阶反例，而是继续解决了两个正面问题，并定位了第一个无法在当前理论内部解决的现实性问题。

1. **Optimal Primary Arity Bound**：若 correction group object 是一个 \((r-1)\)-connected H-space，而 obstruction 位于 degree \(q\)，则普通单值 Coupl 的次数满足
   \[
   \deg(\operatorname{Coupl})\le \left\lfloor\frac qr\right\rfloor .
   \]
2. 对 simply connected \(N\)-types，untwisted primary Coupl 有统一最优界
   \[
   \boxed{
   \deg(\operatorname{Coupl})
   \le
   \left\lfloor\frac{N+1}{2}\right\rfloor .
   }
   \]
   R15 的 \(F_d\) 对所有 \(N\ge3\) 达到这个界。
3. **Resolved Coupl formalism**：部分定义、多值且带有 nullhomotopy choices 的障碍，不应表示成函数 \(H\to G\)，而应表示成
   \[
   H\longleftarrow D\longrightarrow G\longleftarrow N.
   \]
   真正的解空间是 \(D\times_G^hN\)。
4. **Massey Matching Theorem**：任意 \(n\)-重 Massey defining system 都是严格上三角 Maurer--Cartan 矩阵的 punctured matching datum；Massey value 是缺失顶端矩阵元的 matching obstruction，且其消失等价于填入该矩阵元。
5. 构造了一族对每个 \(n\) 都具有非零 \(n\)-元 matching defect 的自由 DGA，证明 secondary arity 同样无统一常数界。
6. 真正阻塞出现在“R3 是否比直接 Postnikov 计算更快”：在没有指定输入编码、\(k\)-invariant 表示和代价模型前，该问题不是一个良定义的数学命题。等价空间可以通过细分或加入可消去胞腔任意放大表示规模。

---

## 1. 一般作用型 Coupl

令 \(A\) 是带单位元 \(e\) 的 grouplike homotopy-commutative H-space，并设它作用在空间 \(X\) 上：

\[
\alpha:A\times X\longrightarrow X.
\]

固定常系数环 \(R\) 和

\[
\kappa\in H^q(X;R).
\]

对一个 branch \(x:B\to X\) 及 corrections

\[
h_1,\ldots,h_j:B\to A,
\]

定义 \(j\)-阶 universal action difference

\[
\Theta_j^\alpha(\kappa)
:=
\sum_{S\subseteq[j]}
(-1)^{j-|S|}
\alpha_S^*\kappa
\in H^q(A^j\times X;R),
\tag{1.1}
\]

其中

\[
\alpha_S(h_1,\ldots,h_j,x)
=
\alpha\left(\sum_{i\in S}h_i,x\right).
\]

沿 \((h_1,\ldots,h_j,x)\) 拉回，正得到 branch-Coupl 的 \(j\)-阶有限差分。

---

## 2. Optimal Primary Arity Bound

### 定理 2.1

假设 \(A\) 是 \((r-1)\)-connected pointed CW H-space，其中 \(r\ge1\)。则

\[
\boxed{
\Theta_j^\alpha(\kappa)=0
\qquad\text{只要}\qquad
jr>q.
}
\tag{2.1}
\]

因而由 \(\kappa\) 产生的所有普通单值 Coupl 都满足

\[
\boxed{
\deg(\operatorname{Coupl})
\le
\left\lfloor\frac qr\right\rfloor .
}
\tag{2.2}
\]

### 证明

若某个 correction coordinate \(h_i=e\)，则 (1.1) 中不含 \(i\) 与含 \(i\) 的两个子集项两两抵消。因此

\[
\Theta_j^\alpha(\kappa)
\big|_{\operatorname{FW}_j(A)\times X}
=0,
\]

其中 \(\operatorname{FW}_j(A)\subseteq A^j\) 是至少一个坐标为单位元的 fat wedge。

所以 \(\Theta_j^\alpha(\kappa)\) 来自相对上同调

\[
H^q\left(
A^j\times X,\,
\operatorname{FW}_j(A)\times X;R
\right).
\tag{2.3}
\]

相对商同伦等价于

\[
\frac{A^j\times X}
{\operatorname{FW}_j(A)\times X}
\simeq
A^{\wedge j}\wedge X_+.
\tag{2.4}
\]

因为 \(A\) 是 \((r-1)\)-connected，\(A^{\wedge j}\) 是 \((jr-1)\)-connected。加入 \(X_+\) 不会产生维数低于 \(jr\) 的相对胞腔。因此当 \(q<jr\) 时，(2.3) 为零，得到 (2.1)。

取

\[
j=\left\lfloor\frac qr\right\rfloor+1
\]

便有 \(jr>q\)，所以第 \(j\) 阶差分消失，得到 (2.2)。证毕。

### 注 2.2

该证明只使用 fat-wedge quotient 与 smash connectivity。它不是对具体多项式展开的估计，因此对任意 \(A\)-action 和任意 \(\kappa\in H^q(X;R)\) 都适用；但这里要求常系数及普通 primary class。

---

## 3. Simply connected \(N\)-types 的最优统一界

### 定理 3.1

考虑 simply connected \(N\)-type 的 untwisted primary Postnikov obstruction。若某个 correction direction 来自

\[
K(G,r),\qquad r\ge2,
\]

而 obstruction 位于 degree \(q\le N+1\)，则

\[
\deg(\operatorname{Coupl})
\le
\left\lfloor\frac qr\right\rfloor
\le
\left\lfloor\frac{N+1}{2}\right\rfloor .
\tag{3.1}
\]

该全局界对每个 \(N\ge3\) 都是最优的。

### 证明

第一不等式是定理 2.1。单连通保证最低 correction degree 为 \(r\ge2\)，而 \(N\)-type 的 primary obstruction degree 不超过 \(N+1\)，所以得到第二不等式。

令

\[
d=\left\lfloor\frac{N+1}{2}\right\rfloor .
\]

R15 构造的

\[
F_d=\operatorname{hofib}
\left(
K(\mathbb Z,2)\xrightarrow{u^d}K(\mathbb Z,2d)
\right)
\]

是一个 \((2d-1)\)-type，因而也是 \(N\)-type，并具有精确 Coupl degree \(d\)。所以 (3.1) 达到等号。证毕。

### 结果

R15 的“无统一次数界”现在被精确化为：

\[
\boxed{
\text{若不固定 }N\text{，次数无界；若固定 }N\text{，simply connected primary sector 的最优界是 }
\left\lfloor\frac{N+1}{2}\right\rfloor .
}
\]

---

## 4. Resolved Coupl

普通 Coupl 是一个函数

\[
q:H\longrightarrow G.
\]

它不能表达以下现象：

1. 某些 corrections 根本没有 admissible defining system；
2. 同一个 correction 有多个 obstruction values；
3. obstruction 虽然为零，但零化它的 nullhomotopies 形成非平凡空间。

### 定义 4.1

一个 resolved Coupl datum 是一个图

\[
H
\xleftarrow{\,p\,}
D
\xrightarrow{\,\omega\,}
G
\xleftarrow{\,\nu\,}
N.
\tag{4.1}
\]

其含义为：

- \(H\)：corrections；
- \(D_h\)：correction \(h\) 的 admissible defining systems；
- \(\omega\)：defining system 所产生的 obstruction；
- \(N\to G\)：nullification data，例如 coboundaries、paths 或 fillers。

定义完整解空间

\[
\mathcal Z
:=
D\times_G^hN.
\tag{4.2}
\]

### 定理 4.2（Resolved Zero-Fiber Criterion）

correction \(h\in H\) 真正可解，当且仅当

\[
\mathcal Z_h
\simeq
D_h\times_G^hN
\]

非空。全部 viable corrections 恰为

\[
\boxed{
V
=
\operatorname{im}_{-1}
\left(
D\times_G^hN\longrightarrow H
\right).
}
\tag{4.3}
\]

若 \(p:D\to H\) 是等价且 \(N=*\to G\) 是零点，则恢复普通函数的零点问题。若只取 \(\pi_0G\) 并把 \(N\) 压成一个点，就只保留存在性而丢失 nullhomotopy choices。

### 与现有理论的关系

(4.3) 正是 R7 exact viability image 在多值障碍中的自然形式；(4.2) 则落实 R8 对“存在交换”与“结构交换”的区分。

---

## 5. \(n\)-重 Massey defining systems

以下在特征 \(2\) 的 cohomological DGA

\[
(C^*,d,\smile)
\]

中工作，以去除无关的符号负担。

固定 cocycles

\[
a_i\in Z^{p_i}(C),
\qquad
1\le i\le n.
\]

一个 \(n\)-重 defining system 是一族元素

\[
a_{ij}\in
C^{p_i+\cdots+p_{j-1}-(j-i-1)},
\]

其中

\[
1\le i<j\le n+1,\qquad
(i,j)\ne(1,n+1),
\]

满足

\[
a_{i,i+1}=a_i
\tag{5.1}
\]

以及

\[
d a_{ij}
=
\sum_{i<k<j}
a_{ik}a_{kj}
\qquad
\bigl((i,j)\ne(1,n+1)\bigr).
\tag{5.2}
\]

定义 top curvature

\[
\Omega(A)
:=
\sum_{k=2}^{n}
a_{1k}a_{k,n+1}.
\tag{5.3}
\]

其次数为

\[
m=p_1+\cdots+p_n-(n-2).
\tag{5.4}
\]

---

## 6. Massey Matching Theorem

### 定理 6.1

对任意 satisfying (5.1)--(5.2) 的 partial defining system \(A\)：

1. \(\Omega(A)\in Z^m(C)\)；
2. \([\Omega(A)]\) 是该 defining system 给出的 \(n\)-重 Massey value；
3. \(A\) 能扩张为包含顶端矩阵元 \(a_{1,n+1}\) 的完整 Maurer--Cartan defining system，当且仅当
   \[
   [\Omega(A)]=0;
   \]
4. 全部完整 extensions 构成严格拉回
   \[
   \mathcal F_n
   \cong
   \mathcal D_n
   \times_{Z^m(C)}
   C^{m-1},
   \tag{6.1}
   \]
   其中
   \[
   \Omega:\mathcal D_n\to Z^m(C),
   \qquad
   d:C^{m-1}\to Z^m(C).
   \]

在 simplicial 或 Dold--Kan enhancement 中，(6.1) 应取 homotopy pullback。

### 证明

对 (5.3) 求微分并使用 (5.2)：

\[
\begin{aligned}
d\Omega(A)
&=
\sum_{k=2}^{n}
\left(
d a_{1k}\,a_{k,n+1}
+
a_{1k}\,d a_{k,n+1}
\right)\\
&=
\sum_{1<i<k<n+1}
a_{1i}a_{ik}a_{k,n+1}
+
\sum_{1<k<j<n+1}
a_{1k}a_{kj}a_{j,n+1}.
\end{aligned}
\]

两重和在重新命名中逐项相同；特征 \(2\) 下每个三重乘积出现两次，故总和为零。这证明 \(\Omega(A)\) 是 cocycle。

经典 \(n\)-重 Massey value 的定义正是 (5.3) 的上同调类，因此得到第 2 点。

完整系统只比 partial system 多一个元素

\[
a_{1,n+1}\in C^{m-1},
\]

其 Maurer--Cartan 方程恰为

\[
d a_{1,n+1}=\Omega(A).
\tag{6.2}
\]

所以 extension 存在当且仅当 \(\Omega(A)\) exact，并且所有 choices 正是 (6.1) 的 fiber product。证毕。

### Matching 解释

以 proper intervals

\[
[i,j]\subsetneq[1,n+1]
\]

为节点，(5.2) 说明每个 interval 的数据由其所有二段分解组成的 matching datum 控制。缺失的 maximal interval \([1,n+1]\) 的 matching defect 正是 \(\Omega(A)\)。

因此：

\[
\boxed{
\text{\(n\)-重 Massey value}
=
\text{缺失 maximal interval 的 R3-type matching obstruction}.
}
\tag{6.3}
\]

在群上同调的 degree-one sector，这与 Dwyer 的上三角幺幂表示刻画一致：defining systems 对应到删去右上角条目的表示，而 Massey value 为零当且仅当该表示提升到完整上三角幺幂群。

---

## 7. 任意高 secondary arity 的显式 DGA

对每个 \(n\ge3\)，令 \(C_n\) 是 \(\mathbb F_2\) 上的自由 associative DGA，其 degree-one generators 为

\[
x_{ij},
\qquad
1\le i<j\le n+1,
\qquad
(i,j)\ne(1,n+1),
\]

微分定义为

\[
d x_{i,i+1}=0,
\]

以及

\[
d x_{ij}
=
\sum_{i<k<j}
x_{ik}x_{kj}
\qquad
j-i\ge2.
\tag{7.1}
\]

同第 6 节的三重乘积消去证明给出 \(d^2=0\)。

令

\[
\Omega_n
=
\sum_{k=2}^{n}
x_{1k}x_{k,n+1}.
\tag{7.2}
\]

则 \(\Omega_n\) 是 degree-two cocycle。它不是 boundary：任意 degree-one 元素是 generators 的线性组合，而每个 proper generator \(x_{ij}\) 的微分只含 outer endpoints 为 \((i,j)\ne(1,n+1)\) 的 quadratic words；(7.2) 中所有 words 的 outer endpoints 都是 \((1,n+1)\)。自由代数中的这些 words 线性独立。

所以

\[
[\Omega_n]\ne0\in H^2(C_n).
\tag{7.3}
\]

### 推论 7.1

对每个 \(n\ge3\)，存在一个完全定义的 \(n\)-重 Massey defining system，其 maximal-interval matching obstruction 非零。

因此 secondary matching arity 同样没有统一常数界，即使所有局部 Maurer--Cartan 方程本身都只是二次方程。

这揭示了一个重要区别：

\[
\boxed{
\text{局部方程的代数次数可以恒为 2，}
\quad
\text{但全局 dependency arity 可以任意高。}
}
\]

---

## 8. 为什么普通 cross-effect 在 Massey sector 中失效

普通有限差分要求：

1. correction domain 对加法封闭；
2. 对 \(h_1,h_2\) 的 defining systems 能规范地产生 \(h_1+h_2\) 的 defining system；
3. 这些选择满足结合、交换和高阶相干性。

triple Massey 已经违反第 2 点。若

\[
d x=ab,\qquad d x'=a'b',
\]

则对和输入需要 nullhomotopy

\[
(a+a')(b+b')
=
ab+a'b'+ab'+a'b.
\tag{8.1}
\]

已知的 \(x,x'\) 只消去前两项；mixed terms

\[
ab'+a'b
\]

没有规范 nullhomotopy，甚至未必 exact。因此 defined-Massey domain 一般不是加法子群，defining-system fibers 也没有规范乘法。

### 结论 8.1

Massey-type Coupl 不能在不增加结构的情况下赋予 Eilenberg--Mac Lane polynomial degree。

要定义 derived cross-effects，至少需要：

1. \(D\to H\) 上的 coherently monoidal transport；
2. mixed nullhomotopies；
3. 它们的全部高阶 coherence。

这些数据本质上组成 \(A_\infty/E_\infty\) enhancement。另一条可行路线是对“输入 DGA \(\mapsto\) Maurer--Cartan moduli space”这一 functor 使用 Goodwillie cross-effects，而不是强行对多值 Massey subset 做有限差分。

本报告已经解决 chosen defining system 上的 matching comparison，但没有从现有 Frozen v1.0 数据中规范地产生上述 enhancement。

---

## 9. Presentation-Invariance Complexity No-Go

R13 的强基准 C 要求找到一个 sector，使 R3 local matching 明显比直接 global Postnikov filling 更便宜。现在可以严格说明：只在 homotopy-invariant 层面，这一问题没有定义。

### 定理 9.1

不存在只依赖于空间的同伦型、Postnikov tower 或 R3/Postnikov 自然比较类的“输入规模”，能够支持有意义的统一渐近复杂度比较。

### 证明

取任意有限 simplicial complex \(K\)。

1. 任意次重心细分
   \[
   \operatorname{sd}^mK
   \]
   与 \(K\) 同胚，但 simplices 数可随 \(m\) 任意增长；
2. 也可加入任意多个 elementary expansion/collapse pairs，在不改变同伦型的情况下任意增加 cells 数；
3. 同一个 \(k\)-invariant 可用显式 cocycle、压缩电路、oracle、巨大查找表或未化简 chain map 表示，它们的求值成本完全不同。

因此同一 homotopy-theoretic 输入可以具有任意膨胀的 presentation size。R3 与 Postnikov 的自然等价只控制数学对象，不选择规范编码，也不规定 cup product、局部系数运输或 matching map 的基本操作成本。

所以任何“R3 更快”或“R11 refinement 更便宜”的渐近命题都必须额外固定计算模型。证毕。

### 要使强基准 C 良定义，至少必须指定

1. 输入是 simplicial complex、finite CW complex、chain complex 还是 oracle；
2. \(k\)-invariants 和 local systems 的编码；
3. 群运算、线性代数、cup product 与 transport 的成本；
4. 输出只要求 yes/no、一个 lift，还是完整 lift space；
5. \(N\) 固定还是输入的一部分；
6. 是否允许预处理和并行。

这些不是 Frozen v1.0 的内部同伦数据。

---

## 10. 对当前理论的严格更新

| 问题 | 本轮状态 |
|---|---|
| 固定 \(q,r\) 的 primary Coupl degree 上界 | 已证明：\(\lfloor q/r\rfloor\) |
| simply connected \(N\)-type 的统一 primary 界 | 已证明且最优：\(\lfloor(N+1)/2\rfloor\) |
| 部分定义、多值 Coupl 的正确对象 | 已建立 resolved span 与 homotopy zero-fiber |
| chosen defining system 上的 Massey/R3 matching 比较 | 已对全部 \(n\) 证明 |
| 任意高 secondary arity | 已由自由 DGA 族证明 |
| Massey operation 的普通 Eilenberg--Mac Lane degree | 一般无定义；domain 不对加法封闭 |
| 模型无关的 full derived cross-effect | 需要额外 \(A_\infty/E_\infty\) coherence |
| R3 相对直接 Postnikov 的普适复杂度优势 | 当前问题未良定义；必须先给计算模型 |

---

## 11. 现实意义评估

### 有现实意义的结果

1. \(\lfloor q/r\rfloor\) 是一个可直接使用的有限性界；在固定 \(N\) 的算法设计中，它规定最多需要保留多少阶 primary cross-effects。
2. \(\lfloor(N+1)/2\rfloor\) 为 simply connected \(N\)-types 给出最坏情形的精确 jet 高度，而不是松散估计。
3. Massey Matching Theorem 把 secondary operation 转换成具体的上三角矩阵补全问题；这可直接用于群上同调、形变理论和 cochain-level obstruction。
4. Resolved Coupl 保留 defining systems 与 nullhomotopies，避免把“零属于 Massey subset”错误压缩成一个任意选取的单值。
5. Presentation-Invariance No-Go 阻止继续提出没有输入模型的虚假“加速定理”。

### 仍未获得的结果

1. 尚无一个统一、模型无关的 derived cross-effect functor；
2. 尚未证明 R3 在任何标准计算模型中具有严格复杂度优势；
3. R11 的结构 refinement 仍没有普适算法优势；
4. 自由 DGA 族证明 secondary arity 无界，但没有给出实际计算困难性的下界。

---

## 12. 当前不可继续解决的精确问题

研究推进到这里后，首个真正不能在现有假设下继续解决的问题是：

> “R3 matching tower 是否比直接 Postnikov obstruction evaluation 渐近更快？”

这不是因为证明技术暂时不足，而是因为题目缺少计算编码与代价模型。不同答案会随以下选择改变：

- cellular sparse encoding 或 dense matrices；
- \(k\)-invariant 是显式 cocycle 还是 oracle；
- \(N\) 固定或可变；
- 顺序计算或并行计算；
- 只判存在性或输出完整解空间。

在这些数据被固定之前，继续宣称复杂度优势没有严格数学含义。

另一个结构性缺口是 Massey sector 的模型无关 derived cross-effect。它需要额外选择一个 \(A_\infty/E_\infty\) 或 Maurer--Cartan moduli doctrine；Frozen v1.0 本身不指定这一选择，因此无法从现有公理唯一推出。

这两个缺口都不是 Frozen v1.0 的矛盾。它们标志着 derived theory 必须引入新 doctrine 的边界。

---

## 参考背景

- J. P. May and K. Ponto, *More Concise Algebraic Topology*：Postnikov towers 与 nilpotent principal refinements。  
  https://www.math.uchicago.edu/~may/PAPERS/116.pdf
- J. Mináč and N. D. Tân, *Triple Massey products and Galois theory*：defining systems、上三角幺幂表示以及 Dwyer lifting criterion。  
  https://ems.press/content/serial-article-files/32174
- D. Fuchs and L. Lang, *Massey Products and Deformations*：Massey equations、严格上三角矩阵与形变问题。  
  https://arxiv.org/abs/q-alg/9602024
- A. Mauer-Oats, *Goodwillie Calculi*：以 iterated cross-effects 和 total homotopy fibers 构造 functorial polynomial approximations。  
  https://arxiv.org/abs/1304.5662

## 最终判定

\[
\boxed{
\begin{array}{rcl}
\deg(\text{primary Coupl})
&\le&
\lfloor q/r\rfloor,\\[2mm]
\deg(\text{simply connected }N\text{-type primary Coupl})
&\le&
\lfloor(N+1)/2\rfloor
\quad\text{且最优},\\[2mm]
\text{Massey value}
&=&
\text{maximal-interval matching obstruction},\\[2mm]
\text{完整 defining systems}
&=&
\text{resolved homotopy zero-fiber},\\[2mm]
\text{secondary arity}
&=&
\text{无统一常数界},\\[2mm]
\text{普适复杂度优势}
&=&
\text{未指定计算模型时不良定义}.
\end{array}
}
\]

R15 给出了任意高 primary Coupl；R16 又给出了最优固定高度上界、任意高 secondary matching arity，并精确找到了理论从纯同伦结构进入计算学时必须补充的新数据。
