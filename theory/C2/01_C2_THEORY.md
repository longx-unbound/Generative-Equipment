# Generative Equipment / 数学内生生成性
## C2：面向 AI 数学创造的结构、实现与搜索理论

版本日期：2026-09-30。基础规范：Frozen v1.0（2026-09-23）。

C2 保留 Frozen v1.0 的 primitive core，不新增核心公理；在 C1 的严格实现之上补充六个派生模块。本文给出这些模块的定义、适用条件、证明和反例。研究目标是使 AI 能够提出可检验的数学问题、改变表示、构造对象并检验结论；该目标不等于已测得 AI 能力增益。

## 0. 版本、范围与记号

Frozen core 原文见 `baseline/01_FROZEN_CORE.md`。C1 的对象实现、饱和、matching、horizon、语言恢复与相干修补继续有效，但必须携带各自假设。C2 不把原有领域报告升级为定理，也不以本文替代 C1 各领域附卷。

以下固定嵌套宇宙，所有“集合”“小图式”“小乘积”“小 coend”均相对指定宇宙。普通范畴与无穷范畴分开使用：§1 主要使用空间值无穷范畴；§3 的独立性模型、§4 的完整 pro 表示证明以及§5–7 的算法性命题有明确的普通范畴／集合值范围。不得把这些范围静默扩大。

“定义”只给出对象；“命题／定理”附证明或明确的经典输入。本文的证明并不表示文献首次性。来源对应与评估位于 `02_EVALUATION_AND_TESTS.md`，不穿插研究过程记录。

---

# 1. 继承的数学基础

## 1.1 预目标、饱和与可能性

给配置

\[
\Xi=(S,\Omega,\mathrm{Prov},\text{允许的等价、构造与观察}),
\]

以及在求解前确定的横向问题

\[
P:\mathcal I^{op}\times\mathcal B\longrightarrow\mathcal S.
\]

其中 \(\mathcal I\) 是问题范畴，\(\mathcal B\) 是候选范畴。饱和 \(P\mapsto P^\sharp\) 由指定语义决定，而不是由期望答案决定。如果输入域也被局部化，记录 \(\lambda_{\mathcal I},\lambda_{\mathcal B}\)。当所需左 Kan 扩张存在时，域扩张可写为

\[
\operatorname{Lan}_{\lambda_{\mathcal I}^{op}\times\lambda_{\mathcal B}}P,
\]

但其是否忠实于题目仍须独立检查。

饱和需要等价下的相干运输（Sat-N）。需要 evaluation 的构造还须证明 evaluation 降到饱和输入（Sat-Eval）。不能把 raw evaluation 的存在当作商上 evaluation 的存在。

固定输入 \(a\)，置

\[
H_a=P^\sharp(a,-),\qquad
\mathfrak G(a)=\int H_a,\qquad
\mathcal M(a)=\mathfrak G(a)^\simeq.
\]

这里的元素无穷范畴由空间值函子的 unstraightening 给出。一般丰富化环境不直接套用这个公式。

**命题 F1（对象化）。** \(H_a\simeq\operatorname{Map}(b_a,-)\) 当且仅当 \(\mathfrak G(a)\) 有初始对象。初始对象的子空间若非空则可缩，不推出整个 \(\mathcal M(a)\) 可缩。

**证明。** 元素 \(u\in H_a(b_a)\) 给出 Yoneda 比较。其在 \(v\in H_a(b)\) 处的纤维是元素范畴中 \((b_a,u)\to(b,v)\) 的映射空间；所有这些纤维可缩等价于初始性。初始对象的唯一性只涉及初始对象子空间。∎

普遍性是可能性几何的一个子区域，不是全部生成现象。

## 1.2 实现及其强度

给比较 \(C:\mathcal A\to\mathcal F\)，定义

\[
\operatorname{Eff}_C(\xi)
=\mathcal A^\simeq\times_{\mathcal F^\simeq}\{\xi\}.
\]

其点包括指定等价 \(Ca\simeq\xi\)，不是任意箭头 \(Ca\to\xi\)。对 \(U:\mathcal B\to\mathcal A\)，exact residue 取对象实现纤维，universal residue 取 \((a\downarrow U)\)，co-universal residue 取 \((U\downarrow a)\)；三者不可互换。

对形状包含 \(i:J\hookrightarrow I\)、形式图式 \(\sigma:I\to\mathcal F\) 和指定实际边界 \(b\)，先定义 \(\operatorname{Lift}_C(\sigma)\) 为对应函子范畴的实现纤维，再取

\[
\operatorname{ShRes}_C(i;\sigma,b)
=\operatorname{hofib}_{b}\bigl(\operatorname{Lift}_C(\sigma)
\to\operatorname{Lift}_C(\sigma|_J)\bigr).
\]

这保留边界标架和相容等价，不是逐对象非空性的列表。

**命题 F2。** \(C\) 本质满当且仅当全部对象实现纤维非空；\(C\) 为等价当且仅当它本质满且全部映射空间比较为等价。

**证明。** 第一项展开本质满的定义；第二项是无穷范畴等价的全忠实—本质满判据。仅取 core 会遗失非可逆态射。∎

比较 \(Z_0\to Z\) 必须区分：非空性等价、\(\pi_0\) 满射、空间等价和完整范畴等价。例 \(*\to\{0,1\}\) 保持存在性但遗漏分支。

## 1.3 匹配与实际化

**命题 F3（相干纤维极限）。** 对相干比较图 \(C_i\)，有

\[
\operatorname{Eff}_{\lim_i C_i}(\xi)
\simeq\operatorname*{holim}_i\operatorname{Eff}_{C_i}(\xi_i).
\]

**证明。** core 是右伴随，保持极限；极限与拉回交换。左侧实际范畴已经是 \(\lim_i\mathcal A_i\)，故本命题不重建另一个事先给定的 \(\mathcal A\)。∎

对有限逆范畴上的 Reedy fibrant 空间图式，沿下闭对象集加入 \(v\) 时，极限由

\[
\lim_{A\cup\{v\}}X\simeq\lim_AX\times_{M_vX}X_v
\]

计算。起点及每一步实际遇到的 matching 纤维非空，足以构造分支；每个这样的纤维可缩，给出相对于原边界的可缩填充空间。这是 Reedy 工具的条件性应用，不把所有二维面当成任意维完整 matching 对象。

给相干塔 \(\mathcal A_n,\mathcal F_n,C_n\) 及比较 \(\alpha,\beta\)，满足指定的 \(\widehat C\alpha\simeq\beta C\)，写

\[
\widehat{\mathcal A}=\lim_n\mathcal A_n,\quad
\widehat{\mathcal F}=\lim_n\mathcal F_n,\quad
\mathcal A_C^{\rm hor}=\mathcal F\times_{\widehat{\mathcal F}}\widehat{\mathcal A},\quad
\delta_C:\mathcal A\to\mathcal A_C^{\rm hor}.
\]

**命题 F4（两道实际化条件）。**

\[
\operatorname*{holim}_n\operatorname{Eff}_{C_n}(\xi_n)
\simeq\operatorname{Eff}_{\mathcal A_C^{\rm hor}\to\mathcal F}(\xi).
\]

全部对象纤维比较为等价，当且仅当 \(\delta_C^\simeq\) 为等价；完整范畴重建还要求 \(\delta_C\) 全忠实。

**证明。** 用 F3 及拉回结合律得到公式；在空间切片范畴中，逐纤维等价检测等价。最后应用 F2。∎

**命题 F5（可数塔的分支条件）。** 若每个实现空间非空，其 \(\pi_0\) 塔满足 Mittag–Leffler，且整体实现已经被识别为该同伦极限，则整体非空。

**证明。** 每一级稳定像非空，稳定像之间的转移满射。递归选择相容分支及相邻路径，得到同伦极限中的点。采用通常的可数选择。∎

有限非空分支集自动满足 ML；一般无限分支集不自动满足。分支上的 \(\lim^1\) 不取代 F4 的实际化比较。

## 1.4 修补、语言与观察

在可由小空间张量且余完备的无穷范畴 \(\mathcal G\) 中，给 \(u:A\to B\) 和 \(d:D\to\operatorname{Map}(A,G)\)，置

\[
P_D=G\amalg_{A\otimes D}(B\otimes D).
\]

**命题 F6（指定族的相干修补）。**

\[
\operatorname{Map}(P_D,X)\simeq
\operatorname{Map}(G,X)
\times_{\operatorname{Map}(D,\operatorname{Map}(A,X))}
\operatorname{Map}(D,\operatorname{Map}(B,X)).
\]

**证明。** 映射出推出得到拉回，再用空间张量伴随。∎

该构造解决指定参数族，不保证全部新出现实例、唯一性、忠实嵌入或其他保存契约。约束修补范畴记为 \(\operatorname{Rep}_K(\Sigma,\delta)\)。若其忘却函子有左伴随，原初始修补的自由提升是约束范畴中的初始对象；左伴随的存在仍是前提。

语言恢复继续使用 C1 的具体范围：局部有限可表示模型范畴的有限极限语言恢复；\(F\dashv U\) 时 \(\operatorname{Nat}(U^n,U)\cong U(F(n))\)；满足适当换基条件的 \(\exists_f\dashv f^*\dashv\forall_f\)；满足 Barr–Beck 条件的单子性重建。它们不由一个裸对象无条件恢复任意逻辑。

固定事件范畴、旧基线和持续观察

\[
N^\infty:\mathcal E\to\mathcal P(\mathcal K),\qquad
\operatorname{OldMatch}(e)=\mathcal E_{\rm old}^\simeq
\times_{\mathcal P(\mathcal K)^\simeq}\{N^\infty(e)\}.
\]

其空性表示相对于该观察及旧基线的新颖性。完整自然观察数据比各个不变量的无组织列表更强；它不判定文献首次性或数学重要性。

## 1.5 语义闭包、耦合与单子性接口

固定满足关系、集合大小模型范围与单调扩张操作 \(K\)。\(\operatorname{Th}\) 和 \(\operatorname{Mod}\) 给出反向Galois对应，\(\operatorname{Def}=\operatorname{Mod}\operatorname{Th}\) 是闭包。由

\[
X_{\alpha+1}=\operatorname{Def}(K(X_\alpha)),\qquad
X_\lambda=\bigcup_{\beta<\lambda}X_\beta
\]

得到最小共同不动点 \(X^*\)。集合大小保证扩张链最终稳定；稳定时
\(X^*\subseteq KX^*\subseteq\operatorname{Def}(KX^*)=X^*\)，所以两算子都固定它。\(\operatorname{Th}(X^*)\) 是这个模型范围的共同真理论；其所有模型已经满足该理论，因此新修补任务必须另行指定，不能由“违反共同真理论”自动产生。

在单值阿贝尔障碍分支，低阶选择的变化可由 \(q:A\to B\) 记录；

\[
\operatorname{cr}_2q(x,y)=q(x+y)-q(x)-q(y)+q(0)
\]

为零当且仅当 \(q-q(0)\) 加性。多值、扭曲或高阶障碍必须保留完整选择空间及零纤维，不适用时不使用单一函数表示。C1 的作用型primary阶数界仍限于其连通度、常系数及smash-product分解假设。

单子性重建须有 \(F\dashv U\)、\(U\) 保守，并具有且保持 Barr–Beck 条件要求的 \(U\)-split simplicial realization，才能得到 \(\mathcal B\simeq\operatorname{Alg}_{UF}(\mathcal A)\)。普通范畴采用对应的split coequalizer版本。它是特定忘却问题的工具，不是全部数学生成的定义。

---

# 2. EC：丰富化与定量观察

## 2.1 横向合成

固定完备、余完备、闭对称幺半范畴 \(\mathcal V\)，其张量逐变量保持所用余极限。对小 \(\mathcal V\)-范畴，取

\[
P:\mathcal A^{op}\otimes\mathcal B\to\mathcal V,
\quad Q:\mathcal B^{op}\otimes\mathcal C\to\mathcal V,
\]

并定义

\[
(Q\odot P)(a,c)=\int^{b\in\mathcal B}P(a,b)\otimes Q(b,c).
\]

单位为 hom-profunctor；结合律由 coend Fubini 与张量保持性给出。函子 \(F:\mathcal A\to\mathcal B\) 的 companion 是 \(F_*(a,b)=\mathcal B(Fa,b)\)，conjoint 是 \(F^*(b,a)=\mathcal B(b,Fa)\)。这是恢复 horizontal-first 所需的明确语义设施。

**命题 EC1（换基保持合成）。** 若强幺半函子 \(T:\mathcal V\to\mathcal W\) 保持上述 coend，则

\[
T(Q\odot P)\cong TQ\odot TP.
\]

若 \(T\) 还反映同构，则它能检测一个已给定的比较是否为同构。

**证明。** 依次交换 \(T\) 与 coend、与张量，得到右式。反映同构是保守性的定义。∎

本命题不说“在换基后的世界找到代表”就能提升出原世界代表。一般无穷丰富化需要相应派生 coend 和相干单子结构，不能用普通公式替代模型验证。

## 2.2 一个完整的度量分支

**定理 EC2（定量探针恢复）。** 对非空度量空间 \((X,d)\)，有

\[
d(x,y)=\sup_{f\in\operatorname{Lip}_1(X,\mathbb R)}|f(x)-f(y)|.
\]

若 \(S\subset X\) 为 \(\delta\)-网，定义

\[
d_S(x,y)=\sup_{s\in S}|d(x,s)-d(y,s)|,
\]

则

\[
0\le d(x,y)-d_S(x,y)\le2\delta.
\]

若 \(S\) 稠密，取任意小 \(\delta\) 的逐点近似，得 \(d_S=d\)。

**证明。** 三角不等式给所有上界。第一式取 \(f(z)=d(z,x)\) 达到等号。第二式取 \(s\) 满足 \(d(x,s)\le\delta\)，则
\(d(y,s)-d(x,s)\ge d(x,y)-2\delta\)。若只知道距离下确界不超过 \(\delta\)，先加任意 \(\eta>0\) 再令 \(\eta\to0\)。∎

有限网的存在需要全有界性。布尔“是否有点”观察无法恢复上述误差；这给出保留丰富化信息的实质理由。

---

# 3. RG：相对 residue、复合与扭曲

## 3.1 有类型的三种对象

对普通小范畴上的函子 \(Q:\mathcal X\to\mathcal Y\)，令 \(\mathcal X_y\) 为对象映到 \(y\)、态射映到 \(1_y\) 的纤维范畴。对 \(u:y\to y'\)，定义

\[
\Lambda_u(x,x')=\{f:x\to x'\mid Qf=u\}.
\]

它是 \(\mathcal X_y^{op}\times\mathcal X_{y'}\to\mathbf{Set}\) 的函子。预合成与后合成给出函子性。

**命题 RG1（相对复合）。** 对可复合的 \(u,v\)，有自然比较

\[
\mu_{v,u}:\Lambda_v\odot\Lambda_u\longrightarrow\Lambda_{vu},
\qquad [f,g]\longmapsto gf.
\]

比较满足单位和结合相干律，但一般不是同构。

**证明。** coend 的关系 \((hf,g')\sim(f,g'h)\) 在复合后都得到 \(g'hf\)。结合与单位继承自 \(\mathcal X\)。∎

记录两轴：

\[
\mathbf R:\ \Lambda_u(x,-)\text{ 是否可余表示（对所有相关 }u,x\text{）};
\quad
\mathbf C:\ \mu_{v,u}\text{ 是否为同构（对所有相关 }u,v\text{）}.
\]

这两轴既不是“对象纤维是否非空”，也不是“群扩张是否分裂”。后一问题另记为**截面／分裂问题**。

## 3.2 两轴确实独立

**命题 RG2。** \((\mathbf R,\mathbf C)\) 的四种真假组合均可出现。

**证明。** 以 \([2]=(0\to1\to2)\) 为底，由下面的纤维范畴及横向 hom 构造总范畴：对象为三个纤维的对象，不同纤维间 hom 按所列 profunctor 给出，复合用 \(\mu\)。底只有两个可复合的非恒等箭头，结合性归结为 profunctor 的自然性。

| \(\mathbf R\) | \(\mathbf C\) | 纤维及非恒等 profunctor |
|---|---|---|
| 真 | 真 | 三个纤维均为 \(*\)，三个横向 hom 均为单点 |
| 假 | 真 | 三个纤维均为 \(*\)，\(P_{01}=P_{12}=2\)，\(P_{02}=2\times2\)，复合为配对双射 |
| 假 | 假 | 三个纤维均为 \(*\)，\(P_{01}=P_{12}=2\)，\(P_{02}=*\)，复合为唯一映射 |
| 真 | 假 | 三个纤维均为 \([1]\)，\(F_{01}=F_{12}=\mathrm{id}\)，\(F_{02}=\mathrm{const}_0\)，取 \(P_{ij}(x,z)=\operatorname{Hom}(F_{ij}x,z)\) |

最后一行，\(0\to x\) 诱导比较 \(\operatorname{Hom}(x,z)\to\operatorname{Hom}(0,z)\)。在 \((x,z)=(1,0)\) 处为 \(\varnothing\to *\)，故不是同构；三个 profunctor 都可余表示。其余各行由单点范畴的唯一 representable 只有一个元素直接判断。∎

## 3.3 扭曲可以在两轴都成立时存在

**命题 RG3（扩张的扭曲）。** 对群扩张

\[
1\to K\to E\xrightarrow q G\to1,
\]

视作 \(BE\to BG\)。每个 \(\Lambda_g=q^{-1}(g)\) 是 \(K\)-bitorsor，\(\mathbf R\) 与 \(\mathbf C\) 都成立；但 \(q\) 未必有群同态截面。

**证明。** 每个 lift \(s(g)\) 将 \(q^{-1}(g)\) 与 \(K\) 的正则右作用识别，并使左作用由共轭自同构给出，故可表示。乘法

\[
q^{-1}(h)\times_K q^{-1}(g)\longrightarrow q^{-1}(hg)
\]

为双射：满性由选取 \(g\) 的 lift；两个乘积分解由唯一的中间 \(K\)-元素关联。截面是更强的数据。∎

若 \(K\) 为中心阿贝尔子群，归一化集合截面给

\[
c(g,h)=s(g)s(h)s(gh)^{-1}\in K.
\]

结合律给 cocycle 方程。换 \(s'(g)=b(g)s(g)\) 给 \(c'=\delta b\cdot c\)。所以存在群同态截面当且仅当某个截面的 cocycle 被一个 coboundary 消去。

对 \(Q_8\to C_2\times C_2\)，每个非平凡商元素的所有 lift 都有阶四，故任何群同态截面会把阶二元素送到阶四元素，矛盾。该例是 \(\mathbf R=\mathbf C=\mathrm{true}\) 但不分裂，而不是两轴独立性的证明。

## 3.4 无穷／参数版本

在空间值设置中，以映射空间的同伦纤维替换严格 hom 纤维，并给出基点运输与 homotopy coend。每个残差仅有一点、连通、可缩和可表示是不同命题。更高 coherences 必须作为结构保留；普通群例子不证明任意高阶扭曲已有计算方法。

---

# 4. ES：pro 对象、统一化与失效尺度

## 4.1 小范围中的完整 pro 表示

**定理 ES1。** 设 \(\mathcal B\) 是小的有限完备普通范畴，\(H:\mathcal B\to\mathbf{Set}\) 保持有限极限。其元素范畴 \(\int H\) 是小 cofiltered 范畴，并有

\[
H(b)\cong\operatorname*{colim}_{(a,x)\in(\int H)^{op}}\operatorname{Hom}_{\mathcal B}(a,b).
\]

因此投影 \(\int H\to\mathcal B\) 给出 pro 对象 \(\widehat a\)，由它余表示 \(H\)。

**证明。** 终对象及 \(H(1)=*\) 保证非空。两元素 \((a,x),(b,y)\) 在积及 \(H\) 保积下有共同来源。对平行态射 \(f,g:(a,x)\rightrightarrows(b,y)\)，有 \(Hf(x)=Hg(x)\)，等化子及保等化子给共同等化来源。因此元素范畴 cofiltered。公式的自然映射将 \((x,f:a\to b)\) 送到 \(Hf(x)\)。任一 \(y\in H(b)\) 由 \((y,1_b)\) 表示；两个给出同一 \(y\) 的表示，经 \(a\times_ba'\) 和保拉回得到共同细化，故此映射单射。∎

对较大范畴，C2 只在已给出小 cofiltered 表示，或已验证相应大小／solution-set 条件时调用 pro 对象。一般高阶 pro 表示使用其专门识别定理，不由 ES1 自动推广。

**命题 ES2（实际对象化）。** 对给定小 pro 对象 \(\widehat a\)，其函子 \(H(b)=\operatorname{Hom}_{\operatorname{Pro}(\mathcal B)}(\widehat a,jb)\) 可由 \(a\in\mathcal B\) 余表示，当且仅当 \(\widehat a\cong ja\)。

**证明。** 常值对象给充分性。必要性使用 pro 对象到余表示函子的反变全忠实嵌入；自然同构对应 pro 同构。该嵌入也可直接由 \(\lim\operatorname{colim}\) 的 pro-hom 公式证明。∎

## 4.2 存在的统一化与等式的统一化

固定有向小偏序 \(J\) 及集合系统 \(A_{j,i}\)。考虑

\[
\chi:\operatorname*{colim}_{j\in J}\prod_{i\in I}A_{j,i}
\longrightarrow\prod_{i\in I}\operatorname*{colim}_{j\in J}A_{j,i}.
\]

**定理 ES3（双重统一化）。** \(\chi\) 为双射，当且仅当以下两项都成立：

1. **共同表示。** 每一族右侧元素都能在一个共同阶段 \(j\) 由元组表示。
2. **共同等式。** 两个共同阶段元组若在每个坐标的 colimit 中相同，则在某个共同后续阶段全部坐标同时相同。

**证明。** 第1项等价于满射。对第2项，先将两个元组送到一个共同阶段；有向集合 colimit 中两个元素相等，当且仅当在某个后续阶段相等。分别在整元组与各坐标应用此判据，得到第2项恰为单射。∎

因此只记录 \(\forall i\exists j_i\Rightarrow\exists j\forall i\) 的见证存在形式不足以完整检验 \(\chi\)。空间值版本还要检查全部同伦纤维，不能只加一项集合单射检查就视为完成。

## 4.3 尺度与谱

对已声明所有相关积存在的 \(H:\mathcal B\to\mathbf{Set}\)，定义乘积比较 \(\chi_{I,(b_i)}\)。先记录完整比较及其纤维，再定义

\[
\rho_{\rm surj}(H)=\min\{|I|:\exists(b_i),\ \chi_{I,(b_i)}\text{ 不满}\},
\]

\[
\rho_{\rm inj}(H)=\min\{|I|:\exists(b_i),\ \chi_{I,(b_i)}\text{ 不单}\},
\qquad \rho_{\rm eff}(H)=\min(\rho_{\rm surj},\rho_{\rm inj}).
\]

无见证时以符号 \(\infty\) 表示“在指定宇宙内未出现失败”。同时定义

\[
\operatorname{EffSpec}(H)=\{\kappa:H\text{ 保持全部 }<\kappa\text{ 阶小乘积}\}.
\]

**命题 ES4。** 这些量在函子的自然同构及 pro 对象的同构下不变；\(\operatorname{EffSpec}\) 向下闭。

**证明。** 自然同构使每个比较方块的竖边都是同构，所以保留单射、满射及双射。较小族是较大基数限制下族的子范围。∎

在普通完备范畴、solution-set／可达伴随函子定理适用且 \(H\) 已保有限极限时，保全部小积使 \(H\) 保全部小极限：任意图式极限由两个积的等化子给出；再由相应伴随函子定理得实际余表示。没有这些条件，\(\rho_{\rm eff}=\infty\) 不推出可表示。

## 4.4 首次失效可以精确计算

**定理 ES5（共尾度族）。** 令 \(\lambda\) 是无限极限序数，定义

\[
H_\lambda(B)=\{f:\lambda\to B:\exists\alpha<\lambda,\ f|_{[\alpha,\lambda)}\text{ 为常值}\}.
\]

取 \(X_\alpha=\alpha+1\)，\(X_\beta\to X_\alpha\) 为 \(\xi\mapsto\min(\xi,\alpha)\)。则 \(H_\lambda\) 由此 pro-set 余表示，保有限极限，且

\[
\rho_{\rm surj}(H_\lambda)=\rho_{\rm eff}(H_\lambda)=\operatorname{cf}(\lambda),
\qquad \rho_{\rm inj}(H_\lambda)=\infty.
\]

**证明。** 过渡映射在函数上延长常值尾部，其 colimit 就是上述函数集合。保有限极限可由有向 colimit 与集合有限极限交换得出，也可逐个取有限稳定阈值的上界。

少于 \(\operatorname{cf}(\lambda)\) 个稳定阈值有共同上界，故对应乘积比较满射；逐坐标相等就是函数相等，故所有比较均单射。取长度为 \(\operatorname{cf}(\lambda)\) 的共尾阈值族 \(\alpha_i\)，并令 \(f_i(t)=\mathbf1_{t\ge\alpha_i}\)。各 \(f_i\) 最终常值，但元组函数在任何尾部都仍有坐标改变，故不是最终常值。∎

特别地 \(\rho_{\rm eff}(H_\omega)=\aleph_0\)。若 \(\lambda\) 奇异，首次失败是 \(\operatorname{cf}(\lambda)\)，不是 \(\lambda\)。

**反例 ES6（存在一致仍不够）。** 取 \(H(B)=B[1/2]\) 并忘却到集合。它由 pro-阿贝尔群 \(\mathbb Z\xleftarrow{2}\mathbb Z\xleftarrow{2}\cdots\) 余表示。

对 \(B_i=\mathbb Z/2^i\)，右侧 \(\prod_iH(B_i)=0\)，故比较满射；但 \(b=(1\bmod 2^i)_i\) 在 \((\prod_i B_i)[1/2]\) 中非零，因为没有统一的 \(2^n\) 杀掉 \(b\)。比较不单射。

对 \(B_i=\mathbb Z\)，右侧元组 \((2^{-i})_i\) 无共同分母，因此比较不满射。这两种失败机制不可互相代替。

---

# 5. IC：目标相对压缩与安全搜索

## 5.1 静态充分性与闭包

给集合 \(E\)、观察目录 \(\mathcal O\) 及 \(o_c:E\to Y_c\)。对 \(U\subseteq\mathcal O\)，记

\[
N_U:E\to\prod_{c\in U}Y_c,\qquad
x\sim_U y\iff N_U(x)=N_U(y).
\]

定义

\[
\operatorname{Cl}(U)=\{c:\ x\sim_Uy\Rightarrow o_c(x)=o_c(y)\}.
\]

**定理 IC1（目标充分性）。** \(\operatorname{Cl}\) 是扩张、单调、幂等闭包。对指定目标 \(t:E\to T\)，以下等价：

\[
\ker N_U\subseteq\ker t;
\qquad
\exists!\bar t:N_U(E)\to T,\quad t=\bar t\circ N_U.
\]

**证明。** 扩张和单调由定义。\(U\subseteq\operatorname{Cl}(U)\) 与反方向的不可区分性说明 \(\sim_U=\sim_{\operatorname{Cl}(U)}\)，故幂等。\(\bar t(N_U(x))=t(x)\) 良定义恰为核包含，且 \(N_U:E\to N_U(E)\) 满射给唯一性。∎

它是集合值目标的充分性，不证明群胚、态射或高阶相干信息被恢复。需要范畴重建时，应使用完整自然探针和全忠实比较。

**反例（不存在最小观察基）。** 在 \(E=\{0,1\}^{\mathbb N}\) 上，\(o_n\) 读取前 \(n\) 位。\(U\subseteq\mathbb N\) 恢复所有序列当且仅当 \(U\) 无界。任何这样的 \(U\) 删除一个元素仍无界，所以没有包含极小的充分基。

## 5.2 持续观察的有限状态版本

给非空有限状态集 \(E\)、有限动作集 \(A\)、总转移 \(T_a:E\to E\) 和输出 \(o:E\to Y\)。令

\[
x\sim_\infty y\iff
\forall w\in A^*,\quad o(T_wx)=o(T_wy).
\]

置 \(R_0=\ker o\)，递归

\[
R_{n+1}=R_0\cap\bigcap_{a\in A}(T_a\times T_a)^{-1}R_n.
\]

**定理 IC2（未来稳定的最粗压缩）。** \(R_n\) 表示所有长度不超过 \(n\) 的动作字不可区分；稳定关系等于 \(\sim_\infty\)，是包含于 \(\ker o\) 且被所有动作保持的最大等价关系。若 \(|E|=m\)，严格细化至多发生 \(m-1\) 次。

**证明。** 第一项按字长归纳。每个 \(R_n\) 是等价关系且逐次缩小；任何稳定关系包含于所有 \(R_n\)。稳定时递归给出动作保持，归纳得全部未来输出一致。有限等价关系每次严格细化至少增加一个分块，而分块数至多为 \(m\)。∎

此定理恢复的是一个指定有限状态系统中的未来观察，不是对无限数学语义的无条件算法。

## 5.3 压缩不能只看眼前结论

**定理 IC3（带见证的搜索商）。** 给标号转移系统 \((E,\to_a)\)、\((Z,\Rightarrow_a)\)，满射 \(q:E\to Z\)，目标集合 \(G\subseteq E\)、\(\bar G\subseteq Z\)。假设：

- 目标精确：\(G=q^{-1}(\bar G)\)；
- 正向保持：\(x\to_a y\Rightarrow qx\Rightarrow_a qy\)；
- 逐状态反向提升：\(qx\Rightarrow_a z'\Rightarrow\exists y\;(x\to_a y\land qy=z')\)。

则对每个起点和每个有限动作字，原系统存在到目标的该标号路径，当且仅当商系统存在相应路径。若边代价由标号给定且非负，两系统在同一起点对应的可达目标路径代价集合相同，因而最小代价／下确界相同。

**证明。** 原路径逐边映射得到商路径。反向从指定的原起点开始，反复使用反向提升选出下一节点；最终用目标精确性。标号未变，故每条有限路径的代价未变。∎

这是存在性与代价的保真，不保证路径数、证明数、对称性或解模空间等价。随机奖励、依赖隐藏状态的代价和无限策略需要额外条件。

**直接推论。** 在确定性系统中，\(q\) 的核是动作保持的等价关系、且目标对该关系饱和时，IC3 条件成立。IC2 因而给出一条可计算的安全压缩路径。

**反例（只保持静态目标）。** 取 \(E=\{a,b,c\}\)，\(G=\{c\}\)，动作 \(a\mapsto a,b\mapsto c,c\mapsto c\)。合并 \(a,b\) 不改变当前是否属于目标，却把“从 \(a\) 永不到达目标”与“从 \(b\) 一步到达目标”混同。静态 IC1 不足以证明动态搜索安全。

## 5.4 相干观察与层级压缩

完整探针 \(i:\mathcal K\to\mathcal E\) 的 restricted Yoneda 全忠实才给范畴恢复。两个稠密包含的复合不自动稠密；不能把在不同环境中各自充分的两个缩减拼成保真缩减。

具体地，\(\Delta\) 在 \(\mathbf{Cat}\) 中稠密，\(\Delta_{\le1}\) 在 \(\Delta\) 中稠密，但 \(\Delta_{\le1}\) 在 \(\mathbf{Cat}\) 中不稠密。两个具有相同底层带单位有向图、不同乘法的单对象范畴已经展示遗漏复合信息的机制。来源：Kerodon 8.4.1.14。

## 5.5 近似压缩的误差证书

**定理 IC4（有限路径误差传播）。** 固定非负常数 \(L,\varepsilon,\eta,M\)。给状态集 \(X\)、度量状态空间 \(Z\)、压缩 \(q:X\to Z\)、动作 \(T_a\) 与 \(\bar T_a\)。若每个 \(\bar T_a\) 为 \(L\)-Lipschitz，且

\[
d_Z(qT_ax,\bar T_aqx)\le\varepsilon
\]

对所有输入和动作成立，那么长度 \(n\) 的同一动作字满足

\[
d_Z(qT_wx,\bar T_wqx)\le\varepsilon\sum_{j=0}^{n-1}L^j.
\]

若输出 \(o:X\to\mathbb R\)、\(\bar o:Z\to\mathbb R\) 满足 \(|o(x)-\bar o(qx)|\le\eta\)，且 \(\bar o\) 为 \(M\)-Lipschitz，则终点输出误差不超过

\[
\eta+M\varepsilon\sum_{j=0}^{n-1}L^j.
\]

**证明。** 令第 \(k\) 步状态误差为 \(e_k\)，初始 \(e_0=0\)。插入 \(\bar T_a q(T_{w_k}x)\) 并用三角不等式，得到 \(e_{k+1}\le\varepsilon+Le_k\)。归纳给第一式，再用输出误差和Lipschitz性给第二式。∎

当 \(L<1\)，得到独立于长度的界 \(\eta+M\varepsilon/(1-L)\)；当 \(L=1\)，一般增长为 \(\eta+Mn\varepsilon\)。因此一步误差小不等于任意长搜索误差小。

该结果可证明具有足够间隔的数值判定稳定，但不能把“近似为零”当作精确等式。它不替代IC3的真实路径提升。

---

# 6. PR：检测、误差与量词提升

## 6.1 检测对象

固定见证集 \(W\)、阶段集 \(I\) 及误差 \(e:W\times I\to[0,\infty]\)。对于序列阶段，定义持久检测谓词

\[
D_\varepsilon(w,N)\iff\forall n\ge N,\quad e(w,n)<\varepsilon.
\]

点态与统一结论分别是

\[
\forall w\ \forall\varepsilon>0\ \exists N\ D_\varepsilon(w,N),
\qquad
\forall\varepsilon>0\ \exists N\ \forall w\ D_\varepsilon(w,N).
\]

“阶段 \(N\) 恰好误差小”不能替代上述尾部条件。升级机制是使这两个量词模式可比较的领域定理。

## 6.2 紧致与有限网机制

**定理 PR1（开覆盖提升）。** 若 \(W\) 紧致，\(U_N\) 为递增开集且 \(\bigcup_N U_N=W\)，则某个 \(U_N=W\)。

**证明。** 有限子覆盖的最大指标即为所需指标。∎

闭集替代开集不成立：\([0,1-1/n]\cup\{1\}\) 是递增闭覆盖但没有一项等于 \([0,1]\)。

**定理 PR2（定量等度连续提升）。** 在非空紧致度量空间 \(W\) 上，若 \(f_n:W\to\mathbb R\) 都为 \(L\)-Lipschitz 且逐点趋于 \(f\)，则 \(f\) 为 \(L\)-Lipschitz。对有限 \(\delta\)-网 \(S\)，有

\[
\sup_W|f_n-f|\le\max_{s\in S}|f_n(s)-f(s)|+2L\delta.
\]

因此 \(f_n\to f\) 一致。

**证明。** 对 Lipschitz 不等式取极限得 \(f\) 的 Lipschitz 性。对每个 \(w\) 取邻近 \(s\)，三角不等式给估计。先令 \(\delta\) 小，再在有限 \(S\) 上取共同收敛阈值。\(L=0\) 时只需一个点。∎

紧致本身不足：\(f_n(x)=x^n\) 在 \([0,1]\) 上逐点收敛到在1处为1、其余为0的函数，误差上确界恒为1。

## 6.3 Baire 机制

**定理 PR3（统一有界）。** 若 \(X\) 为 Banach 空间，\(Y\) 为赋范空间，\(T_i:X\to Y\) 为一族有界线性算子，且每个 \(x\) 满足 \(\sup_i\|T_ix\|<\infty\)，则 \(\sup_i\|T_i\|<\infty\)。

**证明。** 闭集 \(E_m=\{x:\sup_i\|T_ix\|\le m\}\) 覆盖 \(X\)。完备度量空间的 Baire 性使某个 \(E_m\) 含开球 \(B(x_0,r)\)。对 \(\|h\|\le r/2\)，\(x_0+h,x_0\in E_m\)，所以 \(\|T_ih\|\le2m\)，从而 \(\|T_i\|\le4m/r\)。Baire 性可用半径趋零的嵌套闭球证明：若所有闭集均无内点，递归选择第 \(m\) 个闭球避开第 \(m\) 个闭集，完备性给公共极限点，矛盾。∎

删除完备性即失败：\(X=c_{00}\) 赋 sup 范数，\(T_nx=nx_n\)。每个向量有限支撑故逐点有界，但 \(\|T_n\|=n\)。

## 6.4 测度机制

**定理 PR4（有限测度上的近一致提升）。** 在有限测度空间中，可测实函数 \(f_n\to f\) 几乎处处时，对任意 \(\delta>0\)，存在可测 \(E\)，\(\mu(E)<\delta\)，使 \(f_n\to f\) 在 \(X\setminus E\) 上一致。

**证明。** 对整数 \(k\ge1\)，令

\[
A_N^k=\bigcup_{n\ge N}\{|f_n-f|\ge1/k\}.
\]

这些集合随 \(N\) 下降，其交集为零测集。有限测度的从上连续性给 \(N_k\) 使 \(\mu(A_{N_k}^k)<\delta2^{-k}\)。去掉 \(E=\bigcup_k A_{N_k}^k\)；对任意误差要求选择 \(k\)，再取 \(n\ge N_k\)。∎

这是指定异常集预算下的结论，不是全域一致。无限计数测度上 \(f_n(k)=\mathbf1_{k\ge n}\) 逐点趋零，但去掉任何有限测度集后仍不一致。

## 6.5 与 horizon 的关系

PR 研究见证、误差和阶段量词；F4 研究相干形式对象是否来自原实际范畴。二者能够同时需要，但不能互相取代：Banach–Steinhaus 不直接重建一个形式对象，horizon 拉回也不自动给统一范数界。升级机制必须记录输入的完备性、紧致性、拓扑与异常预算。

---

# 7. DG：问题目录、对称性与生成路径

## 7.1 有限模板中的 doctrine 对象

固定小范畴 \(\mathcal C\) 和事先选择的小模板目录

\[
\mathcal L=\{i_\ell:J_\ell\to K_\ell\}_{\ell\in L}.
\]

每个 \(b:J_\ell\to\mathcal C\) 产生一个延拓问题，解空间为

\[
\operatorname{Sol}_\ell(b)=
\operatorname{Fun}(K_\ell,\mathcal C)^\simeq
\times_{\operatorname{Fun}(J_\ell,\mathcal C)^\simeq}\{b\}.
\]

这里指定同构／等价边界；要求逐字相等的边界时须改用严格纤维并说明差异。

定义模板相对的问题群胚

\[
\mathfrak{Doct}_{\mathcal L}(\mathcal C)
=\coprod_{\ell\in L}\operatorname{Fun}(J_\ell,\mathcal C)^\simeq.
\]

模板可编码缺失的极限、延拓、关系或提升。局部比较、误差与代价可作为附加数据，但不能把这些额外数据当成从裸范畴自动得到。

**命题 DG1（可枚举范围）。** 若 \(\mathcal C\)、\(L\)、\(J_\ell\)、\(K_\ell\) 都是有限显式范畴，则全部输入、扩张函子及边界同构可有限枚举；故每个上述解空间的非空性可判定。

**证明。** 枚举对象与箭头的有限映射，再检查端点、单位和复合。自然同构同样是有限个可逆分量及有限自然性方程。∎

这不是任意数学问题的判定算法：有限模板目录不是“所有自然数学问题”，无限语义的枚举通常只提供半判定或搜索。

## 7.2 规范选择与对称性

给 \(G\le\operatorname{Aut}(\mathcal C)\)；后合成作用于问题群胚及解纤维。若模板目录也变化，需要预先指定与之相容的 \(G\)-作用。

**命题 DG2（相对选择障碍）。** 对 \(G\)-空间 \(D\)，若 \(D^{hG}\ne\varnothing\)，则 \(\pi_0D\) 有 \(G\)-不变元素。若 \(D\) 为离散集合，\(D^{hG}=D^G\)。

**证明。** 一个同伦不动点给从连通 \(EG\) 到 \(D\) 的等变映射，其像所在分支不变。离散时映射在 \(EG\) 上常值，常值必须固定。∎

取 \(V=\mathbb F_2^2\)，其三条直线被 \(GL_2(\mathbb F_2)\) 传递作用，故不存在从裸 \(V\) 选择直线的自同构不变规则。给定非零向量 \(v\) 后，对稳定子群 \(G_v\) 有规范直线 \(\mathbb F_2v\)。这是输入结构改变的结果，不是打破同一个输入下的不可选择定理。

不变分支不是充分条件：\(BQ_8\to B(C_2^2)\) 的纤维为连通的 \(BC_2\)，但任何同伦截面会在 \(\pi_1\) 上给群同态截面，与 RG3 矛盾。相应相干作用的同伦不动点为空。

所以可保留多个 orbit，或在明确的随机决策规则下选择分布。有限非空 \(G\)-集总有不变概率分布，但这不是不变的单个选择。

## 7.3 语义与 provenance

令 \(\mathsf P\) 为带类型生成图的自由路径范畴。每个生成边带具体构造或证明证书；给出语义评估 \(E:\mathsf P\to\mathcal E\)。指定允许忽略的路径关系 \(\sim\) 必须满足：端点相同、语义相同，并在要求保留成本时保持相应成本。

**命题 DG3（路径商的可靠性）。** \(E\) 降到 \(\mathsf P/{\sim}\) 当且仅当所有关系生成对具有相同评估。

**证明。** 必要性显然。充分性由复合对相等的保持及商范畴的泛性质得到。∎

同一语义结论可以有不同证明路径。证明依赖是“一个证明的全部前提”的合取，与“多个替代证明”的析取；不能把某条证明失效等同于结论为假。

**命题 DG4（证书闭包）。** 在有限无环证明超图中，若每个初始已接受命题为真，每个验证通过的推理规则在其类型和假设下保真，则按“存在一条所有前提均已接受且验证通过的推理边”闭包得到的全部结论为真。

**证明。** 按超图的拓扑顺序归纳。不同可用推理边只增加替代证明，不破坏归纳。∎

若验证器不可靠，该命题不提供保证。语言模型自称“验证通过”不是本命题的前提证书。

## 7.4 多层级生成

问题可发生在对象、图式、范畴和语义环境层。改变层级必须指定新环境、嵌入和保存性质。

例如 \(\operatorname{Ind}(\operatorname{FinVect}_k)\simeq\operatorname{Vect}_k\)：任意向量空间是其有限维子空间的有向并，有限维空间到该并的映射经有限阶段因子化；这同时恢复对象与 morphism 公式。该完成改变的是可用对象世界，不是有限维范畴内部多选一个对象。

模板目录由输入规则产生，不承诺无条件的唯一“重要问题”。候选重要性可以由预先固定的目标、迁移性、证明成本和独立评价比较；没有把它定义成新的万能标量。

---

# 8. C2 面向创造的组合使用

一次合法的创造尝试可以包含：模板产生问题（DG）；建立横向可能性（EC、§1）；检查对象／复合／扭曲（RG）；找出最先失效的尺度（ES）；证明可安全压缩（IC）；选择适用的量词升级定理（PR）；最后作实际构造或契约修补（F4、F6），并保留证明路径。

这些不是每题必须串行执行的步骤。线性代数中的一个消元问题可以只用直接求解；没有必要人为加入 pro 对象或障碍类。

**条件性组合定理 C2-S。** 若一个具体搜索系统：

1. 所有建模与变换均有目标保持证书；
2. 所用压缩满足 IC3（需要数量／高阶信息时采用相应更强比较）；
3. 所用升级满足相应 EC、ES、PR 或 F4 的全部假设；
4. 每条输出证明由满足 DG4 前提的验证器接受；

则其接受的结论在原目标语义中正确，并且 IC3 覆盖的有限搜索路径不会仅因该压缩而丢失。

**证明。** 逐次用目标保持运输，IC3 提升商路径，升级定理提供对应结论，DG4 保证输出证书的真值。∎

本定理是组件正确性的组合，不是 AI 性能定理。它不保证搜索终止、命中有价值的新结果、降低总成本或超过 C1。经验评价的预注册接口见 `03_AI_CREATIVITY_PROTOCOL.md`。

# 9. 继承、增量与未完成范围

C2 的六个增量为 EC、RG、ES、IC、PR、DG；F1–F6 和语言恢复等是 C1 基础的延续。更具体的 C1 上同调耦合、严格齐次化、变形等领域结论仍按原附卷的范围使用；它们没有因未在本文全文重印而被否定，也没有获得新的普遍化。

尚无本版证明的结论包括：任意丰富化环境的统一实际化算法；任意形式对象由 product spectrum 判定；无限状态搜索的可计算最小充分压缩；不带模板输入的规范重要问题选择；AI 创造力的净提升。这些分别需要额外数学定理或独立实验，而非增加模块名称。

## 文献与来源

项目来源：Frozen v1.0 `01_FROZEN_CORE.md` 与 `02_DERIVED_THEORY.md`；Consolidated C1 主稿 §§2–19 及相应订正。C2 的明确新表述与来源区分见评估文档。

外部标准背景（本版公式的直接推导已在正文给出；以下不承担本项目原创性认证）：

- Stacks Project，4.22，pro 系统及本质常值；用于 ES2。
- Kelly–Schmitt，*Notes on enriched categories with colimits of some class*；用于 EC 的加权完成背景。
- Riehl–Verity，*The theory and practice of Reedy categories*；用于§1.3的 Reedy matching 背景。
- Garner，*Understanding the small object argument*；用于 F6 的自由／代数化修补背景。
- Kerodon，8.4.1，特别是 8.4.1.14；用于 IC 的稠密性边界。
- Stacks Project，087W，有限形式模的仿射实际化；作为 F4 的领域输入例子。

```text
https://stacks.math.columbia.edu/tag/05PT
https://arxiv.org/abs/math/0509102
https://arxiv.org/abs/1304.6871
https://arxiv.org/abs/0712.0724
https://kerodon.net/tag/03V8
https://stacks.math.columbia.edu/tag/087W
```

有限状态分割细化的标准相关研究：Wißmann 等，*Efficient and Modular Coalgebraic Partition Refinement*。IC2 不主张新发明该方法。

```text
https://arxiv.org/abs/1806.05654
```
