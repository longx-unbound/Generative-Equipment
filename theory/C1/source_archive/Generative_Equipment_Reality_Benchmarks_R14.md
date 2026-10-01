# 生成装备研究 R14：现实性实验 A–C

## 0. 实验结论

本报告执行 R13 提出的三个现实性基准中的前两项，并完成第三项的可扩展 pilot。

结果是一负一正一部分通过：

1. **实验 A（unipotent monodromy）**：R11 refinement 正确，但最小实例中没有计算简化，反而增加了一层谱序列/连接同态。
2. **实验 B（非仿射拓扑 Coupl）**：找到真正的 two-stage Postnikov 实例。仿射 residual 给出错误的“无解”预测，而二次 Coupl 给出唯一正确修正。这证明 R10 不只是抽象代数包装。
3. **实验 C（cellwise matching）**：在 \((S^2)^m\) 的 \(4\)-骨架上，全局 cup-square obstruction 精确分解为 \(\binom m2\) 个局部 matching defects；它支持局部化与并行化，但未改善渐近复杂度。

总状态：

\[
\boxed{
\text{R10 获得首个真实拓扑证据；R11 尚无计算优势；R9 有局部化价值但未见加速。}
}
\]

---

## 1. 实验 A：二阶幂零 monodromy

### 1.1 数据

取

\[
M=\mathbb Z e_1\oplus\mathbb Z e_2,
\qquad
T=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]

令

\[
N:=T-I=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
\]

于是

\[
Ne_1=0,\qquad Ne_2=e_1,\qquad N^2=0.
\]

令

\[
B=S^1\times S^{n+1},
\qquad n\ge2,
\]

并令局部系统 \(M_T\) 的 monodromy 沿 \(S^1\) 为 \(T\)，沿球面方向平凡。

固定一个由

\[
x\in H^{n+1}(B;M_T)
\]

分类的 twisted \(K(M,n)\)-torsor

\[
K(M,n)\longrightarrow Q_x\longrightarrow B.
\]

它有 section 当且仅当 \(x=0\)。

---

## 2. 直接 twisted-cohomology 计算

\(B\) 的乘积 CW 结构在相关次数只有

\[
C^{n+1}(B;M_T)\cong M,
\qquad
C^{n+2}(B;M_T)\cong M.
\]

其 twisted coboundary 在统一符号差异下就是

\[
\delta=T-I=N.
\]

因为 \(C^n=0\)，

\[
H^{n+1}(B;M_T)
\cong
\ker N.
\]

由矩阵可见

\[
\ker N=\mathbb Ze_1.
\]

同样，

\[
H^{n+2}(B;M_T)
\cong
\operatorname{coker}N
\cong
\mathbb Z\bar e_2.
\]

因此任意 obstruction 是

\[
x=r e_1,\qquad r\in\mathbb Z,
\]

且

\[
Q_x\text{ 有 section}
\iff
r=0.
\]

直接计算只需一个 \(2\times2\) 整数矩阵的核。

---

## 3. R11 增广过滤计算

由 \(I=(T-I)\) 得

\[
F^0M=M,\qquad
F^1M=IM=\mathbb Ze_1,\qquad
F^2M=0.
\]

两个 associated quotients 为

\[
A_0=M/F^1M\cong\mathbb Z\bar e_2,
\qquad
A_1=F^1M\cong\mathbb Ze_1.
\]

二者 monodromy 均平凡。

于是有短正合列

\[
0\to A_1\to M_T\to A_0\to0.
\]

对 obstruction \(x=re_1\)：

1. 它在
   \[
   H^{n+1}(B;A_0)
   \]
   中的投影恒为零；
2. 因而第一层 constant-coefficient obstruction 永远不检测失败；
3. 它提升为
   \[
   x_1=r e_1\in H^{n+1}(B;A_1)\cong\mathbb Z;
   \]
4. 第二层判定
   \[
   x_1=0\iff r=0.
   \]

相关长正合列中的连接同态

\[
\delta:
H^{n+1}(B;A_0)
\longrightarrow
H^{n+2}(B;A_1)
\]

是同构；它由 \(S^1\) 上的非平凡 extension class 与 \(S^{n+1}\) 的基本上同调类作 cup product 给出。

因此谱序列的第一 differential 恰好重新编码了原 monodromy。

### 实验 A 判定

\[
\boxed{
\text{R11 refinement 正确，但在此实例中没有简化计算。}
}
\]

直接方法：求 \(\ker N\)。

R11 方法：计算两个常系数群，再计算非零连接同态，最后进入第二层。

所以该实验否定了“nilpotent refinement 自动降低计算成本”的强说法。R11 的现实价值必须依赖额外结构，例如：

- 常系数上同调已经预先计算；
- monodromy 只以黑箱形式给出；
- associated graded 具有稀疏性；
- extension differential 比直接 twisted complex 更容易。

这些优势不能只由 \(I^2M=0\) 推出。

---

## 4. 实验 B：真正的非仿射拓扑 Coupl

### 4.1 Two-stage Postnikov 空间

令

\[
\iota\in H^2(K(\mathbb Z,2);\mathbb Z)
\]

为 universal class，并取代表 cup-square 的映射

\[
\kappa:
K(\mathbb Z,2)
\longrightarrow
K(\mathbb Z,4),
\qquad
\kappa^*(\iota_4)=\iota^2.
\]

令

\[
F:=\operatorname{hofib}(\kappa).
\]

则 \(F\) 是一个 simply connected two-stage \(3\)-type，满足

\[
\pi_2(F)\cong\mathbb Z,
\qquad
\pi_3(F)\cong\mathbb Z,
\]

其 \(k\)-invariant 正是 cup-square。

对任意 \(B\)，一个类

\[
a\in H^2(B;\mathbb Z)
\cong
[B,K(\mathbb Z,2)]
\]

能提升为 \(B\to F\)，当且仅当

\[
q(a):=a\smile a=0
\in H^4(B;\mathbb Z).
\]

这是真正的 Postnikov lifting obstruction，而不是人为指定的多项式。

---

## 5. 在 \(\mathbb{CP}^2\) 上计算

令

\[
B=\mathbb{CP}^2,
\qquad
H^*(B;\mathbb Z)\cong\mathbb Z[u]/(u^3),
\qquad |u|=2.
\]

任意 first-stage branch 写成

\[
a_n=nu,\qquad n\in\mathbb Z.
\]

其 obstruction 为

\[
q(a_n)
=
n^2u^2.
\]

因为 \(u^2\) 生成 \(H^4(B;\mathbb Z)\)，

\[
a_n\text{ 可提升}
\iff
n=0.
\]

现在固定初始 branch

\[
a_0=u,
\]

允许修正

\[
h=mu.
\]

Coupl 为

\[
\begin{aligned}
C_{a_0}(h)
&=
q(a_0+h)-q(a_0)\\
&=
(1+m)^2u^2-u^2\\
&=
(2m+m^2)u^2.
\end{aligned}
\]

其二阶 cross-effect 为

\[
\operatorname{cr}_2C(m_1,m_2)
=
2m_1m_2u^2,
\]

故 Coupl 严格非仿射。

---

## 6. 仿射 residual 的失败

若错误地只保留线性部分

\[
D(m)=2m,
\]

则消去初始 obstruction \(u^2\) 的仿射方程是

\[
1+2m=0.
\]

它在整数中无解。相应 residual 是

\[
[-1]\in\operatorname{coker}(2:\mathbb Z\to\mathbb Z)
\cong\mathbb Z/2,
\]

并且非零。

因此仿射近似会判定：

\[
\text{不存在修正。}
\]

但完整二次方程是

\[
1+2m+m^2=(1+m)^2=0,
\]

具有唯一解

\[
m=-1.
\]

它把 \(a_0=u\) 修正为

\[
a_0+h=0,
\]

从而 obstruction 确实消失。

### 实验 B 判定

\[
\boxed{
\text{非零 cross-effect 在真实 Postnikov lifting problem 中改变可解性。}
}
\]

这证明：

1. R10 的“\(\operatorname{cr}_2\neq0\) 时不能使用单一 affine cofiber”具有真实拓扑内容；
2. Coupl 的二次项不是形式修饰，它能把 affine residual 的“无解”翻转为“有解”；
3. cup-square \(k\)-invariant 给出一个自然、非人为的 polynomial Coupl 来源。

这是目前 R10 最重要的现实性证据。

---

## 7. 解空间的高阶结构

修正 \(m=-1\) 后 first-stage branch 为零。其 lift space 是

\[
\operatorname{Map}(\mathbb{CP}^2,K(\mathbb Z,3))
\]

的 torsor。

由于

\[
H^3(\mathbb{CP}^2;\mathbb Z)=0,
\]

lift 只有一个 component；但其高阶同伦并不平凡：

\[
\pi_1\cong H^2(\mathbb{CP}^2;\mathbb Z)\cong\mathbb Z,
\qquad
\pi_3\cong H^0(\mathbb{CP}^2;\mathbb Z)\cong\mathbb Z.
\]

因此该例同时验证：

\[
\text{存在唯一 component}
\centernot\Rightarrow
\text{lift space 可缩}.
\]

这给 R8 的“存在交换与结构交换必须区分”提供了具体拓扑实例。

---

## 8. 实验 C pilot：可扩展的 cellwise matching family

取

\[
B_m:=\operatorname{sk}_4\bigl((S^2)^m\bigr).
\]

记第 \(i\) 个球面的 degree-\(2\) 类为

\[
u_i\in H^2(B_m;\mathbb Z).
\]

有

\[
u_i^2=0,
\]

且 \(H^4\) 由

\[
u_i u_j,\qquad i<j,
\]

生成。

对 first-stage branch

\[
a=\sum_{i=1}^m a_i u_i,
\]

cup-square obstruction 为

\[
q(a)
=
a^2
=
2\sum_{i<j}a_i a_j\,u_i u_j.
\]

因此

\[
q(a)=0
\iff
a_i a_j=0
\quad\text{对所有 }i<j.
\]

在整数系数下，这等价于：

\[
\#\operatorname{supp}(a)\le1.
\]

### Cellular/matching 解释

每个 \(4\)-cell 对应一对 \((i,j)\)，该 cell 上的 R3 matching obstruction 恰为

\[
2a_i a_j.
\]

所以全局 obstruction 的消失严格等价于全部

\[
\binom m2
\]

个局部 matching defects 消失。

这些局部检查彼此可并行，而且每个只读取两个坐标。

### 实验 C pilot 判定

\[
\boxed{
\text{R3 matching 确实把全局 cup-square 分解为可并行的局部二元缺陷。}
}
\]

但直接计算 \(a^2\) 同样需要所有 pair products，复杂度仍为

\[
O(m^2).
\]

因此本实验确认了局部化和并行化意义，没有证明渐近加速。

它还没有完全满足 R13 的强基准 C：尚未找到“小方格 \(\chi\) 易证为有效满射，而直接全局填充明显困难”的实例。

---

## 9. 三项实验后的现实性更新

| 理论部分 | 实验前判断 | 实验后判断 |
|---|---|---|
| R9 matching descent | 形式上正确，应用未知 | cellwise localization 得到验证；复杂度收益未证 |
| R10 polynomial Coupl | 代数正确，拓扑适用性未知 | cup-square 给出真正的二次 Postnikov Coupl，现实性显著提高 |
| R11 nilpotent refinement | 条件性结构工具 | 最小 unipotent 实例无计算优势，不能宣传为自动简化 |
| R8 existence/structure distinction | 抽象区分 | \(\mathbb{CP}^2\) lift space 给出具体非可缩实例 |

---

## 10. 最终结论

这轮实验第一次把 R10 从“条件性抽象工具”推进为“已被自然拓扑实例验证的工具”：

\[
\boxed{
q(a)=a^2
\quad\Longrightarrow\quad
C_a(h)=2ah+h^2.
}
\]

其中 \(h^2\) 能改变整数解的存在性，不能被线性 residual 忽略。

相反，R11 的现实性被收紧：

\[
\boxed{
\text{constant associated gradeds 不等于更便宜的计算。}
}
\]

R9 的结论居中：

\[
\boxed{
\text{它提供真实的局部化与并行接口，但尚无复杂度突破。}
}
\]

下一轮最值得做的不是更多抽象定理，而是：

1. 分类哪些自然 \(k\)-invariants 给出有限-degree Coupl；
2. 把 cup-square 实验推广到 Steenrod、Pontryagin square 与 Massey-type operations；
3. 寻找 R11 refinement 真正优于直接 twisted complex 的系数系统；
4. 完成强基准 C。
