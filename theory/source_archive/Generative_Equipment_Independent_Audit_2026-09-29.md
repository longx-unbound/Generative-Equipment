# Generative Equipment 独立审计：证明边界、反例与发展预测

日期：2026-09-29。审计基线：Frozen v1.0；资料库主线截至 R24–R27。

本记录不修改冻结核心，不覆盖原研究文件，不自行分配新的 R 编号。它区分数学正确性、适用范围、文献新颖性和实际求解能力。文献对照并非穷尽检索；没有为整个定理包作证明助理形式化认证。

## 1. 总判断

Generative Equipment 已经形成有实质数学内容的实现问题组织框架和支撑敏感障碍工具箱。最可靠的增量包括：精确区分存在性与选择空间、全局与逐项可解、primary arity 与 Postnikov 层数、整个支撑上的收缩与区间齐次限制。

但“可以编码三个领域”不等于“在三个领域都产生了独立的新求解技术”。R24 的基本因子化来自自由积泛性质，R26 来自参数环的分裂，R27 的固定边界 H² 障碍属于小扩张的 Maurer–Cartan 障碍论。它们可以有组织和应用价值，却不能仅因改用本项目语言就认定为新的基础理论。

本次独立审计得到两个明确修正：

1. R22 的代表十边图，其普通四重 Massey 乘积包含 0。受限于区间齐次 defining systems 的非零结果不能直接提升为普通 Massey 非平凡性或非形式性证书。
2. R27 检测指定的相容 proper-face 数据能否扩张，不能仅据一个非零障碍就断定其一阶方向在任何高阶补全中均不可实现。

这些问题位于派生结论的量词和适用范围，并不直接否定 Frozen v1.0。

## 2. 核心的表达能力与预测能力必须分开

核心以预先给定的配置、问题 proarrow、饱和 doctrine、实际/形式比较函子和持续观察为输入。它正确组织这些数据，但尚没有从一个未指定目标的数学环境中唯一导出所有这些输入的机制。

例如任取集合 F 及子集 E，视为离散范畴，比较函子 E → F 的有效化子集正是 E。由此可知：只允许任意比较函子而不增加结构限制，不会产生一个非平凡的普遍有效化判据。实际预测力必须来自对比较函子、支撑分解、相干条件、连通度、单值性及可计算性的额外定理。

新颖性也相对于观察 doctrine。常值观察不能区分对象，分离性更强的观察能够区分更多对象。数学对象在一个 doctrine 下的新颖性，与一个定理是否已见于文献，是不同问题。

## 3. R22 的显式反例证书

### 3.1 图与模型

系数为 F₂。设 Jᵢ = {pᵢ,qᵢ}，i=1,2,3,4。三个相邻 K₂,₂ 分别删除边

- p₁p₂；
- q₂p₃；
- q₃p₄。

唯一非相邻边为 p₁p₄，其余非相邻边均不存在。这正是 R19–R23 文稿式 (4.8) 的十边代表图。令 K 为这个无三角形的图，视为单纯复形。

使用标准 moment-angle cellular/Koszul DGA：

\[
R_K=\frac{\Lambda(u_v)\otimes\mathbb F_2[K]}{(u_vv_v,v_v^2)},
\qquad |u_v|=1,\quad |v_v|=2,\quad du_v=v_v,\quad dv_v=0.
\]

这里 Λ 仍施加 uᵥ²=0；面环施加所有非面的 v-单项式为零。令

\[
c(v;S)=v_v\prod_{w\in S\setminus\{v\}}u_w.
\]

它的次数是 |S|+1；其微分对应诱导图 K_S 中与 v 相邻的边。两个支撑有交集的单项式，其乘积为零。

取 aᵢ=c(pᵢ;Jᵢ)。它们是四个非零三次上同调类的代表。

### 3.2 一个区间齐次系统

令

\[
b_{12}=0,\quad b_{23}=c(p_3;J_2\cup J_3),\quad
b_{34}=c(p_4;J_3\cup J_4),
\]
\[
b_{123}=0,\qquad b_{234}=c(p_4;J_2\cup J_3\cup J_4).
\]

则

\[
db_{12}=a_1a_2,\quad db_{23}=a_2a_3,\quad db_{34}=a_3a_4,
\]
\[
db_{123}=a_1b_{23}+b_{12}a_3,\qquad
db_{234}=a_2b_{34}+b_{23}a_4.
\]

顶端曲率为

\[
\Omega=a_1b_{234}+b_{12}b_{34}+b_{123}a_4
=v_{p_1}v_{p_4}\prod_{w\ne p_1,p_4}u_w.
\]

这是 full support 上的唯一长边 cochain。它在环

\[
p_1-q_2-q_1-p_2-p_3-p_4-p_1
\]

上的取值为 1，而顶点 cochain 的边界沿闭环求和为 0。因此该曲率在 full-support cochain complex 中非正合。

### 3.3 普通 defining system 的额外选择

定义五次闭元

\[
z=c(p_1;J_1\cup J_3),\qquad t=c(p_4;J_2\cup J_4).
\]

两个支撑诱导图都是离散图，故 dz=dt=0。更改

\[
b'_{12}=z,\qquad b'_{34}=b_{34}+t,
\]

其余三个 fillers 不变。由于

\[
za_3=0,\qquad a_2t=0,
\]

全部 proper defining equations 仍成立。并且

\[
zb_{34}=0,\qquad zt=\Omega.
\]

因此

\[
\Omega'=\Omega+zb_{34}+zt=0.
\]

取顶端 filler 为 0，即得完整 defining system，故

\[
\boxed{0\in\langle[a_1],[a_2],[a_3],[a_4]\rangle_{\mathrm{ordinary}}.}
\]

### 3.4 精确影响

反例不推翻 R19 的整个支撑收缩：z 和 t 都仍位于同一个全支撑中。它推翻的是把每个矩阵元限制在其指定区间支撑后，未经证明就将不存在受限解提升为不存在任意解。

R22 可以改述为区间齐次匹配系统的有限分类；本次并未重新穷举其所有计数。普通 Massey 非平凡性和由此得到的非形式性证书必须撤回或另行证明。本反例并不证明 Z_K 是形式空间。

附带的 verify_r22_counterexample.py 仅对这个图作精确 F₂ 代数核验，检查五个 proper equations、闭元修正和顶端抵消，没有进行图搜索。

## 4. R27 的固定边界与一阶方向

R27 的核心定理对指定 punctured cube x 正确：

\[
o_J(x)=[\Omega_J]\in H^2(L),\qquad
x\text{ 可补入顶系数}\iff o_J(x)=0.
\]

但障碍依赖整个 proper-face 数据，而非只依赖一阶方向。

取特征零的二步幂零 DGLA

\[
L^1=\langle a,b,c,u\rangle,\quad L^2=\langle w\rangle,\quad d=0,
\]

唯一非零括号为 [a,u]=[u,a]=w，w 为中心元，其他次数为零。Jacobi 恒等式因为所有二重嵌套括号均为零而成立。

在 B₃=k[ε₁,ε₂,ε₃]/(ε₁²,ε₂²,ε₃²) 中取

\[
x=a\varepsilon_1+b\varepsilon_2+c\varepsilon_3+u\varepsilon_2\varepsilon_3.
\]

它的所有 proper-support 曲率为零，但

\[
dx+\tfrac12[x,x]=w\varepsilon_1\varepsilon_2\varepsilon_3.
\]

因 d=0，这个指定边界不能通过增添顶系数填充。然而

\[
x'=a\varepsilon_1+b\varepsilon_2+c\varepsilon_3
\]

已经是完整 MC 元，具有完全相同的一阶方向。

所以：指定相容边界不可填充，不推出同一组一阶方向在所有高阶选择中都不可实现。一般 DGLA 层面已经有这个反例；对具体 coherent sheaf 要得出方向级不可实现性，仍须控制所有相容高阶边界选择。

最小修订是把结论限定为“该指定 proper-face 族不可扩张”，或者研究同一一阶数据上所有障碍值组成的对应，而不是选中的单个 H² 类。

## 5. 哪些成果应保留

R3–R4 的 Reedy/主丛障碍解释有可靠标准基础；R5–R12 不应抹去 R13 已记录的非阿贝尔形式化、有限多项式性、可行性集合计算循环及复杂度边界。

R15 的 cup-power 族给出真实的两阶段、任意高耦合次数例子。R16 在常系数、普通单值 primary 操作及明确 correction action 的条件下给出

\[
\deg\operatorname{Coupl}\le\lfloor q/r\rfloor,
\]

并在相应 simply connected N-type sector 达到

\[
\lfloor(N+1)/2\rfloor.
\]

该证明宜用坐标幂等投影和稳定分裂明确识别 full-smash summand，再应用连通度，而不是仅凭每个坐标面上分别限制为零就忽略并集相干性。

R17、R19、R20 的整个支撑收缩、最低支撑代价及等号交叉多面体几何可以保留。它们不自动证明区间齐次系统对普通 defining systems 的完备性。

R24–R25 在指定有限自由 pro-p 积、固定输入和带标架表示集合层面成立。商掉共轭以后，不能把对角作用的商群胚自动等同于各因子商群胚的乘积。

R26 作为参数环分裂的函子性结论成立。R27 作为固定边界的小扩张障碍定理成立；其方向级解读需要上节修订。

## 6. 可检验的发展预测

### 6.1 优先研究饱和后的支撑障碍

应区分区间齐次 defining systems 与全部 defining systems，并研究它们的完整填充空间之间的比较。R22 的真正误差来自一个双线性交叉项 zt，而不是算术误差。

对四重系统，在 dz=dt=0、za₃=a₂t=0，且其余 fillers 固定的情形，顶曲率变化为

\[
\Delta\Omega=z b_{34}+b_{12}t+zt.
\]

未来判据必须控制这个交叉修正。一个有判别力的候选充分条件是：所有不允许支撑上的相关 filler-degree 上同调消失，进而尝试通过三角规范变换实现齐次化。不能在没有证明前把这个候选写成普遍定理。

### 6.2 非分裂粘合的第一个修正已经可精确预期

设 G=G₁ *ₕ G₂ 是 pro-p 范畴中的推出，给定中央扩张 1→A→Q→Q̄→1 和固定的相容 Q̄-表示。假设两个局部 Q-提升已存在。它们在 H 上之差是连续同态 δ:H→A。

改变两个局部提升分别增加来自 Hom_cont(G₁,A)、Hom_cont(G₂,A) 的限制。因此存在全局提升当且仅当

\[
[\delta]=0\quad\text{于}\quad
\frac{H^1(H;A)}{\operatorname{res}H^1(G_1;A)+\operatorname{res}H^1(G_2;A)},
\]

这里 A 的作用平凡，上同调连续。证明只需中央性和推出泛性质：差值是同态，调整提升改变差值一个限制项，差值可消去恰好等价于两提升可粘合。

所以仅证出这个第一修正不是新的决定性障碍理论。更有价值的目标是处理非中央、带规范对称、分支相关或高阶相干的粘合，并在具体对象上得到新的可用答案。

### 6.3 复杂度与实际作用

多项式数量的二次方程并不等于多项式时间算法；有限层数不界定每层分支数。必须固定输入编码、系数域、预处理、支撑宽度和对照算法。

R14 的错误线性截断不是一个足够强的基线。实际优势须与保留完整经典障碍的直接方法比较，而不是仅证明丢弃二次项会出错。

较有根据的发展方向是支撑稀疏、相干宽度受控的专门算法或饱和障碍判据；现有证据尚不足以预测一个普适的数学创造定律或任意实现问题求解器。

## 7. 最小治理调整

保持 Frozen v1.0。派生账本分别标注 R22 的受限系统范围、R27 的固定边界量词和 R24 的带标架范围。优先修补代表限制到内在障碍之间的比较，再开展非分裂跨域推广。

不以报告轮数、定理名称数量、三个领域的计数或已通过的程序断言代替数学新增量。决定性验收应是：饱和后仍成立、能独立于本项目表述、明确超出已有工具的简单重命名、且解决一个有价值的具体问题。

## 8. 来源定位

用户研究稿：Frozen v1.0 MASTER RECORD；R13 Strict Reality Audit；R14 Reality Benchmarks；R15 Higher Coupl；R16 Optimal Arity；R17 Support and Cube Universality；R19–R23 Five-Step Generalization，尤其 §§2.2、4.1–4.3；R24–R27，尤其 §§1、2.3–2.5；verify_r22_n4_extremal.py。

标准背景核对：

- J. Grbić and A. Linton, Non-trivial higher Massey products in moment-angle complexes, arXiv:1911.07083，§2，尤其 Theorem 2.1 和 Definition 2.3。
- C. Quadrelli, Massey products in Galois cohomology and the elementary type conjecture, arXiv:2203.16232，Proposition 2.7。
- S. Blumer, A. Cassella, C. Quadrelli, Groups of p-absolute Galois type that are not absolute Galois groups, arXiv:2112.06744，§5.1。
- M. Manetti, Deformation theory via differential graded Lie algebras, arXiv:math/0507284，小扩张及 Maurer–Cartan 的 H² 障碍。
- D. Fiorenza, D. Iacono, E. Martinengo, Differential graded Lie algebras controlling infinitesimal deformations of coherent sheaves, arXiv:0904.1301。

以上核对足以辨认主要经典工具，但不是穷尽的原创性检索。
