# 生成装备研究 R10：Polynomial Coupl 微积分、极化与压缩边界

## 0. 本轮结论

R7 已证明：仿射 Coupl 的求零问题可压缩为一个 cofiber 中的残余障碍。R10 研究下一层——有限次数但非仿射的 Coupl。

结论分为正负两部分。

正面：有限差分给出一个有限长度、自然且精确的交互结构：

- 每次差分把次数降低一；
- 最高 cross-effect 是对称多加性的；
- 二次 Coupl 在 \(2\) 可逆时有唯一“常数 + 线性 + 对称二次型”分解；
- 在有理系数下，任意有限次数 Coupl 唯一分解为有限个对称多线性齐次层；
- 平移不变方向组成规范子群，可先作 gauge quotient。

负面：

- 次数 \(\ge2\) 时，一般不存在单一线性 cofiber 残余；
- 差分层是有限交互 jet，不是通用求根算法；
- 限制到子群或沿分支推进不保证次数下降；
- 整数多项式求零已包含 Hilbert 第十问题，故抽象 polynomial Coupl 不存在统一判定算法。

本轮状态：

\[
\boxed{\text{PASS + DERIVED STRUCTURE}}
\]

---

## 1. 有限差分定义

设 \(H,G\) 为阿贝尔群，\(q:H\to G\) 为任意映射。对 \(h\in H\)，定义差分算子

\[
(\Delta_hq)(a):=q(a+h)-q(a).
\]

由于 \(H\) 交换，差分算子彼此交换：

\[
\Delta_h\Delta_kq=\Delta_k\Delta_hq.
\]

### 定义 1.1（Eilenberg–Mac Lane 次数）

称 \(q\) 的次数不超过 \(d\)，若对任意 \(a,h_0,\ldots,h_d\in H\)，

\[
\Delta_{h_d}\cdots\Delta_{h_0}q(a)=0.
\]

常值映射次数 \(\le0\)，仿射映射次数 \(\le1\)。

定义第 \(r\) 个 cross-effect

\[
\operatorname{cr}_rq(h_1,\ldots,h_r)
:=
(\Delta_{h_r}\cdots\Delta_{h_1}q)(0).
\]

---

## 2. 差分降阶与有限 Taylor 恒等式

### 定理 2（Degree Lowering）

若 \(q\) 次数 \(\le d\)，则对任意 \(h\in H\)，映射

\[
\Delta_hq:H\to G
\]

次数 \(\le d-1\)。

#### 证明

任取 \(d\) 个增量 \(k_1,\ldots,k_d\)，有

\[
\Delta_{k_d}\cdots\Delta_{k_1}(\Delta_hq)
=
\Delta_h\Delta_{k_d}\cdots\Delta_{k_1}q
=0.
\]

\(\square\)

### 定理 2.1（Finite Difference Taylor Formula）

对任意映射 \(q\) 及任意 \(a,h_1,\ldots,h_m\)，有恒等式

\[
q\!\left(a+\sum_{i=1}^m h_i\right)
=
\sum_{S\subseteq[m]}
\left(\prod_{i\in S}\Delta_{h_i}\right)q(a).
\]

若 \(q\) 次数 \(\le d\)，则所有 \(|S|>d\) 的项消失，因而

\[
q\!\left(a+\sum_{i=1}^m h_i\right)
=
\sum_{\substack{S\subseteq[m]\\|S|\le d}}
\left(\prod_{i\in S}\Delta_{h_i}\right)q(a).
\]

#### 证明

令平移算子 \(T_hq(a)=q(a+h)\)。由于

\[
T_h=1+\Delta_h
\]

且各算子交换，展开

\[
T_{h_1}\cdots T_{h_m}
=
\prod_{i=1}^m(1+\Delta_{h_i})
\]

即得。\(\square\)

### 解释

次数 \(d\) 的 Coupl 由至多 \(d\) 重的交互差分完全控制。这是一个有限交互 jet；它精确描述多个修正同时施加时出现的非线性项。

---

## 3. 最高 cross-effect 的多加性

差分满足

\[
\Delta_{x+y}
=
\Delta_x+\Delta_y+\Delta_x\Delta_y.
\]

### 定理 3（Top Polarization）

若 \(q\) 次数 \(\le d\)，则

\[
B_d:=\operatorname{cr}_dq:H^d\to G
\]

是对称的 \(d\)-重加性映射。

#### 证明

对称性来自差分算子的交换性。考察第一变量：

\[
B_d(x+y,h_2,\ldots,h_d)
\]

用 \(\Delta_{x+y}=\Delta_x+\Delta_y+\Delta_x\Delta_y\) 展开。前两项分别是 \(B_d(x,-)\) 与 \(B_d(y,-)\)；第三项包含 \(d+1\) 重差分，因次数 \(\le d\) 而为零。其余变量同理。\(\square\)

### 推论 3.1

若 \(B_d=0\)，则 \(q\) 的次数实际上 \(\le d-1\)。因此最高 cross-effect 是次数下降的精确证人。

---

## 4. 仿射压缩的精确边界

### 定理 4（Affine Compression Criterion）

以下三个条件等价：

1. \(\operatorname{cr}_2q=0\)；
2. \(q-q(0):H\to G\) 是群同态；
3. 存在群同态 \(D:H\to G\)，使
   \[
   q(a+h)=q(a)+D(h)
   \]
   对所有 \(a,h\) 成立。

在这些等价条件成立时，对每个基点 \(a\)，方程 \(q(a+h)=0\) 可由 R7 的单一 residual class
   \[
   [-q(a)]\in\operatorname{coker}(D)
   \]
   判定。

#### 证明

\(\operatorname{cr}_2q(x,y)=0\) 等价于

\[
q(x+y)-q(x)-q(y)+q(0)=0,
\]

即 \(D=q-q(0)\) 可加。余下等价正是 R7 的 affine Coupl 定理。\(\square\)

因此：

\[
\boxed{
\operatorname{cr}_2q\ne0
\Longrightarrow
\text{不存在由同一个线性 }D\text{ 给出的通用单一 cofiber 压缩。}
}
\]

这里否定的是“保持 R7 形式的线性压缩”，不是说任何特殊非线性方程都不可解。

---

## 5. 二次 Coupl 的规范形

设 \(q\) 次数 \(\le2\)，并令

\[
B(x,y):=\operatorname{cr}_2q(x,y).
\]

由定理 3，\(B\) 是对称双加性映射。

### 定理 5（Quadratic Normal Form）

若 \(G\) 中乘以 \(2\) 是可逆的，则存在唯一群同态

\[
\ell:H\to G
\]

使得

\[
q(h)=q(0)+\ell(h)+\frac12B(h,h).
\]

具体地，

\[
\ell(h)=q(h)-q(0)-\frac12B(h,h).
\]

#### 证明

由 \(B\) 的定义，

\[
q(x+y)-q(0)
=
[q(x)-q(0)]+[q(y)-q(0)]+B(x,y).
\]

又由双加性与对称性，

\[
\frac12B(x+y,x+y)
=
\frac12B(x,x)+B(x,y)+\frac12B(y,y).
\]

相减即得 \(\ell(x+y)=\ell(x)+\ell(y)\)。唯一性显然。\(\square\)

### 推论 5.1（Quadratic Coupl Formula）

对任意 \(a,h\in H\)，

\[
q(a+h)-q(a)
=
\ell(h)+B(a,h)+\frac12B(h,h).
\]

因此二次 Coupl 的新项精确分为：

- 纯线性修正 \(\ell(h)\)；
- 基点—修正交互 \(B(a,h)\)；
- 修正的自交互 \(\tfrac12B(h,h)\)。

### 特征 \(2\) 边界

若 \(2\) 不可逆，\(B\) 不足以恢复 \(q\)。必须保留二次 refinement 或 divided-power 数据。故不能把有理极化公式无条件搬到整数、\(2\)-torsion 或模 \(2\) 系数。

---

## 6. 有理系数下的有限齐次分解

### 定理 6（Rational Polarization Decomposition）

设 \(G\) 是 \(\mathbb Q\)-向量空间，\(q:H\to G\) 的 Eilenberg–Mac Lane 次数 \(\le d\)。则存在唯一的对称 \(r\)-重加性映射

\[
B_r:H^r\to G,
\qquad 1\le r\le d,
\]

使得

\[
q(h)
=
q(0)+
\sum_{r=1}^d\frac1{r!}B_r(h,\ldots,h).
\]

#### 证明

令 \(B_d=\operatorname{cr}_dq\)。定理 3 保证它对称多加。映射

\[
h\longmapsto \frac1{d!}B_d(h,\ldots,h)
\]

的第 \(d\) cross-effect 正是 \(B_d\)。从 \(q-q(0)\) 中减去该映射后，最高 cross-effect 消失，次数降到 \(d-1\)。归纳得到存在性。

唯一性由最高非零层的 cross-effect 恢复，逐层下降即得。\(\square\)

### 推论 6.1（Finite Interaction Classification over \(\mathbb Q\)）

在有理系数下，一个有限次数 Coupl 的全部非线性信息恰由有限族

\[
(B_1,\ldots,B_d)
\]

给出。次数过滤因此分裂为齐次层。

### 整系数边界

在一般阿贝尔群中，分母 \(r!\) 不可逆，齐次分裂可能失败。正确对象是带整除约束的 polynomial law、divided powers 或未分裂的 cross-effect filtration，而不是强行写成有理多项式。

---

## 7. 自由阿贝尔群上的 Newton 展开

设 \(H=\mathbb Z^n\)，以 \(e_i\) 为标准基。对多重指标

\[
\alpha=(\alpha_1,\ldots,\alpha_n),
\qquad
|\alpha|=\sum_i\alpha_i,
\]

记

\[
\Delta^\alpha
=
\Delta_{e_1}^{\alpha_1}\cdots\Delta_{e_n}^{\alpha_n},
\qquad
\binom{x}{\alpha}
=
\prod_i\binom{x_i}{\alpha_i}.
\]

### 定理 7（Integral Newton Expansion）

若 \(q:\mathbb Z^n\to G\) 次数 \(\le d\)，则

\[
q(x)
=
\sum_{|\alpha|\le d}
\binom{x}{\alpha}\,
(\Delta^\alpha q)(0).
\]

这里广义二项式 \(\binom{x_i}{r}\) 对所有整数 \(x_i\) 都取整数值。

#### 证明要点

一维公式由 Newton 前向差分恒等式得到，并因 \(d+1\) 重差分消失而截断；对各坐标迭代即得多维公式。负整数情形由广义二项式恒等式延拓。\(\square\)

### 推论 7.1

自由有限秩域上的次数 \(\le d\) Coupl 由有限个差分系数

\[
(\Delta^\alpha q)(0),\qquad |\alpha|\le d
\]

完全决定。

这是有限编码定理，不是统一求零定理。

---

## 8. 平移稳定子与规范降维

### 定义 8.1

定义 \(q\) 的平移稳定子

\[
K_q
:=
\{h\in H\mid q(a+h)=q(a)\text{ 对所有 }a\in H\}.
\]

### 定理 8（Translation Gauge Reduction）

\(K_q\) 是 \(H\) 的子群；\(q\) 唯一地下降为

\[
\bar q:H/K_q\to G.
\]

而且零点集 \(q^{-1}(0)\) 是 \(K_q\)-陪集的并。

#### 证明

若 \(h,k\in K_q\)，则

\[
q(a+h+k)=q((a+h)+k)=q(a+h)=q(a).
\]

又由 \(q((a-h)+h)=q(a-h)\) 得 \(q(a)=q(a-h)\)，故 \(-h\in K_q\)。下降与零点陪集结论随即成立。\(\square\)

### 推论 8.1

任何 polynomial Coupl 求零问题都应先除去 \(K_q\)。这是完全规范的 gauge reduction，不需要选基或分裂。

---

## 9. 自然性与基变换稳定性

### 命题 9

若 \(u:H'\to H\)、\(v:G\to G'\) 是群同态，且 \(q:H\to G\) 次数 \(\le d\)，则

\[
v\circ q\circ u:H'\to G'
\]

次数 \(\le d\)，并且其 cross-effect 为

\[
\operatorname{cr}_r(vqu)
=
v\circ\operatorname{cr}_r(q)\circ u^{\times r}.
\]

因此次数过滤、最高极化与平移稳定子降维都与群同态自然相容。

#### 证明

差分与前合成、后合成群同态交换，逐次应用定义即可。\(\square\)

---

## 10. 为什么差分不等于残余求解塔

差分降阶定理降低的是映射

\[
a\longmapsto \Delta_hq(a)

\]

关于基点 \(a\) 的次数，其中 \(h\) 被固定。实际求零时，未知量正是 \(h\)，而

\[
h\longmapsto q(a+h)-q(a)

\]

通常仍有次数 \(d\)。

### 命题 10（No Automatic Degree Descent Along Restrictions）

把 polynomial Coupl 限制到子群、陪集或一个后继分支，不保证次数下降。

#### 反例

取

\[
q:\mathbb Z\to\mathbb Z,
\qquad q(n)=n^2.
\]

它的次数为 \(2\)。限制到任意非零子群 \(m\mathbb Z\) 后，

\[
q(mt)=m^2t^2
\]

仍为二次。沿任意平移陪集 \(a+m\mathbb Z\) 也仍有非零二次项。

因此，cross-effect filtration 是有限结构描述，但不是无条件的“每步降一次直至线性”的 solver。

---

## 11. 统一算法的不可判定边界

### 定理 11（No Universal Polynomial-Coupl Solver over \(\mathbb Z\)）

不存在一个算法，能够对任意有限变量整数 polynomial Coupl

\[
q:\mathbb Z^n\to\mathbb Z
\]

总是判定是否存在 \(x\in\mathbb Z^n\) 使 \(q(x)=0\)。

#### 证明

普通整系数多项式 \(p(x_1,\ldots,x_n)\) 给出有限差分次数的映射

\[
p:\mathbb Z^n\to\mathbb Z.
\]

若存在上述通用 polynomial-Coupl solver，就能判定任意丢番图方程 \(p=0\) 是否有整数解。这与 Davis–Putnam–Robinson–Matiyasevich 定理，即 Hilbert 第十问题的不可判定性矛盾。\(\square\)

### 范围限定

该 no-go 针对**任意抽象整数 polynomial Coupl 输入**。它不自动证明某个具体拓扑来源的受限 Coupl 子类不可判定；特定 Postnikov 不变量可能有额外有限性、稀疏性或同调结构，从而仍可计算。

---

## 12. 与 R7–R9 的拼合

对每个小方格或 obstruction stage 的 Coupl：

1. 若 \(\operatorname{cr}_2=0\)，使用 R7 的 cofiber residual；
2. 若次数 \(=2\) 且 \(2\) 可逆，使用 \((\ell,B)\) 的二次规范形；
3. 若系数有理且次数有限，使用有限多线性层 \((B_1,\ldots,B_d)\)；
4. 一般整数情形保留未分裂 cross-effect filtration；
5. 先除以 \(K_q\) 去掉纯 gauge 方向；
6. 每个局部比较映射一旦被证明为有效满射，R9 自动把它们粘合为二维有限全局填充；
7. 不把有限 jet 误称为统一求根算法，也不把有限矩形结论误推到无限 actualization。

由此得到一条严格分层：

\[
\boxed{
\begin{array}{c}
\text{affine}\Rightarrow\text{single cofiber residual}\\
\text{quadratic}\Rightarrow\text{linear + bilinear interaction}\\
\text{rational degree }d\Rightarrow\text{finite symmetric multilinear layers}\\
\text{integral general degree }d\Rightarrow\text{finite unsplit cross-effect jet}\\
\text{arbitrary integer inputs}\Rightarrow\text{no universal zero solver}
\end{array}
}
\]

---

## 13. 已知性与新颖性边界

有限差分、Eilenberg–Mac Lane polynomial maps、cross-effects、Newton 展开和 Hilbert 第十问题的不可判定性都是经典理论。本报告不主张这些基础结果本身的新颖性。

本项目中的派生贡献是：

1. 把 R7 的 residual cofiber 精确定位为 \(\operatorname{cr}_2=0\) 层；
2. 给出非仿射 Coupl 的有限 interaction-jet 替代物；
3. 区分“有限结构编码”与“有限求解算法”；
4. 将 R9 的局部到全局下降与 polynomial Coupl 的局部判据拼合；
5. 给出抽象生成装备中不可期待统一 solver 的严格 no-go。

参考背景：

- Qimh Richey Xantcha, *Polynomial Maps of Modules*, [arXiv:1112.0991](https://arxiv.org/abs/1112.0991).
- Yu. V. Matiyasevich, *Diophantine Representation of Enumerable Predicates*, Math. USSR-Izvestija 5 (1971), 1–28, [MathNet](https://www.mathnet.ru/eng/im1910).

---

## 14. 最终结论

Polynomial Coupl 的可闭合理论不是“把所有非线性障碍继续压成一个群元素”，而是：

\[
\boxed{
\text{有限差分 jet}
+
\text{最高极化层}
+
\text{可逆阶乘下的齐次分裂}
+
\text{规范 gauge quotient}.
}
\]

其严格边界是：

\[
\boxed{
\text{二次以上一般无单一 cofiber；整数多项式输入一般无统一判定算法。}
}
\]

这已经穷尽仅由“有限 polynomial degree”本身能够无条件推出的主要结构；后续推进应加入 nilpotent 系数作用的中心过滤，而不是假设差分次数自动产生求解塔。
