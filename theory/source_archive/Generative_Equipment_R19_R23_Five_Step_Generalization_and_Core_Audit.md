# R19–R23：五步推广、四重极值分类与核心升级审计

**状态：** 研究报告；不修改 Frozen v1.0 核心。  
**系数约定：** R19–R21 在任意交换系数环/域且相关 Künneth 条件明确满足时成立；R22 的有限分类取系数域 \(\mathbb F_2\)。  
**依赖：** R16（resolved Coupl / Massey matching）、R17（moment-angle 支撑成本与 cube universality）、R18（graph Maurer–Cartan / holonomy 与 \(n=4\) 非线性阈值）。

---

## 0. 五步结论总览

1. **冻结完成。** R17–R18 保持不变，并以校验和固定。
2. **一般定理完成。** 对 Boolean-support DGA，full-support 截断是 split DGA retract；Massey 可定义性与是否含 \(0\) 完全局部化。任意非负支撑代价给出 arity 上界及等号刚性。
3. **polyhedral product 推广完成。** 对 \((\underline{CA},\underline A)^K\)，full subcomplex 给出无条件坐标收缩；在 strong-Künneth/multiplicative BBCG 模型中，R17 的顶点成本与最低 simplicial-degree 的 cube universality 延续成立。
4. **\(n=4\) 新判据与极值分类完成。** 连通 corridor 下，所有 filler 可由生成树积分确定；在八顶点最低支撑 sector 中，非平凡四重积的边数下界从 \(9\) 提升到尖锐的 \(10\)。十边极值图只有一个未标号类型。
5. **核心审计完成。** 结果足以形成候选扩展层，但尚不足以修改 Frozen core：目前的非平凡实例仍集中在同一个 toric-topology/polyhedral-product 生态，未达到“三个相互独立自然领域”的升级阈值。

---

## 1. 第一步：冻结 R17–R18

冻结对象：

- `Generative_Equipment_R17_Moment_Angle_Support_and_Cube_Universality.md`
- `Generative_Equipment_R18_Graph_Holonomy_and_First_Nonlinear_Threshold.md`

SHA256：

```text
R17 e53cfe4dd93d556fa9a222863bb7311b0ec696c6de323b6921368b8b2f3634f5
R18 482df71a762589644c0c8ffac6e90b23a176512c455b50a939e8962efdb93549
```

本报告只在其上增加 R19–R23，不回写旧结论。

---

## 2. 第二步：一般 support-graded DGA

### 2.1 Boolean-support DGA

设 \(V\) 为有限集，\((A,d,\mu)\) 为 DGA，并有直和分解

\[
A=\bigoplus_{S\subseteq V}A_S,
\qquad d(A_S)\subseteq A_S,
\qquad A_SA_T\subseteq A_{S\cup T}.
\tag{2.1}
\]

对 \(J\subseteq V\)，定义

\[
A_{\le J}:=\bigoplus_{S\subseteq J}A_S.
\tag{2.2}
\]

令 \(\iota_J:A_{\le J}\hookrightarrow A\) 为包含，\(\rho_J:A\to A_{\le J}\) 为删除所有不包含于 \(J\) 的支撑分量的投影。

### 定理 R19.1（Split Support-Excision）

\(A_{\le J}\) 是子 DGA，且

\[
A_{\le J}\xrightarrow{\ \iota_J\ }A
\xrightarrow{\ \rho_J\ }A_{\le J},
\qquad \rho_J\iota_J=\mathrm{id},
\tag{2.3}
\]

是 split DGA retract。

若 \(\alpha_1,\ldots,\alpha_n\in H^*(A_{\le J})\)，则：

\[
\langle\alpha_1,\ldots,\alpha_n\rangle
\text{ 在 }A\text{ 中可定义}
\iff
\text{在 }A_{\le J}\text{ 中可定义},
\tag{2.4}
\]

且

\[
0\in\langle\alpha_1,\ldots,\alpha_n\rangle_A
\iff
0\in\langle\alpha_1,\ldots,\alpha_n\rangle_{A_{\le J}}.
\tag{2.5}
\]

同样的结论适用于 R3 matching tower 的“proper defining system 是否存在”与“top filler 是否存在”。

#### 证明

若 \(S\not\subseteq J\)，则对任意 \(T\)，\(S\cup T\not\subseteq J\)。因此删除外部支撑与乘法相容：

\[
\rho_J(xy)=\rho_J(x)\rho_J(y).
\]

又因微分保持支撑，\(\rho_Jd=d\rho_J\)，故 (2.3) 是 DGA retract。局部 defining system 经 \(\iota_J\) 成为整体 defining system；整体 defining system 经 \(\rho_J\) 成为局部 defining system。若 top curvature 在整体中为边界，投影后仍为局部边界；反向由包含成立。证毕。

### 2.2 区间齐次子塔

设输入分别齐次支撑于两两不交的 \(S_1,\ldots,S_n\)，并记

\[
S_{ik}=S_i\cup\cdots\cup S_k.
\]

要求每个 defining entry \(a_{ik}\) 位于 \(A_{S_{ik}}\) 的 defining systems 构成一个对 Maurer–Cartan 方程封闭的子塔，因为

\[
A_{S_{ir}}A_{S_{r+1,k}}\subseteq A_{S_{ik}}.
\tag{2.6}
\]

这里必须保留一个边界：**一般整体 defining system 不必自动等价于区间齐次 defining system。** R17–R18 研究的是 multihomogeneous sector；在该 sector 内，(2.6) 给出严格闭合，而不是对任意非齐次 defining system 的无条件“规范化”。

### 定理 R19.2（Support-Cost）

设 \(w:2^V\to\mathbb R_{\ge0}\) 在不交并上可加：

\[
S\cap T=\varnothing\Longrightarrow w(S\cup T)=w(S)+w(T).
\]

定义第 \(p\) 次非零上同调的最低支撑代价

\[
\nu(p)=\inf\{w(S):H^p(A_S)\ne0\}.
\tag{2.7}
\]

若非零输入 \(\alpha_i\in H^{p_i}(A_{S_i})\) 的支撑两两不交，则

\[
w\!\left(\bigcup_{i=1}^nS_i\right)
=\sum_{i=1}^n w(S_i)
\ge \sum_{i=1}^n\nu(p_i).
\tag{2.8}
\]

若所有允许输入均满足 \(\nu(p)\ge c>0\)，则总支撑预算 \(W\) 内的 arity 满足

\[
n\le \left\lfloor\frac{W}{c}\right\rfloor.
\tag{2.9}
\]

若 (2.8) 取等，则每个 \(S_i\) 都是其次数 \(p_i\) 的最低代价支撑。

#### 证明

由不交可加性与 \(w(S_i)\ge\nu(p_i)\) 逐项求和即得。等号若成立，则任何一项严格大于最低代价都会使总和严格增大。证毕。

### 2.3 意义与限制

R19.1 是 obstruction-theoretic 定理：它说明 full support 外的单形、变量或坐标不可能帮助解决局部 defining/filler 问题。R19.2 是资源定理：它把“高阶操作需要足够多独立支撑”变成可证明的 arity ceiling。二者逻辑独立；前者不要求代价函数，后者不声称 Massey 乘积一定存在。

---

## 3. 第三步：cone polyhedral products

令 \(K\) 是顶点集 \([m]\) 上的单纯复形，\((CA_i,A_i)\) 是带基点 CW-pairs。记

\[
Z_K=(\underline{CA},\underline A)^K.
\]

对 \(J\subseteq[m]\)，\(K_J\) 是 full subcomplex。

### 定理 R20.1（Coordinate-Retract Excision）

存在自然映射

\[
Z_{K_J}\xrightarrow{s_J}Z_K\xrightarrow{p_J}Z_{K_J},
\qquad p_Js_J=\mathrm{id},
\tag{3.1}
\]

其中 \(s_J\) 把 \(J\) 外坐标置为基点，\(p_J\) 忘掉 \(J\) 外坐标。

因此，对来自 \(H^*(Z_{K_J})\) 的类，任意普通 Massey 乘积在 \(Z_K\) 中可定义当且仅当在 \(Z_{K_J}\) 中可定义；在整体中含 \(0\) 当且仅当在局部中含 \(0\)。

#### 证明

若一点属于 \(K\) 的面 \(\sigma\) 对应的坐标块，投影到 \(J\) 后属于 \(\sigma\cap J\in K_J\) 的坐标块，所以 \(p_J\) 良定义。基点属于每个 \(A_i\)，所以 \(s_J\) 良定义，且 (3.1) 显然。奇异/胞腔上链的反变函子性给出 split DGA maps，随后应用 R19.1 的 defining-system 论证。证毕。

### 定理 R20.2（Künneth-Admissible Support Cost）

再假设系数满足 strong Künneth，并选用与 BBCG/Cartan 分解相容的乘法模型。一个由 full-subcomplex 因子

\[
0\ne \xi_i\in\widetilde H^{p_i}(K_{J_i})
\]

与 \(A_j\) 的系数类装饰得到的 multihomogeneous 输入，必满足

\[
|J_i|\ge p_i+2.
\tag{3.2}
\]

若 \(J_i\) 两两不交，则

\[
\left|\bigcup_iJ_i\right|\ge\sum_i(p_i+2).
\tag{3.3}
\]

特别地，在最低 simplicial-degree sector \(p_i=0\) 中，\(|\bigcup_iJ_i|=2n\) 强迫每个 \(J_i\) 有两个顶点且 \(K_{J_i}=S^0\)。于是

\[
K_{\cup J_i}\subseteq (S^0)^{*n}=\partial C_n^\diamond,
\tag{3.4}
\]

即 R17 的 cube/crosspolytope universality 仍成立；\(A_j\) 的类只形成系数装饰，不改变顶点成本。

#### 证明

一个只有 \(q\) 个顶点的复形若 \(\widetilde H^p\ne0\)，必有 \(q\ge p+2\)；否则其维数不足，或在极限维数中只有满单形而无非零约化上同调。对不交 \(J_i\) 求和得到 (3.3)。当 \(p_i=0\) 且取等时，两点 full subcomplex 必不连通，即 \(S^0\)。任何同时含同一 \(J_i\) 两个顶点的单形都会包含该缺边，故不存在；于是得到 (3.4)。证毕。

### 3.1 不能越过的边界

R20.1 无需 Künneth 假设。R20.2 则明确依赖 multiplicative decomposition；稳定分裂本身不能自动升级为链级 DGA 直和。因此，本报告没有声称任意 CW-pair 的所有非齐次 Massey defining systems 都满足 Boolean-support 分级。

---

## 4. 第四步：\(n=4\) 连通 corridor 判据与尖锐极值图

### 4.1 确定性生成树判据

沿用 R18 的最低支撑图模型。四个输入支撑为 \(J_1,\ldots,J_4\)，每个 \(J_i\) 是两个不相连顶点。对区间 \(I=[i,k]\)，记诱导图为 \(G_I\)。

假设每个 proper interval graph

\[
G_{12},G_{23},G_{34},G_{123},G_{234}
\]

连通。实际上，前三者连通已推出后两者连通。

在每个 \(G_I\) 中固定根与生成树。若 \(c\in C^1(G_I)\) 对每条 cycle 的 holonomy 为零，则沿生成树积分得到唯一根归一化 potential，记为

\[
P_I(c)\in C^0(G_I),\qquad \delta P_I(c)=c.
\tag{4.1}
\]

递归定义

\[
\begin{aligned}
a_{12}&=P_{12}(a_1a_2),&
a_{23}&=P_{23}(a_2a_3),&
a_{34}&=P_{34}(a_3a_4),\\
a_{13}&=P_{123}(a_1a_{23}+a_{12}a_3),&&
a_{24}&=P_{234}(a_2a_{34}+a_{23}a_4).
\end{aligned}
\tag{4.2}
\]

### 定理 R21（Connected-Corridor Fourfold Criterion）

在上述假设下：

1. 四重 Massey 乘积可定义，当且仅当 (4.2) 中五个 curvature 依次都具有零 cycle-holonomy；
2. 一旦可定义，其 top class 不依赖 filler choices；
3. 令

   \[
   \Omega^{\mathrm{can}}_4
   =a_1a_{24}+a_{12}a_{34}+a_{13}a_4,
   \tag{4.3}
   \]

   则

   \[
   0\notin\langle\alpha_1,\alpha_2,\alpha_3,\alpha_4\rangle
   \iff
   \exists z\in Z_1(G_{1234}):
   \operatorname{Hol}_z(\Omega^{\mathrm{can}}_4)\ne0.
   \tag{4.4}
   \]

因此，R18 的“存在某组 fillers”二次系统在 connected-corridor sector 中被消成一个确定性的递归积分与 cycle test。

#### 证明

R18 的 graph-holonomy 定理说明 \(\delta f=c\) 当且仅当所有 cycle holonomies 消失。连通性使解只差一个常数；在 augmented cochain complex 中常数是约化边界。改变某个 filler 一个常数，通过 Leibniz 公式只把后续 curvature 改变一个边界。递归可定义性与最终上同调类因而与归一化无关。选择根值为零即得到 (4.2)，最后再次应用 holonomy 判据得到 (4.4)。证毕。

### 4.2 八顶点 extremal sector

现在取 \(J_i=\{x_i^0,x_i^1\}\)，环境图为

\[
(S^0)^{*4}\text{ 的一骨架},
\]

即不同支撑块之间均允许连边、块内不允许连边。取系数 \(\mathbb F_2\)。

connected-corridor 要求三个相邻二部图 \(G_{12},G_{23},G_{34}\) 连通。每个都是四顶点二部图，至少有三条边，故总图至少有九条边。

### 定理 R22（Sharp Ten-Edge Fourfold Classification，计算机辅助有限证明）

在上述八顶点、\(\mathbb F_2\)、connected-corridor sector 中：

1. 任意九边图的四重 Massey 乘积若按 R21 定义，则必含 \(0\)；实际上所有 \(64\) 个标号九边图都可定义且 top class 为零。
2. 因而非平凡四重积至少需要十条边。
3. 十边时，这一下界可达到；在 \(816\) 个标号 connected-corridor 图中：

   \[
   \begin{array}{c|r}
   \text{状态}&\text{数量}\\\hline
   \text{pair obstruction 非零}&48\\
   \text{triple obstruction 非零}&64\\
   \text{定义且 top class 为零}&688\\
   \text{定义且 top class 非零}&16
   \end{array}
   \tag{4.5}
   \]

4. 这 \(16\) 个标号非零图在每个 \(J_i\) 内交换两个顶点后属于同一个未标号类型。

#### 十边闭式判据

三个相邻 corridor 必各为 \(K_{2,2}\) 删除一条边。写被删边为

\[
e_{12}=x_1^{\alpha_1}x_2^{\beta_2},\qquad
e_{23}=x_2^{\alpha_2}x_3^{\beta_3},\qquad
e_{34}=x_3^{\alpha_3}x_4^{\beta_4}.
\tag{4.6}
\]

十边图非平凡，当且仅当唯一额外边与内部端点满足

\[
\boxed{
\beta_2\ne\alpha_2,
\qquad
\beta_3\ne\alpha_3,
\qquad
e_{\mathrm{extra}}=x_1^{\alpha_1}x_4^{\beta_4}.}
\tag{4.7}
\]

换言之，两侧相邻缺边在每个内部支撑块 \(J_2,J_3\) 选取相反顶点，而唯一长边连接首尾缺边的外端点。

一个代表为

\[
e_{12}=x_1^0x_2^0,
\quad e_{23}=x_2^1x_3^0,
\quad e_{34}=x_3^1x_4^0,
\quad e_{\mathrm{extra}}=x_1^0x_4^0.
\tag{4.8}
\]

#### 有限证明结构

- 九边时，三个相邻 corridor 都恰为一棵 \(K_{2,2}\setminus e\) 树，且没有非相邻边。按四个支撑块内的 \(S_2\)-作用，只有四个内部端点相对型；逐型代入 R21，top curvature 均为边界。
- 十边时，相邻边总数只能是 \(9\) 或 \(10\)。因此每个候选都可由一个九边基图增加一条环境边得到。
- 程序枚举全部 \(\binom{24}{9}\)、\(\binom{24}{10}\) 子图后先施加 corridor 连通筛选，再逐层求根归一化 potential；结果为 (4.5)。
- 独立检查 `observed_nonzero == pattern_(4.7)`，从而不是仅有计数吻合，而是闭式分类吻合。

验证脚本：`verify_r22_n4_extremal.py`。其标准输出为：

```text
9-edge connected-corridor graphs: 64 {'defined_zero': 64}
10-edge connected-corridor graphs: 816 {'defined_zero': 688, 'pair_fail': 48, 'triple_fail': 64, 'defined_nonzero': 16}
10-edge nonzero graphs matching closed form: 16
R22 exhaustive verification: PASS
```

### 4.3 现实数学意义

R22 不是纯形式重写：

- 它给出了文献中最低次数高阶 Massey 构造的一个真正 extremal 下界；
- 它把四重非线性耦合首次压缩为唯一的十边组合型；
- 该组合型可直接转回八顶点单纯复形、moment-angle complex、Stanley–Reisner/Tor 代数中的非形式性证书；
- 判据是可执行的，能用于数据库搜索与小顶点反例排除。

但其外推范围必须诚实限定：R22 目前只覆盖 \(\mathbb F_2\)、四个二点不交支撑、最低 simplicial-degree 且 proper corridors 连通的 sector。

---

## 5. 第五步：Frozen core 扩展审计

### 5.1 预先设定的门槛

只有当同一 doctrine 在至少三个**相互独立的自然数学领域**中分别产生非平凡、可检验、不是定义改写的定理，才考虑修改 Frozen core。抽象一般化本身不算一个自然领域；同一生态内的特例与推广不能重复计数。

### 5.2 证据矩阵

| 候选领域 | 本轮产出 | 非平凡性 | 独立性计数 |
|---|---|---:|---:|
| Moment-angle / toric topology | R17、R18、R21、R22；尖锐十边分类 | 高 | 计 1 |
| Cone polyhedral products | R20 坐标收缩、Künneth-admissible 成本与 cube universality | 中高 | 与上一项同一生态，不另计 |
| 一般 support-graded DGA | R19 split excision 与 cost theorem | 高，但为抽象框架 | 不计自然领域 |
| pro-\(p\)/Galois 上同调 | R16 可与 Dwyer unitriangular lifting 对接 | 本轮未推出新的 support-cost/excision 定理 | 不计 |
| Lie algebra / deformation theory | Maurer–Cartan 语言相容 | 本轮没有新的具体对象定理 | 不计 |

### 定理 R23（Core-Promotion Audit Verdict）

截至 R22，候选 doctrine 已满足：

1. 有一般抽象定理；
2. 在一个重要自然生态中有非平凡推广；
3. 有新的尖锐有限分类和可执行证书；
4. 没有发现与 Frozen v1.0 的矛盾。

但它尚未满足“三个独立自然领域”门槛。因此正式结论是

\[
\boxed{\text{不修改 Frozen core；建立 Candidate Extension Layer v0.2。}}
\tag{5.1}
\]

这不是理论失败，而是证据分布尚不够广。若现在升级核心，会把一个在 toric topology 中证据很强、但跨领域尚未验证的模式误写成普适原则。

### 5.3 下一轮真正有判别力的任务

要改变 (5.1)，下一步不应继续堆积同类 polyhedral-product 例子，而应完成至少两个跨域检验：

1. **pro-\(p\)/Galois sector：** 把 support-excision/cost 具体化为 unitriangular representation lifting 的子商或生成元支撑定理，并产生一个新的 arity/局部性结论；
2. **deformation/Čech sector：** 在有覆盖支撑或局部 Artin 参数支撑的 DGLA/L\(_\infty\) obstruction tower 中证明 split excision，并找出严格等号案例。

只有这些检验产出对象级新定理，而非仅仅重新解释已知 Maurer–Cartan 方程，核心升级才有充分依据。

---

## 6. 文献锚点

1. J. Grbić and A. Linton, *Non-trivial higher Massey products in moment-angle complexes*, arXiv:1911.07083. 该文给出 full-subcomplex/Hochster cochain 模型、高阶 defining systems，以及对 cone polyhedral products 的推广方向：<https://arxiv.org/abs/1911.07083>。
2. A. Bahri, M. Bendersky, F. R. Cohen, S. Gitler, *A Cartan formula for the cohomology of polyhedral products and its application to the ring structure*, arXiv:2009.06818. 该文给出 natural stable splitting、full subcomplex 标号及乘法结构：<https://arxiv.org/abs/2009.06818>。
3. C. Quadrelli, *Massey products and the elementary type conjecture*, arXiv:2203.16232，命题 2.7 复述 Dwyer 的 unitriangular 表示判据：<https://arxiv.org/abs/2203.16232>。
4. I. Limonchenko and D. Millionshchikov, *Higher order Massey products and applications*, arXiv:2002.10050，综述 Massey/formal-connection/Maurer–Cartan 与 Lie、deformation、toric topology 的联系：<https://arxiv.org/abs/2002.10050>。

---

## 7. 最终状态

- 第一步：完成。
- 第二步：完成，得到 R19。
- 第三步：完成，得到 R20。
- 第四步：完成，得到 R21–R22，并有通过的穷举验证程序。
- 第五步：完成，得到 R23；审计结论为暂不升级 Frozen core。

本轮最重要的新数学结果是 R22：**connected-corridor 的最低支撑四重 Massey 非平凡图，其尖锐边数为十，且十边极值图只有一个未标号类型。**
