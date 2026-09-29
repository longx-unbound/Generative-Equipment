# 数学内生生成性理论

## Strict Space-Valued Core v0.2 Candidate

日期：2026-09-24  
地位：已通过 R1 内部一致性审计的候选核心；尚未冻结为通用 enriched 核心。

---

## 0. v0.2 的修正目标

v0.1 已经严格定义了空间值 problem、possibility、effectivity、observation 与 provenance，但压力测试发现：

1. saturation 固定 \(\mathcal A,\mathcal B\)，不能统一处理改变对象域或候选域的局部化；
2. 它把 possibility category 与 formal category 直接等同，导致许多 comparison problem 只能退化编码；
3. functor-valued dynamics 不能追踪非单值 witness transport。

v0.2 用三个结构修正：

\[
\boxed{
\text{domain-changing saturation}
}
\]

\[
\boxed{
\mathsf{Act}\xrightarrow{R}\mathfrak G
\xrightarrow{\Phi}\mathsf{Formal}
}
\]

\[
\boxed{
\text{lax Prof-valued dynamics}
}
\]

本版本仍以空间的 \(\infty\)-范畴 \(\mathcal S\) 为基础。真正的
\(\mathbf{Met}\)、\(\mathbf{Ban}\)、dg-enriched 和 \((\infty,2)\)-valued
扩展不在核心中。

---

## 1. 基础环境

在 ZFC 加上所需 Grothendieck 宇宙存在公理的元理论中工作，并固定
Grothendieck 宇宙

\[
\mathbb U_0\in\mathbb U_1\in\mathbb U_2.
\]

记：

\[
\mathcal S=\mathcal S_{\mathbb U_1},
\qquad
\Cat_\infty=\Cat_{\infty,\mathbb U_1}.
\]

所有工作 \(\infty\)-范畴和 indexing diagrams 均为
\(\mathbb U_1\)-小；函子范畴和局部化在 \(\mathbb U_2\) 中形成。
因此本文件使用的 \(\mathbb U_1\)-小 Kan-extension colimits 存在于
\(\mathcal S_{\mathbb U_1}\) 中。\(\mathbb U_0\) 保留给 sector
内部声明为 small 的 probes 与 test shapes。

空间值 profunctor 的方向约定为

\[
P:\mathcal A\nrightarrow\mathcal B
\quad\Longleftrightarrow\quad
P:\mathcal A^{op}\times\mathcal B\to\mathcal S.
\]

---

## 2. Domain-changing saturation

### 定义 2.1（raw problem）

raw problem data 是：

\[
\mathcal A,\mathcal B\in\Cat_\infty,
\qquad
P:\mathcal A^{op}\times\mathcal B\to\mathcal S.
\]

\(\mathcal A\) 是 problem category，\(\mathcal B\) 是 raw candidate category。

### 定义 2.2（domain localizations）

给定两族态射

\[
W_{\mathcal A}\subseteq\operatorname{Mor}(\mathcal A),
\qquad
W_{\mathcal B}\subseteq\operatorname{Mor}(\mathcal B)
\]

以及相应的 \(\infty\)-范畴局部化：

\[
\lambda_{\mathcal A}:
\mathcal A\to\mathcal A^\sharp
=\mathcal A[W_{\mathcal A}^{-1}],
\]

\[
\lambda_{\mathcal B}:
\mathcal B\to\mathcal B^\sharp
=\mathcal B[W_{\mathcal B}^{-1}].
\]

令

\[
\lambda
=
\lambda_{\mathcal A}^{op}\times\lambda_{\mathcal B}:
\mathcal A^{op}\times\mathcal B
\longrightarrow
(\mathcal A^\sharp)^{op}\times\mathcal B^\sharp.
\]

### 定义 2.3（domain saturation）

定义

\[
P^{dom}
:=
\operatorname{Lan}_{\lambda}P:
(\mathcal A^\sharp)^{op}\times\mathcal B^\sharp
\to\mathcal S.
\]

因为 \(\mathcal S\) 余完备且工作范畴在选定宇宙内，所需左 Kan 扩张存在。

其单位为

\[
\eta^{dom}:
P\to\lambda^*P^{dom}.
\]

### 命题 2.4（domain saturation 的泛性质）

对任意

\[
Q:
(\mathcal A^\sharp)^{op}\times\mathcal B^\sharp
\to\mathcal S,
\]

有自然等价

\[
\Map(P^{dom},Q)
\simeq
\Map(P,\lambda^*Q).
\]

#### 证明

这是左 Kan 扩张

\[
\operatorname{Lan}_{\lambda}\dashv\lambda^*
\]

的伴随泛性质。证毕。

### 命题 2.5（局部化后的 functor category）

预合成

\[
\lambda^*:
\Fun((\mathcal A^\sharp)^{op}\times\mathcal B^\sharp,\mathcal S)
\longrightarrow
\Fun(\mathcal A^{op}\times\mathcal B,\mathcal S)
\]

fully faithful；其本质像由下列 profunctors 组成：

- 在 \(\mathcal A\)-变量中把 \(W_{\mathcal A}\) 送到等价；
- 在 \(\mathcal B\)-变量中把 \(W_{\mathcal B}\) 送到等价。

#### 证明

\(\lambda_{\mathcal A}\) 与 \(\lambda_{\mathcal B}\) 的局部化泛性质分别给出对应 functor-category 等价。对 product 取合成即可。证毕。

### 推论 2.6（domain saturation 是反射）

在命题 2.5 的本质像与原 functor category 之间，

\[
\lambda^*\operatorname{Lan}_{\lambda}
\]

给出到“两个变量分别反演 \(W_{\mathcal A}\) 与
\(W_{\mathcal B}\)”的 profunctors 的反射。特别地，
\(P^{dom}\) 是满足该反演条件的泛初始扩张。

#### 证明

命题 2.4 给出伴随，命题 2.5 给出右伴随
\(\lambda^*\) 的 fully faithfulness 与本质像。fully faithful
右伴随所对应的左伴随正是到该本质像的反射。证毕。

### 定理 2.7（localized-Hom adequacy）

令 \(\mathcal A=\mathcal B=\mathcal C\)、
\(\lambda_{\mathcal A}=\lambda_{\mathcal B}=\lambda:\mathcal C\to
\mathcal C^\sharp\)，并取

\[
P=\Map_{\mathcal C}(-,-).
\]

\(\lambda\) 在映射空间上诱导自然变换

\[
\Map_{\mathcal C}(-,-)
\longrightarrow
(\lambda^{op}\times\lambda)^*
\Map_{\mathcal C^\sharp}(-,-).
\]

由 Kan-extension 伴随得到规范比较

\[
\theta_\lambda:
\operatorname{Lan}_{\lambda^{op}\times\lambda}
\Map_{\mathcal C}(-,-)
\longrightarrow
\Map_{\mathcal C^\sharp}(-,-).
\]

则 \(\theta_\lambda\) 是等价。换言之，每个上述意义下的
\(\infty\)-范畴局部化对 mapping profunctor 都是
**Prof-exact**（localized-Hom adequate）。

#### 证明

先只在第二个变量作左 Kan 扩张。对每个 \(c\in\mathcal C\)
与 \(Q:\mathcal C^\sharp\to\mathcal S\)，有

\[
\begin{aligned}
\Map_{\Fun(\mathcal C^\sharp,\mathcal S)}
\bigl(
\operatorname{Lan}_{\lambda}\Map_{\mathcal C}(c,-),Q
\bigr)
&\simeq
\Map_{\Fun(\mathcal C,\mathcal S)}
\bigl(
\Map_{\mathcal C}(c,-),\lambda^*Q
\bigr)\\
&\simeq Q(\lambda c)\\
&\simeq
\Map_{\Fun(\mathcal C^\sharp,\mathcal S)}
\bigl(
\Map_{\mathcal C^\sharp}(\lambda c,-),Q
\bigr).
\end{aligned}
\]

第一与第三个等价分别来自 Kan-extension 伴随与 Yoneda；中间的
等价是 \(\mathcal C\) 中的 Yoneda。故自然地

\[
\operatorname{Lan}_{\lambda}
\Map_{\mathcal C}(c,-)
\simeq
\Map_{\mathcal C^\sharp}(\lambda c,-).
\]

此时在第一个变量得到的是

\[
(\lambda^{op})^*
\Map_{\mathcal C^\sharp}(-,-).
\]

由于 \(\lambda^{op}\) 仍是局部化，预合成
\((\lambda^{op})^*\) fully faithful；所以伴随的 counit

\[
\operatorname{Lan}_{\lambda^{op}}(\lambda^{op})^*
\Map_{\mathcal C^\sharp}(-,-)
\longrightarrow
\Map_{\mathcal C^\sharp}(-,-)
\]

是等价。最后用 product Kan extension 的 Fubini 性质合并两步，
所得比较正是 \(\theta_\lambda\)。证毕。

该定理依赖 \(\lambda\) 确为具有命题 2.5 泛性质的局部化；对任意
domain-changing functor，同样的比较不必是等价。

### 定义 2.8（internal semantic saturation）

令

\[
\mathcal D^\sharp
=
\Fun((\mathcal A^\sharp)^{op}\times\mathcal B^\sharp,\mathcal S).
\]

给定 reflective localization

\[
\ell:\mathcal D^\sharp
\rightleftarrows
\mathcal D^{sat}:i,
\qquad
\ell\dashv i,
\]

其中 \(i\) fully faithful。记幂等 localization endofunctor 为

\[
L^{sem}:=i\ell.
\]

定义最终 saturated problem：

\[
\boxed{
P^\sharp
:=
L^{sem}(P^{dom})
=
L^{sem}\operatorname{Lan}_{\lambda}P.
}
\]

raw-to-saturated unit 是复合

\[
P
\longrightarrow
\lambda^*P^{dom}
\longrightarrow
\lambda^*P^\sharp.
\]

domain-changing saturation 与 fixed-domain semantic saturation 因而被分开。

### 定义 2.9（gauge equivalence）

给定具有相同 saturation doctrine 的

\[
f:P\to Q,
\]

称 \(f\) 是 gauge equivalence，若

\[
L^{sem}\operatorname{Lan}_{\lambda}(f)
\]

是等价。

---

## 3. Saturated possibility geometry

对 \(a^\sharp\in\mathcal A^\sharp\)，定义

\[
H_{a^\sharp}:
\mathcal B^\sharp\to\mathcal S,
\qquad
H_{a^\sharp}(b^\sharp)
=
P^\sharp(a^\sharp,b^\sharp).
\]

由 unstraightening 得 left fibration

\[
\pi_{a^\sharp}:
\mathfrak G(a^\sharp)\to\mathcal B^\sharp.
\]

随 \(a^\sharp\) 变化得到

\[
\mathfrak G:
(\mathcal A^\sharp)^{op}\to\Cat_\infty.
\]

定义 generative moduli：

\[
\mathcal M_\Xi(a^\sharp)
=
\mathfrak G(a^\sharp)^\simeq.
\]

定义 universal locus：

\[
\mathcal U_\Xi(a^\sharp)
=
\bigl(
\mathfrak G(a^\sharp)^{init}
\bigr)^\simeq.
\]

若非空，则

\[
\mathcal U_\Xi(a^\sharp)\simeq *.
\]

### 定理 3.1（表示性）

下列条件等价：

1. \(H_{a^\sharp}\) 可 corepresent；
2. 存在 \(F(a^\sharp)\in\mathcal B^\sharp\) 及
   \[
   P^\sharp(a^\sharp,b^\sharp)
   \simeq
   \Map_{\mathcal B^\sharp}(F(a^\sharp),b^\sharp);
   \]
3. \(\mathfrak G(a^\sharp)\) 有初始对象。

证明与 v0.1 相同：从 \(u\in H_{a^\sharp}(b_0)\) 得到
\[
\Map(b_0,-)\to H_{a^\sharp},
\]
其在 \(v\) 上的同伦纤维正是元素范畴中的映射空间。

### 定理 3.2（saturation invariance）

若 \(f:P\to Q\) 是 gauge equivalence，则

\[
\mathfrak G_P\simeq\mathfrak G_Q,
\qquad
\mathcal M_P\simeq\mathcal M_Q,
\qquad
\mathcal U_P\simeq\mathcal U_Q.
\]

#### 证明

gauge equivalence 给出 \(P^\sharp\simeq Q^\sharp\)。逐
\(a^\sharp\) unstraighten，再取 cores 与 initial loci。证毕。

---

## 4. Possibility、actuality 与 formality 分层

### 定义 4.1（three-layer comparison datum）

给定三个函子：

\[
\mathsf{Act},\mathfrak G,\mathsf{Formal}:
(\mathcal A^\sharp)^{op}\to\Cat_\infty,
\]

其中 \(\mathfrak G\) 是第 3 节构造的 possibility functor。

配置包含自然变换：

\[
R:\mathsf{Act}\to\mathfrak G,
\]

\[
\Phi:\mathfrak G\to\mathsf{Formal}.
\]

定义 actual/formal comparison：

\[
\boxed{
C:=\Phi R:
\mathsf{Act}\to\mathsf{Formal}.
}
\]

解释：

- \(R\) 把 actual object 视为一个 admissible possibility；
- \(\Phi\) 把 possibility 送到它的 formal/local datum；
- \(C\) 直接比较 actual 与 formal。

v0.1 是特殊情形：

\[
\mathsf{Formal}=\mathfrak G,
\qquad
\Phi=\id_{\mathfrak G},
\qquad
C=R.
\]

### 定义 4.2（candidate-realization fiber）

对

\[
\gamma\in\mathfrak G(a^\sharp),
\]

定义

\[
\operatorname{RealFib}_{a^\sharp}(\gamma)
:=
\mathsf{Act}(a^\sharp)^\simeq
\mathop{\times}_{\mathfrak G(a^\sharp)^\simeq}
\{\gamma\}.
\]

### 定义 4.3（formalization fiber）

对

\[
\xi\in\mathsf{Formal}(a^\sharp),
\]

定义

\[
\operatorname{FormFib}_{a^\sharp}(\xi)
:=
\mathfrak G(a^\sharp)^\simeq
\mathop{\times}_{\mathsf{Formal}(a^\sharp)^\simeq}
\{\xi\}.
\]

### 定义 4.4（effectivity fiber）

定义

\[
\operatorname{EffFib}_{a^\sharp}(\xi)
:=
\mathsf{Act}(a^\sharp)^\simeq
\mathop{\times}_{\mathsf{Formal}(a^\sharp)^\simeq}
\{\xi\}.
\]

### 定理 4.5（two-stage effectivity decomposition）

存在自然等价：

\[
\boxed{
\operatorname{EffFib}_{a^\sharp}(\xi)
\simeq
\mathsf{Act}(a^\sharp)^\simeq
\mathop{\times}_{\mathfrak G(a^\sharp)^\simeq}
\operatorname{FormFib}_{a^\sharp}(\xi).
}
\]

#### 证明

右侧为

\[
\mathsf{Act}^\simeq
\mathop{\times}_{\mathfrak G^\simeq}
\left(
\mathfrak G^\simeq
\mathop{\times}_{\mathsf{Formal}^\simeq}
\{\xi\}
\right).
\]

由同伦拉回的结合律，它自然等价于

\[
\mathsf{Act}^\simeq
\mathop{\times}_{\mathsf{Formal}^\simeq}
\{\xi\},
\]

即左侧。证毕。

### 推论 4.6

1. 若 \(\operatorname{FormFib}(\xi)=\varnothing\)，则
   \[
   \operatorname{EffFib}(\xi)=\varnothing.
   \]
2. 若 \(R\) 是等价，则
   \[
   \operatorname{EffFib}(\xi)
   \simeq
   \operatorname{FormFib}(\xi).
   \]
3. 若 \(\Phi\) 是等价，则 effectivity 完全由 \(R\) 的 realization fibers 决定。

### 定理 4.7（effectivity 与 reconstruction）

\[
C_{a^\sharp}\text{ 本质满射}
\]

当且仅当每个 \(\xi\) 的
\(\operatorname{EffFib}_{a^\sharp}(\xi)\) 非空。

\[
C_{a^\sharp}\text{ 是等价}
\]

当且仅当它 fully faithful 且每个 effectivity fiber 非空。

### 警告 4.8（不能逐因子判定 composite）

由

\[
C=\Phi R
\]

是等价，不能推出 \(R\) 与 \(\Phi\) 分别是等价。

例：令 \(\mathsf{Act}=\mathsf{Formal}=*\)，令
\(\mathfrak G\) 是任意含指定对象的非平凡 \(\infty\)-范畴；
\(R\) 选定该对象，\(\Phi\) 为唯一函子。则 \(C=\id_*\)，但
\(R,\Phi\) 通常都不是等价。

---

## 5. Provenance 与 normalized events

给定：

\[
\widetilde{\mathsf E},
\qquad
W_{\mathsf E}\subseteq\operatorname{Mor}(\widetilde{\mathsf E}),
\]

以及局部化

\[
q:
\widetilde{\mathsf E}\to
\mathsf E^{GM}
=
\widetilde{\mathsf E}[W_{\mathsf E}^{-1}].
\]

给定 semantic category \(\mathsf E^{sem}\) 和

\[
p:\widetilde{\mathsf E}\to\mathsf E^{sem}
\]

把 \(W_{\mathsf E}\) 送到等价。于是存在本质唯一的

\[
\overline p:\mathsf E^{GM}\to\mathsf E^{sem}
\]

满足

\[
p\simeq\overline p q.
\]

给定 event functor

\[
\widetilde{\mathrm{Ev}}:
\int_{(\mathcal A^\sharp)^{op}}\mathsf{Act}
\to
\widetilde{\mathsf E}.
\]

这保持：

\[
\text{same normalized provenance}
\Longrightarrow
\text{same semantics},
\]

但不要求逆命题。

---

## 6. Observation 与 novelty

给定：

\[
\mathsf K\in\Cat_\infty,
\]

\[
\mathbb O:
\mathsf K^{op}\times\mathsf E^{GM}
\to\mathcal S,
\]

以及旧事件基线

\[
j:\mathsf E_{\mathrm{old}}\to\mathsf E^{GM}.
\]

定义 persistent nerve：

\[
N^\infty_{\mathbb O}:
\mathsf E^{GM}\to\mathcal P(\mathsf K),
\qquad
N^\infty_{\mathbb O}(e)(k)=\mathbb O(k,e).
\]

下式中从 \(\mathsf E_{\mathrm{old}}^\simeq\) 到
\(\mathcal P(\mathsf K)^\simeq\) 的结构映射明确取为

\[
\mathsf E_{\mathrm{old}}^\simeq
\xrightarrow{j}
(\mathsf E^{GM})^\simeq
\xrightarrow{N^\infty_{\mathbb O}}
\mathcal P(\mathsf K)^\simeq.
\]

定义：

\[
\operatorname{OldMatch}(e)
:=
\mathsf E_{\mathrm{old}}^\simeq
\mathop{\times}_{\mathcal P(\mathsf K)^\simeq}
\{N^\infty_{\mathbb O}(e)\}.
\]

\(e\) 相对于 \((j,\mathbb O)\) novel，当且仅当

\[
\operatorname{OldMatch}(e)=\varnothing.
\]

若 \(N^\infty_{\mathbb O}\) fully faithful，则 observation-relative
novelty 等价于 \(e\) 不属于 \(j\) 的本质像。

若

\[
r:\mathsf K_0\to\mathsf K_1,
\qquad
N_0=r^*N_1,
\]

则

\[
\text{\(e\) 在 }\mathsf K_0\text{ 中 novel}
\Longrightarrow
\text{\(e\) 在 }\mathsf K_1\text{ 中 novel}.
\]

若扩大 context 时同时改变 gauge 或 observation law，则不满足
\(N_0=r^*N_1\)，上述单调性定理不适用。

---

## 7. Prof-valued dynamics

记 \(\operatorname{Prof}_{\mathcal S}\) 为如下
\((\infty,2)\)-范畴：对象是工作宇宙中的小
\(\infty\)-范畴，从 \(\mathcal C\) 到 \(\mathcal D\) 的 hom
\(\infty\)-范畴为

\[
\Fun(\mathcal C^{op}\times\mathcal D,\mathcal S),
\]

横向合成由 coend 给出，单位 1-cell 是 mapping profunctor。

### 定义 7.1（stage system）

给定小 \(\infty\)-范畴 \(\mathsf D\)。对每个
\(d\in\mathsf D\)，给定 event/witness category

\[
\mathsf E_d\in\Cat_\infty.
\]

### 定义 7.2（transition profunctor）

对每个箭头

\[
u:d\to d',
\]

给定

\[
\mathbb T_u:
\mathsf E_d^{op}\times\mathsf E_{d'}
\to\mathcal S.
\]

\(\mathbb T_u(x,y)\) 是 witness \(x\) 沿 \(u\) 演化为 \(y\) 的方式空间。

### 定义 7.3（lax dynamics）

一套 Prof-valued dynamics 是一个采用下述 compositor 方向约定的
lax functor

\[
\mathbb T:\mathsf D\longrightarrow
\operatorname{Prof}_{\mathcal S},
\qquad
d\longmapsto\mathsf E_d.
\]

其在 1-simplex 上的数据就是定义 7.2 的 \(\mathbb T_u\)。对可复合箭头

对可复合箭头

\[
d\xrightarrow u d'\xrightarrow v d'',
\]

profunctor composition 为

\[
(\mathbb T_v\odot\mathbb T_u)(x,z)
=
\int^{y\in\mathsf E_{d'}}
\mathbb T_u(x,y)\times\mathbb T_v(y,z).
\]

给定自然变换

\[
\mu_{v,u}:
\mathbb T_v\odot\mathbb T_u
\to
\mathbb T_{vu},
\]

以及 unit maps

\[
\Map_{\mathsf E_d}(-,-)
\to
\mathbb T_{\id_d},
\]

这些 maps 连同 \(\mathsf D\) 的每个高阶 simplex 所要求的全部
高阶相干，构成上述 lax functor。若 \(\mathsf D\) 是普通 1-category，
这退化为 associativity pentagon 与左右 unit triangles。若 unit maps
均为等价，则称为 normal lax dynamics。

这里“lax”专指显示的方向
\(\mathbb T_v\odot\mathbb T_u\to\mathbb T_{vu}\)；采用相反
compositor 约定的文献会把同一方向称为 oplax。


### 定义 7.4（representable dynamics）

若对每个 \(u:d\to d'\) 存在函子

\[
T_u:\mathsf E_d\to\mathsf E_{d'}
\]

及自然等价

\[
\mathbb T_u(x,y)
\simeq
\Map_{\mathsf E_{d'}}(T_u x,y),
\]

则称该 transition representable。

当所有 transition representable 且 composition cells 为等价时，得到通常的 functorial dynamics。

### 例 7.5（span 诱导 dynamics）

span

\[
\mathsf E_d
\xleftarrow s
\mathsf Z_u
\xrightarrow t
\mathsf E_{d'}
\]

诱导 profunctor

\[
\mathbb T_u(x,y)
=
\int^{z\in\mathsf Z_u}
\Map_{\mathsf E_d}(x,s(z))
\times
\Map_{\mathsf E_{d'}}(t(z),y).
\]

它一般不由单值函子表示。若所有范畴离散，上式退化为以满足
\(s(z)=x,t(z)=y\) 的 \(z\) 为元素的关系空间。这覆盖
spectral-sequence witness 的“只有 cycles 才进入下一页”的情形。

---

## 8. Pro-effectivity sector

本节中 “small” 指 \(\mathbb U_0\)-small，accessible 与 complete
也相对于 \(\mathbb U_0\)；\(\mathcal B^\sharp\) 本身允许为
\(\mathbb U_1\)-小，相关 Pro-category 在 \(\mathbb U_2\) 中形成。

若 \(\mathcal B^\sharp\) accessible 且 complete，并且

\[
H_{a^\sharp}:
\mathcal B^\sharp\to\mathcal S
\]

accessible，则：

\[
H_{a^\sharp}\text{ 可 corepresent}
\quad\Longleftrightarrow\quad
H_{a^\sharp}\text{ 保所有小极限}.
\]

若 \(H_{a^\sharp}\) 已保有限极限，则进一步等价于保持所有小乘积。

若 \(\mathcal B^\sharp\) 只要求 accessible 且有有限极限，而
\(H_{a^\sharp}\) accessible、保有限极限，则它对应

\[
\widehat F(a^\sharp)\in\Pro(\mathcal B^\sharp).
\]

actual representability 等价于

\[
\widehat F(a^\sharp)
\in
\operatorname{EssIm}
\bigl(
\mathcal B^\sharp\to\Pro(\mathcal B^\sharp)
\bigr).
\]

v0.1 的超限 product-rank 定理保持有效。

---

## 9. Anti-tautology discipline

所有 prediction claim 必须具有量词顺序：

\[
\forall\Xi\in\mathcal C_{\mathrm{adm}},
\quad
\forall x,
\quad
\mathcal H(\Xi,x)\Rightarrow\mathcal Q(\Xi,x),
\]

其中

\[
\Xi=
(\mathcal A,\mathcal B,P,
W_{\mathcal A},W_{\mathcal B},
\lambda_{\mathcal A},\lambda_{\mathcal B},
L^{sem},
\mathsf{Act},R,\Phi,
\widetilde{\mathsf E},q,p,
\mathsf K,\mathbb O,j,
\mathbb T)
\]

在选择目标 \(x\) 前固定。

以下量词顺序不计为预测：

\[
\forall x\ \exists\Xi_x:
\mathcal Q(\Xi_x,x).
\]

数学文件只能规定依赖顺序；历史上的独立性仍需要 provenance certificate、
版本记录或形式化依赖图。

---

## 10. v0.2 的定理边界

### 已严格解决

1. raw domain 与 saturated domain 可以不同；
2. 对真正的 categorical localization，双变量 Kan extension 恢复
   localized mapping profunctor；
3. fixed-domain reflector 仍作为特殊情形保留；
4. possibility 与 formal category 不再被等同；
5. effectivity 被分解为 formalization 与 realization 两层；
6. nonfunctorial witness evolution 可以用带全部高阶相干的 lax
   Prof-valued dynamics 表示；
7. v0.1 的 representability、observation、provenance 与 Pro-sector 定理保留。

### 尚未解决

1. 一般 \(\mathcal V\)-enriched category of elements；
2. Banach/metric quantitative mapping objects；
3. 完整 \((\infty,2)\)-categorical moduli；
4. 从 bare configuration 内生地产生
   \(W_{\mathcal A},W_{\mathcal B},L^{sem},\Phi,\mathbb O\)；
5. 从抽象 effectivity fiber 自动提取所有 sector obstruction；
6. 把 pre-target 的历史独立性变成内部可判定性质。

因此 v0.2 是扩大后的严格空间值核心候选，不宣称已经覆盖 Frozen v1.0
中所有 enriched 语义。
