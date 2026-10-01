# 生成装备研究 R6：耦合障碍演算、分支零点与开放边界

## 0. 本轮结论

R5 已证明：对连通、截断、幂零纤维，R3 matching tower 与经典 Postnikov obstruction tower 在共同双滤过

\[
\mathcal S_{r,k}=\Gamma(B^{(r)},P_k^B E)
\]

中自然比较，并在完整分支空间上给出同一对象；逐层障碍类、提升扭子与高阶自同伦群相同。

本轮把“分支改变如何改变下一障碍”推进到一个完整的有限阶段理论：

1. 在固定系数的两阶段情形，耦合项由 Postnikov 类的约化余乘积（cross-effect）完全控制。
2. 分支轨道是否含有有效分支，等价于一个精确的障碍像集命中条件。
3. 在一般幂零情形，不同分支的障碍可能落在不同的局部系数上；正确对象是分支群胚上的**依赖型障碍截面**，而不是预先固定的单一群值函数。
4. 选定系数运输后，Coupl 是该群胚上的一个扭曲 1-余循环；没有这种选择时，全局相减一般没有自然意义。
5. 固定截断高度的理论在结构上闭合，而且在适当有限输入下可算法化。第一处真正的当前开放边界，是要求对任意高度统一输出完整 Coupl/Postnikov 塔；即使只对球面做到这一点，也会给出全部稳定同伦群。

因此，本项目在“任意给定的有限 Postnikov 数据”范围内已经从障碍检测推进到分支预测；尚未解决的不是有限层理论，而是**无限高度的统一求值问题**。

---

## 1. 两阶段模型：Coupl 的精确来源

令 \(A,C\) 为阿贝尔群，\(m<n\)，并令

\[
\kappa:K(A,m)\longrightarrow K(C,n+1)
\]

表示一个上同调类

\[
[\kappa]\in H^{n+1}(K(A,m);C).
\]

定义两阶段空间

\[
F_\kappa:=\operatorname{hofib}(\kappa).
\]

于是有纤维序列

\[
K(C,n)\longrightarrow F_\kappa\longrightarrow K(A,m).
\]

对 CW 复形或 Kan 型基空间 \(B\)，一个低阶分支是映射

\[
a:B\to K(A,m),\qquad [a]\in H^m(B;A).
\]

定义其下一层障碍

\[
o_\kappa(a):=a^*[\kappa]\in H^{n+1}(B;C).
\]

### 定理 1（两阶段提升定理）

低阶分支 \(a\) 能提升到 \(F_\kappa\) 当且仅当

\[
o_\kappa(a)=0.
\]

若提升存在，则提升的同伦类构成 \(H^n(B;C)\)-扭子；更完整地，提升空间是映射空间

\[
\operatorname{Map}(B,K(C,n))
\]

的主齐性空间，因而在选定基点后

\[
\pi_i(\mathrm{Lift}(a))\cong H^{n-i}(B;C)
\]

（在相应指标范围内）。

#### 证明

提升 \(a\) 到同伦纤维，等价于给出 \(\kappa\circ a\) 到常值映射的零伦。由于

\[
[B,K(C,n+1)]\cong H^{n+1}(B;C),
\]

零伦存在恰好等价于 \(a^*[\kappa]=0\)。两个零伦之差由
\([B,\Omega K(C,n+1)]\cong H^n(B;C)\) 测量；对完整映射空间取同伦群便得到最后一个公式。∎

---

## 2. 约化余乘积公式

用

\[
\mu:K(A,m)\times K(A,m)\to K(A,m)
\]

表示加法。定义 \(\kappa\) 的二阶 cross-effect

\[
\operatorname{cr}_2(\kappa)
:=
\mu^*[\kappa]-p_1^*[\kappa]-p_2^*[\kappa]
\in H^{n+1}(K(A,m)^2;C).
\]

### 定理 2（Coupl 公式）

对 \(a,b\in H^m(B;A)\)，有

\[
o_\kappa(a+b)
=o_\kappa(a)+o_\kappa(b)
+(a,b)^*\operatorname{cr}_2(\kappa).
\]

所以相对于背景分支 \(a\) 的有限差分为

\[
\Delta_b o_\kappa(a)
:=o_\kappa(a+b)-o_\kappa(a)
=o_\kappa(b)+(a,b)^*\operatorname{cr}_2(\kappa).
\]

这给出 Coupl 的精确定义：

\[
\boxed{\operatorname{Coupl}_\kappa(a;b)=\Delta_b o_\kappa(a)}.
\]

#### 证明

由 \(a+b=\mu\circ(a,b)\)，

\[
o_\kappa(a+b)=(a,b)^*\mu^*[\kappa].
\]

把 \(\mu^*[\kappa]\) 按定义拆为两个投影项与约化余乘积项即可。∎

### 推论 2.1（何时没有耦合）

下列条件等价：

1. 对所有 \(B,a,b\)，\(o_\kappa(a+b)=o_\kappa(a)+o_\kappa(b)\)；
2. \(\operatorname{cr}_2(\kappa)=0\)；
3. \([\kappa]\) 对 \(K(A,m)\) 的 Hopf 代数结构是 primitive 元。

反向蕴含可在 \(B=K(A,m)^2\) 上取两个通用投影类得到。因此，“障碍可加”不是默认事实，而是 \(k\)-不变量 primitive 的等价条件。

---

## 3. 高阶耦合与多项式次数

对 \(r\ge 2\)，令 \(\mu_S:K(A,m)^r\to K(A,m)\) 为把指标在 \(S\) 中的坐标相加的映射，并定义

\[
\operatorname{cr}_r(\kappa)
=
\sum_{S\subseteq\{1,\dots,r\}}
(-1)^{r-|S|}\mu_S^*[\kappa].
\]

这里空集项由基点给出，约化类情形下为零。对任意 \(a_1,\dots,a_r\in H^m(B;A)\)，

\[
(a_1,\dots,a_r)^*\operatorname{cr}_r(\kappa)
=
\sum_S(-1)^{r-|S|}
o_\kappa\!\left(\sum_{i\in S}a_i\right).
\]

### 定理 3（高阶 Coupl）

所有 \(r\) 分支相互作用均由 \(\operatorname{cr}_r(\kappa)\) 控制。若

\[
\operatorname{cr}_{d+1}(\kappa)=0,
\]

则 \(o_\kappa\) 是 Eilenberg–Mac Lane 意义下次数至多 \(d\) 的自然上同调运算；所有 \((d+1)\) 阶及更高的约化有限差分消失。

因此，Coupl 不只是“一阶修正项”：它有由同一个 \(k\)-不变量生成的完整有限差分层级。线性、二次和更高相互作用分别对应 primitive、二阶以及更高 cross-effect。

---

## 4. 分支轨道的有效性判据

设允许的低阶修改形成子群

\[
H\le H^m(B;A),
\]

并固定背景分支 \(a_0\)。可达分支轨道为

\[
\mathcal O(a_0)=a_0+H.
\]

### 定理 4（Branch-Orbit Effectivity）

轨道 \(\mathcal O(a_0)\) 中存在可提升分支，当且仅当

\[
-o_\kappa(a_0)
\in
\left\{
\operatorname{Coupl}_\kappa(a_0;h):h\in H
\right\}.
\]

#### 证明

存在 \(h\in H\) 使 \(a_0+h\) 可提升，等价于

\[
0=o_\kappa(a_0+h)
=o_\kappa(a_0)+\operatorname{Coupl}_\kappa(a_0;h).
\]

移项即得。∎

重要的是，右侧一般只是一个像集，不必是子群；只有在 primitive/线性情形，它才退化为群同态的像。由此可见，非线性 Coupl 的本质不是“多一个障碍群”，而是**有效分支构成非线性零点集**。

---

## 5. 最小二次基准：两个可行分支之和可以失效

令

\[
u\in H^2(K(\mathbb Z,2);\mathbb Z)
\]

为通用类，并取

\[
\kappa=u^2\in H^4(K(\mathbb Z,2);\mathbb Z).
\]

于是

\[
K(\mathbb Z,3)\to F_{u^2}\to K(\mathbb Z,2)
\]

是一个两阶段 Postnikov 模型，且

\[
o(a)=a^2,
\qquad
\operatorname{Coupl}(a;b)=2ab+b^2,
\qquad
\operatorname{cr}_2(u^2)=2u_1u_2.
\]

取

\[
B=S^2\times S^2,
\]

并令 \(x,y\in H^2(B;\mathbb Z)\) 是两个因子的生成元。因为

\[
x^2=y^2=0,
\]

分支 \(x\) 与 \(y\) 各自都可提升；但

\[
o(x+y)=(x+y)^2=2xy\ne0,
\]

所以它们的和不能提升。

这给出最小的“耦合不是独立障碍之和”样例：失败完全由交叉项 \(2xy\) 产生。

---

## 6. 一般幂零塔：障碍不是单一群值函数

现在考虑 Moore–Postnikov 塔的一层

\[
E_k\longrightarrow E_{k-1}
\]

及低阶分支群胚

\[
\mathcal B_{k-1}:=\Gamma_B(E_{k-1}).
\]

对每个分支 \(s\)，第 \(k\) 个同伦群给出局部系数

\[
\Pi_k(s),
\]

而障碍位于

\[
o_k(s)\in H^{k+1}(B;\Pi_k(s)).
\]

当 \(s\) 改变时，\(\Pi_k(s)\) 也可能改变。因此表达式

\[
o_k(s')-o_k(s)
\]

在没有额外数据时甚至不一定有类型。

### 定理 5（依赖型障碍截面）

存在分支群胚上的上同调空间族

\[
\mathscr K_{k+1}\longrightarrow\mathcal B_{k-1},
\]

其在 \(s\) 上的纤维为带局部系数的上同调表示空间

\[
\operatorname{Map}_B(B,K(\Pi_k(s),k+1)).
\]

第 \(k\) 层 Postnikov 类给出自然障碍截面

\[
\mathrm{Obs}_k:\mathcal B_{k-1}\longrightarrow\mathscr K_{k+1}.
\]

若 \(0\) 表示零截面，则第 \(k\) 层提升空间由同伦零点给出：

\[
\boxed{
\mathcal B_k
\simeq
\operatorname{Eq}^{h}_{\mathcal B_{k-1}}
(\mathrm{Obs}_k,0)
\simeq
\mathcal B_{k-1}
\mathop{\times^{h}}_{\mathscr K_{k+1}}
\mathcal B_{k-1}
}.
\]

最后一个同伦拉回的两条映射分别是 \(\mathrm{Obs}_k\) 与零截面。

在 \(\pi_0\) 上，这正是

\[
[s]\text{ 可提升}
\iff
o_k(s)=0\in H^{k+1}(B;\Pi_k(s)).
\]

#### 证明要点

Postnikov 层是相应 Eilenberg–Mac Lane 局部系统的扭曲同伦纤维。沿每个 \(s\) 拉回后，提升等价于给出拉回 \(k\)-不变量的零伦。把所有 \(s\) 同时参数化，恰得到障碍截面与零截面的同伦拉回。R5 的比较定理再把这个同伦拉回逐层运输到 R3 matching 模型。∎

这个公式是本轮的结构性突破：它同时包含存在性、扭子、多分支以及高阶自同伦，而不强迫所有分支共享同一个障碍群。

---

## 7. 运输后的 Coupl 是扭曲 1-余循环

若一个允许的分支修改 \(\alpha:s\rightsquigarrow s'\) 同时给出系数运输

\[
T_\alpha:
H^{k+1}(B;\Pi_k(s'))
\xrightarrow{\cong}
H^{k+1}(B;\Pi_k(s)),
\]

则可以定义有类型的相对耦合

\[
\operatorname{Coupl}_\alpha(s;s')
:=
T_\alpha(o_k(s'))-o_k(s).
\]

对可复合修改 \(s\xrightarrow{\alpha}s'\xrightarrow{\beta}s''\)，有

\[
\operatorname{Coupl}_{\beta\circ\alpha}(s;s'')
=
\operatorname{Coupl}_\alpha(s;s')
+T_\alpha\bigl(\operatorname{Coupl}_\beta(s';s'')\bigr).
\]

所以 Coupl 不是任意差分，而是分支群胚上由系数运输扭曲的 1-余循环。

### 推论 7.1（全局标量 Coupl 的无规范性）

只有在选定 \(H^{k+1}(B;\Pi_k(s))\) 的一致平凡化，或限制到系数自然固定的分支族后，Coupl 才退化为单个固定阿贝尔群中的函数。改变平凡化会按相应自同构改变 Coupl；若障碍群族存在非平凡单值化，便不存在路径无关的规范相减。

这不是技术缺陷，而是一般局部系数问题的正确类型。

---

## 8. 即使在幂零情形，障碍群也确实会漂移

令

\[
G=\mathbb Z,\qquad M=\mathbb Z^2,
\]

并令生成元通过幺幂矩阵

\[
T=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}
\]

作用在 \(M\) 上。该作用是幂零的：存在由平凡作用商组成的有限过滤。

取 \(B=S^1\times S^2\)。一个低阶分支可令 \(\pi_1(B)\to G\) 把生成元送到 \(r\in\mathbb Z\)，从而诱导单值化为 \(T^r\) 的局部系统 \(M_r\)。此时

\[
H^3(B;M_r)
\cong H^1(S^1;M_r)
\cong M/(T^r-I)M.
\]

于是

\[
H^3(B;M_0)\cong\mathbb Z^2,
\qquad
H^3(B;M_1)\cong\mathbb Z,
\qquad
H^3(B;M_2)\cong\mathbb Z\oplus\mathbb Z/2.
\]

这些群甚至不彼此同构。因此，在一般截断幂零塔中，把所有分支障碍强行写进一个预先固定的群，不可能是自然的。依赖型障碍截面不是抽象修饰，而是被具体例子迫使出来的结构。

---

## 9. 有限截断幂零纤维的闭合递归

设纤维 \(F\) 连通、\(N\)-截断且幂零。定义

\[
\mathcal B_k:=\Gamma(B,P_k^B E).
\]

则：

1. \(\mathcal B_1\) 由非阿贝尔 \(\pi_1\) 数据、带状 \(H^2\) 障碍及必要的下中心列细化控制；
2. 对每个 \(k\ge2\)，存在依赖型障碍截面 \(\mathrm{Obs}_k\)，并有
   \[
   \mathcal B_k\simeq
   \operatorname{Eq}^{h}_{\mathcal B_{k-1}}(\mathrm{Obs}_k,0);
   \]
3. 因为 \(F\) 是 \(N\)-截断的，该递归在有限步终止，且
   \[
   \mathcal B_N\simeq\Gamma(B,E);
   \]
4. 由 R5，自然同一个递归也可在 R3 matching tower 中计算；两套障碍、运输、扭子和高阶同伦群一致。

### 有限范围的最终判据

一个初始分支有效，当且仅当存在一条有限分支链

\[
s_1\leftarrow s_2\leftarrow\cdots\leftarrow s_N
\]

使每一级依赖型障碍都落在零截面。若只允许给定的分支修改群胚 \(\mathcal O\)，则把每一步限制到相应轨道即可。

这已经是一般截断幂零纤维的完整结构答案；剩余工作是输入具体 Postnikov 数据并求各零点集，而不是再增加新的普遍障碍层。

---

## 10. “困难”与“开放”的精确分界

### 10.1 固定高度：原则上可解

对每个预先固定的 \(k>1\)，有限单连通 simplicial 输入的 \(\pi_k\) 与前 \(k\) 层 Postnikov 系统存在多项式时间算法（当 \(k\) 被视为固定常数）。因此，不能把“固定截断高度下提取 Postnikov 数据”称为普遍不可解。

这与本研究的结论一致：给定有限高度与有效表示，R3/Postnikov/Coupl 递归是有限过程。

### 10.2 任意高度统一输出：触及开放问题

考虑下面的假想引擎 \(\mathbf U\)：

> 输入球面 \(S^n\)，输出它在所有高度的完整 Postnikov/Coupl 塔，包括每个 \(\pi_j(S^n)\)、相应作用与所有 \(k\)-不变量。

若 \(\mathbf U\) 存在，则对任意稳定茎指标 \(q\)，选取处在 Freudenthal 稳定范围内的 \(n\)，便可从塔中读出

\[
\pi_{n+q}(S^n)\cong\pi_q^{\mathrm S}.
\]

所以：

### 定理 6（开放边界归约）

一个能对所有球面、所有高度统一完成 Coupl/Postnikov 求值的理论，将计算全部稳定同伦群 \(\pi_*^{\mathrm S}\)，并且还包含更强的不稳定信息。

现有稳定茎方法只在有限范围内给出完整或近完整结果；计算会遭遇新的微分与扩张问题，尚无覆盖所有维数的闭式或完成算法。因此，完整无限高度 Coupl 引擎至少与这一经典未解计算同样困难。

这里的结论是一个**归约与当前知识边界**，不是不可判定性定理：我们没有证明这样的引擎逻辑上不可能，而是证明继续完成它需要解决一个公认尚未完成的核心问题。

---

## 11. 研究状态判定

| 范围 | 状态 | 本轮给出的结果 |
|---|---|---|
| 固定系数两阶段纤维 | 已闭合 | Coupl = \(k\)-不变量的有限差分；cross-effect 完全控制非线性 |
| 固定分支轨道 | 已闭合 | 有效性等价于 Coupl 像集命中 \(-o(a_0)\) |
| 一般截断幂零纤维 | 结构上已闭合 | 依赖型障碍截面及逐层同伦零点递归 |
| R3 与 Postnikov 的兼容 | 已闭合 | R5 比较把上述结构自然运输到 matching tower |
| 固定截断高度的有限输入 | 原则上可算法化 | 不构成开放边界 |
| 所有高度、所有球面的统一求值 | 当前开放 | 至少包含全部稳定茎及球面不稳定 Postnikov 数据 |

---

## 12. 对总体理论的更新

原先的“Coupl 变化律”应升级为以下三层陈述：

1. **局部代数层**：当系数固定时，Coupl 是 \(k\)-不变量的 cross-effect；其多项式次数测量分支相互作用的最高阶。
2. **全局几何层**：当系数随分支改变时，障碍是上同调空间族的截面；Coupl 只有在选择运输后才成为扭曲 1-余循环。
3. **预测层**：有效分支是障碍截面的同伦零点；R3 matching 计算与 Postnikov 计算给出同一个零点空间。

这使理论从“列出障碍”进入“预测分支改变后哪些障碍会被消去、保留或由交叉项重新产生”的阶段。

同时，本轮也确定了停止点：若不再限制截断高度，下一步不再只是完善形式体系，而会直接进入球面稳定与不稳定同伦群的开放计算。

---

## 参考入口

- J. P. May, *A Concise Course in Algebraic Topology*：经典障碍论、Postnikov 系统与 \(k\)-不变量。  
  <https://www.math.uchicago.edu/~may/CONCISE/ConciseRevised.pdf>
- M. Čadek, M. Krčál, J. Matoušek, L. Vokřínek, U. Wagner, *Polynomial-time computation of homotopy groups and Postnikov systems in fixed dimension*：固定高度的算法边界。  
  <https://arxiv.org/abs/1211.3093>
- D. C. Isaksen, G. Wang, Z. Xu, *Stable homotopy groups of spheres*：稳定茎的有限范围计算及其困难。  
  <https://arxiv.org/abs/2001.04247>
- D. C. Isaksen, G. Wang, Z. Xu, *More stable stems*：截至有限范围的系统计算、剩余微分与扩张不确定性。  
  <https://arxiv.org/abs/2001.04511>

---

## 最终结论

在“给定一般截断幂零纤维”的范围内，理论已经完成下一次关键升级：

\[
\boxed{
\text{有效分支空间}
=
\text{依赖型 Postnikov 障碍截面与零截面的同伦交}
}
\]

固定系数时，这一同伦交可由 \(k\)-不变量的 cross-effect 展开为显式 Coupl 演算；一般局部系数时，Coupl 是带运输的扭曲余循环。

继续要求一个覆盖所有高度的统一显式求值理论，会包含全部球面稳定同伦群的计算。这里是本轮抵达的第一个真正未解决边界。
