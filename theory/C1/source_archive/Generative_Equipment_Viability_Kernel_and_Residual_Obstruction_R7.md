# 生成装备研究 R7：可生存核、普遍有效性像与残余障碍压缩

## 0. 研究判定

本轮不修改 Frozen v1.0，判定为：

\[
\boxed{\texttt{PASS + DERIVED STRUCTURE}}
\]

R6 给出了逐层前向结构：每一层分支空间是障碍截面与零截面的同伦等化子。R7 解决此前尚未区分的问题：

> 一个分支能够通过当前障碍，并不意味着它能延伸到塔顶。

正确的完整理论必须同时包含：

- **前向生成**：产生所有当前可提升分支；
- **反向筛除**：删除以后必然死亡的分支；
- **分支消元**：在线性/仿射 Coupl 情形，把中间选择压缩成规范的余纤维值残余障碍。

本轮得到三个主要结论：

1. **Viability-Kernel Theorem**：任意有限障碍塔都有规范的反向可生存核塔，精确刻画哪些部分分支能延伸为完整解。
2. **Universal Effectivity Image Theorem**：完整有效性是塔顶到初始分支空间之映射的 \((-1)\)-像；它具有最小性、基变换稳定性，并与 R3/Postnikov 表示无关。
3. **Residual Obstruction Compression Theorem**：若下一障碍沿提升扭子的变化是仿射的，则所有中间分支选择可消去为一个 \(\operatorname{cofib}(D)\)-值残余障碍；可行提升空间是 \(\operatorname{fib}(D)\)-扭子。二阶 cross-effect 恰是这种线性压缩的完全障碍。

这些结果避开了无限高度球面同伦群问题，完全处于有限截断范围。

---

## 1. 设置：有限分支塔

工作在空间范畴，或更一般地工作在一个 \(\infty\)-拓扑斯 \(\mathcal X\) 中。考虑有限塔

\[
\mathcal B_N
\xrightarrow{p_N}
\mathcal B_{N-1}
\longrightarrow\cdots\longrightarrow
\mathcal B_1
\xrightarrow{p_1}
\mathcal B_0.
\]

在 R6 的 Postnikov/R3 应用中，\(\mathcal B_k\) 是高度 \(k\) 的部分分支空间，并且

\[
\mathcal B_k
\simeq
\operatorname{Eq}^{h}_{\mathcal B_{k-1}}
(\mathrm{Obs}_k,0).
\]

对 \(x\in\mathcal B_{k-1}\)，记一步提升空间为

\[
L_k(x):=\operatorname{fib}_x(p_k).
\]

于是

\[
L_k(x)\not\simeq\varnothing
\iff
o_k(x)=0.
\]

这里必须保留两个不同层次：

- \(\|L_k(x)\|_{-1}\) 只记录“是否存在提升”；
- \(L_k(x)\) 本身还记录提升之间的变形、自同构与高阶同伦。

后续所有像都取 \((-1)\)-截断像，因而只用于存在性；高阶信息始终保留在相应纤维空间中。

---

## 2. 普遍有效性像

令

\[
p_{N,0}:=p_1p_2\cdots p_N:
\mathcal B_N\to\mathcal B_0.
\]

### 定义 2.1（普遍有效性谓词）

定义

\[
\operatorname{Eff}_N
:=
\operatorname{im}_{-1}(p_{N,0})
\hookrightarrow
\mathcal B_0.
\]

在空间范畴中，它是 \(\mathcal B_0\) 中真正被完整分支击中的连通分支之并。内部点态地，

\[
\operatorname{Eff}_N(x)
\simeq
\left\|
\operatorname{fib}_x(p_{N,0})
\right\|_{-1}.
\]

### 定理 2（Universal Effectivity Image）

\(\operatorname{Eff}_N\) 是满足下列性质的唯一子对象：

1. \(p_{N,0}\) 通过 \(\operatorname{Eff}_N\hookrightarrow\mathcal B_0\) 分解；
2. 对任何子对象 \(U\hookrightarrow\mathcal B_0\)，若 \(p_{N,0}\) 通过 \(U\) 分解，则
   \[
   \operatorname{Eff}_N\hookrightarrow U;
   \]
3. 对任意基变换 \(f:T\to\mathcal B_0\)，有自然等价
   \[
   f^*\operatorname{Eff}_N
   \simeq
   \operatorname{im}_{-1}
   (T\times_{\mathcal B_0}\mathcal B_N\to T).
   \]

#### 证明

前两条正是 \((-1)\)-连通/\((-1)\)-截断像分解的普遍性质。\(\infty\)-拓扑斯中的该分解系统在拉回下稳定，所以得到第三条。空间情形也可直接逐纤维验证：拉回后某点的纤维非空，当且仅当原映射在相应点的纤维非空。∎

### 解释

这给出了一个完全分支无关的总障碍提取器，但它不是预先指定阿贝尔群中的单一类，而是初始分支空间上的真值型子对象。

因此，普遍情形下的“总障碍”应当写成

\[
x\longmapsto
\left\|
\text{完整延伸空间 over }x
\right\|_{-1},
\]

而不是强行写成 \(x\mapsto o(x)\in G\)。后者只在额外线性结构存在时才可能。

---

## 3. 反向可生存核塔

对 \(0\le j\le N\)，令

\[
p_{N,j}:\mathcal B_N\to\mathcal B_j
\]

为复合投影。

### 定义 3.1（高度 \(N\) 的可生存核）

定义

\[
V_j^{(N)}
:=
\operatorname{im}_{-1}(p_{N,j})
\hookrightarrow
\mathcal B_j.
\]

一个部分分支 \(x\in\mathcal B_j\) 属于 \(V_j^{(N)}\)，当且仅当它至少有一个延伸到塔顶 \(\mathcal B_N\)。

显然

\[
V_N^{(N)}=\mathcal B_N,
\qquad
V_0^{(N)}=\operatorname{Eff}_N.
\]

### 定理 3（Viability-Kernel Backward Recursion）

对每个 \(1\le j\le N\)，有

\[
\boxed{
V_{j-1}^{(N)}
=
\operatorname{im}_{-1}
\bigl(V_j^{(N)}\to\mathcal B_{j-1}\bigr)
}.
\]

点态地，

\[
\boxed{
V_{j-1}^{(N)}(x)
\simeq
\left\|
\sum_{y\in L_j(x)}V_j^{(N)}(y)
\right\|_{-1}
}.
\]

换言之，\(x\) 可生存，当且仅当它有一个一步提升 \(y\)，而且该 \(y\) 自身可生存。

#### 证明

把 \(p_{N,j}:\mathcal B_N\to\mathcal B_j\) 分解为有效满射

\[
\mathcal B_N\twoheadrightarrow V_j^{(N)}
\]

与单射

\[
V_j^{(N)}\hookrightarrow\mathcal B_j.
\]

有效满射前合成不改变后续复合的 \((-1)\)-像，因此

\[
\operatorname{im}_{-1}(p_{N,j-1})
=
\operatorname{im}_{-1}
(V_j^{(N)}\to\mathcal B_{j-1}).
\]

逐纤维展开像的内部逻辑，便得到依赖和及 \((-1)\)-截断公式。∎

---

## 4. 当前可提升不等于最终可生存

令当前障碍的零点像为

\[
Z_j
:=
\operatorname{im}_{-1}(p_j)
\hookrightarrow
\mathcal B_{j-1}.
\]

因为任何可延伸到塔顶的分支必然能通过当前一步，存在规范包含

\[
V_{j-1}^{(N)}\hookrightarrow Z_j.
\]

### 定理 4（Dead-End Criterion）

下列条件等价：

1. \(V_{j-1}^{(N)}=Z_j\)；
2. 每个当前可提升的 \(x\in\mathcal B_{j-1}\)，至少有一个一步提升 \(y\in L_j(x)\) 属于 \(V_j^{(N)}\)；
3. 映射
   \[
   V_j^{(N)}\to Z_j
   \]
   是有效满射。

#### 证明

由定理 3，\(V_{j-1}^{(N)}\) 正是 \(V_j^{(N)}\to\mathcal B_{j-1}\) 的像；而 \(Z_j\) 是全部一步提升 \(\mathcal B_j\to\mathcal B_{j-1}\) 的像。两像相等，恰等价于 \(Z_j\) 中每点的 \(V_j^{(N)}\)-纤维非空，也就是第二、第三条件。∎

### 结论

逐层检查

\[
o_j(x)=0
\]

只产生候选分支；它不能单独判定该候选是否有完整未来。完整 effectivity 必须使用反向递归，或者使用与之等价的总像 \(\operatorname{Eff}_N\)。

这正是“逐层局部可行”与“同时有效化”之间的差别。

---

## 5. 自然性与 R3/Postnikov 不变性

设有两个有限塔及其层间交换的映射

\[
F_j:\mathcal B_j\to\mathcal B'_j.
\]

则塔顶完整分支被送到塔顶完整分支，因此

\[
F_j(V_j^{(N)})\subseteq V_j'{}^{(N)}.
\]

若每个 \(F_j\) 是等价，则诱导

\[
V_j^{(N)}\simeq V_j'{}^{(N)}.
\]

### 推论 5.1

R5 的 R3/Postnikov 自然比较不仅识别逐层障碍空间，也识别整个反向可生存核塔：

\[
V_{j,\mathrm{R3}}^{(N)}
\simeq
V_{j,\mathrm{Post}}^{(N)}.
\]

所以“哪些部分分支最终能活到塔顶”不是所选 resolution 的产物，而是完整解空间到部分分支空间之投影的内在像。

---

## 6. 仿射 Coupl 的中间分支消元

现在固定一个部分分支 \(x\)。设其一步提升的连通分支构成 \(H\)-扭子 \(T\)，而下一障碍取值于阿贝尔群 \(G\)：

\[
q:T\to G.
\]

假设存在群同态

\[
D:H\to G
\]

使得

\[
q(t+h)=q(t)+D(h).
\]

这正是下一障碍沿当前提升扭子的 Coupl 为线性的情形。

### 定理 6（Residual Obstruction Compression，离散形式）

定义

\[
\rho(q):=[q(t)]\in\operatorname{coker}(D).
\]

则：

1. \(\rho(q)\) 与基准提升 \(t\in T\) 的选择无关；
2. 存在 \(t'\in T\) 使 \(q(t')=0\)，当且仅当
   \[
   \rho(q)=0;
   \]
3. 若零点存在，则
   \[
   q^{-1}(0)
   \]
   是 \(\ker(D)\)-扭子。

#### 证明

若把基准点从 \(t\) 改为 \(t+h\)，则障碍值改变 \(D(h)\)，故其余核类不变。存在 \(h\) 使

\[
q(t+h)=q(t)+D(h)=0
\]

等价于 \(-q(t)\in\operatorname{im}D\)，即余核类为零。若 \(h_0\) 是一个解，则全部解恰为 \(h_0+\ker D\)。∎

这个定理把“在整个提升扭子中搜索下一障碍零点”压缩成一个不依赖提升选择的残余障碍。

---

## 7. 谱值加强：余核应替换为余纤维

离散群只记录 \(\pi_0\)。若要保留高阶变形，令 \(H,G\) 为 connective spectra，令

\[
D:H\to G
\]

为谱映射，并令 \(T\) 是 \(\Omega^\infty H\)-扭子。设

\[
q:T\to\Omega^\infty G
\]

对平移作用是 \(D\)-仿射的。

### 定理 7（Residual Cofiber Obstruction）

存在规范残余点

\[
\rho(q)\in
\Omega^\infty\operatorname{cofib}(D),
\]

并且：

1. \(q^{-1}(0)\) 非空，当且仅当 \(\rho(q)\) 位于零点所在的连通分支；
2. 若非空，则完整零点空间是
   \[
   \Omega^\infty\operatorname{fib}(D)
   \]
   的扭子；
3. 取 \(\pi_0\) 后恢复定理 6：
   \[
   \pi_0\operatorname{cofib}(D)
   \cong
   \operatorname{coker}(\pi_0D)
   \]
   （在相应 connective 条件下），而零点连通分支构成 \(\ker(\pi_0D)\)-扭子。

#### 证明

\(D\) 使 \(\Omega^\infty H\) 通过平移作用在 \(\Omega^\infty G\) 上。仿射性使 \(q\) 成为等变映射。对作用取同伦商，利用

\[
T//\Omega^\infty H\simeq *,
\qquad
(\Omega^\infty G)//\Omega^\infty H
\simeq
\Omega^\infty\operatorname{cofib}(D),
\]

得到残余点 \(\rho(q)\)。选取局部基准点后，零点空间等价于 \(D\) 在 \(-q(t)\) 上的同伦纤维；若该纤维非空，它是 \(\operatorname{fib}(D)\) 的主齐性空间。∎

### 意义

R4 的“障碍群 + 提升扭子 + 高阶自同伦”现在统一为一个纤维—余纤维对：

\[
\operatorname{fib}(D)
\quad\text{控制解的自由度},
\qquad
\operatorname{cofib}(D)
\quad\text{承载消去分支选择后的残余障碍}.
\]

---

## 8. 三角仿射塔的一次性压缩

设在固定初始分支上，所有提升选择合起来形成 \(H\)-扭子

\[
T,
\qquad
H=\bigoplus_{j=1}^r H_j,
\]

所有待满足的障碍合起来取值于

\[
G=\bigoplus_{i=1}^r G_i.
\]

选定一个参考部分分支链后，假设障碍方程具有三角仿射形式

\[
q_i(h_1,\dots,h_i)
=
c_i+
\sum_{j\le i}D_{ij}h_j.
\]

令

\[
D=(D_{ij}):H\to G,
\qquad
c=(c_1,\dots,c_r).
\]

### 定理 8（Triangular Affine Compression）

完整分支存在，当且仅当

\[
[c]=0
\in
\pi_0\operatorname{cofib}(D).
\]

若完整分支存在，则完整分支空间是

\[
\Omega^\infty\operatorname{fib}(D)
\]

的扭子。

此外，改变参考分支链只把 \(c\) 改变为 \(c+D(h_0)\)，所以残余类 \([c]\) 规范且与参考链无关。

#### 证明

全部三角方程共同定义一个仿射映射

\[
q:T\to\Omega^\infty G
\]

其线性部分为 \(D\)。直接应用定理 7。三角性只编码“第 \(i\) 个障碍只依赖此前选择”，不影响纤维—余纤维论证。∎

这给出有限线性 sector 的真正总障碍：它不是逐层类的简单直和，而是三角 Coupl 矩阵 \(D\) 的余纤维中的一个类。

---

## 9. Cross-effect 是线性压缩的完全障碍

令 \(T\) 是 \(H\)-扭子，选定 \(t_0\in T\)，并写

\[
\widetilde q(h):=q(t_0+h)-q(t_0).
\]

定义二阶 cross-effect

\[
\operatorname{cr}_2(q)(h_1,h_2)
=
\widetilde q(h_1+h_2)
-\widetilde q(h_1)
-\widetilde q(h_2).
\]

### 定理 9（Linear-Compression Criterion）

下列条件等价：

1. 存在群同态 \(D:H\to G\) 使
   \[
   q(t_0+h)=q(t_0)+D(h);
   \]
2. \(\operatorname{cr}_2(q)=0\)；
3. Coupl 与背景分支无关且对修改变量可加。

#### 证明

第一条件显然推出 cross-effect 为零。反之，cross-effect 为零说明 \(\widetilde q(h_1+h_2)=\widetilde q(h_1)+\widetilde q(h_2)\)，故 \(\widetilde q\) 本身就是群同态，取 \(D=\widetilde q\)。第三条件只是同一陈述的 Coupl 表达。∎

### 推论 9.1（精确 no-go）

若 \(\operatorname{cr}_2(q)\ne0\)，则不存在与分支平移兼容的余核/余纤维值线性残余障碍，能够把整个零点问题压缩为一个仿射方程。

此时不能把 \(\operatorname{im}D\) 或 \(\operatorname{coker}D\) 当作总答案；必须保留非线性零点像，或使用定理 3 的可生存核递归。

R6 的二次模型 \(q(a)=a^2\) 满足

\[
\operatorname{cr}_2(q)(a,b)=2ab,
\]

因而正是最小的不可线性压缩模型。

---

## 10. 一般有限塔的精确算法性形式

对任意有限截断幂零障碍塔，不要求 Coupl 线性，存在下列精确过程：

### 前向阶段

构造

\[
\mathcal B_0,\mathcal B_1,\dots,\mathcal B_N
\]

及每层依赖型障碍零点。

### 反向阶段

令

\[
V_N^{(N)}=\mathcal B_N,
\]

并递归计算

\[
V_{j-1}^{(N)}
=
\operatorname{im}_{-1}
(V_j^{(N)}\to\mathcal B_{j-1}).
\]

最终得到

\[
V_0^{(N)}=\operatorname{Eff}_N.
\]

### 局部压缩

若某一层的 Coupl 是仿射的，则用定理 6 或定理 7 消去该层提升选择；若若干层联合为三角仿射系统，则用定理 8 一次压缩。

### 非线性保留

若第一非零 cross-effect 出现在阶数 \(d\ge2\)，则保留该多项式零点问题，不把它伪装成群商。可生存核递归仍然完全有效。

这个过程有限终止，因为纤维是有限截断的。它不要求计算任意高度球面同伦群。

---

## 11. 正证书与反证书

### 正有效性证书

一个完整分支链

\[
x_0\leftarrow x_1\leftarrow\cdots\leftarrow x_N
\]

连同每层障碍的零伦，是 \(x_0\in\operatorname{Eff}_N\) 的见证。

### 反有效性证书

在分支集合有限离散的情形，从塔顶开始反向标记所有可生存节点。若根分支最终未被标记，则得到一个有限反证书：根的每个一步提升都在更高层被某个障碍或已证明的死端截断。

这比“某个选定分支失败”更强；它证明所有允许分支同时失败。

在线性 sector，反证书可进一步压缩为非零残余类

\[
[c]\ne0
\in
\pi_0\operatorname{cofib}(D).
\]

在非线性 sector，一般只能保留零点像未命中的证明，不能无损压缩为一个余核类。

---

## 12. 与 Frozen v1.0 的对应

R7 没有增加核心公理，而是把 Frozen v1.0 的三个原则具体化：

| Frozen 原则 | R7 的数学实现 |
|---|---|
| 分层 Resolution | 前向障碍塔 \(\mathcal B_0\leftarrow\cdots\leftarrow\mathcal B_N\) |
| Simultaneous Effectivity | 反向可生存核 \(V_j^{(N)}\) 与总像 \(\operatorname{Eff}_N\) |
| Obstruction / Solution 分离 | \((-1)\)-像判存在；完整纤维保留解的高阶结构 |
| Coupl | 提升扭子上的障碍变化律 |
| Activation | 完整分支纤维 \(\operatorname{fib}_x(p_{N,0})\) |

理论状态因此是 derived strengthening，而非核心升级。

---

## 13. 已知成分与新组合的纪律性判断

### 标准成分

1. Postnikov/Moore–Postnikov 塔中的障碍类与提升扭子是经典障碍论。
2. \(\infty\)-拓扑斯中的有效满射—单射像分解及其基变换稳定性是标准高阶拓扑斯理论。
3. 仿射方程的核—余核判据，以及其谱化后的纤维—余纤维形式，是稳定同伦代数的标准机制。

### 本项目形成的派生组合

1. 把有限障碍塔系统地分解为“前向候选生成 + 反向可生存核筛除”；
2. 证明该可生存核在 R3 matching 与 Postnikov 表示之间自然不变；
3. 用 cross-effect 给出“何时可以把分支搜索压缩成余纤维残余障碍”的充要条件；
4. 把线性多阶段 Coupl 组织成三角算子 \(D\)，以单一 \(\operatorname{cofib}(D)\)-值类判定完整 effectivity，同时用 \(\operatorname{fib}(D)\) 描述全部解自由度。

针对 “viability kernel + Postnikov obstruction tower + affine residual cofiber” 的组合检索未发现直接同名结果；但这不足以证明发表级新颖性。当前可确认的是：它是一个正确、领域独立、可验证且非单纯改名的定理包；正式新颖性仍需更系统的文献复审。

---

## 14. 下一条可闭合路线

不进入无限高度开放问题，下一阶段应研究：

1. **Polynomial Residual Tower**：当 \(\operatorname{cr}_{d+1}=0\) 但 \(\operatorname{cr}_2\ne0\) 时，用次数过滤逐次提取高阶残余，而不是错误线性化；
2. **Central Nilpotent Refinement**：用幂零作用的中心过滤，把变系数障碍细化为有限个平凡作用商上的障碍，再把扩张数据记录为新的 Coupl；
3. **Obstruction-Fubini Theorem**：在 R3 matching 维与 Postnikov 维组成的有限双塔中，比较两种反向可生存核消元顺序，并找出它们交换的精确条件。

这三条都保持有限高度，因而不会触及完整球面同伦群计算。

---

## 参考边界

- J. P. May, *A Concise Course in Algebraic Topology*：Postnikov 系统与经典障碍论。  
  <https://www.math.uchicago.edu/~may/CONCISE/ConciseRevised.pdf>
- J. Lurie, *Higher Topos Theory*：\(\infty\)-拓扑斯中的截断、像分解与有效满射。  
  <https://arxiv.org/abs/math/0608040>
- M. Čadek, M. Krčál, J. Matoušek, L. Vokřínek, U. Wagner, *Polynomial-time computation of homotopy groups and Postnikov systems in fixed dimension*：固定高度 Postnikov 数据的算法边界。  
  <https://arxiv.org/abs/1211.3093>

---

## 最终结论

R6 的逐层零点理论必须补上一个反向层。完整有限截断理论现在具有如下规范形态：

\[
\boxed{
\begin{array}{c}
\text{前向障碍零点产生部分分支}\\[2mm]
\Downarrow\\[2mm]
\text{反向 }(-1)\text{-像递归删除死端}\\[2mm]
\Downarrow\\[2mm]
\operatorname{Eff}_N
=
\operatorname{im}_{-1}(\mathcal B_N\to\mathcal B_0)
\end{array}
}
\]

在线性/仿射 sector，这一真值型总像进一步压缩为

\[
\boxed{
[c]\in\pi_0\operatorname{cofib}(D),
\qquad
\text{解空间为 }\Omega^\infty\operatorname{fib}(D)\text{-扭子}
}
\]

而 \(\operatorname{cr}_2\ne0\) 恰好说明这种线性压缩不可能，必须保留非线性可生存核。
