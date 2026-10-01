# 数学内生生成性理论

## R3 Matching Tower 与 Postnikov Obstruction Tower 的自然比较定理 R5

日期：2026-09-28  
逻辑地位：Frozen v1.0 的派生 sector theorem；不修改冻结核心  
直接前置：

- `Generative_Equipment_Effectivity_Obstruction_Program_R3.md`
- `Generative_Equipment_Cohomological_Torsor_Obstruction_R4.md`

目标：证明对有限底空间上的一般 connected truncated nilpotent fiber，
R3 matching obstruction tower 与经典 Moore--Postnikov obstruction tower
在严格意义下自然等价。

---

## 0. 主结论与必要校正

设 \(B=|K|\) 是有限 simplicial complex 的几何实现，\(\dim K=d\)，并设

\[
p:E\longrightarrow B
\]

为 Kan/Serre fibration；其每个 fiber 是 connected nilpotent
\(n\)-type。令

\[
E_k:=\tau^{B}_{\leq k}E,
\qquad 0\leq k\leq n,
\tag{0.1}
\]

为 fiberwise Postnikov truncation。由于 fibers connected，\(E_0\simeq B\)；
由于 fibers 为 \(n\)-types，\(E_n\simeq E\)。

对底空间骨架与 fiber Postnikov stage 同时过滤，定义

\[
\mathcal S_{r,k}
:=
\Gamma(B^{(r)},E_k|_{B^{(r)}}),
\qquad
0\leq r\leq d,\qquad 0\leq k\leq n.
\tag{0.2}
\]

这形成一个双过滤截面系统：

\[
\begin{array}{ccc}
\mathcal S_{r,k} &\longrightarrow& \mathcal S_{r-1,k}\\
\downarrow &&\downarrow\\
\mathcal S_{r,k-1}&\longrightarrow&\mathcal S_{r-1,k-1}.
\end{array}
\tag{0.3}
\]

- 顶行 \(r\mapsto\mathcal S_{r,n}\) 是 R3 的 skeletal/matching tower；
- 右列 \(k\mapsto\mathcal S_{d,k}\) 是 classical fiberwise Postnikov
  lifting tower。

### 必要校正

这两个原始 towers 一般**不是逐项等价**：一个截断底空间，一个截断 fiber。
正确的自然等价是：

1. 二者是同一双过滤对象的两条边；
2. 二者的完整 branch \(\infty\)-groupoids 都自然等价于
   \(\Gamma(B,E)\)；
3. 对每个 \(k\geq2\)，R3 在 degree \(k+1\) 产生的 matching cocycle 与
   Postnikov \(k\)-invariant 给出的 obstruction 是同一个类：
   \[
   \boxed{
   [o^{\mathrm{R3}}_{k+1}(s_{k-1})]
   =
   s_{k-1}^{*}\kappa_{k+1}
   =
   o^{\mathrm{Post}}_{k+1}(s_{k-1})
   \in
   H^{k+1}(B;\Pi_k(s_{k-1})).
   }
   \tag{0.4}
   \]
4. 二者的 vanishing criterion、lift torsor、deformation groups 与全部高阶
   lift homotopy groups一致；
5. \(k=1\) 时同一结论成立于 banded nonabelian \(H^2\)；fiberwise
   nilpotence 可把该 fringe 分解成有限列阿贝尔中心扩张障碍。若还要求
   这些阿贝尔层成为常系数，则必须另加 R11 的 relative-nilpotence 假设。

这就是本文使用的“自然等价”的精确定义。它比只证明两个方法给出相同 yes/no
更强，又避免虚假的 termwise identification。

---

## 1. 模型、局部系数与相对 Postnikov 塔

### 1.1 工作范畴

可以在以下任一等价模型中工作：

1. Kan complexes over \(\operatorname{Sing}B\)；
2. compactly generated spaces over \(B\)；
3. \(\infty\)-category \(\mathcal S_{/B}\)。

为了使 functoriality 清楚，本文使用 \(\mathcal S_{/B}\) 的语言。relative
truncation

\[
\tau^B_{\leq k}:\mathcal S_{/B}\longrightarrow
(\mathcal S_{/B})_{\leq k}
\]

是 functorial reflector。因此 fiberwise Postnikov tower 不依赖任意选取的
CW model；传统模型中的选择空间在 \(\infty\)-categorical formulation 中是
可缩的。

### 1.2 相对 homotopy local systems

给定 \(E_{k-1}\) 上一点或 section branch，\(E\to B\) 的第 \(k\) 个 fiber
homotopy group 形成 local coefficient system。具体地，对 section

\[
s_{k-1}:B\longrightarrow E_{k-1},
\]

记

\[
\Pi_k(s_{k-1})
:=
s_{k-1}^{*}\pi_k(E/B).
\tag{1.1}
\]

当 \(k\geq2\) 时，这是 \(B\) 上的阿贝尔群 local system；当 \(k=1\)
时，它是群 local system/band，一般非阿贝尔。fiber 的 nilpotence 保证
每个 fiber 中的 \(\Pi_1\) 为 nilpotent group，并保证其**内在**作用具有有限
nilpotent filtration；它不自动保证来自 \(\pi_1(B)\) 的外部 monodromy
作用幂零。自然比较定理本身允许任意 twisted local systems；只有把它们
进一步细化为常系数层时，才需要 R11 的 relative nilpotence。

### 1.3 relative Postnikov stage

对 \(k\geq2\)，map

\[
q_k:E_k\longrightarrow E_{k-1}
\]

局部具有 fiber \(K(\pi_kF,k)\)，并由 twisted fiberwise \(k\)-invariant

\[
\kappa_{k+1}:
E_{k-1}\longrightarrow
K_{E_{k-1}}(\pi_k(E/B),k+1)
\tag{1.2}
\]

分类。等价地，\(E_k\) 是 (1.2) 与 fiberwise path fibration 的 homotopy
pullback。

沿 \(s_{k-1}\) 拉回得到

\[
Q_k(s_{k-1})
:=
B\times_{s_{k-1},E_{k-1}}E_k
\longrightarrow B.
\tag{1.3}
\]

这是一个 twisted \(K(\Pi_k(s_{k-1}),k)\)-torsor，其分类类为

\[
\omega_k(s_{k-1})
=
s_{k-1}^{*}\kappa_{k+1}
\in H^{k+1}(B;\Pi_k(s_{k-1})).
\tag{1.4}
\]

而 \(s_{k-1}\) 提升为 \(s_k:B\to E_k\) 的空间正是

\[
\operatorname{Lift}_k(s_{k-1})
\simeq
\Gamma(B,Q_k(s_{k-1})).
\tag{1.5}
\]

公式 (1.3)--(1.5) 是两个 obstruction towers 相遇的接口。

---

## 2. R3 tower 是底空间骨架上的截面 tower

令 \(I_K\) 为 \(K\) 的反向面范畴：\(\sigma\to\tau\) 当且仅当
\(\tau\subseteq\sigma\)。对 \(E_k\to B\) 定义局部截面图

\[
X_k(\sigma)
:=
\Gamma(|\sigma|,E_k|_{|\sigma|}).
\tag{2.1}
\]

必要时取 singular Kan complex。restriction 给出
\(X_k:I_K\to\mathcal S\)。

### 引理 2.1（matching object）

对每个 simplex \(\sigma\)，有自然等价

\[
M_\sigma X_k
\simeq
\Gamma(\partial|\sigma|,E_k|_{\partial|\sigma|}),
\tag{2.2}
\]

且 matching map 是边界 restriction

\[
\Gamma(|\sigma|,E_k)\longrightarrow
\Gamma(\partial|\sigma|,E_k).
\tag{2.3}
\]

在标准 fibrant model 中这些 maps 是 fibrations，故 \(X_k\) Reedy
fibrant。

#### 证明

proper faces 覆盖 \(\partial|\sigma|\)，兼容的 facewise sections 严格粘合成
边界截面，给出 (2.2)。由于
\(\partial\Delta^r\hookrightarrow\Delta^r\) 是 cofibration，fibrant
object 上的 relative mapping-space restriction 是 fibration。证毕。

### 引理 2.2（R3 partial limit identification）

令

\[
L_{r,k}:=lim_{\dim\sigma\leq r}X_k(\sigma).
\]

则有自然等价

\[
\boxed{
L_{r,k}simeq
\Gamma(B^{(r)},E_k|_{B^{(r)}})
=\mathcal S_{r,k}.
}
\tag{2.4}
\]

特别地，\(L_{r,n}\simeq\mathcal S_{r,n}\) 正是 R3 matching tower 的第
\(r\) 层。

#### 证明

一个极限点是每个维数至多 \(r\) 的 simplex 上的截面，并在所有 faces 上
严格相容。gluing lemma 把它唯一粘成 \(B^{(r)}\) 上的截面。该论证在全部
simplicial degrees 上自然成立。Reedy fibrancy 保证 strict limit 计算
homotopy limit。证毕。

### 推论 2.3（R3 完整 branch space）

R3 全部成功 branches 的 \(\infty\)-groupoid 为

\[
\mathcal B_{\mathrm{R3}}(p)
:=
\lim_{0\leq r\leq d}\mathcal S_{r,n}
\simeq
\Gamma(B,E).
\tag{2.5}
\]

这里极限记录一个 section 及其在所有 skeleta 上的兼容 restrictions。

---

## 3. Postnikov tower 是 fiber truncation 上的截面 tower

定义

\[
\mathcal B_{\mathrm{Post}}(p)
:=
\lim_{0\leq k\leq n}\Gamma(B,E_k).
\tag{3.1}
\]

### 引理 3.1（Postnikov branch space）

存在自然等价

\[
\boxed{
\mathcal B_{\mathrm{Post}}(p)
\simeq
\Gamma(B,E).
}
\tag{3.2}
\]

#### 证明

relative truncation tower 的顶层 \(E_n\to B\) 与 \(E\to B\) 等价，因为
fibers 是 \(n\)-types。一个 compatible Postnikov branch 是 sections

\[
s_k:B\to E_k,
\qquad q_k s_k=s_{k-1},
\]

的相容族；其最高分量 \(s_n\) 唯一决定全部较低分量。故 (3.1) 自然等价于
\(\Gamma(B,E_n)\simeq\Gamma(B,E)\)。证毕。

### 推论 3.2（完整 branch spaces 的自然等价）

组合 (2.5) 与 (3.2) 得

\[
\boxed{
\mathcal B_{\mathrm{R3}}(p)
\simeq
\Gamma(B,E)
\simeq
\mathcal B_{\mathrm{Post}}(p).
}
\tag{3.3}
\]

该等价自然于底空间的 simplicial maps、fibrations 的 maps 以及 pullback。

#### 注意 3.3

(3.3) 单独仍不足以称为 obstruction theories 等价；任何两个正确计算
\(\Gamma(B,E)\) 的方法都会满足类似结论。真正的内容是下面证明的逐 stage
obstruction、torsor 与 deformation data 的一致性。

---

## 4. 带局部系数的 R4 torsor theorem

R4 处理 constant \(A\)。一般 nilpotent fiber 要求 twisted coefficients。

设 \(\mathcal A\) 为 \(B\) 上的阿贝尔群 local system，\(k\geq1\)。令

\[
K_B(\mathcal A,k)\longrightarrow B
\]

表示对应的 fiberwise Eilenberg--Mac Lane group object。

### 定理 4.1（Twisted Cohomological Torsor Obstruction）

令 \(Q\to B\) 是一个 \(K_B(\mathcal A,k)\)-torsor，并令

\[
[Q]=\omega(Q)\in H^{k+1}(B;\mathcal A)
\tag{4.1}
\]

为其分类类。对面范畴上的局部截面图

\[
Y_Q(\sigma)=\Gamma(|\sigma|,Q|_{|\sigma|})
\]

有：

1. 每个 \(Y_Q(\sigma)\) 非空且等价于局部
   \(K(\mathcal A_\sigma,k)\)；
2. 每条 face restriction 是弱等价；
3. R3 的 degree \(k+1\) matching obstruction values 组成 twisted cocycle
   \[
   o^{\mathrm{R3}}_{k+1}(Q)
   \in Z^{k+1}(K;\mathcal A);
   \tag{4.2}
   \]
4. 该 cocycle 的 cohomology class 为
   \[
   [o^{\mathrm{R3}}_{k+1}(Q)]=\omega(Q);
   \tag{4.3}
   \]
5. 以下条件等价：
   \[
   \operatorname*{holim}_{I_K}Y_Q\neq\varnothing;
   \quad
   Q\text{ 有 section};
   \quad
   \omega(Q)=0;
   \tag{4.4}
   \]
6. 若 \(\omega(Q)=0\)，则 section space 是
   \(\Gamma(B,K_B(\mathcal A,k))\) 的 torsor；选择一个 section 后，
   \[
   \pi_q\Gamma(B,Q)
   \cong
   H^{k-q}(B;\mathcal A),
   \qquad 0\leq q\leq k,
   \tag{4.5}
   \]
   且 \(q>k\) 时为零。对 \(q=0\)，这是 torsor identification，而非
   无选择的群同构。

#### 证明

每个 simplex 可缩，所以 \(Q\) 在其上平凡；local system 在 simplex 上也
可由任一 vertex 的 fiber 平凡化。因而局部 section spaces 与 face maps 的
性质同 R4。

先在 \(k\)-skeleton 上选 section。对每个定向 \((k+1)\)-simplex
\(\sigma\)，boundary section 在局部平凡化下给出

\[
S^k\longrightarrow K(\mathcal A_\sigma,k),
\]

其 homotopy class 是 \(\mathcal A_\sigma\) 中元素。沿 faces 比较时必须用
local-system transports；带入 simplicial incidence signs 后得到 twisted
cochain (4.2)。boundary-of-boundary identity 给出 cocycle condition。

改变低阶 section 或 local trivializations 会加上 twisted coboundary。torsor
由 map

\[
B\longrightarrow K_B(\mathcal A,k+1)
\]

分类，而上述 cellular cocycle正是该 map 对 universal class 的 pullback，
所以得到 (4.3)。torsor 有 section 当且仅当平凡，故得到 (4.4)。

若选定 section，pointwise group action 把 \(Q\) 的 section space 识别为
\(\Gamma(B,K_B(\mathcal A,k))\) 的 torsor。fiberwise Eilenberg--Mac Lane
representability 给出 (4.5)。证毕。

### 注 4.2（R4 是 constant-coefficient 特例）

当 \(\mathcal A=\underline A\) 时，定理 4.1 完全恢复 R4；Hopf 例对应
\(k=1,\mathcal A=\underline{\mathbb Z}\)。

---

## 5. 逐 Postnikov stage 的核心比较

固定 \(k\geq2\)，并假设已经得到一个 Postnikov branch

\[
s_{k-1}:B\longrightarrow E_{k-1}.
\]

令 \(Q_k(s_{k-1})\) 如 (1.3)，并令

\[
\mathcal A_k:=\Pi_k(s_{k-1}).
\]

### 引理 5.1（第 \(k+1\) 层 matching obstruction 的 truncation invariance）

设先前 stages 已成功，并把一个 \(E\)-section branch 构造到
\(B^{(k)}\)。将它投影到 \(E_k\)，再视为 pulled-back torsor
\(Q_k(s_{k-1})\) 的 partial section。则对每个 \((k+1)\)-simplex，原始
\(E\)-diagram 的 R3 component obstruction 与 \(Q_k(s_{k-1})\) 的 R3
component obstruction 在

\[
\pi_k(F)\xrightarrow{\cong}\pi_k(P_kF)
\]

下相同。反之，torsor 的任意 \(k\)-skeletal branch 都可提升为原始
\(E\)-diagram 的 \(k\)-skeletal branch，且该提升不改变 degree
\(k+1\) obstruction。

#### 证明

在一个 \((k+1)\)-simplex 上，matching obstruction 只读取 boundary map

\[
S^k\longrightarrow F
\]

的 \(\pi_k(F)\)-class。truncation map \(F\to P_kF\) 在 \(\pi_i\)、
\(i\leq k\) 上为同构，所以该 class 与其 truncated image 完全相同。

另一方面，\(F\to P_kF\) 的 homotopy fiber 是 \(k\)-connected。把一个
\(P_kF\)-valued section 从不超过 \(k\) 维的 complex 提升到 \(F\) 的所有
obstructions 均落在该 homotopy fiber 的 \(\pi_i\)、\(i<k\) 中，故消失。
因此 \(k\)-skeletal branches 可提升；不同提升在下一层产生的
\(\pi_k\)-class 仍由上述同构识别。证毕。

### 定理 5.2（Stagewise R3--Postnikov Obstruction Identity）

R3 应用于 \(Q_k(s_{k-1})\) 的 local section diagram 时，其 degree
\(k+1\) matching obstruction cocycle 与 classical Postnikov lifting
obstruction 满足

\[
\boxed{
[o^{\mathrm{R3}}_{k+1}(s_{k-1})]
=
s_{k-1}^{*}\kappa_{k+1}
=
o^{\mathrm{Post}}_{k+1}(s_{k-1})
\in
H^{k+1}(B;\mathcal A_k).
}
\tag{5.1}
\]

并且以下数据自然一致：

1. obstruction 的消失；
2. \(s_{k-1}\) 到 \(E_k\) 的 lifts 的 components；
3. lift components 上的 \(H^k(B;\mathcal A_k)\)-torsor action；
4. lift space 的 higher homotopy groups
   \[
   \pi_q\operatorname{Lift}_k(s_{k-1})
   \cong
   H^{k-q}(B;\mathcal A_k),
   \qquad 1\leq q\leq k.
   \tag{5.2}
   \]

#### 证明

relative Postnikov construction 把 \(E_k\to E_{k-1}\) 表示为
\(\kappa_{k+1}\) 与 universal path fibration 的 homotopy pullback。沿
\(s_{k-1}\) 拉回后，\(Q_k(s_{k-1})\to B\) 因而是由 map

\[
s_{k-1}^{*}\kappa_{k+1}:
B\longrightarrow K_B(\mathcal A_k,k+1)
\]

分类的 \(K_B(\mathcal A_k,k)\)-torsor。这证明其 torsor class 等于中间项。

另一方面，\(s_{k-1}\) 的 lift 正是该 torsor 的 section，见 (1.5)。应用
定理 4.1，R3 degree \(k+1\) matching cocycle 的类等于同一个 torsor
class。这给出 (5.1)。

由引理 5.1，这也是原始 \(E\)-diagram 的 degree \(k+1\) matching
obstruction，而不只是 auxiliary torsor diagram 的障碍。更直接地，在一个
\((k+1)\)-simplex \(\sigma\) 上，两种构造都做同一件事：
把 boundary lift 看作

\[
S^k\longrightarrow K(\mathcal A_{k,\sigma},k)
\]

并读取其 \(\pi_k\)-class。采用同一 orientation 与 transport convention
后，Postnikov 语言称其为 pulled-back
\(k\)-invariant 的 cellular value；R3 语言称其为 matching datum 是否落入
restriction map 的 image。两者在 cochain level 已相同，而不只是同类。
逐 simplex 可写成

\[
o^{\mathrm{R3}}_{k+1}(s_{k-1})(\sigma)
=
\left\langle
s_{k-1}^{*}\kappa_{k+1},
[\sigma,\partial\sigma]
\right\rangle,
\tag{5.2a}
\]

其中 pairing 使用 \(\mathcal A_k\) 的平行移动。若采用相反的统一 cellular
boundary convention，两边同时乘同一 universal sign，不影响自然比较。

若该类消失，定理 4.1 将 lift space 识别为
\(\Gamma(B,K_B(\mathcal A_k,k))\)-torsor，于是 components、torsor
action 与 (5.2) 同时得到。所有 construction 均由 pullback、relative
truncation 与 restriction 给出，故自然。证毕。

### 推论 5.3（cochain adjustment 完全相同）

若选择的 degree \(k+1\) matching cocycle 为

\[
o\in Z^{k+1}(K;\mathcal A_k),
\]

则修改 \(k\)-skeleton lift by

\[
b\in C^k(K;\mathcal A_k)
\]

在 R3 与 Postnikov 两种语言中都把 obstruction 改为

\[
o\longmapsto o+\delta b.
\tag{5.3}
\]

所以“存在某条 successful R3 branch”与“Postnikov obstruction class 为零”
是同一个必要充分条件，而不只是两个独立充分条件。

---

## 6. 非阿贝尔 \(k=1\) fringe

connected nilpotent fiber 的 \(\pi_1\) 可以非阿贝尔，因此不能把第一层强行
写成普通阿贝尔群值 \(H^2(B;\Pi_1)\)。

令

\[
q_1:E_1\longrightarrow E_0\simeq B
\]

为 relative \(1\)-type stage。其 fiber 是 \(K(\Pi_1,1)\)，连同 monodromy
形成一个 banded gerbe-type lifting problem。

### 定理 6.1（Nonabelian First-Stage Comparison）

R3 在 degree \(2\) 的 matching data 形成一个 banded nonabelian
2-cocycle；其 class

\[
o_2^{\mathrm{R3}}
\in
\mathbf H^2(B;\Pi_1)
\tag{6.1}
\]

正是 Postnikov \(1\)-stage 的 gerbe/lifting class

\[
o_2^{\mathrm{Post}}.
\]

该 pointed nonabelian class 为 basepoint 当且仅当 \(E_1\to B\) 有 section。
若 class 消失，section groupoid 是 \(\Pi_1\)-torsor groupoid 的
pseudo-torsor；其 components 受 pointed nonabelian
\(\mathbf H^1(B;\Pi_1)\) 作用。这里不把 \(\mathbf H^1\) 错称为群。

#### 证明

在 vertices 上选局部 lifts，在 edges 上选 transports。对每个定向
2-simplex，三条 edge transports 的 composite 与直接 transport 的差给出
\(\Pi_1\) 中元素；face changes 按 conjugation/transport 作用。R3 matching
要求这个 boundary loop 在 \(K(\Pi_1,1)\) 中可填充，恰要求该元素为单位。

这些 triangle values 与 transports 组成标准 banded nonabelian 2-cocycle。
另一方面，\(E_1\to B\) 的 descent data 产生完全相同的 edge transports 与
triangle associativity defect；这正是 classical first Postnikov lifting gerbe。
因此两者 cocycles 相同，改变局部 lifts 给出相同 coboundary/conjugacy
relation。零类等价于 descent data 可严格化为全局 section。证毕。

### 推论 6.2（nilpotent central refinement）

若 \(G=\Pi_1\) 的 nilpotency class 为 \(c\)，其 characteristic lower central
series

\[
G=G_1\supseteq G_2\supseteq\cdots\supseteq G_{c+1}=1
\]

被所有 monodromy automorphisms 保持。令

\[
A_j:=G_j/G_{j+1}.
\]

则 first-stage nonabelian lifting problem 可细化为有限列 central extension
lifting problems。每一步的 obstruction 是依赖先前 branch 的 twisted class

\[
o_{2,j}\in H^2(B;\mathcal A_j),
\tag{6.2}
\]

而 lift choices 形成 \(H^1(B;\mathcal A_j)\)-torsor。R3 的 triangle
matching defects 投影到 \(A_j\) 后，逐项等于这些 central Postnikov
obstructions。

#### 证明

lower central quotients \(A_j\) 在 \(G/G_{j+1}\) 中为 central abelian
subgroups，故每个

\[
1\to A_j\to G/G_{j+1}\to G/G_j\to1
\]

给出 central lifting problem。对 R3 triangle cocycle 逐商投影，得到其
阿贝尔 obstruction cocycle；central extension 的 standard lifting formula
给出同一个 cocycle。有限归纳得到结论。证毕。

因此一般 nilpotent \(\pi_1\) 没有被排除；只是第一层必须保留非阿贝尔
fringe，或使用其有限 central refinement，不能伪装成单个阿贝尔群。

---

## 7. 完整自然比较定理

### 定义 7.1（obstruction towers 的自然等价）

称两个 section obstruction towers 自然等价，如果：

1. 它们的 complete branch \(\infty\)-groupoids 自然等价；
2. 每一级 coefficient local systems/crossed data 自然对应；
3. 对应下 obstruction classes 相同；
4. obstruction 消失后的 lift spaces 连同 torsor action 与 higher homotopy
   groups 自然等价。

该定义不要求两个不同 filtration 的原始 stage spaces 逐项相等。

### 定理 7.2（R3--Postnikov Natural Comparison Theorem）

令 \(p:E\to B=|K|\) 为有限 simplicial base 上的 fibration，fibers 为
connected nilpotent \(n\)-types。则 R3 matching obstruction tower 与
fiberwise Moore--Postnikov obstruction tower 在定义 7.1 的意义下自然等价。

更明确地：

1. 二者完整 branch spaces 均自然等价于 \(\Gamma(B,E)\)：
   \[
   \mathcal B_{\mathrm{R3}}(p)
   \simeq
   \Gamma(B,E)
   \simeq
   \mathcal B_{\mathrm{Post}}(p);
   \tag{7.1}
   \]
2. \(k=1\) 的 degree-2 R3 obstruction 等于 banded nonabelian first
   Postnikov obstruction；
3. 对每个 \(2\leq k\leq n\)，degree \(k+1\) R3 obstruction 等于
   \[
   s_{k-1}^{*}\kappa_{k+1}
   \in H^{k+1}(B;\Pi_k(s_{k-1}));
   \tag{7.2}
   \]
4. 全局 section 存在，当且仅当存在一条 successive branch，使 first
   nonabelian class 及所有后续 classes (7.2) 依次消失；
5. 在每个成功 stage，两个 theories 给出相同的 lift torsor 与 deformation
   groups；
6. 该比较自然于 pullback square
   \[
   \begin{array}{ccc}
   E'&\longrightarrow&E\\
   \downarrow&&\downarrow\\
   B'&\longrightarrow&B
   \end{array}
   \]
   以及 preserving-fiber maps of fibrations。

#### 证明

第 1 项是推论 3.2。第 2 项是定理 6.1。对 \(k\geq2\)，给定已成功的
\((k-1)\)-stage branch，定理 5.2 将 Postnikov lifting problem 识别为一个
twisted \(K(\Pi_k,k)\)-torsor，并证明其 R3 matching class 与 pulled-back
\(k\)-invariant 相同。这证明第 3 与第 5 项。

从 \(E_0\simeq B\) 的 canonical section 开始，先解决 nonabelian first
 stage，再对 \(k=2,\ldots,n\) 归纳使用定理 5.2。所有 obstruction 消失时
得到 \(s_n:B\to E_n\simeq E\)，即全局 section。反之全局 section 投影到
每个 \(E_k\)，给出一条所有 classes 均为零的 branch。这证明第 4 项。

relative truncation、homotopy pullback、local section restriction、
homotopy-group local systems 与 cohomology pullback 都是 functorial 的。
因此比较与 pullback 及 maps of fibrations 相容，证明第 6 项。证毕。

### 推论 7.3（R3 是 Postnikov tower 的 cellular resolution）

Postnikov tower 在 stage \(k\) 输出一个 global class

\[
o_{k+1}\in H^{k+1}(B;\Pi_k).
\]

R3 matching tower 给出它的逐 simplex representative

\[
\sigma^{k+1}longmapsto
o_{k+1,\sigma}^{\mathrm{match}}in(\Pi_k)_\sigma.
\]

因此两者关系不是“竞争的两套障碍理论”，而是：

\[
\boxed{
\text{R3 matching tower}
=
\text{Postnikov obstruction tower 的 cellular/Reedy resolution}.
}
\tag{7.3}
\]

Postnikov theory 给出 invariant cohomology class；R3 额外给出该类在哪些 cells
首次显现以及哪些 partial branches 导致失败。

---

## 8. 有限终止、完整递归与算法条件

### 定理 8.1（Finite Structural Completeness）

若 \(\dim B=d\)，fiber 为 nilpotent \(n\)-type，则 section existence 只需
处理

\[
k+1\leq d,
\qquad
k\leq n.
\]

亦即至多

\[
1\leq k\leq\min\{n,d-1\}
\tag{8.1}
\]

的 obstruction stages。更高 \(H^{k+1}\) 因维数自动消失。所有这些 classes
沿某条 successive branch 消失，当且仅当 \(p\) 有 section。

#### 证明

定理 7.2 给出必要充分的 successive obstruction list。有限
\(d\)-complex 上任意 local system 的 cellular cochain groups 在次数
\(>d\) 为零，故相应 cohomology groups 消失。fiber 在 \(n\) 后没有新的
homotopy groups。证毕。

### 有限递归 8.2

对具体 finite sector：

1. 构造 relative Postnikov stages \(E_k\to E_{k-1}\)；
2. 处理 \(\Pi_1\) 的 banded nonabelian 2-cocycle；若需要，用 lower central
   series 分解；
3. 给定成功 \(s_{k-1}\)，计算 local system
   \(\Pi_k(s_{k-1})\)；
4. 在每个 \((k+1)\)-simplex 上计算 R3 boundary matching class；
5. 组成 twisted cocycle
   \[
   o_{k+1}^{\mathrm{R3}}\in Z^{k+1}(K;\Pi_k);
   \]
6. 取其 cohomology class；若非零则该 branch 失败；
7. 若为零，解
   \[
   \delta b=-o_{k+1}
   \]
   并用 \(b\) 修改 \(k\)-skeleton lifts；
8. 记录 lift ambiguity
   \(H^k(B;\Pi_k)\) 与 higher deformation groups
   \(H^{k-q}(B;\Pi_k)\)；
9. 迭代至 \(k=\min\{n,d-1\}\)。

这是一套有限、完整且 branch-sensitive 的 simultaneous-effectivity
递归。只有当各 Postnikov 数据、局部系数上同调和 Coupl 零点问题带有
有效表示并可计算时，它才升级为算法；有限层数本身不蕴含可判定性。

---

## 9. 压力测试与边界

### 9.1 单层 Eilenberg--Mac Lane fiber

若 fiber 只有 \(\pi_n=A\) 非零，则 Postnikov tower 只有一个非平凡 stage。
定理 7.2 退化为 R4：

\[
o_{n+1}^{\mathrm{R3}}
=
\kappa_{n+1}
\in H^{n+1}(B;\mathcal A).
\]

通过。

### 9.2 Hopf bundle

fiber \(S^1=K(\mathbb Z,1)\)；第一 fringe 已阿贝尔。degree-2 matching
cocycle 等于

\[
c_1\in H^2(S^2;\mathbb Z),
\]

恢复 R4 的显式二维失败。通过。

### 9.3 simple two-stage fiber

若 \(F\) 只有 \(\pi_a=A\)、\(\pi_b=C\) 非零，\(a<b\)，且 actions 平凡，
则递归先处理

\[
o_{a+1}\in H^{a+1}(B;A),
\]

选定 lift 后再处理由 \(k\)-invariant pullback 产生的

\[
o_{b+1}\in H^{b+1}(B;C).
\]

第二类依赖第一阶段 branch；R3 同样通过 matching data 对该依赖进行 transport。
没有把两个 classes 错误地视为彼此独立。通过。

### 9.4 非阿贝尔 nilpotent \(\pi_1\)

若 \(\pi_1=G\) 非阿贝尔，直接写
\(H^2(B;G)\) 为阿贝尔群是错误的。定理 6.1 保留 banded nonabelian
pointed set，推论 6.2 才在 lower central quotients 上产生普通 twisted
cohomology groups。边界通过。

### 9.5 原始 stage spaces 不逐项相等

例如 \(B=S^r\) 且 fiber 有高于 \(r\) 的 homotopy groups 时，
\(\Gamma(B^{(r)},E)\) 的 higher homotopy 仍能看到这些群，而低 Postnikov
truncation 看不到。因此不能声称

\[
\mathcal S_{r,n}\simeq\mathcal S_{d,r}
\]

之类的 termwise equivalence。本文只声称并证明定义 7.1 的 obstruction
equivalence。边界通过。

---

## 10. 新颖性边界与理论意义

### 10.1 标准背景

以下是经典工具，本报告不宣称其本身为新发现：

1. cellular obstruction cocycle 与 deformation cochain；
2. Moore--Postnikov tower 与 \(k\)-invariants；
3. twisted Eilenberg--Mac Lane objects 表示 local-coefficient cohomology；
4. nilpotent spaces admit principal/central refinements of Postnikov towers；
5. section/lifting spaces of a trivialized \(K(\mathcal A,k)\)-torsor 由
   cohomology groups计算。

### 10.2 本报告完成的 derived-theory 推进

1. 构造统一双过滤系统 \(\mathcal S_{r,k}\)，精确定位两座 towers 的关系；
2. 证明 R3 matching cocycle 在 cochain level 等于 pulled-back Postnikov
   \(k\)-invariant；
3. 证明 complete branches、vanishing、lift torsors 与 higher deformations
   全部自然一致；
4. 把 R4 constant torsor theorem 推广到 twisted local coefficients；
5. 严格处理一般 nilpotent \(\pi_1\) 的 nonabelian fringe；
6. 得到一般 finite-dimensional truncated nilpotent effectivity 的有限完整
   obstruction recursion；其算法性需要额外有效性假设。

这使 R3 不再只是与经典 obstruction theory “相似”：它被证明为后者的
cellular/Reedy resolution，并额外保留 failure localization 信息。

---

## 11. 对 Frozen v1.0 的影响

无需修改 Frozen v1.0。R5 是 derived layer 中的 comparison theorem：

\[
\boxed{
\begin{array}{c}
\text{Frozen comparison/effectivity fiber}\\
\Downarrow\\
\text{R3 Reedy matching tower}\\
\Updownarrow\ \text{R5}\\
\text{fiberwise Postnikov obstruction tower}\\
\Downarrow\\
\text{twisted cohomology classes and lift torsors}.
\end{array}
}
\]

它说明 R3 的新增价值不在于替代 Postnikov theory，而在于把 global
\(k\)-invariants 解析为 branch-sensitive local matching failures，并统一接回
simultaneous effectivity 接口。

---

## 12. 标准背景来源

1. J. P. May, *A Concise Course in Algebraic Topology*，cellular obstruction
   cocycles、deformation cochains 与 \(H^{k+1}(-;\pi_k)\) 判据。
2. J. P. May, *A Concise Course in Algebraic Topology*，Postnikov systems 与
   \(k\)-invariants。
3. J. P. May and K. Ponto, *More Concise Algebraic Topology*，nilpotent spaces
   的 Postnikov \(\mathcal A\)-towers、central refinements 与 functoriality。
4. J. P. May and J. Sigurdsson, *Parametrized Homotopy Theory*，fiberwise
   homotopy objects 与 parametrized/fiberwise constructions。
5. A. K. Bousfield and D. M. Kan,
   *Homotopy Limits, Completions and Localizations*，homotopy limits 与
   Postnikov/derived-limit machinery。

---

## 13. 最终判定

\[
\boxed{
\begin{array}{rcl}
\text{raw towers termwise equivalent}
&=&\text{FALSE IN GENERAL},\\[1mm]
\text{common bifiltration}
&=&\mathcal S_{r,k}=\Gamma(B^{(r)},P_k^BE),\\[1mm]
\text{complete branch spaces}
&\simeq&\Gamma(B,E),\\[1mm]
\text{R3 obstruction cocycle}
&=&\text{pulled-back Postnikov }k\text{-invariant},\\[1mm]
\text{abelian stages}
&=&H^{k+1}(B;\Pi_k),\\[1mm]
\text{first nonabelian stage}
&=&\mathbf H^2(B;\Pi_1),\\[1mm]
\text{lift ambiguity}
&=&H^k(B;\Pi_k)\text{-torsor},\\[1mm]
\text{finite completeness}
&=&k\leq\min\{n,d-1\},\\[1mm]
\text{Frozen v1.0}
&=&\text{UNCHANGED}.
\end{array}
}
\]

因此，在数学上正确的强形式已经证明：对一般 connected truncated
nilpotent fiber，R3 matching tower 与 classical Postnikov obstruction tower
具有自然等价的 obstruction data；R3 正是 Postnikov tower 的
cellular/Reedy resolution。
