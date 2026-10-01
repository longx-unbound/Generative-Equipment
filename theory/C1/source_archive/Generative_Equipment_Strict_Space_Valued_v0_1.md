# 数学内生生成性理论：空间值严格版本

## Strict Space-Valued Sector v0.1

日期：2026-09-24  
地位：Frozen v1.0 的严格实现分支；不替换、不修改冻结核心。

---

## 0. 严格化目标

本文件固定一个单一语义环境，把 Frozen v1.0 中下列链条写成类型一致、可逐项验证的数学结构：

\[
\text{problem}
\longrightarrow
\text{saturation}
\longrightarrow
\text{possibility}
\longrightarrow
\text{actualization}
\longrightarrow
\text{event}
\longrightarrow
\text{observation}
\longrightarrow
\text{novelty}.
\]

本版本作出三个限制：

1. 所有 profunctor 都取值于空间的 \(\infty\)-范畴 \(\mathcal S\)；
2. possibility geometry 由空间值函子的 unstraightening 定义；
3. formal category 取为 saturated possibility category。

这些限制给出 Frozen v1.0 的一个严格 sector。一般 enriched、Prof-valued dynamics 及其他 formalization doctrine 留待后续版本。

---

## 1. 宇宙与记号

在带选择公理的 ZFC 中工作，并固定三个 Grothendieck 宇宙

\[
\mathbb U_0\in\mathbb U_1\in\mathbb U_2.
\]

记：

- \(\mathcal S=\mathcal S_{\mathbb U_0}\)：\(\mathbb U_0\)-小空间的 \(\infty\)-范畴；
- \(\Cat_\infty=\Cat_{\infty,\mathbb U_1}\)：\(\mathbb U_1\)-小、局部 \(\mathbb U_0\)-小的 \(\infty\)-范畴；
- 所有函子范畴、局部化和模空间都在 \(\mathbb U_2\) 中形成。

对 \(\mathcal C\in\Cat_\infty\)：

- \(\mathcal C^\simeq\) 表示其 maximal \(\infty\)-groupoid；
- \(\Map_{\mathcal C}(x,y)\in\mathcal S\) 表示映射空间；
- \(\mathcal P(\mathcal C)=\Fun(\mathcal C^{op},\mathcal S)\)；
- “非空空间”表示存在一个点，而不是只要求 \(\pi_0\) 形式存在。

本文件约定从 \(\mathcal A\) 到 \(\mathcal B\) 的空间值 profunctor 为

\[
P:\mathcal A^{op}\times\mathcal B\longrightarrow\mathcal S.
\]

---

## 2. 严格 generative configuration

### 定义 2.1（空间值严格配置）

一个 **strict space-valued generative configuration** \(\Xi\) 是以下数据。

### A. 问题数据

1. problem category \(\mathcal A\in\Cat_\infty\)；
2. candidate category \(\mathcal B\in\Cat_\infty\)；
3. raw problem profunctor
   \[
   P:\mathcal A^{op}\times\mathcal B\to\mathcal S.
   \]

### B. 饱和数据

令

\[
\mathcal D=\Fun(\mathcal A^{op}\times\mathcal B,\mathcal S).
\]

给定一个 reflective localization

\[
\ell:\mathcal D\rightleftarrows\mathcal D_L:i,
\qquad
\ell\dashv i,
\]

其中 \(i\) fully faithful。把相应的幂等 localization endofunctor 记为

\[
L:=i\ell:\mathcal D\to\mathcal D,
\]

其单位为

\[
\eta:\id_{\mathcal D}\to L.
\]

要求 \(L\eta\) 与 \(\eta L\) 都是等价。定义

\[
P^\sharp:=L(P).
\]

一个态射 \(f:P\to Q\) 称为 **gauge equivalence**，若

\[
L(f):L(P)\xrightarrow{\simeq}L(Q)
\]

是等价。

### C. 实际化数据

给定一个函子

\[
\mathsf{Act}:\mathcal A^{op}\to\Cat_\infty.
\]

\(\mathsf{Act}(a)\) 是问题 \(a\) 的 actual objects 及其实际态射组成的 \(\infty\)-范畴。

第 3 节将从 \(P^\sharp\) 构造 formal possibility functor

\[
\mathfrak G:\mathcal A^{op}\to\Cat_\infty.
\]

配置还包含一个自然变换

\[
C:\mathsf{Act}\Longrightarrow\mathfrak G.
\]

其分量

\[
C_a:\mathsf{Act}(a)\to\mathfrak G(a)
\]

称为 actual/formal comparison。

### D. 事件与 provenance 数据

给定：

1. raw provenance category \(\widetilde{\mathsf E}\)；
2. 一族声明为 zero-cost gauge 的态射 \(W\subseteq\operatorname{Mor}(\widetilde{\mathsf E})\)；
3. 一个 \(\infty\)-范畴局部化
   \[
   q:\widetilde{\mathsf E}\to
   \mathsf E^{GM}:=\widetilde{\mathsf E}[W^{-1}] ;
   \]
4. semantic event category \(\mathsf E^{sem}\)；
5. 一个发送 \(W\) 中态射为等价的函子
   \[
   p:\widetilde{\mathsf E}\to\mathsf E^{sem}.
   \]

由局部化的泛性质，存在本质唯一的

\[
\overline p:\mathsf E^{GM}\to\mathsf E^{sem}
\]

使得

\[
p\simeq\overline p\,q.
\]

令

\[
\int_{\mathcal A^{op}}\mathsf{Act}
\]

表示 \(\mathsf{Act}\) 的 Grothendieck construction。配置给定 event/provenance functor

\[
\widetilde{\mathrm{Ev}}:
\int_{\mathcal A^{op}}\mathsf{Act}
\longrightarrow
\widetilde{\mathsf E}.
\]

因此一个 actualization \(x\in\mathsf{Act}(a)\) 产生：

\[
\widetilde e_x:=\widetilde{\mathrm{Ev}}(a,x),\qquad
e_x^{GM}:=q(\widetilde e_x),\qquad
e_x^{sem}:=p(\widetilde e_x).
\]

### E. 持续观察与基线数据

给定：

1. future-context category \(\mathsf K\in\Cat_\infty\)；
2. observation profunctor
   \[
   \mathbb O:
   \mathsf K^{op}\times\mathsf E^{GM}
   \longrightarrow\mathcal S ;
   \]
3. old-event category \(\mathsf E_{\mathrm{old}}\) 及基线函子
   \[
   j:\mathsf E_{\mathrm{old}}\to\mathsf E^{GM}.
   \]

注意这里的方差经过固定：按照本文件的 profunctor 约定，

\[
\mathbb O:\mathsf K\nrightarrow\mathsf E^{GM}.
\]

因此它诱导协变 persistent nerve

\[
N^\infty_{\mathbb O}:
\mathsf E^{GM}\longrightarrow
\mathcal P(\mathsf K),
\qquad
N^\infty_{\mathbb O}(e)(k)=\mathbb O(k,e).
\]

这修正了把

\[
\mathsf E\nrightarrow\mathsf K
\]

与协变 nerve 同时使用时产生的方差冲突。

---

## 3. Possibility geometry 的严格构造

### 3.1 从 saturated problem 到 left fibration

对 \(a\in\mathcal A\)，定义

\[
H_a:\mathcal B\to\mathcal S,
\qquad
H_a(b)=P^\sharp(a,b).
\]

由 straightening/unstraightening，\(H_a\) 对应一个 left fibration

\[
\pi_a:\mathfrak G(a)\to\mathcal B.
\]

把 \(\mathfrak G(a)\) 称为问题 \(a\) 的 **possibility \(\infty\)-category**。

其对象可记为二元组

\[
(b,u),\qquad b\in\mathcal B,\quad u\in P^\sharp(a,b).
\]

若

\[
f:b\to b'
\]

是 \(\mathcal B\) 中的态射，则从 \((b,u)\) 到 \((b',u')\) 的映射空间是

\[
\Map_{\mathfrak G(a)}((b,u),(b',u'))
\simeq
\operatorname{hofib}_{u'}
\left(
\Map_{\mathcal B}(b,b')
\xrightarrow{\,f\mapsto H_a(f)(u)\,}
H_a(b')
\right).
\]

因为 \(P^\sharp\) 在 \(\mathcal A\) 上反变，赋值

\[
a\longmapsto\mathfrak G(a)
\]

自然形成

\[
\mathfrak G:\mathcal A^{op}\to\Cat_\infty.
\]

这就是定义 2.1.C 中 comparison 的目标。

### 3.2 Generative moduli

定义

\[
\mathcal M_\Xi(a):=\mathfrak G(a)^\simeq.
\]

严格采用以下术语：

- \(\mathcal M_\Xi(a)=\varnothing\)：没有 saturated formal candidate；
- \(|\pi_0\mathcal M_\Xi(a)|\ge2\)：存在不同等价类型的 branching；
- \(\mathcal M_\Xi(a)\) 连通但不可缩：只有一个候选等价类型，但存在 isotropy 或 higher coherence；
- \(\mathcal M_\Xi(a)\simeq *\)：所有候选在 groupoidal 意义下刚性。

最后一种情况仍不蕴含整个 \(\mathfrak G(a)\) 等价于终范畴，因为 maximal groupoid 不记录非可逆态射。

### 3.3 Universal locus

令 \(\mathfrak G(a)^{init}\) 为由初始对象张成的满子范畴，定义

\[
\mathcal U_\Xi(a)
:=
\bigl(\mathfrak G(a)^{init}\bigr)^\simeq.
\]

若 \(\mathcal U_\Xi(a)\neq\varnothing\)，则

\[
\mathcal U_\Xi(a)\simeq *.
\]

这只说明 universal locus 可缩，不说明 \(\mathcal M_\Xi(a)\) 可缩。

---

## 4. 表示性定理

### 定理 4.1（初始对象与 oriented representability）

对固定的 \(a\in\mathcal A\)，以下条件等价：

1. \(H_a=P^\sharp(a,-)\) 可 corepresent；
2. 存在 \(F(a)\in\mathcal B\) 及自然等价
   \[
   H_a(b)\simeq\Map_{\mathcal B}(F(a),b) ;
   \]
3. \(\mathfrak G(a)\) 有初始对象。

#### 证明

给定 \(u\in H_a(b_0)\)，由 Yoneda 得到自然变换

\[
\theta_u:
\Map_{\mathcal B}(b_0,-)\to H_a.
\]

对任意 \((b,v)\in\mathfrak G(a)\)，其在 \(v\) 上的同伦纤维为

\[
\operatorname{hofib}_{v}
\left(
\Map_{\mathcal B}(b_0,b)\to H_a(b)
\right),
\]

这正是

\[
\Map_{\mathfrak G(a)}((b_0,u),(b,v)).
\]

因此 \((b_0,u)\) 初始，当且仅当 \(\theta_u\) 的所有同伦纤维可缩，当且仅当 \(\theta_u\) 是等价。证毕。

### 推论 4.2（functorial objectification）

若每个 \(H_a\) 都可 corepresent，则存在函子

\[
F:\mathcal A\to\mathcal B
\]

及自然等价

\[
P^\sharp(a,b)\simeq
\Map_{\mathcal B}(F(a),b).
\]

#### 说明

corepresentable functors 构成 \(\Fun(\mathcal B,\mathcal S)\) 的满子范畴，并与 \(\mathcal B^{op}\) 等价。函子

\[
\mathcal A^{op}\to\Fun(\mathcal B,\mathcal S),
\qquad
a\mapsto H_a
\]

因而经该满子范畴分解；取 opposite 得到 \(F:\mathcal A\to\mathcal B\)。

### 推论 4.3（reduct sector）

设

\[
U:\mathcal B\to\mathcal A
\]

且

\[
P^\sharp(a,b)\simeq\Map_{\mathcal A}(a,U(b)).
\]

若 \(P^\sharp\) 可 functorially corepresent 为 \(F\)，则

\[
F\dashv U.
\]

反之亦然。

因此伴随是本严格版本中的 representable reduct sector，而不是 generativity 的定义。

---

## 5. Actualization 与 effectivity

### 定义 5.1（对象级效性纤维）

对 \(a\in\mathcal A\) 和

\[
\xi\in\mathfrak G(a)
\]

定义

\[
\operatorname{EffFib}_{\Xi,a}(\xi)
:=
\mathsf{Act}(a)^\simeq
\mathop{\times}_{\mathfrak G(a)^\simeq}
\{\xi\}.
\]

其点是二元组

\[
(x,\alpha),
\qquad
x\in\mathsf{Act}(a),\quad
\alpha:C_a(x)\simeq\xi.
\]

定义：

- \(\xi\) **effective**，若 \(\operatorname{EffFib}_{\Xi,a}(\xi)\neq\varnothing\)；
- \(\xi\) **object-rigidly effective**，若
  \[
  \operatorname{EffFib}_{\Xi,a}(\xi)\simeq * ;
  \]
- 非可缩的效性纤维记录多个 actual realization、自同构或更高相干性。

这个定义使用 cores 后的拉回，避免把“Cat\(_\infty\) 中的严格纤维”“对象等价纤维”和“类空间映射的同伦纤维”混为一谈。

### 定理 5.2（对象效性与重构）

对固定 \(a\)：

1. \(C_a\) 本质满射，当且仅当每个
   \(\xi\in\mathfrak G(a)\) 的效性纤维非空；
2. \(C_a\) 是等价，当且仅当：
   - 每个效性纤维非空；
   - \(C_a\) fully faithful。

#### 证明

第一条是本质满射的定义。第二条是 \(\infty\)-范畴中“fully faithful + essentially surjective”判据。证毕。

### 注 5.3

即使每个效性纤维都可缩，也不能省去 fully faithful 条件。对象级唯一实现不能自动恢复实际态射。

---

## 6. Provenance、规范化与语义

### 命题 6.1（语义因子化）

若

\[
p:\widetilde{\mathsf E}\to\mathsf E^{sem}
\]

把 \(W\) 中每个态射送到等价，则存在本质唯一的

\[
\overline p:\mathsf E^{GM}\to\mathsf E^{sem}
\]

满足

\[
p\simeq\overline p q.
\]

这是 \(\infty\)-范畴局部化的泛性质。

### 推论 6.2

若

\[
q(\widetilde e)\simeq q(\widetilde e'),
\]

则

\[
p(\widetilde e)\simeq p(\widetilde e').
\]

逆命题一般不成立。故

\[
\text{same semantic event}
\]

可以保留多个非 gauge-equivalent provenance classes。

本结构精确表达：

\[
\text{same final semantics}
\not\Rightarrow
\text{same normalized generative history}.
\]

---

## 7. Persistent observation 与 novelty

### 7.1 观察等价

对 \(e,f\in\mathsf E^{GM}\)，定义

\[
e\simeq_{\mathbb O}f
\quad\Longleftrightarrow\quad
N^\infty_{\mathbb O}(e)
\simeq
N^\infty_{\mathbb O}(f)
\quad\text{于 }\mathcal P(\mathsf K).
\]

这里要求 presheaf 的自然等价，包括所有 context morphism 和高阶相干性。只验证

\[
\mathbb O(k,e)\simeq\mathbb O(k,f)
\quad\text{对每个对象 }k
\]

通常不够。

### 定义 7.1（观察充分性）

称 \(\mathbb O\)：

- **object-conservative**，若
  \[
  N^\infty_{\mathbb O}(e)\simeq
  N^\infty_{\mathbb O}(f)
  \Longrightarrow e\simeq f ;
  \]
- **adequate**，若
  \[
  N^\infty_{\mathbb O}:
  \mathsf E^{GM}\to\mathcal P(\mathsf K)
  \]
  fully faithful。

adequate 蕴含 object-conservative。

### 7.2 旧事件匹配空间

对 \(e\in\mathsf E^{GM}\)，定义

\[
\operatorname{OldMatch}_{\Xi}(e)
:=
\mathsf E_{\mathrm{old}}^\simeq
\mathop{\times}_{\mathcal P(\mathsf K)^\simeq}
\{N^\infty_{\mathbb O}(e)\},
\]

其中左侧映射由

\[
N^\infty_{\mathbb O}\circ j
\]

诱导。

### 定义 7.2（观察相对的新颖性）

称 \(e\) 相对于 \((j,\mathbb O)\) **novel**，若

\[
\operatorname{OldMatch}_{\Xi}(e)=\varnothing.
\]

称 actualization \(x\in\mathsf{Act}(a)\) novel，若其规范化事件

\[
e_x^{GM}=q\widetilde{\mathrm{Ev}}(a,x)
\]

novel。

这给出一条完全类型一致的链：

\[
x
\xmapsto{\widetilde{\mathrm{Ev}}}
\widetilde e_x
\xmapsto q
e_x^{GM}
\xmapsto{N^\infty_{\mathbb O}}
N^\infty_{\mathbb O}(e_x^{GM})
\]

并与旧事件的观察像比较。

### 定理 7.3（充分观察下的新颖性）

若 \(N^\infty_{\mathbb O}\) fully faithful，则

\[
\operatorname{OldMatch}_{\Xi}(e)\neq\varnothing
\]

当且仅当存在 \(e_0\in\mathsf E_{\mathrm{old}}\) 使

\[
j(e_0)\simeq e.
\]

所以在 adequate observation 下，观察相对的新颖性等价于不属于旧事件的本质像。

### 定理 7.4（horizon 单调性）

设

\[
r:\mathsf K_0\to\mathsf K_1
\]

是 context enlargement，并有 nerve

\[
N_1:\mathsf E^{GM}\to\mathcal P(\mathsf K_1),
\qquad
N_0=r^*N_1.
\]

若 \(e\) 相对于 \(\mathsf K_0\) novel，则 \(e\) 相对于 \(\mathsf K_1\) novel。

#### 证明

若 \(e\) 在 \(\mathsf K_1\) 中与某个旧事件 \(j(e_0)\) 观察等价，则限制到 \(\mathsf K_0\) 后仍等价。这与其在 \(\mathsf K_0\) 中 novel 矛盾。证毕。

因此加入相容的新 context 只能增加区分能力。

---

## 8. Saturation invariance

### 定理 8.1

若

\[
f:P\to Q
\]

是 gauge equivalence，则 \(P\) 与 \(Q\) 诱导自然等价的：

1. saturated problems；
2. possibility functors
   \[
   \mathfrak G_P\simeq\mathfrak G_Q ;
   \]
3. generative moduli
   \[
   \mathcal M_P(a)\simeq\mathcal M_Q(a)
   \quad\text{对所有 }a ;
   \]
4. universal loci。

#### 证明

由定义 \(L(f)\) 是函子

\[
P^\sharp\to Q^\sharp
\]

的等价。逐 \(a\) 柯里化后得到

\[
P^\sharp(a,-)\simeq Q^\sharp(a,-).
\]

unstraightening 保持函子等价，故 possibility categories 自然等价。取 cores 和初始对象子空间得到其余结论。证毕。

这给出“raw representatives 在饱和前不定义 branching”的精确版本。

---

## 9. 严格 Pro-effectivity sector

本节增加条件：

- \(\mathcal B\) 是 accessible 且 complete 的 \(\infty\)-范畴；
- \(H_a=P^\sharp(a,-):\mathcal B\to\mathcal S\) accessible。

### 定理 9.1（严格 representability criterion）

以下条件等价：

1. \(H_a\) 可 corepresent；
2. \(H_a\) 保持所有小极限。

这是 accessible adjoint/representability theorem 的标准形式。

若再假设 \(H_a\) 保有限极限，则以上条件还等价于：

3. \(H_a\) 保持所有小乘积。

#### 证明

余表示函子保持所有小极限。反向使用 accessible complete \(\infty\)-category 上的表示性定理。

若 \(H_a\) 已保有限极限，则它保终对象和 pullback。任意小极限可由小乘积与 pullback 构造；因此保持所有小乘积等价于保持所有小极限。证毕。

### 定理 9.2（Pro-objectification）

若 \(\mathcal B\) accessible、具有有限极限，且 \(H_a\) accessible、保有限极限，则存在唯一到等价的

\[
\widehat F(a)\in\Pro(\mathcal B)
\]

满足

\[
H_a(b)\simeq
\Map_{\Pro(\mathcal B)}
(\widehat F(a),j(b)).
\]

并且：

\[
H_a\text{ 在 }\mathcal B\text{ 中可 corepresent}
\]

当且仅当

\[
\widehat F(a)\in\operatorname{EssIm}
\bigl(j:\mathcal B\to\Pro(\mathcal B)\bigr).
\]

这里 Pro-objectification 是 formal objectification；落回 \(j(\mathcal B)\) 是该 sector 中的 actual effectivity。

### 9.3 乘积比较与完整一致化

若

\[
H(b)\simeq\operatorname*{colim}_{j}
\Map_{\mathcal B}(x_j,b),
\]

则对一族 \((b_i)_{i\in I}\)，有比较映射

\[
\chi_I:
\operatorname*{colim}_{j}
\prod_{i\in I}\Map(x_j,b_i)
\longrightarrow
\prod_{i\in I}
\operatorname*{colim}_{j}\Map(x_j,b_i).
\]

\(\chi_I\) 为等价，不仅要求右侧各元素的代表元能选择在同一个 stage，还要求：

- 等式能在同一个 stage 成立；
- 空间值情形下，路径与全部 higher coherence 能同时一致化。

所以

\[
\forall i\,\exists j_i
\Longrightarrow
\exists j\,\forall i
\]

只描述 \(\pi_0\) 上满射性的一个部分，不能单独替代“\(\chi_I\) 是空间等价”。

### 定义 9.3（product effectivity rank）

对保有限极限的 \(H\)，定义

\[
\rho_{\mathrm{prod}}(H)
=
\inf
\left\{
|I|:\chi_I\text{ 不是等价}
\right\}.
\]

若不存在失败的 \(\mathbb U_0\)-小基数，则规定

\[
\rho_{\mathrm{prod}}(H)=\infty.
\]

这只是 Pro-sector 的 product rank，不是一般效性问题的完整 obstruction。

---

## 10. 一个严格的超限测试秩定理

### 定理 10.1

对每个无限正则基数 \(\kappa\)，存在一个 accessible、保有限极限的函子

\[
H_\kappa:\mathbf{Set}\to\mathbf{Set}
\]

使得：

1. \(H_\kappa\) 保持所有由少于 \(\kappa\) 个因子组成的乘积；
2. \(H_\kappa\) 不保持 \(\kappa\)-元乘积；
3. 因而
   \[
   \rho_{\mathrm{prod}}(H_\kappa)=\kappa ;
   \]
4. 相应 Pro-object 不来自一个实际集合。

### 构造

对 \(\alpha<\kappa\)，令

\[
T_\alpha=[\alpha,\kappa).
\]

定义

\[
H_\kappa(X)
=
\operatorname*{colim}_{\alpha<\kappa}
\operatorname{Hom}(T_\alpha,X),
\]

其中 transition map 是对更短尾集的限制。

换言之，\(H_\kappa(X)\) 是函数

\[
\kappa\to X
\]

关于“最终相等”的等价类。

### 证明

每个

\[
\operatorname{Hom}(T_\alpha,-)
\]

保持所有极限。因为 \(\kappa\) 是滤过索引，Set 中滤过余极限与有限极限交换，所以 \(H_\kappa\) 保有限极限。

取任意正则 \(\lambda>\kappa\)。由于

\[
|T_\alpha|\le\kappa<\lambda,
\]

函子 \(\operatorname{Hom}(T_\alpha,-)\) 保 \(\lambda\)-滤过余极限，故 \(H_\kappa\) accessible。

令 \(|I|<\kappa\)。对乘积比较

\[
\chi_I:
H_\kappa\!\left(\prod_{i\in I}X_i\right)
\to
\prod_{i\in I}H_\kappa(X_i),
\]

证明其满射：右侧每个分量可由

\[
f_i:T_{\alpha_i}\to X_i
\]

表示。正则性给出

\[
\alpha:=\sup_{i\in I}\alpha_i<\kappa.
\]

把所有 \(f_i\) 限制到 \(T_\alpha\)，即可组成

\[
T_\alpha\to\prod_{i\in I}X_i.
\]

证明其单射：设两个向量值尾函数逐坐标表示相同的芽。对每个 \(i\) 存在阈值 \(\gamma_i<\kappa\)，使该坐标在 \(T_{\gamma_i}\) 上相等。再次由正则性，

\[
\gamma:=\sup_{i\in I}\gamma_i<\kappa.
\]

故两个向量值函数在 \(T_\gamma\) 上相等。

现在取 \(I=\kappa\) 且 \(X_i=\{0,1\}\)。定义

\[
u_\beta(i)=0
\]

以及

\[
v_\beta(i)=
\begin{cases}
1,&i=\beta,\\
0,&i\ne\beta.
\end{cases}
\]

对固定 \(i\)，两个坐标序列只在 \(\beta=i\) 处不同，因此最终相等。故

\[
\chi_\kappa([u])=\chi_\kappa([v]).
\]

但是对每个 \(\beta<\kappa\)，向量 \(u_\beta\) 与 \(v_\beta\) 都不同，所以两个向量序列从不最终相等：

\[
[u]\ne[v].
\]

因此 \(\chi_\kappa\) 不单。前三条得证。若相应 Pro-object 来自实际集合，则 \(H_\kappa\) 可余表示，从而保持所有乘积，与上面矛盾。证毕。

### 推论 10.2

不存在一个正则基数 \(\kappa_0\)，使得对所有 accessible left-exact

\[
H:\mathbf{Set}\to\mathbf{Set}
\]

只检验 \(<\kappa_0\)-元乘积就能判定其可余表示。

这严格证明了 Frozen v1.0 中“No Universal Bounded Effectivity-Test Rank”在 product Pro-sector 的版本。它不自动推广为所有 comparison functor 的一般定理。

---

## 11. 三个边界例子

### 例 11.1（representability 不压缩 whole moduli）

令

\[
\mathcal B=\mathbf{FinSet},
\qquad
H(X)=\operatorname{Hom}(1,X).
\]

\(H\) 由单点集合余表示。其元素范畴是有限非空带基点集合范畴，单点带基点集合为初始对象。

然而

\[
\mathcal M
\simeq
\coprod_{n\ge1}B\mathfrak S_{n-1}.
\]

故 universal locus 可缩，而 whole moduli 既不连通也不可缩。

### 例 11.2（对象级刚性效性不等于 reconstruction）

令 \(\mathcal D\) 是对象 \(0,1\) 组成的离散范畴，并令

\[
[1]=(0\to1).
\]

取同对象函子

\[
C:\mathcal D\to[1].
\]

两个 formal objects 的对象级效性纤维都可缩，但 \(C\) 漏掉态射

\[
0\to1,
\]

所以 \(C\) 不是 fully faithful，也不是范畴等价。

### 例 11.3（逐 context 同构不等于观察 presheaf 等价）

令

\[
\mathsf K=B(\mathbb Z/2).
\]

\(\mathcal P(\mathsf K)\) 中的 Set 值对象等价于带 \(\mathbb Z/2\)-作用的集合。

取同一个二元素集合上的：

- 平凡作用；
- 交换两个元素的作用。

在 \(\mathsf K\) 的唯一对象处，二者底层集合同构；但不存在 equivariant bijection，因此相应 presheaves 不等价。

这说明观察等价必须在 \(\mathcal P(\mathsf K)\) 中定义，不能只要求对 context objects 逐点存在某个不相容的等价。

---

## 12. 对称性 no-go 的严格版本

### 命题 12.1

设群 \(G\) 作用于空间 \(D\)。若

\[
\pi_0(D)^G=\varnothing,
\]

则

\[
D^{hG}=\varnothing.
\]

#### 证明

一个 homotopy fixed point 给出 \(D\) 的一个点及相干的 \(G\)-不变结构，因而其连通分支在 \(\pi_0(D)\) 中被 \(G\) 固定。与假设矛盾。证毕。

该命题支持如下精确结论：

> 若候选 doctrines 的所有连通分支都被对称性非平凡置换，则不存在保持该对称性的 coherent doctrine selection。

它不推出“裸范畴不能产生任何 canonical 非平凡构造”；后一个更强说法需要先定义允许的 doctrine 类并另行证明。

---

## 13. Anti-tautology 的形式化研究协议

“预目标”不是 \(P\) 的内部同伦不变量。相同的 \(P\) 可以在知道答案之前或之后被选出。因此本严格版本把它规定为**量词顺序与依赖纪律**。

一个有效的预测性主张必须具有形式：

\[
\forall\Xi\in\mathcal C_{\mathrm{adm}},
\quad
\forall x\in\mathsf{Act}_\Xi(a),
\quad
\mathcal H(\Xi,x)\Longrightarrow\mathcal Q(\Xi,x),
\]

其中整个配置

\[
\Xi=
(\mathcal A,\mathcal B,P,L,\mathsf{Act},C,
\widetilde{\mathsf E},W,q,p,
\widetilde{\mathrm{Ev}},\mathsf K,\mathbb O,j)
\]

在量化 \(x\) 之前固定。

下列形式不能作为理论预测：

\[
\forall x\ \exists\Xi_x
\quad
\mathcal Q(\Xi_x,x),
\]

因为 \(P,L,C,\mathbb O\) 或 \(j\) 可以依赖目标 \(x\) 事后选取。

每个 sector application 应提交：

1. 配置数据的独立来源；
2. 允许使用的先验领域定理；
3. 待预测对象出现前已经固定的 \(P,L,C,\mathbb O,j\)；
4. 一个可被否定的结论；
5. 从配置假设到该结论的证明；
6. 相邻正例和反例。

provenance 可以用证明项、依赖图或版本化定义记录。单凭最终函子不能恢复研究过程中的量词顺序。

---

## 14. 本版本的逻辑地位

### 14.1 已经严格定义

- raw problem 与 saturated problem；
- gauge equivalence；
- possibility \(\infty\)-category；
- generative moduli；
- universal locus；
- actual/formal comparison；
- 对象级 effectivity fiber；
- provenance localization；
- semantic forgetful map；
- persistent nerve；
- old-event match space；
- observation-relative novelty。

### 14.2 已经证明

- saturation invariance；
- initiality 与 corepresentability 等价；
- reduct sector 中的 adjunction；
- effectivity 与本质满射的关系；
- reconstruction 的 fully faithful 条件不能省略；
- observation adequacy 下的 novelty 判据；
- context enlargement 的单调性；
- Pro-sector 的 representability/effectivity 判据；
- 任意正则基数上的 product effectivity rank 例子；
- doctrine symmetry 的精确 no-go。

### 14.3 仍作为输入

- 为什么选取某个具体 \(P\)；
- 为什么某种 gauge localization \(L\) 是正确语义；
- comparison \(C\) 的本质像；
- future-context category \(\mathsf K\) 是否充分；
- observation \(\mathbb O\) 是否 adequate；
- 哪些 provenance differences 应进入 \(W\)；
- 某个 sector 的实际 obstruction theory。

这些问题不能由“存在一个配置”自动回答。它们正是具体领域中需要证明的内容。

### 14.4 本版本不宣称

- 存在适用于所有 enriched bases 的单一 Grothendieck construction；
- 所有 effectivity 都是 Pro-object constancy；
- 所有生成问题都可表示；
- 所有 novelty 都与 observation doctrine 无关；
- 所有自然 doctrine 都能从 bare carrier 唯一导出；
- 只由抽象框架即可解决任意领域问题。

---

## 15. 与 Frozen v1.0 的对应

| Frozen v1.0 概念 | 本严格版本中的对象 |
|---|---|
| configuration \(\Xi\) | 定义 2.1 的有类型数据 |
| pre-target horizontal problem | \(P:\mathcal A^{op}\times\mathcal B\to\mathcal S\) |
| saturation/gauge | reflective localization \(L\) |
| \(P^\sharp\) | \(L(P)\) |
| possibility geometry | \(H_a\) 的 left unstraightening \(\mathfrak G(a)\) |
| generative moduli | \(\mathfrak G(a)^\simeq\) |
| universal locus | 初始对象空间 \(\mathcal U_\Xi(a)\) |
| formal category | \(\mathfrak G(a)\) |
| actual category | \(\mathsf{Act}(a)\) |
| comparison functor | \(C_a:\mathsf{Act}(a)\to\mathfrak G(a)\) |
| effectivity fiber | cores 上的同伦拉回 |
| provenance lift | \(\widetilde{\mathrm{Ev}}\) |
| GM normalization | \(q:\widetilde{\mathsf E}\to\widetilde{\mathsf E}[W^{-1}]\) |
| persistent observation | \(\mathbb O:\mathsf K^{op}\times\mathsf E^{GM}\to\mathcal S\) |
| persistent nerve | \(N^\infty_{\mathbb O}:\mathsf E^{GM}\to\mathcal P(\mathsf K)\) |
| novelty | \(\operatorname{OldMatch}_\Xi(e)=\varnothing\) |

---

## 16. 下一步可证明的核心问题

本版本把未来研究集中为三个严格问题。

### A. Effectivity image

对具体 sector，刻画

\[
\operatorname{EssIm}
\left(
C_a:\mathsf{Act}(a)\to\mathfrak G(a)
\right).
\]

目标是给出只依赖 formal datum 的必要充分条件。

### B. Observation adequacy

证明或否定

\[
N^\infty_{\mathbb O}:
\mathsf E^{GM}\to\mathcal P(\mathsf K)
\]

fully faithful，或寻找一个小的 context 子范畴

\[
\mathsf K_0\subseteq\mathsf K
\]

仍能检测所需对象与态射。

### C. Derived obstruction extraction

从 \(C_a\) 的几何构造 obstruction object

\[
\operatorname{Obs}_a(\xi)
\]

及一个定理

\[
\xi\in\operatorname{EssIm}(C_a)
\quad\Longleftrightarrow\quad
\operatorname{Obs}_a(\xi)\simeq0
\]

或在明确附加条件下的充分、必要版本。

一旦其中任一问题在非平凡 sector 中得到新解，本理论就产生了可脱离其哲学语言独立检验的数学结果。

---

## 17. 规范参考

本版本使用的标准背景包括：

1. Jacob Lurie, *Higher Topos Theory*：\(\infty\)-范畴、straightening/unstraightening、accessible representability；
2. Jacob Lurie, *Derived Algebraic Geometry XIII: Rational and \(p\)-adic Homotopy Theory*, §3.1：accessible left-exact functors 与 Pro-objects；
3. Michael Shulman, *Framed Bicategories and Monoidal Fibrations*：equipment/proarrow 背景；
4. Jaco Ruit, *Formal Category Theory in \(\infty\)-Equipments I*：\(\infty\)-equipment 背景。

这些参考提供标准工具。本文件的严格化贡献是固定一个一致的类型系统，把 Frozen v1.0 的各层连接起来，并给出 product effectivity rank 的完整 sector 证明。
