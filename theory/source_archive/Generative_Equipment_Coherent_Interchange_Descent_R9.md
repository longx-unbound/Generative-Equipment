# 生成装备研究 R9：相干交换下降与高维匹配边界

## 0. 本轮结论

本报告修正 R8 对有限二维矩形过于保守的一点，并完成其提出的 **Coherent Interchange Descent Theorem**。

核心结论是：

> 对有限二维双塔，不需要在小方格条件之外另加独立的 cocycle 公理。每个小方格的同伦拉回已经包含重叠上的全部二维相干性；若每个小方格比较映射都是有效满射，则任意有限矩形的兼容边界数据都局部可填充。若每个比较映射都是等价，则填充空间可缩，得到结构级交换。

证明不是逐点选取填充，而是沿有限下闭子集逐格附加；每一步都是一个匹配映射的基变换。因此不存在“选择之后再检查相容”的漏洞。

同时得到准确的高维边界：三维及以上，所有二维面分别可填充并不足够；必须控制完整的高阶匹配对象，即 punctured cube 的同伦极限。

本轮状态：

\[
\boxed{\text{PASS + DERIVED STRUCTURE}}
\]

---

## 1. 有限逆图与匹配对象

设 \(P\) 是有限偏序集，并把它看成逆范畴：当 \(u\le v\) 时有箭头

\[
v\longrightarrow u.
\]

设 \(\mathcal X\) 是一个 \(\infty\)-topos，且

\[
X:P\longrightarrow \mathcal X
\]

是一个图表。对 \(v\in P\)，记

\[
P_{<v}:=\{u\in P\mid u<v\},
\qquad
M_vX:=\lim_{u<v}X_u.
\]

由图表结构得到规范的匹配映射

\[
m_v:X_v\longrightarrow M_vX.
\]

若 \(A\subseteq P\) 满足

\[
v\in A, u\le v\Longrightarrow u\in A,
\]

则称 \(A\) 为下闭子集。

这些定义是标准 Reedy 匹配对象语言；这里的新工作是把它与 R7/R8 的存在像、交换缺陷及有限障碍塔精确拼合。

---

## 2. 单格附加引理

### 引理 2.1（One-cell Matching Attachment）

设 \(A\subseteq P\) 为下闭子集，\(v\notin A\)，并且

\[
P_{<v}\subseteq A.
\]

则 \(A\cup\{v\}\) 仍为下闭子集，且有同伦笛卡尔方块

\[
\begin{CD}
\displaystyle\lim_{A\cup\{v\}}X @>>> X_v\\
@VVV @VV m_v V\\
\displaystyle\lim_A X @>>> M_vX.
\end{CD}
\]

换言之，

\[
\lim_{A\cup\{v\}}X
\simeq
\left(\lim_A X\right)\times_{M_vX}X_v.
\]

#### 证明

一个 \(A\cup\{v\}\)-相容锥，等价于：

1. 一个 \(A\)-相容锥；
2. 一个 \(X_v\) 中的点；
3. 两者在所有严格前驱 \(u<v\) 上给出的锥相同。

第 3 条正是它们在 \(M_vX\) 中像相同。该等价在映射空间层面成立，故给出上述同伦拉回。\(\square\)

### 推论 2.2

若 \(m_v\) 为有效满射，则

\[
\lim_{A\cup\{v\}}X\longrightarrow\lim_A X
\]

为有效满射；若 \(m_v\) 为等价，则该限制映射为等价。

这是因为在 \(\infty\)-topos 中，有效满射与等价都在基变换下稳定。

---

## 3. 有限匹配下降定理

### 定理 3（Finite Matching Descent）

设 \(A\subseteq B\subseteq P\) 是有限偏序集 \(P\) 的下闭子集。假设对每个

\[
v\in B\setminus A
\]

匹配映射

\[
m_v:X_v\longrightarrow M_vX
\]

都是有效满射。则限制映射

\[
\operatorname{res}_{B,A}:
\lim_BX\longrightarrow\lim_AX
\]

是有效满射。

若所有这些 \(m_v\) 都是等价，则 \(\operatorname{res}_{B,A}\) 是等价。

#### 证明

对有限集 \(B\setminus A\) 取一个与偏序相容的线性排列

\[
v_1,\ldots,v_s,
\]

使得每个 \(v_t\) 的所有严格前驱都属于

\[
A_{t-1}:=A\cup\{v_1,\ldots,v_{t-1}\}.
\]

令 \(A_t=A_{t-1}\cup\{v_t\}\)。由引理 2.1，

\[
\lim_{A_t}X\longrightarrow\lim_{A_{t-1}}X
\]

是 \(m_{v_t}\) 的基变换。因此它是有效满射；若 \(m_{v_t}\) 是等价，则它是等价。有限复合保持这两个性质，故结论成立。\(\square\)

### 定理 3.1（Connectivity Refinement）

若每个 \(m_v\) 是 \(c_v\)-连通的，则

\[
\lim_BX\longrightarrow\lim_AX
\]

至少是

\[
\min_{v\in B\setminus A}c_v
\]

连通的。

特别地，有效满射情形就是 \((-1)\)-连通情形。

#### 证明

连通映射在基变换下稳定，有限复合的连通度至少为各因子的最小值。逐格应用引理 2.1 即得。\(\square\)

---

## 4. 二维矩形中的匹配对象

取

\[
P=[0,R]\times[0,N]
\]

及双塔

\[
\mathcal S_{r,k}.
\]

对 \(r,k>0\)，严格下集 \(P_{<(r,k)}\) 是两个主下集之并：

\[
\downarrow(r-1,k)\ \cup\ \downarrow(r,k-1),
\]

其交为

\[
\downarrow(r-1,k-1).
\]

主下集有最大元，所以其上图表的极限就是最大元处的值。故有规范等价

\[
M_{r,k}\mathcal S
\simeq
\mathcal S_{r-1,k}
\times_{\mathcal S_{r-1,k-1}}
\mathcal S_{r,k-1}.
\]

于是匹配映射正是 R8 的小方格比较映射

\[
\chi_{r-1,k-1}:
\mathcal S_{r,k}\longrightarrow
\mathcal S_{r-1,k}
\times_{\mathcal S_{r-1,k-1}}
\mathcal S_{r,k-1}.
\]

这一步是二维闭合的关键：一个格点的全部过去不是比这个拉回更大的对象。

---

## 5. 相干交换下降定理

记坐标轴边界

\[
\partial_-P
:=
([0,R]\times\{0\})
\cup
(\{0\}\times[0,N]).
\]

它是 \(P\) 的下闭子集。

### 定理 5（Coherent Interchange Descent）

若对所有 \(1\le r\le R\)、\(1\le k\le N\)，

\[
\chi_{r-1,k-1}
\]

都是有效满射，则

\[
\lim_{[0,R]\times[0,N]}\mathcal S
\longrightarrow
\lim_{\partial_-P}\mathcal S
\]

是有效满射。

等价地：任意沿两条坐标轴给出的相容边界分支，都局部地延拓为整个有限矩形上的相干分支。

若每个 \(\chi_{r-1,k-1}\) 都是等价，则上述限制映射是等价；因此每组边界数据的全矩形填充空间可缩。

#### 证明

由第 4 节，所有内部格点的匹配映射恰为对应的 \(\chi\)。对下闭包含

\[
\partial_-P\subseteq P
\]

应用定理 3 即得。\(\square\)

### 推论 5.1（任意下闭边界）

设 \(A\subseteq P\) 是任意下闭子集。若每个 \((r,k)\in P\setminus A\) 的 \(\chi_{r-1,k-1}\) 是有效满射，则

\[
\lim_P\mathcal S\longrightarrow\lim_A\mathcal S
\]

是有效满射；若这些 \(\chi\) 都是等价，则该映射是等价。

### 推论 5.2（大矩形比较）

任意有限子矩形的大尺度比较映射的有效满射性，由其中所有小方格比较映射的有效满射性推出。二维有限情形没有额外独立的高阶 cocycle 障碍。

### 严格解释

这里的“无额外 cocycle”不表示可以任意逐格选择点。逐格选择通常不能严格相容。定理使用的是同伦极限与有效满射的基变换稳定性，因此相干性在每一步已经包含在匹配对象中。

---

## 6. 全局填充空间的迭代纤维分解

固定一个边界点

\[
b\in \lim_A X.
\]

沿定理 3 的线性排列定义

\[
F_0:=\{b\},
\qquad
F_t:=F_{t-1}\times_{M_{v_t}X}X_{v_t}.
\]

则有规范等价

\[
F_s
\simeq
\operatorname{fib}_b
\left(
\lim_BX\to\lim_AX
\right).
\]

因此得到：

1. 每一阶段的选择空间是一个匹配映射纤维的基变换；
2. 若所有匹配纤维局部非空，则全局填充纤维局部非空；
3. 若所有匹配纤维可缩，则全局填充纤维可缩；
4. 若各匹配纤维是群对象作用下的 torsor，则全局填充空间是一个有限迭代 torsor。

最后一项一般不能无条件写成这些群对象的直积：前面阶段的选择可能扭曲后面阶段的作用。只有在作用平凡或给定相容分裂时，才可进一步压成直积描述。

---

## 7. 与 R7 的残余障碍拼合

假设每个小方格比较映射的纤维问题处于 R7 的仿射情形。对某个兼容角数据 \(c\)，其局部残余障碍为

\[
[\rho_{r,k}(c)]
\in
\pi_0\operatorname{cofib}(D_{r,k}).
\]

则定理 5 给出：

### 定理 7（Residual-to-Global Descent）

若每个内部格点的局部残余类都普遍为零，即相应 \(\chi_{r,k}\) 为有效满射，则任意有限矩形的边界数据都局部可延拓为全局相干填充。

若进一步每个局部解纤维可缩，则全局填充唯一至可缩选择。

因此二维全局判据可以完全分解为有限个局部 residual obstruction；但其解空间一般仍是迭代 torsor，而不是无条件的单一群。

---

## 8. 三维及以上的精确边界

对

\[
P=\prod_{i=1}^d[0,N_i],
\]

格点 \(v\) 的严格下集由各坐标方向的直接前驱主下集覆盖。其匹配对象是这些面及全部交的同伦极限；在单位 \(d\)-立方体中，这正是 punctured \(d\)-cube 的极限。

### 定理 8（Higher Matching Descent）

对有限 \(d\)-维网格及下闭包含 \(A\subseteq B\)，若每个新格点的完整高阶匹配映射

\[
X_v\longrightarrow M_vX
\]

是有效满射，则

\[
\lim_BX\longrightarrow\lim_AX
\]

是有效满射；若全部为等价，则限制映射为等价。

证明仍是定理 3。

### 命题 8.1（二维面条件在三维不充分）

在三维中，所有二维边际比较都为满射，不推出完整三维匹配映射为满射。

#### 有限集合反例

取三个立即前驱的值均为 \(\{0,1\}\)，所有更低交叠数据为终对象。令顶点对象为偶校验子集

\[
Q=
\{(a,b,c)\in\{0,1\}^3\mid a+b+c=0\pmod 2\}.
\]

三个两两投影

\[
Q\to\{0,1\}^2
\]

全为满射，所以每个二维边际都可实现；但

\[
Q\longrightarrow\{0,1\}^3
\]

不是满射，例如 \((0,0,1)\) 无提升。因此两两兼容不蕴含三重同时兼容。

这给出准确 no-go：

\[
\boxed{
d\ge3\text{ 时，不能只用二维小方格替代完整高阶匹配对象。}
}
\]

---

## 9. 对 R3/Postnikov matching tower 的意义

在 R8 的双滤过

\[
\mathcal S_{r,k}
=
\Gamma(B^{(r)},P_k^B E)
\]

中：

1. R7 的精确可生存像给出“是否有完整未来”；
2. R8 的 \(\chi_{r,k}\) 给出一个小方格的 simultaneous-effectivity defect；
3. R9 证明二维有限矩形的全部相干交换由这些 \(\chi_{r,k}\) 完全控制；
4. 若 \(\chi_{r,k}\) 全为等价，则 cellular truncation 与 Postnikov truncation 在整个有限矩形上满足结构级 Beck–Chevalley 交换；
5. 若它们仅为有效满射，则得到存在级交换，但仍保留非平凡选择与自同构。

这把“R3 matching tower 与经典 Postnikov tower 自然等价”的有限版本拆为两个独立且可验证的断言：

\[
\text{终点比较等价}
\quad+
\quad
\text{所有局部 }\chi_{r,k}\text{ 为等价}.
\]

第一项比较解空间，第二项保证比较与两个截断方向的全部有限相干结构相容。仅有最终总极限等价，仍不能推出第二项。

---

## 10. 有限与无限之间的边界

本报告只证明有限下闭附加。对无限网格，有限阶段全部可填充不自动给出一个实际无限填充；还需要控制：

- 逆极限是否保持有关有效性；
- \(\lim^1\) 或更高派生极限；
- 超完备性或收敛性；
- Mittag–Leffler 型条件。

因此不能把定理 5 偷换成无限塔的无条件 actualization。正确结论是：

\[
\boxed{
\text{finite coherent descent 已闭合；infinite actualization 仍需独立收敛输入。}
}
\]

---

## 11. 已知性与新颖性边界

标准输入包括：

- Reedy 匹配对象与有限逆范畴；
- 同伦极限的逐格构造；
- 有效满射、等价与连通映射的基变换稳定性；
- 主下集上的极限等于最大元处的值。

本项目中的派生结构是：

1. 识别 R8 的 \(\chi_{r,k}\) 正是二维格点匹配映射；
2. 将有限 matching descent 应用于 R3/Postnikov 双滤过；
3. 证明局部交换缺陷到全矩形填充的严格传递；
4. 给出全局填充纤维的迭代 torsor 分解；
5. 用奇偶校验反例划出二维与三维之间的精确边界。

这些结果主要是标准同伦极限技术在冻结装备上的系统派生，不主张未经文献核查的原创优先权。

参考背景：

- Emily Riehl and Dominic Verity, *The Theory and Practice of Reedy Categories*, 2014, [arXiv:1304.6871](https://arxiv.org/abs/1304.6871).
- Michael Shulman, *Homotopy Limits and Colimits and Enriched Homotopy Theory*, 2008, [arXiv:math/0610194](https://arxiv.org/abs/math/0610194).

---

## 12. 最终定理包

本轮得到以下闭合链条：

\[
\boxed{
\begin{gathered}
\text{matching effective epis}
\\\Downarrow\\
\text{finite lower-ideal descent}
\\\Downarrow\\
\text{2D local squares imply global rectangle fillability}
\\\Downarrow\\
\text{global filler = iterated local homotopy fiber}
\end{gathered}
}
\]

并有高维修正：

\[
\boxed{
\text{在 }d\ge3\text{ 中，把 matching map 降为全部 pairwise squares 是错误的。}
}
\]

因此，R8 留下的二维相干下降问题已经解决；下一步应转向非仿射 Coupl 的有限差分结构，以及 nilpotent 系数作用的中心分层，而不是继续寻找一个实际上并不存在的二维额外 cocycle 条件。
