# 数学内生生成性理论

## Cohomological Torsor Obstruction Theorem R4

日期：2026-09-28  
逻辑地位：Frozen v1.0 的派生 sector theorem；不修改冻结核心  
直接前置：`Generative_Equipment_Effectivity_Obstruction_Program_R3.md`  
研究目标：在有限二维 poset 与低 Postnikov 空间中，构造首个显式非零
\(R^2\!\lim\) 存在障碍，并把 R3 的逐层 component obstruction 提升为
与选择无关的完整上同调类。

---

## 0. 决定性结论

令 \(I\) 为有限逆范畴，\(A\) 为阿贝尔群，\(G=K(A,n)\)；考虑
所有由 \(G\)-主丛产生的 locally constant \(G\)-torsor 型空间图。则其
等价类由

\[
\boxed{
\pi_0\operatorname{Tor}_{K(A,n)}(I)
\cong
H^{n+1}(N I;A)
\cong
R^{n+1}\!\lim_I\underline A
}
\tag{0.1}
\]

这里 \(\operatorname{Tor}_G(I)\) 表示 \(|NI|\) 上 principal
\(G\)-bundles（等价地，其 unstraightening 为 principal \(G\)-bundle 的
locally constant torsor diagrams）所成的 \(\infty\)-groupoid。

分类。对相应图 \(X_\omega:I\to\mathcal S\)，有精确判据

\[
\boxed{
\operatorname*{holim}_I X_\omega\neq\varnothing
\quad\Longleftrightarrow\quad
\omega=0.
}
\tag{0.2}
\]

因此在这个 sector 中，\(R^{n+1}\!\lim\) 不再只是在已有 branch 之后
计算 deformation 的谱序列项；它直接承载一个**无基点的存在性障碍**。

当 \(I\) 是三角剖分 \(S^2=\partial\Delta^3\) 的反向面范畴、
\(A=\mathbb Z,n=1\) 时，Hopf 主 \(S^1\)-丛给出

\[
R^2\!\lim_I\underline{\mathbb Z}
\cong H^2(S^2;\mathbb Z)
\cong\mathbb Z,
\qquad
\omega=1.
\tag{0.3}
\]

所得有限逆图满足：

1. 每个局部 realization space 都非空且弱等价于 \(S^1\)；
2. 每条 transition map 都是弱等价；
3. 全局 homotopy limit 为空。

这给出一个尖锐的 no-go：即使没有 automorphisms、所有局部对象非空、所有
一阶 transition 都是等价，仍不能推出 simultaneous effectivity。真正缺少的
是二维 coherence，其精确值就是第一 Chern 类。

---

## 1. 为什么 R3 的下一步不应先追逐非零 \(d_2\)

R3 已严格区分：

- matching calculus 负责判断全局 branch 是否存在；
- Bousfield--Kan 谱序列只在选定 branch 后计算其高阶变形。

非零

\[
d_2:E_2^{0,t}\longrightarrow E_2^{2,t+1}
\]

当然有价值，但它属于第二层，不能解释 homotopy limit 本身为空的情形。
二维 sector 的第一个必要突破应当是一个不预设全局基点的群值障碍。

本报告表明：对 \(K(A,n)\)-torsor，这个障碍天然存在，而且恰为

\[
\omega\in H^{n+1}(NI;A)=R^{n+1}\!\lim_I\underline A.
\]

它把 R3 中依赖所选低阶 branch 的 component-membership tests 商去选择依赖，
得到一个规范的完整 obstruction class。

---

## 2. 面范畴与局部截面图

### 定义 2.1（反向面范畴）

令 \(K\) 为有限 simplicial complex。定义 \(I_K\) 的对象为 \(K\) 的非空
单形，并规定

\[
\sigma\longrightarrow\tau
\quad\Longleftrightarrow\quad
\tau\subseteq\sigma.
\]

取 degree \(|\sigma|=\dim\sigma\)。每个非恒等 morphism 严格降 degree，
所以 \(I_K\) 是有限逆范畴。其 nerve 的几何实现是 \(|K|\) 的重心细分：

\[
|N(I_K)|\cong|\operatorname{sd}K|\cong|K|.
\tag{2.1}
\]

### 定义 2.2（局部截面图）

令 \(G\) 为具有 CW 型的拓扑群，令

\[
p:P\longrightarrow |K|
\]

为 principal \(G\)-bundle。对每个非空单形 \(\sigma\)，置

\[
X_P(\sigma)
:=
\operatorname{Sing}\Gamma(|\sigma|,P|_{|\sigma|}),
\tag{2.2}
\]

即限制丛在该单形上的截面空间的 singular Kan complex。若
\(\tau\subseteq\sigma\)，以 restriction 定义

\[
X_P(\sigma)\longrightarrow X_P(\tau).
\]

由此得到严格图

\[
X_P:I_K\longrightarrow\mathsf{sSet}_{\mathrm{Kan}}.
\]

### 引理 2.3（局部对象与一阶 transition 都看不见扭曲）

对每个 \(\sigma\in I_K\)：

\[
X_P(\sigma)\simeq G.
\tag{2.3}
\]

对每个面包含 \(\tau\subseteq\sigma\)，restriction map

\[
X_P(\sigma)\longrightarrow X_P(\tau)
\tag{2.4}
\]

是弱同伦等价。特别地，若 \(G\neq\varnothing\)，则每个局部 realization
space 非空，且任意单箭头检查均无法发现全局扭曲。

#### 证明

每个闭单形 \(|\sigma|\) 可缩，故主丛限制 \(P|_{|\sigma|}\) 平凡。选定一个
局部截面后，截面空间成为

\[
\Gamma(|\sigma|,P|_{|\sigma|})
\cong
\operatorname{Map}(|\sigma|,G),
\]

而 evaluation at a vertex 是到 \(G\) 的同伦等价，得到 (2.3)。面包含
\(|\tau|\hookrightarrow|\sigma|\) 是两个非空可缩 CW 复形之间的同伦等价；
mapping-space contravariance 把它送到弱等价。不同局部平凡化只改变上述
识别，不改变结论。证毕。

### 引理 2.4（matching object 就是边界截面空间）

对 \(k\)-单形 \(\sigma\)，R3 的 matching object 自然同构于

\[
M_\sigma X_P
\cong
\operatorname{Sing}\Gamma(\partial|\sigma|,P|_{\partial|\sigma|}),
\tag{2.5}
\]

且 matching map 是通常的边界 restriction：

\[
m_\sigma:
\Gamma(|\sigma|,P)longrightarrow
\Gamma(\partial|\sigma|,P).
\tag{2.6}
\]

在标准 fibrant bundle model 中，\(m_\sigma\) 是 Kan fibration。因此
\(X_P\) 是 Reedy fibrant。

#### 证明

proper faces 覆盖 \(\partial|\sigma|\)。在交面上严格相容的一族截面唯一
粘合成边界截面，所以 matching limit 给出 (2.5)。face inclusion
\(\partial\Delta^k\hookrightarrow\Delta^k\) 是 cofibration；在 slice model
或等价的 section-space model 中，沿 cofibration 的 mapping-space restriction
对 fibrant bundle 是 fibration。取 singular complex 后得到 Kan fibration。
证毕。

### 引理 2.5（全局极限就是全局截面空间）

存在自然弱等价

\[
\boxed{
\operatorname*{holim}_{I_K}X_P
\simeq
\lim_{I_K}X_P
\cong
\operatorname{Sing}\Gamma(|K|,P).
}
\tag{2.7}
\]

#### 证明

由引理 2.4，\(X_P\) Reedy fibrant，所以 R3 推论 2.6 给出
\(\operatorname{holim}X_P\simeq\lim X_P\)。极限的一个点是在每个单形上
选取截面，并要求其在所有面上严格相等。有限 simplicial complex 的 gluing
lemma 将这种数据唯一粘成全局截面；反向限制显然给出兼容局部族。该对应在
simplicial mapping spaces 的每一维成立，得到 (2.7)。证毕。

---

## 3. Cohomological Torsor Obstruction Theorem

固定阿贝尔群 \(A\) 与 \(n\geq0\)。取一个拓扑阿贝尔群模型

\[
G=K(A,n),
\qquad
BG\simeq K(A,n+1).
\]

一个 principal \(G\)-bundle \(P\to|K|\) 由 classifying map

\[
c_P:|K|\longrightarrow BG\simeq K(A,n+1)
\]

分类。记其分类类为

\[
\omega(P):=c_P^*(\iota)\in H^{n+1}(|K|;A),
\tag{3.1}
\]

其中 \(\iota\) 是 \(K(A,n+1)\) 的 universal class。

### 定理 3.1（完整的无基点存在障碍）

对上述 \(P\) 与局部截面图 \(X_P\)，以下条件等价：

1. \(\operatorname*{holim}_{I_K}X_P\neq\varnothing\)；
2. \(P\to|K|\) 有全局截面；
3. \(P\) 是平凡 principal \(G\)-bundle；
4. \(c_P\) 零伦；
5. \(\omega(P)=0\in H^{n+1}(|K|;A)\)。

因此

\[
\boxed{
\operatorname*{holim}_{I_K}X_P\neq\varnothing
\iff
\omega(P)=0.
}
\tag{3.2}
\]

#### 证明

(1) 与 (2) 由引理 2.5 等价。principal bundle 的一个截面 \(s\) 给出

\[
|K|\times G\longrightarrow P,
\qquad
(x,g)\longmapsto s(x)g,
\]

这是 bundle isomorphism；反之平凡丛有单位截面，故 (2) 与 (3) 等价。
主丛分类定理给出 (3) 与 (4) 等价。最后

\[
[|K|,K(A,n+1)]\cong H^{n+1}(|K|;A),
\]

并且该同构把 \([c_P]\) 送到 \(\omega(P)\)，所以 (4) 与 (5) 等价。
证毕。

### 定理 3.2（R3 matching profile 组成 characteristic cocycle）

设 \(n\geq1\)。任取 \(P\) 在 \(n\)-骨架 \(|K^{(n)}|\) 上的截面
\(s^{(n)}\)。对每个定向 \((n+1)\)-单形 \(\sigma\)，在
\(P|_{|\sigma|}\) 的任一平凡化下，边界截面给出映射

\[
s^{(n)}|_{\partial\sigma}:S^n\longrightarrow K(A,n).
\]

记其同伦类为

\[
o_\sigma(s^{(n)})
\in
\pi_nK(A,n)\cong A.
\tag{3.3}
\]

则：

1. \(o_\sigma=0\) 当且仅当 R3 在对象 \(\sigma\) 的 matching
   component obstruction 消失；
2. \(o(s^{(n)})=(o_\sigma)_\sigma\) 是 cellular/simplicial
   \((n+1)\)-cocycle；
3. 改变 \(n\)-骨架截面或局部平凡化，只把 \(o\) 改变一个 coboundary；
4. 其上同调类精确等于主丛分类类：
   \[
   [o(s^{(n)})]=\omega(P)\in H^{n+1}(|K|;A);
   \tag{3.4}
   \]
5. 因而存在某条 R3 branch 穿过全部 \((n+1)\)-单形，当且仅当
   \(\omega(P)=0\)。

#### 证明

由于 \(P|_{|\sigma|}\) 平凡，matching map 在所选平凡化下为

\[
\operatorname{Map}(D^{n+1},G)
\longrightarrow
\operatorname{Map}(S^n,G).
\]

其像恰是 null-homotopic component，所以边界 datum 可提升当且仅当
\([s^{(n)}|_{\partial\sigma}]=0\in\pi_nG=A\)。这证明第 1 项。

从 obstruction theory 看，在 \(n\)-骨架上选截面等价于在该骨架上选取
classifying map \(c_P\) 的零伦。将此零伦越过一个 \((n+1)\)-单形的障碍
正是 (3.3)。对所有 \((n+1)\)-单形收集这些障碍得到 primary obstruction
cocycle；改变低阶零伦使它改变一个 coboundary。由于
\(BG=K(A,n+1)\)，该 primary obstruction 正是 \(c_P\) 拉回的 universal
class，故得到 (3.4)。这同时证明第 2--4 项。

若 \(\omega(P)=0\)，可调整 \(n\)-骨架截面使 obstruction cocycle 逐单形
为零，故穿过全部 \((n+1)\)-单形。更高维 extension obstruction 位于
\(\pi_{k-1}G\)，\(k>n+1\)，而这些群均为零。反之成功的全局 branch 给出
全局截面，由定理 3.1 得 \(\omega(P)=0\)。证毕。

### 推论 3.3（首次可能失败层恰为 \(n+1\)）

对 \(K(A,n)\)-torsor sector：

- 在每个 degree \(k\leq n\)，matching component obstruction 自动消失；
- degree \(n+1\) 的障碍值在 \(A\) 中，并组成 \(\omega(P)\)；
- 一旦 \(\omega(P)=0\) 并穿过 degree \(n+1\)，以后不再有存在障碍。

因此非平凡 torsor 的 effectivity obstruction height 精确为

\[
\boxed{h_{\mathrm{eff}}(P)=n+1.}
\tag{3.5}
\]

#### 证明

在一个 \(k\)-单形上，边界 extension obstruction 属于
\(\pi_{k-1}K(A,n)\)。该群只在 \(k-1=n\) 时非零。结合定理 3.2 即得。
证毕。

### 定理 3.4（有效时的全部 realization homotopy type）

若 \(\omega(P)=0\)，则选择任一全局截面 \(s\) 后有自然于该选择的
torsor identification

\[
\operatorname*{holim}_{I_K}X_P
\simeq
\operatorname{Map}(|K|,K(A,n)).
\tag{3.6}
\]

特别地，对 \(0\leq q\leq n\)，

\[
\pi_q\operatorname*{holim}_{I_K}X_P
\cong
H^{n-q}(|K|;A),
\tag{3.7}
\]

而 \(q>n\) 时该 homotopy group 为零。对 \(q=0\)，(3.7) 表示
realization components 构成 \(H^n(|K|;A)\)-torsor；只有在选择 \(s\) 后
才把它识别成群本身。

#### 证明

全局截面平凡化 \(P\)，且 principal action 给出截面空间与
\(\operatorname{Map}(|K|,G)\) 的等价。再利用

\[
\pi_q\operatorname{Map}(|K|,K(A,n))
\cong
[S^q\wedge |K|_+,K(A,n)]
\cong
H^{n-q}(|K|;A)
\]

得到结论。证毕。

---

## 4. 与 derived limit 的精确接口

### 命题 4.1（constant coefficient derived limits）

对反向面范畴 \(I_K\) 与常值 coefficient diagram
\(\underline A:I_K\to\mathsf{Ab}\)，有自然同构

\[
R^s\!\lim_{I_K}\underline A
\cong
H^s(NI_K;A)
\cong
H^s(|K|;A).
\tag{4.1}
\]

#### 证明

R3 定理 4.2 使用的 normalized cosimplicial replacement 在常值系数下正是
nerve \(NI_K\) 的 normalized cochain complex。再由 (2.1) 得到第二个
同构。证毕。

### 定理 4.2（torsor 分类即 unpointed derived-limit obstruction）

principal \(K(A,n)\)-torsor diagrams 的等价类与

\[
R^{n+1}\!\lim_{I_K}\underline A
\]

自然双射；在该双射下，零元恰对应 simultaneously effective diagrams。
换言之，存在性判据为

\[
\boxed{
X_P\text{ simultaneously effective}
\iff
[X_P]=0\in R^{n+1}\!\lim_{I_K}\underline A.
}
\tag{4.2}
\]

#### 证明

主 \(K(A,n)\)-丛由

\[
[|K|,BK(A,n)]
\cong
[|K|,K(A,n+1)]
\cong
H^{n+1}(|K|;A)
\]

分类。应用命题 4.1，并用定理 3.1 识别零类与全局截面的存在性。证毕。

### 命题 4.3（任意有限逆范畴的形式）

令 \(I\) 为任意有限逆范畴。把 principal \(K(A,n)\)-torsor diagram
定义为 \(NI\) 上 principal \(K(A,n)\)-bundle 的 straightening。则

\[
\pi_0\operatorname{Tor}_{K(A,n)}(I)
\cong
H^{n+1}(NI;A)
\cong
R^{n+1}\!\lim_I\underline A,
\tag{4.3}
\]

且相应 diagram 的 homotopy limit 非空当且仅当其类为零。

#### 证明

space-valued straightening/unstraightening 把该 diagram 的 homotopy limit
识别为所分类 bundle 的 derived section space。principal bundle 有截面当且
仅当它平凡。另一方面，principal \(K(A,n)\)-bundles 由

\[
[|NI|,BK(A,n)]
\cong
H^{n+1}(NI;A)
\]

分类；category cohomology 的 normalized cochain complex 又计算
\(R^*\!\lim_I\underline A\)。证毕。

面范畴模型的额外价值在于：它不只给出分类，还把抽象 section obstruction
逐单形展开为 R3 的 matching profile，从而定位首次失败位置。

### 解释 4.4（这不与 R3 的“先有 branch 再有谱序列”冲突）

定理 4.2 的 \(R^{n+1}\!\lim\) 是**torsor 分类类**，不是把不存在的全局
branch 偷当作基点后形成的 \(R^s\!\lim\pi_t\) 项。它来自无基点的
delooping：

\[
K(A,n)\longmapsto BK(A,n)=K(A,n+1).
\]

因此正确的逻辑顺序是：

\[
\boxed{
\text{unpointed torsor class }\omega
\ \leadsto\ 
\text{existence}
\ \leadsto\ 
\text{choose a branch}
\ \leadsto\ 
\text{pointed deformation spectral sequence}.
}
\tag{4.4}
\]

这正是 R3 逻辑校正的强化，而不是例外。

---

## 5. 尖锐维数阈值

### 定理 5.1（Sharp Cohomological-Dimension Threshold）

固定 \(A,n\)。对有限逆面范畴 \(I_K\)：

1. 若
   \[
   R^{n+1}\!\lim_{I_K}\underline A=0,
   \]
   则每个 \(K(A,n)\)-torsor 型局部实现系统都 simultaneously effective；
2. 若
   \[
   R^{n+1}\!\lim_{I_K}\underline A\neq0,
   \]
   则每个非零类都实现为一个 objectwise nonempty、arrowwise equivalence、
   但 globally ineffective 的系统；
3. 特别地，\(\dim K\leq n\) 时所有此类系统有效；
4. 该维数界尖锐：取 \(K\) 为 \(S^{n+1}\) 的有限三角剖分及
   \(0\neq a\in A\)，则生成类
   \[
   a\in H^{n+1}(S^{n+1};A)\cong A
   \]
   产生一个在所有 \(n\)-骨架数据上有效、但全局无效的系统。

#### 证明

前两项由定理 4.2。第三项来自高于维数的上同调消失。第四项由球面的
顶维上同调与推论 3.3。证毕。

### 推论 5.2（没有跨 Postnikov 高度的统一有限 matching 深度）

对每个 \(m\geq1\)，存在一个 finite inverse poset 与一个局部 realization
diagram，使得：

- 所有 degree \(<m\) 的 matching extension 都成功；
- 每个对象非空，每条箭头为弱等价；
- 首次且完整的存在障碍恰在 degree \(m\)；
- 全局 homotopy limit 为空。

取 \(n=m-1\)、\(K=S^m\) 与非零
\(K(A,m-1)\)-torsor 即得。

这给出一个比单纯“测试秩无界”更结构化的结论：所需 matching 深度由
局部 realization fiber 的 Postnikov 高度精确控制。

---

## 6. 最小二维实例：Hopf torsor

令

\[
K=\partial\Delta^3,
\qquad
|K|\cong S^2,
\]

并令 \(I=I_K\) 为其非空面的反向包含 poset。对象共有四个顶点、六条边、
四个三角面；最大非退化链长度为二，因此 \(\dim N(I)=2\)。

取 Hopf principal circle bundle

\[
S^1\longrightarrow S^3\xrightarrow{p}S^2,
\]

其第一 Chern 类为生成元

\[
c_1(p)=1\in H^2(S^2;\mathbb Z)\cong\mathbb Z.
\]

定义

\[
X(\sigma)=\operatorname{Sing}\Gamma(|\sigma|,p|_{|\sigma|}).
\]

### 定理 6.1（Explicit Two-Dimensional Failure）

该图满足：

\[
X(\sigma)\simeq S^1
\quad\text{对所有 }\sigma,
\tag{6.1}
\]

每条结构映射 \(X(\sigma)\to X(\tau)\) 都是弱等价，但

\[
\boxed{
\operatorname*{holim}_{I}X
\simeq
\Gamma(p:S^3\to S^2)
=\varnothing.
}
\tag{6.2}
\]

其完整障碍为

\[
\boxed{
\omega(X)=c_1(p)=1
\in
R^2\!\lim_I\underline{\mathbb Z}
\cong\mathbb Z.
}
\tag{6.3}
\]

#### 证明

(6.1) 与 arrowwise weak equivalence 由引理 2.3。由引理 2.5，homotopy
limit 是 Hopf bundle 的截面空间。若该 bundle 有截面，它将平凡化为
\(S^2\times S^1\)，与 \(c_1(p)=1\) 矛盾，故得到 (6.2)。命题 4.1 与
定理 4.2 给出 (6.3)。证毕。

### 6.2 obstruction profile 的完全显式形式

先在一维骨架 \(K^{(1)}\) 上选截面 \(s\)。对四个定向三角面
\(\sigma_0,\ldots,\sigma_3\)，边界 restriction 在局部平凡化下给出
loops

\[
S^1\longrightarrow S^1
\]

及 winding numbers

\[
o_j(s)\in\mathbb Z.
\]

对第 \(j\) 个三角面，R3 matching extension 成功当且仅当
\(o_j(s)=0\)。四个整数形成一个 simplicial 2-cocycle，而且在基本类上的
取值满足

\[
\sum_{j=0}^{3}\varepsilon_j o_j(s)=1,
\tag{6.4}
\]

其中 \(\varepsilon_j\) 是边界定向符号。因此它们不可能同时为零。改变
一维骨架截面只给 \((o_j)\) 加上一个 coboundary，不改变 (6.4)。

这给出了 failure 的精确位置：不是某条 edge restriction 失败，而是四个
triangle-boundary conditions 无法被同一一维 branch 同时消去。

### 6.3 对 R3 压力测试 6.6 的升级

R3 只证明二维允许非零 \(R^2\!\lim\) 或 \(d_2\)。这里已经给出：

1. 明确的有限 poset；
2. 明确的 coefficient diagram \(\underline{\mathbb Z}\)；
3. 明确的生成元 \(1\in R^2\!\lim\)；
4. 明确的局部 realization spaces 与 transitions；
5. 该生成元对 simultaneous effectivity 的实际影响：它使全局 fiber 为空。

因此二维边界不再只是“谱序列可能不退化”的形式警告，而成为一个完整可验的
sector theorem。

---

## 7. 嵌入 Frozen v1.0 的 comparison 接口

对每个 \(\sigma\in I_K\)，把空间 \(X_P(\sigma)\) 看作 \(\infty\)-groupoid，
并取 comparison functor

\[
C_\sigma:X_P(\sigma)\longrightarrow *.
\]

唯一 formal datum 记为 \(\xi_\sigma=*\)。则

\[
\operatorname{EffFib}_{C_\sigma}(\xi_\sigma)
\simeq X_P(\sigma).
\]

所有局部 formal data 均 effective；结构映射甚至都是 equivalences。但 R1--R3
的 comparison-fiber theorem 给出

\[
\operatorname{EffFib}_{\lim C_\sigma}(\xi)
\simeq
\operatorname*{holim}_{I_K}X_P,
\]

故定理 3.1 变成 Frozen v1.0 导出层中的判据

\[
\boxed{
\xi\text{ simultaneously effective}
\iff
\omega(P)=0.
}
\tag{7.1}
\]

这不是对标准 bundle classification 的替代；理论新增的内容是把它识别为
generative/effectivity 系统的完整 obstruction，并说明 R3 的 matching
diagnostics 如何逐单形计算该类。

---

## 8. 研究意义与边界

### 8.1 本轮真正取得的推进

R3 中的一般 existence layer 只有 branch-dependent 的二值 profile：

\[
o_{r,i}(x)\in\{0,1\}.
\]

在本 sector 中，这些局部 tests 现在被提升为：

\[
\{o_{n+1,\sigma}(x)\}_{\sigma}
\rightsquigarrow
o(x)\in Z^{n+1}(K;A)
\rightsquigarrow
\omega\in H^{n+1}(K;A).
\]

最后的 \(\omega\)：

- 不依赖低阶 branch；
- 不依赖局部平凡化；
- 是 simultaneous effectivity 的必要充分条件；
- 可用普通上同调计算；
- 给出尖锐失败维数；
- 在有效时还控制 realization space 的全部 homotopy groups。

这正是此前计划中的“effectivity obstruction profile”第一次在非平凡 sector
中成为完整、可计算、可反驳的数学对象。

### 8.2 标准背景与本报告的新组合

以下事实是标准背景，不宣称为新发现：

1. principal \(G\)-bundles 由 \([B,BG]\) 分类；
2. \([B,K(A,m)]\cong H^m(B;A)\)；
3. section 等价于 principal bundle 的平凡化；
4. cellular obstruction cocycle 表示 characteristic class；
5. constant coefficient derived limits 计算 nerve cohomology。

本报告的 derived-sector 贡献是：

1. 把上述 classification 接到 R3 comparison-fiber/matching 接口；
2. 证明 R3 component obstruction 在 \(K(A,n)\)-torsor sector 中规范地
   组装为 \(R^{n+1}\!\lim\) 类；
3. 给出 effectivity 的必要充分判据与尖锐高度 \(n+1\)；
4. 给出 finite two-dimensional Hopf counterexample，证明 arrowwise equivalence
   远不足以保证 simultaneous effectivity。

### 8.3 尚未声称的推广

本报告没有无条件声称：

1. 任意 effectivity diagram 的 component obstructions 都能阿贝尔群值化；
2. 非阿贝尔 \(1\)-types 仍由普通 \(H^2(-;A)\) 分类；
3. 有 monodromy 时可以忽略 local coefficients；
4. principal torsor 以外的一般 Postnikov fiber 只有一个 obstruction；
5. 本报告使用的标准 bundle/obstruction theory 本身具有文献新颖性。

---

## 9. 从这一突破继续发展的精确方向

本轮以后，最自然的三步不再是继续搜随机例子，而是扩展已得到的完整定理。

### 9.1 Twisted coefficients

若 \(\pi_1(NI)\) 作用于 \(A\)，应把 (0.1) 升级为

\[
\omega\in H^{n+1}(NI;\mathcal A)
\cong R^{n+1}\!\lim_I\mathcal A,
\]

并核对 matching cocycle 的 transport signs 与 local system。

### 9.2 Nonabelian one-type

对一般群 \(G\)，principal \(G\)-bundles 仍由 \([NI,BG]\) 分类，但不再能
统一写成普通阿贝尔上同调。应建立 nonabelian \(H^1/H^2\) 或 crossed-module
版本，而不是强行阿贝尔化。

### 9.3 Full Postnikov effectivity tower

对一般 nilpotent truncated fiber \(F\)，逐 Postnikov stage 预期给出

\[
\omega_{k+1}
\in
H^{k+1}(NI;\pi_kF_{\mathrm{tw}}),
\]

其定义依赖先前 stages 的成功 branch。\(K(A,n)\)-torsor 定理应成为每一层的
原子模块。真正的下一旗舰目标是证明：R3 matching obstruction tower 与经典
Postnikov obstruction tower 自然等价，并由此得到一般 truncated effectivity
的有限完整算法。

---

## 10. 最终判定

\[
\boxed{
\begin{array}{rcl}
\text{explicit finite 2D }R^2\!\lim
&=&\mathbb Z\text{ on }I_{\partial\Delta^3},\\[1mm]
\text{nonzero class}
&=&c_1(\text{Hopf})=1,\\[1mm]
\text{local effectivity}
&=&\text{EVERYWHERE TRUE},\\[1mm]
\text{arrowwise transitions}
&=&\text{ALL WEAK EQUIVALENCES},\\[1mm]
\text{simultaneous effectivity}
&=&\text{FALSE},\\[1mm]
\text{complete obstruction}
&=&\omega\in R^{n+1}\!\lim\underline A,\\[1mm]
\text{first failure degree}
&=&n+1\text{, SHARP},\\[1mm]
\text{Frozen v1.0}
&=&\text{UNCHANGED}.
\end{array}
}
\]

R4 因而取得了 R3 所要求的 sector breakthrough：不仅构造了显式非零
\(R^2\!\lim\)，还证明该类是 simultaneous effectivity 的完整无基点障碍，
并把逐层 matching failure、characteristic class、derived limit 与
Postnikov 高度统一为同一个对象。

---

## 11. 标准背景来源

1. J. P. May, *A Concise Course in Algebraic Topology*：principal
   \(G\)-bundle 的 classifying-space theorem，以及
   \(\pi_q(BG)\cong\pi_{q-1}(G)\)。
2. A. Hatcher, *Vector Bundles and K-Theory*：
   \(\mathbb CP^\infty=K(\mathbb Z,2)\)、complex line bundles 与
   \(H^2(-;\mathbb Z)\) 的 \(c_1\)-分类。
3. A. K. Bousfield and D. M. Kan,
   *Homotopy Limits, Completions and Localizations*：homotopy limits 与
   derived limits。
4. E. Riehl and D. Verity,
   *The Theory and Practice of Reedy Categories*：inverse Reedy diagrams、
   matching objects 与 strict-limit models。
