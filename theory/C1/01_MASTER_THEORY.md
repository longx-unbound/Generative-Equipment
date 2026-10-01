# 数学内生生成性 / Generative Equipment
## 理论总整理与精炼稿 C1
### 冻结核心、严格实现、识别定理、领域工具与未闭合接口

**编纂日期：2026-09-29**  
**性质：C1 是对 Generative Equipment 的编纂、严格化与订正版；它不是新的冻结版本。**  
**冻结基线：Frozen v1.0，2026-09-23。其冻结核心原文保持不变。**  
**范围：Generative Equipment 主线及其直接前置，包括 Strict v0.1/v0.2、GE-R1–R35、ENDO-1–6、Horizon 系列，以及 moment-angle、变形、SNT 等应用接口。**  
**范围边界：未纳入的独立项目不因与 Generative Equipment 有关联而自动成为 C1 的组成部分。**

C1 是当前的规范阅读与使用入口。历史编号、证明、反例和程序保存在 `source_archive/`；Frozen v1.0 原始材料保存在 `frozen_original/` 与 `evidence/`。引用 `[Sxx]` 指项目原稿，`[Bxx]` 指文献，完整索引见附卷。历史材料用于追溯来源与理论演化，不因归档而自动取得当前定理地位。

### Frozen v1.0 与 C1 的版本关系

- **Frozen v1.0 是冻结的基础版本。** 其中 `01_FROZEN_CORE.md` 规定 primitive core 与必须保持的语义边界；该核心是 C1 的基础规范，不由 C1 静默改写。
- **C1 是当前综合版本。** 它在 Frozen v1.0 的核心之上提供严格实现、派生定理、订正、证据状态、领域接口与当前使用规则。
- **冻结核心与冻结包中的派生材料必须区分。** “Frozen”首先表示版本冻结，不等于其中每条派生陈述都获得不可修订的正确性认证。Frozen 包中的派生结论若被后续证明、反例或类型检查收窄，其当前使用以 C1 的定理账本和订正表为准；这不构成对 Frozen core 的回写。
- **Frozen core 若需要改变，必须显式发布新的 Frozen 版本。** 只有明确反例、内部矛盾、良定义性失败，或核心无法表达其明确承诺覆盖的现象，才构成修改核心的理由；修改必须留下版本差异与理由，不能通过 C1 的编纂层隐式完成。
- 因而，**primitive core 的规范基线看 Frozen v1.0；当前派生结果、订正、状态和应用边界看 C1。**

---

## 0. 理论定位

目前最准确的定位是：

> **一套相对于明确数学结构、问题语义和观察标准的内生生成研究框架；在若干领域有严格的实现、相干性、语言恢复与修补定理，但尚不是无条件自启动的数学创造算法。**

整理后的架构不再靠不断增加 ENDO 编号解释，而分为四个功能模块：

\[
\boxed{\text{发生 Genesis}\quad\text{实现 Effectivity}\quad
\text{修补 Mutation}\quad\text{观察 Observation}.}
\]

四者共用一个小的冻结语义骨架：

\[
\Xi\longmapsto P_\Xi\longmapsto P_\Xi^\sharp
\longmapsto\mathfrak G_\Xi
\longmapsto C_\Xi:\mathcal A_\Xi\to\mathcal F_\Xi
\longmapsto N^\infty_\Xi.
\]

必须同时保留三个层次的区别：

\[
\text{能定义问题}\ne\text{能判定问题}\ne\text{能有效求解问题},
\]

\[
\text{语义允许}\ne\text{已有实际构造}\ne\text{相对于旧世界有新颖性},
\]

\[
\text{数学命题成立}\ne\text{文献首创}\ne\text{已有方法优势}.
\]

C1 的整理原则不是增加术语，而是移除已被反例、类型检查或更严格分析排除的错误蕴含，并使历史结论按当前条件与证据状态使用。历史版本中的完成度或价值评级不构成数学证据。

---

## 1. 证据地位与使用规则

### 1.1 数学地位

| 标签 | 含义 | 可以怎样使用 |
|---|---|---|
| **DEF** | 定义、数据契约或逻辑重述 | 可作记号与证明目标；不算新求解工具 |
| **STD** | 经典定理或标准直接推论 | 明确引用，不能改名后宣称原创 |
| **DER** | 本稿给出可逐项核对的派生证明 | 可在所列条件下使用；首创性另判 |
| **COND** | 正确的条件性结果，目标领域中的前提尚未验证 | 必须携带前提；不能据此宣布应用完成 |
| **REPORT** | 历史报告中的结果，现有归档证据尚不足以完成独立核验 | 不作为新的已验证依赖 |
| **OPEN** | 待证接口或研究目标 | 不可用于闭合证明 |
| **RETRACT** | 已有反例，或已识别无效的证明/外推 | 禁止重新引入 |

“DER”不等于“新于文献”；“COND”不等于命题错误；“REPORT”不等于命题为假。“Frozen”只是版本约束，不是独立正确性认证。

### 1.2 编号去混淆

历史版本编号只用于来源追踪；C1 使用模块与定理 ID 表示当前依赖，不以编号大小表示强度。

### 1.3 原文与当前规范分离

Frozen v1.0 的冻结核心保持原文不变；C1 对其空间值严格分支、派生层与应用层给出当前规范。Frozen 包中的派生内容不因与核心共同冻结而免于后续订正；若派生陈述与已建立的 C1 订正冲突，当前派生使用以 C1 为准，而 Frozen core 本身仍保持不变。特别是“无规范语言”的绝对解释，按 ENDO-5 的信息遗失判据收窄。[S00–S03, S36]

---

# 第一编　冻结骨架与严格数学实现

## 2. 最小工作数据：保留什么，不新增什么

在一个声明好的语义宇宙中，给：

\[
\Xi=(S,\Omega,\mathrm{Prov},\text{允许的等价、构造与观察数据}).
\]

空间值严格分支包含：

\[
P:\mathcal I^{op}\times\mathcal B\to\mathcal S,
\]

其中 \(\mathcal I\) 是问题范畴，\(\mathcal B\) 是候选范畴。其语义经事先确定的饱和得到 \(P^\sharp\)。若饱和改变定义域，同时记录

\[
\lambda_{\mathcal I}:\mathcal I\to\mathcal I^\sharp,
\qquad
\lambda_{\mathcal B}:\mathcal B\to\mathcal B^\sharp.
\]

另给实际范畴 \(\mathcal A\)、形式范畴 \(\mathcal F\) 及

\[
C:\mathcal A\to\mathcal F.
\]

当确有三层模型时，还记录

\[
\mathcal A\xrightarrow{R}\mathfrak G\xrightarrow{\Phi}\mathcal F,
\qquad C\simeq\Phi R.
\]

**不能默认 \(\mathfrak G=\mathcal F\)，也不能因为 \(\Phi R\) 是等价就断言 \(R,\Phi\) 分别是等价。**

事件及观察采用明确的方差约定：

\[
\widetilde{\mathcal E}\to\mathcal E,
\qquad
\mathbb O:\mathcal K^{op}\times\mathcal E\to\mathcal S,
\qquad
N^\infty(e)=\mathbb O(-,e).
\]

这只是一个严格实现，不把所有 Banach、度量、稳定或 \((\infty,2)\) 语义强行降为空间值非空性问题。冻结核心允许更广的丰富化环境。[S00, S04–S08]

### 不列为新 primitive 的对象

Repair Profile、Horizon Residue、frontier、Coupl、viability、各种 rank、闭包、单子与 pro-generator，均从上述数据与领域结构派生。它们有不同用途，不能全部合并成一个无类型的“obstruction”。

---

## 3. 饱和：既要反演表示差异，也要证明没有改错问题

### 3.1 域改变的严格模型

当局部化与所需 Kan 扩张存在时，可以取

\[
P^{\rm dom}=
\operatorname{Lan}_{\lambda_{\mathcal I}^{op}\times\lambda_{\mathcal B}}P.
\]

这是对声明反演条件的泛扩张。它不是任意 sector 中唯一正确的 saturation；必须另证这个扩张符合原问题的语义意图。[S05, S07]

### 3.2 两项不可遗漏的接口

**Sat-N：**在声明的等价下，饱和的定义数据、输入纤维和满足关系必须相干运输。

**Sat-Eval：**若修补阶段需要一个映射
\(D^\sharp(G)\to\operatorname{Map}(A,G)\)，这个映射必须实际存在。仅有 raw 数据上的 evaluation，不意味着它自动下降到 gauge 商。

如果 saturation 把若干不同输入也识别，目标应相应改成输入的饱和范畴，而不是继续假装它是 raw mapping space 的子空间。

### 3.3 限制模型与完整模型

令 \(D_0\to D\) 为简化定义系统到完整系统的比较，\(Z_0\to Z\) 为相应解空间比较。

\[
Z_0\ne\varnothing\iff Z\ne\varnothing
\]

仅表示存在性完整；它不推出覆盖 \(Z\) 的全部连通分支，也不推出 \(Z_0\simeq Z\)。例如 \(*\to\{0,1\}\) 两边非空，却漏掉一个分支。

今后必须说明需要的是：非空性等价、\(\pi_0\) 满射、全忠实、或完整等价中的哪一项。旧 GE-R28 把前两者靠得过近的解释不再使用。[S27, S29]


### 3.4 GE-R1/R2 的 saturation 演算

在相关 Kan 扩张存在时，

\[
\operatorname{Lan}_{\mu\lambda}P\simeq
\operatorname{Lan}_{\mu}\operatorname{Lan}_{\lambda}P.
\]

这是左伴随复合的泛性质。对换基方块，pointwise comma 索引比较函子 final 是 Beck–Chevalley mate 为等价的充分条件；没有 finality 不能只凭方块交换推断 mate 等价。

对既有函子 F，若它把源局部等价送到目标局部等价，则 `L_Y F` 通过源局部化下降。若还要求不再对已局部对象作目标层化，必须验证 F 保持局部对象。域饱和与语义饱和的交换因此是兼容性结论，不是无条件恒等式。[S07–S08]

---

## 4. 可能性、普遍性与实际实现不是同一个对象

对固定输入 \(a\)，令

\[
H_a=P^\sharp(a,-):\mathcal B^\sharp\to\mathcal S.
\]

其 unstraightening 为

\[
\mathfrak G(a)=\int H_a.
\]

定义

\[
\mathcal M(a)=\mathfrak G(a)^\simeq,
\qquad
\mathcal U(a)=\bigl(\mathfrak G(a)^{\rm init}\bigr)^\simeq.
\]

### 定理 G1：有向对象化判据　【STD/DER】

\[
H_a\simeq\operatorname{Map}(F(a),-)
\iff
\mathfrak G(a)\text{ 有初始对象}.
\]

证明：一个 \(u\in H_a(b_0)\) 给出 Yoneda 比较
\(\operatorname{Map}(b_0,-)\to H_a\)。它在 \(v\in H_a(b)\) 上的纤维就是元素范畴中的映射空间；其全部可缩正是初始性。

初始对象若存在，其所在的**初始对象子空间**可缩，但整个 \(\mathcal M(a)\) 可以很大。所有输入均可余表示时，Yoneda 的全忠实性使其组装为函子；不是先人为选择不相容的逐点代表再宣布自然性。[S05, S07]

### 表示性识别引擎

在 presentable 范畴等标准伴随函子定理适用的范围，若 \(H:\mathcal B\to\mathcal S\) 可达且保持所有小极限，则它有左伴随 \(L\)，从而

\[
H(b)\simeq\operatorname{Map}_{\mathcal B}(L(*),b).
\]

这是经典识别工具；真正的领域难点是证明可达性和极限保持。只保持有限极限的 pro-sector 需要相应 pro-representability 定理与大小条件，不自动有实际代表。[S01, S04–S08]

---

## 5. 实现纤维、逗号范畴与对象重建

对象级实际化固定为

\[
\operatorname{Eff}_C(\xi)
=
\mathcal A^\simeq\times_{\mathcal F^\simeq}\{\xi\}.
\]

其点是 \((a,C(a)\simeq\xi)\)，不是任意箭头 \(C(a)\to\xi\)。因此它与逗号范畴 \((C\downarrow\xi)\) 一般不同。

### 定理 E1：对象实现与全语义重建　【STD】

\[
C\text{ 本质满}\iff\forall\xi,\ \operatorname{Eff}_C(\xi)\ne\varnothing.
\]

\[
C\text{ 是等价}\iff
C\text{ 全忠实且所有对象实现纤维非空}.
\]

对每个实际对象对 \(a,b\)，还需要保留

\[
\operatorname{Map}_{\mathcal A}(a,b)
\longrightarrow
\operatorname{Map}_{\mathcal F}(Ca,Cb).
\]

对象群胚上的等价不能恢复非可逆态射。例如单对象范畴的自同态幺半群为 \(\{1,e\}\)、\(e^2=e\)，其 core 是一点，但整个范畴不是终范畴。

### 统一的相对提升接口

对图式限制 \(J\hookrightarrow I\)，给定形式 \(I\)-图式及其实际 \(J\)-部分，可以在相应函子范畴中取同伦纤维。它就是历史的 Shape Residue。对象、箭头、粘合和高阶相干问题都可作为不同形状的提升问题，但仍需声明是哪种图式、边界和目标。[S01, S05]

---

# 第二编　实现、匹配与无穷相干

## 6. GE-R1–R12 的共同内容：先求相容分支，再分析障碍

### 定理 E2：纤维与极限交换　【STD/DER】

给一图比较 \(C_i:\mathcal A_i\to\mathcal F_i\) 及相干形式数据 \(\xi=(\xi_i)\)，有

\[
\operatorname{Eff}_{\lim_i C_i}(\xi)
\simeq
\operatorname*{holim}_i\operatorname{Eff}_{C_i}(\xi_i).
\]

证明来自 core 作为右伴随保持极限，以及极限之间交换。**左侧的实际范畴已经是 \(\lim_i\mathcal A_i\)**；这个定理不说明另一个预先给定的实际范畴 \(\mathcal A\) 等于该极限。[S07–S09, S42]

### 定理 E3：有限逆图匹配下降　【STD/DER】

给有限逆范畴上的 Reedy 纤维化图式 \(X\)。沿下闭子图加入对象 \(v\) 时：

\[
\lim_{A\cup\{v\}}X
\simeq
\lim_AX\times_{M_vX}X_v.
\]

因而，如果起点非空，且每个实际遇到的 matching 纤维非空，就能逐步得到全局分支。要求所有 \(X_v\to M_vX\) 在 \(\pi_0\) 上满射，是更强但便利的统一充分条件，不是必要条件。

若每个相对 matching 纤维可缩，则完整填充空间相对于给定边界可缩。二维小方格充足性的结论只在它们确实给出完整 matching 对象时成立；三维一般必须保留整个穿孔立方体，不能只看二维面。[S09, S15]

### R3–Postnikov 比较的正确强度

在有限 CW 底、截断纤维和相应局部系数设置中，cellular/Reedy 匹配法可以解析 Moore–Postnikov 的障碍类与提升空间。GE-R5 的合理结论是这种**障碍理论比较**，不是任意两个原始双滤过塔的逐项等价。非阿贝尔低阶 fringe 需固定 torsor/gerbe 模型；不能给一个 pointed set 凭空赋群作用。[S11, S19]

### Viability 与 Fubini

有限塔终点到中间点的同伦像记录“存在完整未来的分支”，反向求像可作精确语义递归。若它的定义已经用到未知终点解空间，则只是规范，不是独立算法。所谓障碍 Fubini 的许多等式来自复合与取像的结合律；不能据此宣称获得新的计算复杂度优势。[S13–S15, S19]

---

## 7. 全局效性有两道不同的关口

给 horizon 比较图：

\[
C:\mathcal A\to\mathcal F,
\qquad
C_n:\mathcal A_n\to\mathcal F_n,
\]

并给相干的 \(\alpha:\mathcal A\to\widehat{\mathcal A}\)、\(\beta:\mathcal F\to\widehat{\mathcal F}\)，其中

\[
\widehat{\mathcal A}=\lim_n\mathcal A_n,
\qquad
\widehat{\mathcal F}=\lim_n\mathcal F_n.
\]

定义

\[
\mathcal A_C^{\rm hor}
=
\mathcal F\times_{\widehat{\mathcal F}}\widehat{\mathcal A},
\qquad
\delta_C:\mathcal A\to\mathcal A_C^{\rm hor}.
\]

对 \(\xi\in\mathcal F\)，令

\[
\mathcal R_n(\xi)=\operatorname{Eff}_{C_n}(\xi_n).
\]

则

\[
\operatorname*{holim}_n\mathcal R_n(\xi)
\simeq
\operatorname{Eff}_{\mathcal A_C^{\rm hor}\to\mathcal F}(\xi).
\]

### 定理 E4：相对 horizon 比较　【STD/DER；精确重述】

全部对象级比较

\[
\operatorname{Eff}_C(\xi)\to\operatorname*{holim}_n\mathcal R_n(\xi)
\]

为等价，当且仅当 \(\delta_C^\simeq\) 是等价。完整语义重建则要求 \(\delta_C\) 本身为等价。

其全忠实条件明确为

\[
\operatorname{Map}_{\mathcal A}(a,b)\simeq
\operatorname{Map}_{\mathcal F}(Ca,Cb)
\times_{\operatorname{Map}_{\widehat{\mathcal F}}(\beta Ca,\beta Cb)}
\operatorname{Map}_{\widehat{\mathcal A}}(\alpha a,\alpha b).
\]

**精炼后的评价：这是有用的类型化与等价刻画，不是一般实际效性问题已经被解掉。** 在 \(\mathcal F\simeq\widehat{\mathcal F}\) 时，它恰好把问题退回实际侧重建 \(\mathcal A\simeq\widehat{\mathcal A}\)。不能把困难命题重新命名为 cartesianness 后算作闭合。[S42]

### 两道关口

\[
\boxed{
\text{有限数据是否有相干极限}
\quad\text{与}\quad
\text{该极限是否来自原实际世界}
}
\]

分别由 tower 的内部相容性与 \(\delta_C\) 控制。Milnor 项不能替代实际化比较。

---

## 8. 有限 horizon 到整体：保留可用的充分条件

### 定理 E5：可数塔的分支-ML 推广　【STD/DER】

设每个 \(\mathcal R_n\) 非空，\(\pi_0\mathcal R_n\) 的逆系统满足 Mittag–Leffler，且实际实现空间已被证明等价于 \(\operatorname{holim}\mathcal R_n\)。则整体实现非空。

证明：固定层的最终像组成非空且转移满射的子塔；选择相容点类，再选择逐步路径，就得到同伦极限中的点。可数塔允许使用这种递归模型。

若各 \(\pi_0\mathcal R_n\) 有限且非空，下降像自动稳定。[S08, S41]

### 正确的有限可见性条件

对于集合像链，要有一个固定有限集包含**充分高的全部像**。仅有“所有最终相容点落在某个有限集”不够。例如 \(I_m=\{j\ge m\}\) 的交为空，仍不满足 ML。

对于群塔，只要在固定 horizon 的每个高层像中，都包含同一个固定有限指数子群 \(H\)，这些像便位于有限个中间子群中，故稳定。没有这样的统一子群，不能由每一步各自有限指数推出稳定：\(2^m\mathbb Z\) 就是反例。

### branch-relative Milnor 结构

选定同伦极限中的基点及相容运输以后，标准塔公式给出

\[
0\to\lim{}^1\pi_{q+1}\mathcal R_n
\to\pi_q\operatorname{holim}\mathcal R_n
\to\lim\pi_q\mathcal R_n\to0,
\qquad q\ge1,
\]

其中低阶按群或 pointed-set 的正确类型解释。\(q=0\) 对每条相容 component branch 的纤维涉及相应运输后的非阿贝尔 \(\lim^1\pi_1\)。

不应把 \(\lim^1\pi_1\) 无基点地当作一个全局统一障碍群；它还依赖分支及局部系数。它可以控制不可见的整体分支，而不是自动阻止整体存在。

### 三个识别引擎

| 条件包 | 能推出什么 | 不能省略什么 |
|---|---|---|
| 两侧 horizon 比较都是等价 | 相对 horizon 完备 | 各自重建的独立证明 |
| 两侧左完备稳定 \(t\)-结构，比较与截断相容 | 截断 horizon 重建 | 左完备；仅有所有截断不够 |
| Noether 仿射 \(I\)-adic 有限模效性 | 兼容有限商模来自有限完备模 | 完备化后的系数环、相容性与有限性 |

仿射完备化的模型见 Stacks 09B8、087W；这是领域定理输入，不是 core 自动推出的事实。[B07–B08]

---

## 9. 阻碍、耦合与有限压缩

### 9.1 torsor 扇区

对一个 \(K(A,n)\)-主丛／torsor，存在性障碍在

\[
H^{n+1}(B;A).
\]

它消失当且仅当存在平凡化／截面；一旦存在，平凡化空间由相应映射空间控制。扭曲系数和非阿贝尔低阶情形必须使用其正确的局部系统或群胚，而不能总写成一个阿贝尔群。[S10–S11]

### 9.2 Coupl 不是额外原始公理

改变低阶提升 \(s\mapsto s+h\) 后，高阶障碍可能改变。这个变化对应就是 Coupl。在有单值阿贝尔表示的 sector 才能把它当作群值函数；一般应保留完整的定义数据空间与零纤维。[S12–S13, S22, S27]

对阿贝尔群映射 \(q\)，令

\[
\operatorname{cr}_2q(x,y)=q(x+y)-q(x)-q(y)+q(0).
\]

\(\operatorname{cr}_2q=0\) 当且仅当 \(q-q(0)\) 加性。这是允许线性／仿射压缩的代数判据，不保证一切几何障碍都落入此 sector。

### 9.3 有理多项式、整数运算与扭曲不能混为一谈

有限差分次数、齐次次数、极化可恢复性依赖系数环。整数除法、阶乘与 torsion 必须保留；不可把特征零多项式公式直接用到所有上同调操作。

### 9.4 相对幂零性

若群作用满足 \(I_G^cM=0\)，则增广过滤的 successive quotients 为平凡作用。它把扭曲问题细分成常系数层，但连接映射和 extension data 仍保留原扭曲。\(c\) 控制层数，不控制搜索成本。纤维本身幂零不自动保证外部 monodromy 相对幂零。[S17–S19]

### 9.5 保留的尖锐阶数机制

在作用型、常系数的 primary 上同调障碍中，若修正空间 \(E\) 是 \((r-1)\)-连通的、障碍位于次数 \(q\)，则第 \(j\) 个 universal cross-effect 经过 \(E^{\wedge j}\)。当 \(jr>q\) 时其相关约化上同调消失，故

\[
\deg\operatorname{Coupl}\le\lfloor q/r\rfloor.
\]

对该特定 sector 的 simply-connected \(N\)-type，得 \(\lfloor(N+1)/2\rfloor\) 界；\(u^d\) 给出达到阶数 \(d\) 的例子。不能把它扩成任意多值、twisted 或 secondary 高阶障碍的统一次数界。[S21–S22]

---

# 第三编　问题、语言与定律的发生

## 10. ENDO-1 的当前形式：结构相对的问题发生器

给小加法范畴 \(\mathcal C\)，其加法预层包络为

\[
\widehat{\mathcal C}_{\rm Ab}
=\operatorname{Add}(\mathcal C^{op},\mathbf{Ab}).
\]

对每个原生态射 \(f:a\to b\)，统一产生

\[
\mathcal K_f(c)=\ker[\mathcal C(c,a)\to\mathcal C(c,b)],
\]

\[
\mathcal Q_f(c)=\operatorname{coker}[\mathcal C(c,a)\to\mathcal C(c,b)].
\]

问题是这些观察轮廓能否由当前对象表示。这里不逐个指定目标对象，但仍预设了“有限线性方程／关系”的发生规则。

有限关系完成得到 \(\operatorname{mod}(\mathcal C)\)。其对核封闭，当且仅当原范畴有弱核；这是 Freyd 范畴的标准判据。环模 sector 对应相干性。从 \(\operatorname{Free}_f(\mathbb Z)\) 出发，关系余核产生循环群等有限生成阿贝尔群，是正确但经典的发生示范。[S29]

**输入原有的结构必须声明。** 遗忘一个已有余核、再在预层包络中重新添加其轮廓，不一定是数学增长；可能只是忘却造成的信息损失。

---

## 11. ENDO-2 的当前形式：保真扩充与有限语法闭包

### 11.1 正合语义的修补

小正合范畴的 deflations 产生相应覆盖。局部加法预层要求把指定正合列送成左正合列；在经典嵌入假设下，Yoneda 经层化保持原有正合关系。

对原始 deflation \(p:y\to z\)，

\[
D_p=\operatorname{coker}(yp)
\]

的每个截面沿该 deflation 的拉回局部消失，因而层化后 \(aD_p=0\)。这消除的是“原结构早已满足、但 raw Hom 预层没完整表现”的关系缺陷。[S30; B12]

### 11.2 张量语义不能假设新对象自动平坦

Day 卷积下降需要原覆盖／正合结构与张量相容。即使强幺半嵌入成立，也不表示所有新对象的普通张量保持单射。

\(n:\mathbb Z\to\mathbb Z\) 与 \(\mathbb Z/n\) 张量成为零自映射；这阻止同时保留忠实性、通常正合性、普通张量和非零挠对象，又强制目标张量逐变量正合。[S30]

### 11.3 有限语法闭包

固定语义环境、种子及一组小的有限元构造规则。逐层加入全部输出与声明允许的态射，\(\omega\)-并给最小有限构造闭包，前提是这些解释存在且所需大小受控。

“每层取全子范畴”意味着全部语义态射已经免费可用；这是语义闭包，不是一般的有限计算程序。

### 11.4 完美复形与截断

在交换环 sector：稳定有限构造及 retract 从 \(R\) 生成 \(\operatorname{Perf}(R)\)。标准截断保持完美性，当且仅当 \(R\) 相干且每个有限表示模有有限投射维数（不要求统一上界）。

在指定同步语法中：第零层有限自由模，下一层只读取上一层，允许 cone、移位、retract、导出张量、截断等。对不正则 Noether 局部环，剩余域 \(k\) 第二轮出现，\(k\otimes_R^{\mathbf L}k\) 第三轮无界；前两轮有界。这个“三”依赖原子语法，不是结构的绝对不变量。[S30; B09]

双数环 \(k[\varepsilon]/(\varepsilon^2)\) 的周期解消给出 \(\operatorname{Tor}_i(k,k)\cong k\)，是完整的正负控制。

---

## 12. ENDO-5：能够恢复哪些语言？

### 定理 G2：有限极限语言恢复　【STD】

若 \(\mathcal K\) 局部有限可表示，取小骨架 \(\mathcal A=\mathcal K_{\rm fp}\)，则

\[
\mathbb T_\mathcal K=\mathcal A^{op},
\qquad
\mathcal K\simeq\operatorname{Lex}(\mathbb T_\mathcal K,\mathbf{Set}).
\]

它从完整模型范畴恢复多排序有限极限语言；不需预设某一个载体函子，但也不由一个孤立模型恢复整个领域。这是 Gabriel–Ulmer 重建。[S36; B03]

### 定理 G3：自然运算恢复　【STD】

若 \(F\dashv U:\mathcal K\to\mathbf{Set}\)，则

\[
\operatorname{Nat}(U^n,U)\cong U(F(n)).
\]

若 \(U\) 还是有限元单子的单子性函子，则得到恢复模型的 Lawvere 理论。Top 的离散自由函子只给投影运算，说明单有自由对象还不够。[S36; B02]

### 定理 G4：内部量词由伴随确定　【STD】

有限极限给子对象、合取、等号、代入。正规性给

\[
\exists_f(P)=\operatorname{im}(P\to X\xrightarrow fY),
\qquad \exists_f\dashv f^*.
\]

若右伴随及相应换基相容性存在，便得到 \(\forall_f\)；若 \(P\wedge-\) 有右伴随，便得到蕴含。伴随唯一性使这些操作在给定语义中非任意。[S36; B04]

**并非所有 sector 都支持同样的逻辑。** 模的子对象格一般不分配；稳定无穷范畴中的单态都是等价，所以普通 \(\operatorname{Sub}\) 逻辑退化。必须换成完整高阶探针、谱丰富化或另外声明的 \(t\)-结构语义。

### 其余恢复机制

可达无穷范畴在指定 \(\kappa\) 下有 \(\operatorname{Ind}_\kappa\) 重建；clan 对偶需合适 WFS；形式模问题需基域与完整高阶参数语义；度量可由全部 1-Lipschitz 实值谓词恢复。这些是不同的恢复定理，不是一个无条件的普适 logic genesis 定理。[S36; B03, B11]

### 完整 institution 的额外数据

不仅要有固定 \((\mathrm{Models},\mathrm{Sentences},\models)\)，还要给签名变化、句子运输、模型约化及满足条件：

\[
M'\models\operatorname{Sen}(h)\varphi
\iff
\operatorname{Mod}(h)(M')\models\varphi.
\]

内部解释、institution 和模型重建是三个不同等级。[B01]

---

## 13. ENDO-4：语义闭定律，而非自动出现的规范性目标

固定一个满足系统、一个集合大小的模型范围 \(\mathcal M\) 和事先声明的单调扩张型 continuation \(\mathsf K\)。

\[
\operatorname{Th}(X)=\{\varphi:\forall M\in X,\ M\models\varphi\},
\quad
\operatorname{Mod}(\Gamma)=\{M:\forall\varphi\in\Gamma,\ M\models\varphi\}.
\]

\[
X\subseteq\operatorname{Mod}(\Gamma)
\iff\Gamma\subseteq\operatorname{Th}(X).
\]

令 \(\operatorname{Def}=\operatorname{Mod}\operatorname{Th}\)，迭代

\[
X_{\alpha+1}=\operatorname{Def}(\mathsf K(X_\alpha)),
\qquad
X_\lambda=\bigcup_{\beta<\lambda}X_\beta.
\]

在集合大小范围中它稳定于最小共同不动点 \(X^*\)。因为两种操作均扩张：

\[
X^*\subseteq\mathsf K(X^*)\subseteq
\operatorname{Def}(\mathsf K(X^*))=X^*,
\]

所以 \(\mathsf K(X^*)=\operatorname{Def}(X^*)=X^*\)。令

\[
\Theta^*=\operatorname{Th}(X^*).
\]

则 \(\Gamma\) 对全部稳定未来安全，当且仅当 \(\Gamma\subseteq\Theta^*\)。这是最大安全描述理论。[S35]

### 三个必须保留的边界

第一，\(\mathsf K\)、满足系统与模型范围仍为输入；没有从裸结构唯一选出全部未来。

第二，\(\operatorname{Def}\) 允许的模型未必已有实际构造路径。

第三，对所有 \(M\in X^*\)，按定义 \(M\models\Theta^*\)。因此在同一模型范围里检查“违反 \(\Theta^*\)”不会产生非空缺陷。新的修补问题必须来自另一个明确的实现、运输、相干性或扩张目标。[S36 §13]

两套公理基给出同一闭理论，只保证相同模型类；不保证它们产生相同的带见证修补范畴。把公式编译成 walking lifting laws，还需要独立的可靠性和完整性比较定理。

---

# 第四编　修补、语法变异与动态

## 14. Repair Profile：保留完整范畴，不以“无初始对象”替代分支

给当前状态 \(\Sigma\)、真正的饱和缺陷 \(\delta\) 和保存契约 \(K\)，构造

\[
\mathcal R=\operatorname{Rep}_K(\Sigma,\delta).
\]

其 profile 包括

\[
\mathcal R,
\quad \mathcal R^\simeq,
\quad (\mathcal R^{\rm init})^\simeq,
\quad\pi_0\mathcal R^\simeq,
\quad\Omega_r\mathcal R^\simeq.
\]

分别检测：可行性、对象类型、普遍解、类型分支和自同构／高阶对称性。初始对象存在仍可与许多非初始修补类型共存。[S31–S34]

一维向量空间的同构群胚 \(Bk^\times\) 有唯一类型而无初始对象；单对象幺半群 \(\{1,e\}\) 的 core 可缩却也无初始对象。这两种失败不相同。

所有修补定律在偏序中的 meet，只叫 **mandatory doctrine kernel**；除非另证可行，否则不是修补。

---

## 15. 相干联合修补的正确普遍性质

设 \(\mathbf{Gram}\) 余完备，给 \(u:A\to B\) 和一个小空间参数族

\[
d:D\to\operatorname{Map}(A,G).
\]

由空间 copower 得 evaluation \(A\otimes D\to G\)。定义

\[
P_D=G\amalg_{A\otimes D}(B\otimes D).
\]

### 定理 M1：参数化 pointed repair　【STD/DER】

\[
\operatorname{Map}(P_D,X)\simeq
\operatorname{Map}(G,X)
\times_{\operatorname{Map}(D,\operatorname{Map}(A,X))}
\operatorname{Map}(D,\operatorname{Map}(B,X)).
\]

因而带完整 \(D\)-族相干见证的修补范畴是 \(\mathbf{Gram}_{P_D/}\)。小族 laws 可再取余积；图式内关系可在已明确编码关系的模型／图式范畴中作相应推出。[S34]

### 本定理不说什么

它保证**指定旧参数族的一组相干见证**，不保证新对象的全部新出现实例已经满足所有 law，也不保证唯一性／可缩性 law 被修好。

“每个纤维非空”不等于“整族有相干截面”。例如非平凡主丛 \(EG\to BG\) 的各纤维均非空，但对非平凡 \(G\) 无全局截面。因此 pointed/coherent repair 与仅存在某个 witness 的 repair，必须分别定义。

同样，Fun\((J,\mathbf{Gram})\) 内的推出只自动保留 \(J\) 已经编码的相干关系；不会凭“图式”二字自动产生未编码的 pentagon 或全部 \(A_\infty\) 条件。

---

## 16. 保存契约：性质与附加结构统一，但可实现性必须另证

给忘却函子

\[
U:\mathcal R_K\to\mathcal R_0,
\]

其中 \(\mathcal R_0\) 有初始对象 \(0\)。

### 定理 M2：伴随约束修补　【STD/DER】

若 \(F\dashv U\)，则 \(F(0)\) 初始，因为

\[
\operatorname{Map}_{\mathcal R_K}(F0,X)
\simeq\operatorname{Map}_{\mathcal R_0}(0,UX)\simeq *.
\]

反射子范畴是 \(U\) 全忠实的特例；带指定代数结构的自由函子是另一类。标准 AWFS、局部化和自由完成可以提供引擎，但不自动保持忠实性、旧对象非零或指定张量。[B05–B06]

**“存在左伴随”是充分结构条件，不是算法，也不是所有契约都具备的性质。**

### 松弛前沿

有限保存契约的可行子集形成下闭集；若非空，它有极大元。无限契约需链并可行等额外紧致性：若修补由 \(n\in\mathbb N\) 表示，条款 \(k_j\) 要求 \(n\ge j\)，每个有界子集可行，却没有极大可行子集。[S33–S34]

---

## 17. 发生器与多步动态：正确的条件性形式

### 17.1 law-relative occurrence compiler

给小 law signature，并在输入纤维上自然完成 saturation。取全部违反满足条件的输入，得到对**声明等价**不变的缺陷空间。它消除了逐实例挑选，但不独立决定 law universe。

更重要的是：缺陷子空间通常不沿任意态射协变。一个没有根的环映到有根扩环，缺陷恰好消失；不存在从非空缺陷空间到空缺陷空间的映射。因此不能从等价不变性直接写出

\[
\mathscr C:\mathbf{Gram}\to\mathcal S
\]

作为所有态射上的函子。

下降判据“反演 \(W\) 当且仅当通过局部化”只有在该完整函子或相应相干运输结构已经构造后才能使用。缺陷消失本身应由 occurrence/solution correspondence 记录，而不是强行保持失败标签。[S34；本版订正 C07]

### 17.2 单值动态与多值动态

若修补确实对两个端点具有所需的拉回／推出稳定性，可以得到 profunctor 并用 coend 复合。这个方差和稳定性是额外定理；任意“允许修补关系”不自动是 profunctor。

\(\mathbb R^*=\coprod_n\mathbb R^{\odot n}\) 是在这些前提下的有限形式路径闭包。coend 会识别中间运输，故它保存的是声明商关系下的路径，不是未经商化的全部历史。如果要求更细 provenance，应另存带中间对象和见证的路径范畴。

### 17.3 不动点与实际极限

单调且扩张的 \(T:L\to L\) 是 preclosure；其超限稳定值 \(\operatorname{cl}_T\) 才是幂等闭包。形式定律格的不动点不自动由实际 grammar 实现。

若确有实际变异 \(\widetilde T\)、\(q\widetilde T=Tq\)、保持契约的极限、\(q\) 将这些极限送为并，以及 \(q\) 反映相关变异箭头的等价，则可以把形式稳定运输为实际稳定。这是条件性 transfer theorem；最后的反映性是实质前提，不能视为已自动解决效性。[S34]


### 17.4 可表示动态的方差与严格化

当 `F_* (a,b)=Map(Fa,b)` 时，co-Yoneda给出

\[
\operatorname{Nat}(F_*,G_*)\simeq\operatorname{Nat}(G,F),
\qquad
G_*\odot F_*\simeq(GF)_*.
\]

因此 Prof 中的 lax compositor，在此表示约定下对应函数侧的 **oplax** compositor；不能忽略2-态射方向。只有 compositor 与 unit 都是等价时，才得到相干的 pseudofunctor/functor 动态。on-the-nose等式需要所选模型中的额外 rectification 定理。[S07–S08]

---

# 第五编　观察、来源与模型精炼

## 18. 持续观察决定相对新颖性，不决定论文原创性

给旧事件基线 \(j:\mathcal E_{\rm old}\to\mathcal E\) 和观察

\[
N^\infty:\mathcal E\to\mathcal P(\mathcal K).
\]

定义

\[
\operatorname{OldMatch}(e)=
\mathcal E_{\rm old}^\simeq
\times_{\mathcal P(\mathcal K)^\simeq}
\{N^\infty(e)\}.
\]

观察相对新颖性即 \(\operatorname{OldMatch}(e)=\varnothing\)。若 \(N^\infty\) 全忠实，则等价于 \(e\) 不在旧基线本质像中。

若扩大观察时满足 \(N_0=r^*N_1\)，在弱观察下已能区别的旧／新对象在强观察下仍能区别。若同时改变 gauge、baseline 或观察规律，这个单调性不能直接沿用。[S05, S07–S08]

这不是文献优先权判据。论文原创性需要独立查重；数学重要性、算法优势及物理经验价值也不由这个纤维推出。

### 探针充分性

对小探针 \(i:\mathcal K\to\mathcal E\)，restricted Yoneda

\[
e\mapsto\operatorname{Map}(i(-),e)
\]

全忠实就是稠密／重建充分性。对象不变量的逐项一致，比自然等价弱；仅同伦群、同调群或相同基数一般不够。[S07–S08, S36]


### 小 probes、coprobes 与局部化

若小 `i:K→E` 稠密，则 `Map(i(-),-)` 全忠实。反射 `L:E→D` 的右伴随全忠实时，`Li` 在 D 中仍稠密，因为对 d∈D有

\[
\operatorname{Map}_D(Li(-),d)\simeq
\operatorname{Map}_E(i(-),jd).
\]

对偶地，coreflective 子范畴的右伴随把小 codense coprobes 送成 codense coprobes。`E` 可达只给一侧的小探针结论；不能不加 `E^op` 可达或相应其他条件就推出小 coprobes。

任意非反射局部化 λ 后，原探针是否仍充分，要检查

\[
a^*\lambda^*y_D:D\to\mathcal P(K)
\]

是否全忠实。它是准确判据，不保证自动成立。稠密函子的普通复合也不可不加条件当作稠密。[S07–S08]

### 丰富化的不可退化观察

在 pointed enriched base中，`Map(1,X)` 总有零映射，所以“存在underlying point”恒真。更强地，不存在同时保持初对象并strong-unital-monoidal到 `(Spaces,×,*)` 的shadow：它会把 `1→0` 送成不存在的 `*→∅`。

若某个非退化change-of-base确实strong monoidal且保持相关coends，则可运输equipment合成和Kan扩张；若还保守，则能检测一个**已经给定**比较映射是否等价。仅在shadow中找到代表，不能据此发明原层代表。

dense probe profile可检测完整语义，但不自动保持张量与coends。度量阈值、Banach范数球、谱值mapping或其他丰富化要保留各自数量／高阶信息。[S07–S08]

### provenance 的独立性

同一语义终点可以有不同实际证明和生成路径。保留路径不表示把历史每个细节都定义为新数学；要明确哪些差异允许 gauge 掉，哪些是研究问题需要的因果／构造信息。

---

## 19. 核心最小性：当前能说到哪里

C1 不修改 `01_FROZEN_CORE.md`，也不把“六项工作数据”宣布为已证的最小公理基。

可以作的是**相对数据独立性测试**：在不加桥接公理时，同一 raw 问题可以配不同 saturation；同一形式世界可以配不同实际像；同一实际事件可以配常值观察或充分观察；同一语义事件可以有不同 provenance。

这些例子表明删除某一字段会丢失本项目确实要区分的信息。它们不是一个已经完成的形式公理独立性证明，也不证明不存在另一种等价但更小的编码。严格最小性还需要先固定公理语言、结构态射与允许的定义等价。[S00, S05]

精炼原则是：把能够通过泛性质唯一恢复的对象移入派生层；把必须独立选择且会改变结论的对象明确保留为输入。

---

# 第六编　领域定理、应用与证据边界

## 20. 当前可以保留的领域数学

| 领域 | 保留的内容 | 不再作的外推 |
|---|---|---|
| 有限障碍论 | Reedy 逐点填充、torsor 障碍、相对幂零分层 | 不称一般有限塔求解算法；不以层数代替成本 |
| Coupl | 作用型 primary 阶数界及 \(u^d\) 无界族 | 不扩至所有不稳定高阶操作 |
| moment-angle | 整个支撑上的 DGA 收缩；非零输入支撑下界；F2 下齐次化充分条件 | 不把 input-support 等号称为非平凡 Massey 极值已达到 |
| 四重 Massey | 完整变分公式及二次项 \(z_{12}z_{34}\) | 不把某一受限系统非零当 ordinary 非平凡 |
| DGLA 立方体 | 固定边界 \(H^2\) 障碍；三方向 quotient；四方向首个潜在二次选择交互 | 固定边界失败不推出同一一阶方向全失败 |
| 小扩张 | section 乘法缺陷与曲率的精确公式 | 不说这些标准障碍群由母模型独自发明 |
| pro-p / Galois | fixed representation 的因子化及中央 overlap mismatch | 不自动下降到共轭商或全部 defining representations 的饱和问题 |
| SNT | finite-visibility 的有限指数稳定化引理与奇球楔综合推论 | 不宣称已确认文献首创或解决了 CP2 case |

详细定理、证明和状态在 `05_SECTORS_AND_APPLICATIONS.md` 与 `02_THEOREM_LEDGER.md`。

---

## 21. 两项必须降级的应用成果

### 21.1 “512000 图全部消失”的地位

目前归档的报告确实声称完整分类，并列出 512000 个图、8192 个 restricted-nonzero 候选及全部可消去的结果。[S38]

当前归档中可定位的程序是旧 R22 的 9/10 边**受限**枚举，以及一个十边反例的单例验证；它们不是 512000 图 ordinary 饱和分类的完整程序和证书。当前报告也没有逐例证书或可替代枚举的全称证明。

因此该全称分类保持 **REPORT / 待证据核验**：现有证据不足以把它作为“整个一维 sector 已被可靠排除”的已验证结论，也不足以仅凭历史执行声称替代完整证书或全称证明。

### 21.2 奇维球面有限楔 loop-SNT 刚性结果的地位

奇维球面有限楔的 loop-SNT 刚性，有可核对的 Hilton–Milnor 与 McGibbon–Møller 组合证明。在已核对的原文中，相关定理确实覆盖相应 \(\mathbb Z_P\)-有限型与有限 rational-H 源。[S40; B10]

它保留为**领域综合推论／待优先权审计的候选成果**。是否已知、是否新到足以单独发表、是否可归因于本理论的优势，不由短证明或未命中搜索确定。

---

## 22. SNT：带粘合资料的塔与只有层类型的列表

在空间范畴中，完整相干 Postnikov 塔可重建空间。但

\[
P_nX\simeq P_nY\quad\forall n
\]

只给逐层存在的等价，不提供一族相干等价，所以可能有 SNT 分支。经典分类中的 \(\lim^1\operatorname{Aut}(P_nX)\) 正处理这件事。[B10]

\(B\pi_0\operatorname{Aut}(P_nX)\) 可以计算这项集合级分类；它不是完整空间对象的高阶模群胚，不能据此丢掉更高自同伦数据。

对 \(\Omega\Sigma\mathbb{CP}^2\) 的整数 shear 链，本稿只保留条件性诊断：如果已有正确低层 Postnikov 模型，且在固定群中的下降像不稳定，则群塔非 ML。有限范围的 shear 稳定不证明全部 horizon 稳定。

历史稿 [S39] 曾使用“cofiber sequence 的同伦长正合列”来直接计算 \(\pi_*(\Sigma\mathbb{CP}^2)\)。一般 cofiber sequence 不产生这种协变同伦长正合列；需要相对同伦、纤维替代、稳定范围或独立文献计算。原数值不因此自动为假，但在补齐正确依据前不作为 C1 的主定理依赖。

---

# 第七编　识别地图、最小研发闭环与成熟度

## 23. 三类“完成”不能再混称

**表达完成：**已把某种问题写成精确对象、纤维或拉回。

**条件性定理完成：**在明确前提下证明了存在、唯一或重建。

**领域问题完成：**还证明了目标对象实际满足全部前提。

Horizon 相对拉回主要完成第一类，并连接若干第二类引擎。一般 CP2-SNT 的第三类完成尚无本稿证明。将第一类直接称作“THEORETICALLY CLOSED”会掩盖真正任务，今后不用这种无分层状态词。

---

## 24. 研究账本中的保留核心与待解接口

### 保留的稳定骨架

预目标问题、自然饱和、可能性群胚、初始对象子空间、实际／形式比较、相对提升、独立持续观察及 provenance。这些概念不再增加新同义名。

### 保留的通用证明引擎

Yoneda 与表示性；有限 Reedy 匹配；在正确实际比较前提下的 tower-ML；相干纤维极限；伴随约束修补；结构恢复；固定模型范围中的 Th–Mod 闭包。

### 当前真正需要领域输入的接口

1. **语义到修补语法：**闭理论如何编译成可靠且完整的见证／coherence laws？相同模型类不保证相同修补空间。
2. **frontier 的有效提取：**不能仅用未知全局解空间的空性作“算法”。
3. **相对 horizon 完备的局部识别：**需要容易核验而非同等难度的前提。
4. **约束与多步动态的运输：**证明所需方差、复合及极限保持，不能凭“自然”两个字。
5. **应用证据与原创性：**恢复精确计算证书，进行独立数学审核与文献优先权审计。

这些接口不因编号更多而自动缩小。

---

## 25. 推荐的验证闭环

后续研究与应用验证采用如下可核验链：

\[
\text{固定输入与旧基线}
\to\text{问题/观察接口}
\to\text{候选与比较}
\to\text{独立前提验证}
\to\text{正结果或反例}
\to\text{反馈到一般条件}.
\]

不要求每个一般定理必须先跨两个领域才算数学定理；一个严格证明已足够成立。但跨领域实例是**通用适用性与研究价值**的证据，不能与数学正确性混为一谈。

不以程序断言数量代替 theorem coverage；不把 proof-of-concept 等同自然问题突破；不把模型引导过思考的时间顺序当作它优于基线方法的因果证明。

---

## 26. 总结：精炼后的理论与没有得到的承诺

现在可以用一句话描述本项目：

> **从给定数学结构中构造相对于语义和观察的可能性、实现与修补问题，研究哪些有限／局部／简化数据足以控制整体数学，以及失败时具体丢失了什么信息。**

它的可信数学内容来自明确的数据、比较、泛性质、障碍计算和反例，而不是由“生成性”这一名称保证。

目前没有建立：无条件唯一的全部数学语言、通用有效 solver、自动重要性排序、已认证的新基础理论或完整 two-cell loop-SNT 分类。

目前确有：可用的严格空间值实现、有限 matching 与 horizon 的正确接口、若干领域识别判据、完全写出的反例与小型非线性例子，以及一套能继续接受反例检验的研究组织方式。

**派生研究与应用以附卷定理账本为准：只有具备明确证明与条件的结论才能作为后续证明依赖，其余内容保持可见的未证状态。**
