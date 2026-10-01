# 生成装备研究 R8：障碍 Fubini 定理与二维交换缺陷

## 0. 本轮突破

R5 的共同双滤过

\[
\mathcal S_{r,k}
=
\Gamma(B^{(r)},P_k^B E)
\]

同时具有两个方向：

- \(r\)-方向：扩大基空间骨架，对应 R3 matching/cellular extension；
- \(k\)-方向：提高纤维 Postnikov 阶段，对应经典 obstruction tower。

R7 已证明有限障碍塔必须同时进行前向分支生成与反向可生存核筛除。本轮证明：

1. 以精确 \((-1)\)-像定义的可生存核，在双塔中满足无条件的路径独立性；这是 **Obstruction Fubini Theorem**。
2. “分别可沿两个方向提升”与“可同时提升”之间的差异，由每个小方格的比较映射
   \[
   \chi_{r,k}:
   \mathcal S_{r+1,k+1}	o
   \mathcal S_{r+1,k}	imes_{\mathcal S_{r,k}}
   \mathcal S_{r,k+1}
   \]
   完全测量。
3. \(\chi_{r,k}\) 为有效满射，当且仅当两个单方向有效性谓词的交，等于真正的同时有效性谓词。
4. \(\chi_{r,k}\) 为等价，当且仅当该小方格是同伦拉回；此时不仅存在性，而且全部选择、变形与高阶自同伦都交换。
5. 若 \(\chi_{r,k}\) 的纤维提升问题是仿射的，则 R7 的余纤维残余障碍给出交换缺陷的群值压缩；非线性时必须保留其像子对象。

这把“R3 与 Postnikov 最终得到同一解空间”加强成了一个逐角点、逐小方格的二维 simultaneous-effectivity 理论。

本轮仍不修改 Frozen v1.0：

\[
\boxed{\texttt{PASS + DERIVED STRUCTURE}}.
\]

---

## 1. 有限交换双塔

设 \(0\le r\le R\)、\(0\le k\le N\)，并有交换双塔

\[
\{\mathcal S_{r,k}\}_{[R]^{op}\times[N]^{op}}
\]

其结构映射记为

\[
h_{r,k}:\mathcal S_{r+1,k}\to\mathcal S_{r,k},
\qquad
v_{r,k}:\mathcal S_{r,k+1}\to\mathcal S_{r,k}.
\]

所有小方格同伦交换。终端精细对象为

\[
\mathcal S_{R,N}.
\]

在应用中，若 \(B\) 的相关骨架在 \(R\) 停止且纤维 \(N\)-截断，则

\[
\mathcal S_{R,N}\simeq\Gamma(B,E).
\]

---

## 2. 二维可生存像

### 定义 2.1

在每个角点 \((r,k)\)，定义相对于终端高度 \((R,N)\) 的可生存子对象

\[
V_{r,k}^{R,N}
:=
\operatorname{im}_{-1}
\bigl(\mathcal S_{R,N}\to\mathcal S_{r,k}\bigr)
\hookrightarrow
\mathcal S_{r,k}.
\]

一个 \((r,k)\)-部分分支属于 \(V_{r,k}^{R,N}\)，当且仅当它能同时延伸到完整骨架与完整 Postnikov 高度。

### 定理 2（Obstruction Fubini Theorem）

对所有 \(r<R\)、\(k<N\)，有

\[
\boxed{
V_{r,k}^{R,N}
=
\operatorname{im}_{-1}
(V_{r+1,k}^{R,N}\to\mathcal S_{r,k})
}
\]

以及

\[
\boxed{
V_{r,k}^{R,N}
=
\operatorname{im}_{-1}
(V_{r,k+1}^{R,N}\to\mathcal S_{r,k})
}.
\]

因此，从 \((R,N)\) 到 \((r,k)\) 选择任意单调格路径，沿路径反复取精确 \((-1)\)-像，最终都得到同一个 \(V_{r,k}^{R,N}\)。

#### 证明

考虑分解

\[
\mathcal S_{R,N}
\twoheadrightarrow
V_{r+1,k}^{R,N}
\hookrightarrow
\mathcal S_{r+1,k}
\to
\mathcal S_{r,k}.
\]

前一个映射是有效满射。前合成有效满射不改变复合映射的 \((-1)\)-像，因此其到 \(\mathcal S_{r,k}\) 的像就是

\[
\operatorname{im}_{-1}
(V_{r+1,k}^{R,N}\to\mathcal S_{r,k}).
\]

但整个复合正是 \(\mathcal S_{R,N}\to\mathcal S_{r,k}\)，故该像等于 \(V_{r,k}^{R,N}\)。竖直方向相同。沿任意单调路径归纳即可。∎

### 解释

这个 Fubini 定理不是说逐层障碍类可以任意交换，也不是说每个小方格是拉回。它说的是：

> 只要每一步都保留精确的可生存像，而不以不完备的局部摘要替代它，消去 matching 变量与 Postnikov 变量的顺序不影响最终有效分支谓词。

---

## 3. 单方向零点与同时零点

固定一个小方格，并简写

\[
S:=\mathcal S_{r,k},
\quad
H:=\mathcal S_{r+1,k},
\quad
P:=\mathcal S_{r,k+1},
\quad
Q:=\mathcal S_{r+1,k+1}.
\]

定义两个单方向可提升谓词

\[
Z_h:=\operatorname{im}_{-1}(H\to S),
\qquad
Z_v:=\operatorname{im}_{-1}(P\to S).
\]

定义真正的同时提升谓词

\[
Z_{hv}:=\operatorname{im}_{-1}(Q\to S).
\]

显然存在包含

\[
Z_{hv}\hookrightarrow Z_h\cap Z_v.
\]

但这个包含一般不必是等价：两个分别存在的提升可能彼此不兼容。

---

## 4. 兼容对空间与交换比较映射

定义兼容的一步提升对空间

\[
C_{r,k}
:=
H\times_S P
=
\mathcal S_{r+1,k}
\times_{\mathcal S_{r,k}}
\mathcal S_{r,k+1}.
\]

一个点是同一底层分支的一个 matching 提升和一个 Postnikov 提升。

双塔的交换性给出规范比较映射

\[
\boxed{
\chi_{r,k}:Q\to C_{r,k}.
}
\]

它把一个真正的双向提升忘却为两个兼容的单方向提升。

### 引理 4.1

有

\[
\operatorname{im}_{-1}(C_{r,k}\to S)
\simeq
Z_h\cap Z_v.
\]

#### 证明

在内部逻辑中，\(s\in S\) 属于左侧，当且仅当存在

\[
h\in H_s,
\qquad
p\in P_s.
\]

这等价于 \(H_s\) 与 \(P_s\) 都非空，也就是 \(s\in Z_h\cap Z_v\)。∎

---

## 5. 局部同时有效性的充要条件

### 定理 5（Elementary Simultaneous Effectivity Criterion）

下列条件等价：

1. \(\chi_{r,k}:Q\to C_{r,k}\) 是有效满射；
2. 每一对兼容的单方向提升，至少有一个共同双向提升；
3. 对每个基变换 \(T\to S\)，两个单方向有效性谓词的交都恰等于真正同时有效性谓词：
   \[
   \boxed{
   \operatorname{im}_{-1}(Q_T\to T)
   =
   \operatorname{im}_{-1}(H_T\to T)
   \cap
   \operatorname{im}_{-1}(P_T\to T)
   };
   \]
4. \(Q\to C_{r,k}\) 的每个纤维非空。

#### 证明

条件 1、2、4 是有效满射的逐纤维刻画。若条件 1 成立，则前合成 \(\chi_{r,k}\) 不改变到 \(S\) 的像，所以

\[
Z_{hv}
=
\operatorname{im}_{-1}(Q\to S)
=
\operatorname{im}_{-1}(C_{r,k}\to S)
=
Z_h\cap Z_v.
\]

反之，条件 3 中取 \(T=C_{r,k}\)；两个投影给出一对通用兼容提升，所以右侧是整个 \(C_{r,k}\)。左侧为 \(\chi_{r,k}\) 的像，故它必须是有效满射。∎

### 严格性说明

若只比较 \(S\) 上的全局连通分支集合，\(Z_{hv}=Z_h\cap Z_v\) 可能偶然成立，而某些指定兼容对仍无共同填充。充要条件必须是所有基变换后的谓词相等，等价地直接要求 \(\chi_{r,k}\) 为有效满射。

---

## 6. 存在交换与结构交换

### 定理 6（Interchange Trichotomy）

小方格有三个严格不同的层次：

1. **失败层**：\(\chi_{r,k}\) 不是有效满射。存在兼容的单方向提升对，但没有共同双向提升。
2. **存在交换层**：\(\chi_{r,k}\) 是有效满射但不是等价。每个兼容对都可共同提升，但提升选择空间可能非平凡。
3. **结构交换层**：\(\chi_{r,k}\) 是等价。小方格是同伦拉回；共同提升存在且其全部高阶结构完全由两个单方向提升的兼容对决定。

#### 证明

第一、二层由定理 5。第三层是同伦拉回方格的定义：规范映射

\[
Q\to H\times_S P
\]

为等价。有效满射只控制 \((-1)\)-层存在性；等价还要求所有纤维可缩，因而控制唯一性、变形与高阶自同伦。∎

这严格区分了：

\[
\text{有共同解}
\quad\ne\quad
\text{共同解空间可缩}.
\]

---

## 7. 交换缺陷的普遍对象

### 定义 7.1（Interchange Effectivity Locus）

定义

\[
I_{r,k}
:=
\operatorname{im}_{-1}(\chi_{r,k})
\hookrightarrow
C_{r,k}.
\]

它是兼容提升对空间上的真值型谓词：

\[
I_{r,k}(h,p)
\simeq
\left\|
\operatorname{fib}_{(h,p)}(\chi_{r,k})
\right\|_{-1}.
\]

### 定义 7.2（Interchange Defect）

交换缺陷不是强行定义为集合差，而定义为单射

\[
I_{r,k}\hookrightarrow C_{r,k}
\]

未成为等价的程度：

- 存在性缺陷：该单射不是等价，即 \(\chi_{r,k}\) 非有效满；
- 高阶缺陷：\(\chi_{r,k}\) 已有效满，但不是等价；
- 无缺陷：\(\chi_{r,k}\) 为等价。

这一定义在没有补对象、没有经典排中律、没有固定障碍群的 \(\infty\)-拓扑斯中仍然良定义。

---

## 8. R7 残余障碍对交换缺陷的压缩

固定兼容对

\[
c=(h,p)\in C_{r,k}.
\]

其共同双向提升空间是

\[
F_c:=\operatorname{fib}_c(\chi_{r,k}).
\]

假设该提升问题具有以下仿射模型：

- 候选共同填充构成 \(\Omega^\infty H_c\)-扭子 \(T_c\)；
- 兼容障碍取值于 \(\Omega^\infty G_c\)；
- Coupl 的线性部分为谱映射
  \[
  D_c:H_c\to G_c.
  \]

### 定理 8（Affine Interchange Obstruction）

存在规范残余点

\[
\rho_{r,k}(c)\in
\Omega^\infty\operatorname{cofib}(D_c)
\]

使得

\[
c\in I_{r,k}
\iff
[\rho_{r,k}(c)]=0
\in
\pi_0\operatorname{cofib}(D_c).
\]

若共同提升存在，则

\[
F_c
\]

是 \(\Omega^\infty\operatorname{fib}(D_c)\)-扭子。

#### 证明

对兼容对 \(c\) 的共同填充问题直接应用 R7 的 Residual Cofiber Obstruction Theorem。∎

### 非线性边界

若相应障碍映射的

\[
\operatorname{cr}_2\ne0,
\]

则不存在与平移兼容的单一余纤维值线性压缩。此时 \(I_{r,k}\hookrightarrow C_{r,k}\) 本身就是规范的交换障碍对象。

---

## 9. Fubini 定理并不消灭 Coupl

表面上，定理 2 说两种消元顺序总给出同一可生存像；这并不意味着两个方向互不耦合。

准确关系是：

1. **精确全局消元**总是路径独立，因为它始终从同一个终端解空间取像；
2. **局部贪心消元**可能失败，因为分别可提升不保证同时可提升；
3. 失败由 \(\chi_{r,k}\) 的非有效满射性检测；
4. 即便存在级无失败，\(\chi_{r,k}\) 的非可缩纤维仍保存高阶 Coupl；
5. 只有当每个相关 \(\chi_{r,k}\) 是等价时，两个方向才在完整结构上局部独立。

所以 Coupl 不是 Fubini 路径依赖，而是**局部摘要与精确可生存像之间的缺口**。

---

## 10. 一个最小反例

在集合中取

\[
S=\{*\},
\qquad
H=\{h\},
\qquad
P=\{p\},
\qquad
Q=\varnothing.
\]

则

\[
Z_h=Z_v=S,
\]

所以两个方向分别可提升；但

\[
Z_{hv}=\varnothing.
\]

此时

\[
C=H\times_S P=\{(h,p)\},
\qquad
\chi:Q\to C
\]

不是满射。

这个最小模型证明：仅凭两个单方向障碍分别为零，不能推出 simultaneous effectivity。任何一般定理都必须加入 \(\chi\) 的有效满射性、等价性，或等价的交换障碍消失条件。

---

## 11. 对 R3/Postnikov 比较的加强

R5 已证明两种完整塔在共同双滤过中给出同一最终分支空间。R8 增加三项内容：

### 11.1 角点级不变量

每个

\[
V_{r,k}^{R,N}

\]

都是“可延伸到完整解”的内在子对象，而不仅是某条计算路线的中间产物。

### 11.2 顺序独立

先做 matching 方向的反向筛除，再做 Postnikov 方向，或反过来，得到同一个角点可生存像。

### 11.3 局部交互测量

每个 \(\chi_{r,k}\) 精确测量一格内两个方向的 simultaneous-effectivity defect。R3 与 Postnikov 的“自然等价”因此不再只是终点等价，还带有局部交换缺陷数据。

---

## 12. 有限矩形的推广

对任意子矩形

\[
[r,r']\times[k,k']
\]

可把右上角 \(\mathcal S_{r',k'}\) 与其余边界兼容数据的同伦极限比较。记该比较映射为

\[
\chi_{[r,r']\times[k,k']}.
\]

则：

- 其 \((-1)\)-像给出该矩形边界数据可否被内部完整填充的普遍谓词；
- 它为有效满射，当且仅当所有兼容边界数据都有内部填充；
- 它为等价，当且仅当内部填充空间对每组边界数据可缩；
- 小方格 \(\chi_{r,k}\) 是最初级情形。

R9 完成了这里所需的 descent 证明，并修正本报告初稿中过于保守的判断：在**有限二维矩形**中，每个小方格比较映射都是有效满射，已经足以推出任意大矩形比较映射为有效满射；若小方格比较映射都是等价，则大矩形比较映射也是等价。

理由是：每个小方格比较映射恰是对应内部格点的 Reedy 匹配映射。沿下闭子集逐格附加时，每一步都是该匹配映射的基变换；有效满射与等价在基变换和有限复合下稳定。同伦拉回已经编码了二维重叠上的 coherence，不需要另加独立 cocycle 公理。

这一结论严格限于二维有限网格。在三维及以上，所有二维边际可填充不推出完整高阶匹配对象可填充；必须使用 punctured cube 的完整匹配映射。无限塔仍需独立的收敛与派生逆极限条件。

---

## 13. 理论含义

R8 产生一个领域独立的三层结构：

| 层次 | 规范对象 | 回答的问题 |
|---|---|---|
| 全局存在性 | \(V_{r,k}^{R,N}\) | 当前部分分支是否有完整未来？ |
| 局部同时有效性 | \(I_{r,k}\hookrightarrow C_{r,k}\) | 两个单方向提升能否共同实现？ |
| 高阶兼容性 | \(\operatorname{fib}(\chi_{r,k})\) | 共同实现的选择、变形与自同构是什么？ |

这比“两个障碍分别消失”严格更强，也比只比较最终解空间更细。

---

## 14. 已知性与新颖性边界

标准基础包括：

- 同伦拉回与兼容提升对；
- \((-1)\)-像和有效满射；
- 有限极限之间的交换；
- Moore–Postnikov 与 cellular obstruction theory。

本轮的新增派生结构是：

1. 在 R3/Postnikov 共同双滤过上定义角点可生存像；
2. 用像的结合律证明消元路径无关的 Obstruction Fubini Theorem；
3. 用 \(\chi_{r,k}\) 的有效满射/等价二分 simultaneous existence 与 full structural interchange；
4. 将 R7 的 residual cofiber 应用于交换缺陷，形成局部可计算压缩；
5. 把“小方格到大矩形”的问题隔离为一个有限 matching-descent 命题；R9 已证明该命题，并把真正的高阶边界定位在三维及以上。

这些结论的组成部分是标准的；当前没有证据可宣称整个定理包具有发表级新颖性。但它满足项目要求：陈述独立于具体领域、具有严格充要条件、能够产生反例与 no-go，并非用新术语重述单个经典定理。

---

## 15. 下一步：已由 R9 闭合并转向新方向

R9 已证明 **Coherent Interchange Descent Theorem**：有限二维矩形中，小方格比较映射的有效满射性足以推出全矩形存在级下降；小方格比较映射全为等价则推出结构级下降。

因此下一条可闭合路线转为：

1. 用有限差分与 cross-effect 分析非仿射 Coupl；
2. 证明何时高次 Coupl 可以有限分层，何时不能压成单一 cofiber；
3. 对 nilpotent 系数作用建立中心分层 obstruction tower；
4. 保持有限层结论与无限 actualization 的严格分界。

---

## 最终结论

精确的障碍消元满足 Fubini：

\[
\boxed{
V_{r,k}^{R,N}
=
\operatorname{im}_{-1}
(\mathcal S_{R,N}\to\mathcal S_{r,k})
}
\]

与从右上角走到 \((r,k)\) 的路径无关。

但局部独立零点不自动给出同时零点。其精确缺陷是

\[
\boxed{
\chi_{r,k}:
\mathcal S_{r+1,k+1}	o
\mathcal S_{r+1,k}
\times_{\mathcal S_{r,k}}
\mathcal S_{r,k+1}
}.
\]

\(\chi_{r,k}\) 有效满恰对应存在级交换；\(\chi_{r,k}\) 为等价恰对应完整高阶结构交换。由此，R3 matching 与 Postnikov obstruction 的相互作用获得了一个局部、自然、可基变换且可进一步压缩的精确载体。
