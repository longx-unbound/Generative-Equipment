# 领域定理与应用附卷
## 以可独立核验的数学命题代替自我评级

以下给出代表性证明，并注明它们与原稿的关系。未在此重写的长证明仍归档在原稿，地位见账本；本附卷不等于整个 R1–R35 或 DHH 依赖链的重新证明。

# A. 真正的跨尺度反例：没有统一有界局部测试

固定无限正则基数 κ。对 α<κ，令离散空间

\[
T_\alpha=\{\beta<\kappa:\beta\ge\alpha\},
\]

并对 α≤β 取包含 `T_β→T_α`。

任意少于 κ 个索引组成的子系统，索引集合在 κ 中有界。因此交集包含其上确界，逆极限非空。整个系统的交集为空，所以其极限为空。由于这是0-截断空间的图式，其空间极限仍为相应集合极限。

\[
\boxed{\text{所有}<\kappa\text{的小子系统可解，不推出全系统可解。}}
\]

该例只用正则性、离散空间和逆极限；它排除无条件统一有界测试秩，不排除在紧致或 ML 假设下的正面定理。源：GE-R1/R2 [S07–S08]。

# B. 普通 Massey 与区间齐次模型的正确比较

设 A 是 F2 上的幺 DGA，有限顶点集 J 给支撑分解

\[
A=\bigoplus_{S\subseteq J}A_S,\quad dA_S\subseteq A_S,
\quad A_SA_T\subseteq A_{S\cup T}.
\]

固定互不相交支撑 J_i 与齐次闭元 `a_i∈A_(J_i)^{q_i}`。对 proper interval I=[i,j]，令

\[
r_I=\sum_{k=i}^j q_k-(|I|-1),\qquad J_I=\bigcup_{k=i}^jJ_k,
\]

\[
Q_I=\bigoplus_{S\ne J_I}A_S.
\]

## B1　充分齐次化定理

若对全部 `2≤|I|<n` 都有 `H^{r_I}(Q_I)=0`，则任何固定输入的普通 defining system 能被三角规范变换改为区间齐次系统，并保持顶端 Massey 同调类。

### 证明的完整归纳机制

用 n+1 阶严格上三角矩阵 M 编码系统，M_(i,j) 对应输入区间 `[i,j−1]`，全长顶项暂取0。令 `s_1=0`、`s_(i+1)=s_i+q_i−1`，矩阵单位 E_(ij) 的次数设为 s_i−s_j。则所有定义项的总矩阵次数均为1。

在 F2 上，proper defining equations 恰是

\[
F(M)=dM+M^2
\]

除顶右角外为零。假设已经规范化所有宽度小于 ℓ 的项。宽度 ℓ 的曲率方程右侧是较小区间项的乘积，因此支撑仅在 J_I。该项的 off-support 部分 z 是闭元。由假设存在 h∈Q_I，次数 r_I−1，使 dh=z。

取总次数0的 `H=hE_(ij)`，令 `U=1+H`。它可逆，作

\[
M^U=U^{-1}MU+U^{-1}dU.
\]

当前宽度只增加 dh，从而消去 z；乘法交叉项只影响更大宽度，不改变此前已规范化的项。曲率满足

\[
F(M^U)=U^{-1}F(M)U.
\]

由于 F(M) 只在顶右角，严格上三角规范不改变这个中心位置的曲率。变换可能产生顶右角 defining coefficient；把该顶项重置为0，仅改变顶曲率一个边界。按宽度归纳完成。

每个区间齐次系统原本就是普通系统，反向包含显然。因此两类 fixed-input Massey 取值集合相等。不同闭元代表的通常不变性另外按标准 Massey 理论使用。证毕。

这是 GE-R29 的**受限而可使用的版本**，不在此宣称任意特征的符号版本，也不把 off-support 群非零当成必然非完备。

## B2　Hochster 方程的准确支撑范围

最低输入次数3、区间长 ℓ 时，entry总次数2ℓ+1，而 S分量为

\[
A_S^{2\ell+1}\cong\widetilde C^{2\ell-|S|}(K_S).
\]

当 `|S|=2ℓ+1`，右侧可能是 augmented degree−1，不能把这个 raw vector space 说成零。它对应全-u单项式。

在已求解较小宽度并知道其支撑大小≤2×宽度时，当前曲率右侧的支撑大小≤2ℓ。于是 |S|=2ℓ+1 的分量满足 da=0；对非空顶点诱导复形，`d:C^-1→C^0` 把1送成非零常数，所以该系数确实必须为零。这是**解方程后的归纳结论**。

因此可用的齐次化充分条件是全部相关

\[
\widetilde H^{2|I|-|S|}(K_S;\mathbb F_2)=0\quad(S\ne J_I).
\]

一般 ordinary 一骨架不可决定性尚不能仅由这个分解推出。[S27]

## B3　十边反例与更大分类分离

S45 的单例给定四个输入 a_i、五个 proper fillers，然后构造五次非区间闭元 z,t，使

\[
za_3=a_2t=zb_{34}=0,\qquad zt=\Omega.
\]

替换 `b12→b12+z`、`b34→b34+t` 后，所有 proper方程保持，顶曲率在 F2 上成为0。因此 ordinary product含0。

本版实际重跑该脚本；结果留存 `evidence/r22_counterexample_run.txt`。与之不同，S38 的512000图总分类尚缺对应的完整可复核证据，仍是 REPORT。一个精确反例不能充当整个分类的验证。

# C. 四方向 DGLA 例子的更简洁正规形

在特征零域 k 上取 L⁰=0、

\[
L^1=\langle v_1,v_2,v_3,v_4,e_{12},e_{34}\rangle,
\quad L^2=\langle p_{12},p_{34},w\rangle.
\]

令 de12=p12、de34=p34；其余微分零。唯一非零基本括号为

\[
[v_1,v_2]=-p_{12},\quad[v_3,v_4]=-p_{34},\quad[e_{12},e_{34}]=w,
\]

L²中心。度1括号对称，所有 Jacobi 嵌套括号零；d的导子条件由中心性满足。

## C1　整个普通 Artin MC 函子的显式方程

对任意局部 Artin k-代数 B，写

\[
x=\sum_{i=1}^4 a_iv_i+s e_{12}+t e_{34},\quad a_i,s,t\in\mathfrak m_B.
\]

直接展开：

\[
dx+\frac12[x,x]
=(s-a_1a_2)p_{12}+(t-a_3a_4)p_{34}+st\,w.
\]

所以 MC 条件精确等价于

\[
s=a_1a_2,\quad t=a_3a_4,\quad a_1a_2a_3a_4=0.
\]

因此在**普通 Artin 参数上的集合值 MC 函子**层面，有自然表示

\[
\boxed{k[[a_1,a_2,a_3,a_4]]/(a_1a_2a_3a_4).}
\]

L⁰=0，所以没有通常的度0 gauge需要再商。这里不宣称普通环的结论已经刻画所有 derived 参数上的增强形式模问题。

这使 ENDO-6 的例子透明化：它就是一个四重正常交叉方程的DGLA模型，而不是仅靠复杂障碍术语才能看见的未知机制。

## C2　完全饱和的方向失败

在 `B4=k[ε1,…,ε4]/(ε_i²)` 中固定一阶系数 vi，意味着

\[
a_i=\varepsilon_i+\text{至少二阶项}.
\]

乘积 a1a2a3a4 的 ε1ε2ε3ε4 系数恒为1，因为任何高阶修正使总次数至少5，而 B4 中全部总次数≥5项为零。

所以无论怎样修改二、三、四阶系数，全 MC 方程都失败。任意proper标签子集则可把缺少的 a_i设为0，立刻可解。

等价地，punctured obstruction在 `H²(L)=kw` 中恒为[w]，饱和像为单点{[w]}。

**地位：**这是完整的显式例子与派生正规形；没有文献首创或普遍方法优势认证。[S37]

# D. 三方向与小扩张：保留选择层次

## D1　三方向完整商障碍

固定闭的一阶方向 vi，并假设 `dx_ij+[vi,vj]=0` 可解。令

\[
\Omega_3=[v_1,x_{23}]+[v_2,x_{13}]+[v_3,x_{12}],
\]

\[
I_v=\sum_i\operatorname{ad}_{[v_i]}H^1(L).
\]

改变 pair filler 的差为闭元，故顶障碍的变化恰在 I_v内。于是

\[
[\Omega_3]\bmod I_v=0
\iff\text{存在具有这些singleton coefficients的完整MC三立方体}.
\]

必要性来自完整解。充分性：用三个闭元修改 pair fillers 抵消H²类，再取顶系数消去其边界代表。此处 pair choices没有额外耦合方程；四方向不再具有这个简单线性商结论。[S27]

## D2　非分裂 small extension 的曲率

设 `0→I→B'→B→0` 且 `m_(B')I=0`。取线性 section s，定义

\[
\mu_s(b,c)=s(b)s(c)-s(bc).
\]

对 `x=∑x_a⊗b_a∈MC(L⊗m_B)`，其线性提升的曲率是

\[
\frac12\sum_{a,b}[x_a,x_b]\otimes\mu_s(b_a,b_b).
\]

Bianchi恒等式给闭性；换lift只改变一个 d-边界，因为含I的交叉项被small条件杀掉。所得H²(L)⊗I类零，当且仅当能加入一个I值一次修正完成提升。

这属于标准变形障碍理论的显式相对公式，不是项目首次建立H²障碍。[S27]

# E. pro-p 与中央粘合

设 `G=G1 amalg_H G2` 具有所用类别中的推积泛性质；中央扩张 `1→A→Q→Qbar→1` 适配该类别。固定 `barρ:G→Qbar`，并假设局部提升 ρ1、ρ2存在。

差值

\[
\delta(h)=\rho_1(h)\rho_2(h)^{-1}\in A
\]

由中央性成为同态。改变局部lift恰好用 `Hom(G_i,A)` 相乘，因此剩余类属于

\[
\frac{H^1(H;A)}{\operatorname{res}H^1(G_1;A)+\operatorname{res}H^1(G_2;A)}.
\]

其为零 iff 两个局部lift可调整为在H上相同，推积便给全局lift。连续／pro-p版本使用连续同态与连续H¹。

此为**固定表示**的完整判据。对整个Massey tuple还要遍历全部允许的 defining representations；商共轭也不能自动逐因子分开。[S26–S27]

# F. 有限可见性与 SNT：保留正确组合证明

## F1　群像的有限指数夹逼

固定horizon n，若所有高层自同伦等价像 `I_(n,m)` 都包含同一有限指数子群 H，则这些下降像最终稳定。原因是含H的中间子群只有有限多个：可先取H在ambient群中的有限指数正规core，再在有限商中考虑子群。

注意 H 必须独立于m；仅仅每个I_(n,m)分别有限指数不够。

## F2　奇维球楔的组合结论

令 `W=∨_(i=1)^r S^(2d_i+1)`，d_i≥1。Hilton–Milnor把ΩW分解成连通度趋于无穷的奇球loop weak product。固定n，只有有限因子影响Pn，故

\[
\Omega W\simeq Y_n\times Z_n,\quad P_nZ_n\simeq *,
\quad Y_n\simeq\Omega\bigl(\prod_{j=1}^{s_n}S^{N_j}\bigr),
\]

各N_j奇数。球乘积是有限、单连通的 rational H-space。McGibbon–Møller 的 Theorem5与Theorem3给

\[
\operatorname{im}\bigl(\operatorname{Aut}(Y_n)\to\operatorname{Aut}(P_nY_n)\bigr)
\]

有限指数。每个Y_n自等价通过 `f×id_(Z_n)` 延拓到ΩW，所以ΩW的高层像含该同一子群。F1逐n给ML，Wilkerson/MM的结论给SNT(ΩW)=*。[S40; B10]

该证明是经典输入的组合。MM原文Theorem3允许其所述Z_P有限型条件，Theorem5也有局部版本；局部应用必须保留这些范围。本版不以局部版本“未经检查”为由错撤回它，但也不由局部刚性宣布integral torsion attachment问题已解决。

**优先权：**未建立。此前“第一个publication-level新定理”的评级撤回，保留“可供独立审稿的组合论证”。

# G. DHH 的当前接口而非完整证明

目标仍是

\[
\mathsf{Gra}[W_A^{-1}]\simeq\mathsf{Spc}.
\]

本次归档的 R96 声称 PBFT6 与 `N1D6≃S4`，下一局部目标为 `H7(N1A2^6,B6)`。这些作为来源快照，不在本卷独立认证全依赖链。

若已经另证相容有限阶段等价，最终要证明的是图局部化映射空间与正确目标截断塔的比较，以及对象实际化。不能把旧错误的 `τ≤n Map ≃ Map(τ≤n-,τ≤n-)` 当成引理。

“局部carrier维数越来越高”与“全局实际化越来越接近”没有统一完成百分比。PBFT可以是有效工具，但其到任意图式实现、相干性和无限阶段的桥梁必须逐个证明。
