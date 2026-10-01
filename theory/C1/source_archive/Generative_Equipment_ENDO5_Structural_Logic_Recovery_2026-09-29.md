# Generative Equipment — ENDO-5
## 哪些数学 sector 能从自身恢复 law universe？
### 模型范畴重建、内在逻辑能力与不可遗漏的结构数据

日期：2026-09-29。  
状态：新派生研究分支；不修改 Frozen v1.0。  
前置：ENDO-4、ENDO-3 v1.2；本稿的正面结果不依赖其尚未验证的普适性解释。  
范围：普通有限乘积/有限极限/正规逻辑、局部有限可表示范畴、指定基数的可达无穷范畴、拓扑斯、特征零形式变形与度量语义。  
证明地位：本文给出可直接证明的引理、若干经典重建定理的证明或准确调用，以及明确反例。未作证明助理形式化；不宣称这些经典理论或本综合具有已确认的文献原创性。

---

## 0. 总结

对问题“哪些 sector 自身能规范地产生其 law universe / institution”，答案不是一律能或不能。

最强的正例是：

1. **局部有限可表示模型范畴 K**：自身的有限可表示对象给出小有限极限理论 `T_K=(K_fp)^op`，并重建 `K ≃ Lex(T_K,Set)`。无需预先指定一个忘却函子或某个具体公理表。
2. **带原生载体函子的有限代数 sector (K,U)**：当 U 是有限元单子的单子性函子时，可由全部自然运算恢复 Lawvere 理论。它恢复的不只是哪些恒等式成立，还包括有哪些有限元运算。
3. **有限极限/正规/拓扑斯 sector C**：子对象、拉回、像、伴随及幂对象决定所支持的内部逻辑片段；量词可由伴随的泛性质强迫，而不是逐个任意指定。
4. **可达无穷范畴**：指定可达基数后，完整的紧对象及其映射空间重建语义；不能只保留同伦范畴或分次不变量。
5. **形式变形 sector**：完整的形式模问题在适当基域/参数对象假设下恢复控制 dg Lie 对象；一般 operadic 版本由参数运算的 Koszul 对偶决定控制语言。但“只有切复形”远远不足。
6. **度量 sector**：保留度量值域与距离后有规范的定量谓词语义；忘掉距离、只留拓扑或底集合，不可能恢复相应定量法律。

这些结论并不挑选所有可能逻辑中的唯一“正确逻辑”。它们建立：**某个由输入自身识别的语义结构，确实决定一个可解释、可运输、在若干 sector 中还可重建全部模型的逻辑语言。**

本文最重要的修正：此前用“同一个结构能使用多种逻辑”来支持一般规范构造不存在，论证过强。多种自然输出可以共存。准确的否定结论是：**忘掉会改变待恢复语言的信息后，不能要求一个恢复器同时忠实恢复所有被忘掉的选择。**

---

## 1. 四个对象必须分开

### 1.1 结构签名

例如一个单排序代数签名，包括运算符及其元数；或者指定的正合结构、张量、显示映射类。

### 1.2 可表达语言

包括项、公式、变量上下文、允许的逻辑联结词、量词及变元替换。

### 1.3 理论

语言中的一个定律集或其语义闭包。ENDO-4 的 `Theta*=Th(X*)` 属于这一层。

### 1.4 Institution

严格说，一个 institution 需要：

- 签名范畴 `Sign`；
- `Sen:Sign→Set`；
- `Mod:Sign^op→Cat`；
- 满足关系，且对每个签名映射 h:S→S' 满足

\[
M'\models_{S'}\operatorname{Sen}(h)(\varphi)
\iff
\operatorname{Mod}(h)(M')\models_S\varphi.
\]

单个 `(models,sentences,models-relation)` 只是 satisfaction system，不应因为有 Th–Mod Galois connection 就称为已经恢复整个 institution。[B1]

本文区分三个正面等级：

- **解释级**：逻辑操作由输入决定；
- **institution 级**：签名变化、模型约化和满足条件也已定义；
- **重建级**：由生成的语言可恢复原模型范畴。

它们不能相互替代。

---

## 2. SG1：从原生载体函子恢复所有有限元运算

设 `U:K→Set` 有左伴随 `F`。对有限集合 n，记自由对象为 `F(n)`。

定义 n 元自然运算

\[
\operatorname{Op}_U(n)=\operatorname{Nat}(U^n,U).
\]

### 定理 SG1.1：自然运算恢复

\[
\boxed{\operatorname{Op}_U(n)\cong U(F(n)).}
\]

### 证明

伴随给出

\[
U(X)^n\cong\operatorname{Hom}_K(F(n),X).
\]

因此 U^n 是可表示函子。对这个可表示函子使用 Yoneda：

\[
\operatorname{Nat}(U^n,U)
\cong U(F(n)).
\]

具体地，自然运算 theta 对自由生成元的取值 `w=theta_{F(n)}(x_1,...,x_n)` 决定它。在任意 X 中给定元组 `(a_1,...,a_n)`，唯一的自由延拓 f:F(n)→X 满足

\[
\theta_X(a_1,\ldots,a_n)=U(f)(w).
\]

反之任意 w 定义这样一个自然运算。证毕。

### 定义 SG1.2：恢复的理论

\[
T_U(n,m)=\operatorname{Nat}(U^n,U^m)
\cong\operatorname{Hom}_K(F(m),F(n)).
\]

复合就是自然变换复合，即运算代入；`n+m` 是对象 n,m 的乘积，0 是终对象。

### 定理 SG1.3：有限代数语义恢复

若 U 单子性，且 `UF` 保持滤过余极限，则

\[
\boxed{K\simeq\operatorname{FP}(T_U,Set)}
\]

并与 U 相容。这是有限元单子与 Lawvere 理论的经典对应 [B2]。

因此输入 `(K,U)` 产生全体运算、代入、恒等式语义和模型，而非只为预先指定的运算寻找公理。

### 群例子

对群的原生底集合函子，`U(F(n))` 是 n 个字母的自由群。所以全部自然 n 元群运算恰好是群字运算。无需先挑选乘法、逆元、单位这一组生成符号；这些只是整个理论的一组有限呈现。

### 必要边界：Top 的失败

对 `U:Top→Set`，左伴随是离散空间函子。故 `U(F(n))=n`，恢复出的有限元运算只有投影，和 Set 完全相同。

于是自然有限元运算语言重建的是 Set，不能重建 Top。U 不是单子性；其诱导单子是恒等单子。

这证明：**“有自由对象”与“所有自然有限元运算可写出”不足以保证完整语义恢复。**

---

## 3. SG2：不指定 U，也可以从局部有限可表示范畴恢复语言

设 K 是局部有限可表示范畴。令 A 是其全部有限可表示对象的一个小骨架：

\[
A\simeq K_{\mathrm{fp}},\qquad T_K=A^{op}.
\]

“有限可表示”由 Hom 保持滤过余极限定义，是范畴等价不变量。

### 定理 SG2：有限极限语言恢复

1. A 对有限余极限封闭，T_K 有有限极限。
2. 评价函子给出等价

\[
\boxed{
K\simeq\operatorname{Lex}(T_K,Set),
\quad
X\longmapsto \operatorname{Hom}_K(-,X)|_A.
}
\]

3. 若 K≃K'，则 T_K≃T_K'，相应评价等价可交换。

这是 Gabriel–Ulmer 对偶的核心结果 [B3,B4]。

### 证明

**有限余极限。** 对有限图 a_i，

\[
\operatorname{Hom}(\operatorname{colim}_i a_i,-)
\cong\lim_i\operatorname{Hom}(a_i,-).
\]

Set 中有限极限与滤过余极限交换，所以该有限余极限仍有限可表示。

**重建本质满性。** 给定 `H:A^op→Set` 保持有限极限，考虑其元素范畴 El(H)。

它非空，因为 A 的初对象 0 满足 H(0)=*。两点 `(a,x),(b,y)` 可由 `a⊔b` 上对应 `(x,y)` 的元素共同支配。对两条平行元素范畴态射，A 中的余等化子与 H 对有限极限的保持性给出共同等化的后续对象。因此 El(H) 滤过。

令

\[
X_H=\operatorname{colim}_{(a,x)\in\operatorname{El}(H)}a.
\]

对 b∈A，由有限可表示性和预层的元素余极限表示，

\[
\operatorname{Hom}(b,X_H)
\cong\operatorname{colim}_{(a,x)}\operatorname{Hom}(b,a)
\cong H(b).
\]

**全忠实。** 每个 X 是有限可表示对象的滤过余极限；在这些对象上的相容自然变换唯一延拓成 X→Y。等价地，A 是稠密子范畴。

最后，范畴等价保持滤过余极限、有限可表示性及所有相关 Hom，故得到第三项。证毕。

### 具体语言如何写出？

由 T_K 产生一个完整有限极限 sketch：每个对象为一个 sort，每个态射为一个操作；保留全部复合、恒等关系及有限极限锥。模型恰好为 Lex(T_K,Set)。

其“逻辑”是 cartesian/有限极限逻辑，允许有唯一见证的有限方程系统，而不自动包括任意存在、否定、全称等构造。

### 这解决与没有解决什么

解决：从整个模型范畴反推一套可重建它的有限极限语言，无需事先指定单排序 carrier。

没有解决：唯一恢复某种人类最喜欢的原始符号、原始 sorts 及依赖结构；也没有证明它是该模型范畴唯一有用的逻辑。

例如 Grp、R-Mod、图、小范畴等局部有限可表示 sector 都适用。但单个群或单个模不是整个 K，不能直接用这一结论。

---

## 4. SG3：从子对象与伴随产生内部逻辑

设 C 有有限极限。构造规范的子对象纤维

\[
\operatorname{Sub}_C:C^{op}\to Pos.
\]

对象 X 是上下文，子对象 P↪X 是谓词，f:X→Y 的拉回 f* 是代入。

已经强迫出现：

- 真：`id_X`；
- 合取：子对象拉回交；
- 等号：对角 `X→X×X`；
- 代入：沿态射拉回。

### 定理 SG3.1：正规范畴的存在量词

若 C 正规，则

\[
\exists_f(P)=\operatorname{im}(P\hookrightarrow X\xrightarrow fY)
\]

满足

\[
\boxed{\exists_f\dashv f^*.}
\]

且满足 Frobenius 和拉回方块的 Beck–Chevalley 公式。

### 证明

像的最小子对象性质给出

\[
\exists_f(P)\le Q
\iff f\circ P\text{ 因子分解经过 }Q
\iff P\le f^*Q.
\]

正规范畴中像分解沿拉回稳定，因此像与参数代换交换，得到 Beck–Chevalley。把 Q↪Y 的拉回与 P 的像分解组合，同样得到

\[
\exists_f(P\wedge f^*Q)=\exists_f(P)\wedge Q.
\]

证毕。

### 定理 SG3.2：量词与逻辑操作的非任意性

在固定的 Sub(C) 与 f* 上，如果左伴随或右伴随存在，它们唯一；在子对象偏序中是逐点相等，而不只是非规范同构。

因此若 f* 有右伴随并满足所需参数代换相容性，则全称量词被决定：

\[
\boxed{\exists_f\dashv f^*\dashv\forall_f.}
\]

若 `P∧-` 有右伴随，则蕴含 `P⇒-` 被决定。

证明是伴随唯一性。例如两个左伴随 L,L' 对每个 P,Q 满足同一等价 `LP≤Q iff P≤f*Q iff L'P≤Q`，故 LP=L'P。

### 逻辑能力表

| 已有结构 | 被支持的内部语义 |
|---|---|
| 有限极限 | 代入、等号、真、有限合取 |
| 正规像且拉回稳定 | 存在量词 |
| 拉回稳定的有限并，包括空并 | 析取与假；coherent logic |
| 子对象 Heyting 结构、相应右伴随及 Beck–Chevalley | 蕴含、全称；相应 intuitionistic predicate fragment |
| elementary topos 的子对象分类器与幂对象 | 直觉主义高阶内部逻辑 |
| Boolean topos | 该内部逻辑中排中律成立 |

这里采用经典范畴逻辑的量词-伴随语义 [B5]。不同能力不必构成一个严格线性层级；尤其不能由“范畴有很多极限”直接推出所有子对象纤维都是 Heyting 代数。

### 定理 SG3.3：等价运输

范畴等价 E:C≃D 诱导子对象偏序的自然等价，保存可用的上述逻辑操作。

原因：等价保持单态、拉回、像及所有有关泛性质；伴随唯一性强迫逻辑操作相容。需要 Beck–Chevalley 的位置仍使用原结构对它的证明，而不是由“伴随存在”无条件推断。

---

## 5. 内部谓词逻辑不是外部模型逻辑

### 明确反例：二维向量空间的子空间格

令 V=F_2^2，三个不同直线为 L1,L2,L3。则

\[
L_1\cap(L_2+L_3)=L_1,
\]

但

\[
(L_1\cap L_2)+(L_1\cap L_3)=0.
\]

因此 Sub(V) 非分配，不能是 Heyting 代数。

甚至对固定直线 L1，映射 `L1∩-` 没有到 0 的右伴随值：与 L1 交为 0 的候选包含 L2,L3，却没有最大的候选。

所以模范畴虽然是阿贝尔且正规，天然子对象语义一般只支持正规逻辑，而非全部 coherent/Heyting 逻辑。

这与在 Set 中使用经典一阶逻辑研究“所有模”不冲突：后者使用任意可定义子集和外部赋值；内部 Sub(R-Mod) 只使用线性子对象。

**语言恢复时必须说明是在恢复模型的外部描述语言，还是数学世界自己的内部谓词逻辑。**

---

## 6. SG4：从生成的语义得到真正的 institution

为了避免“给出一个 hyperdoctrine 就声称产生整个 institution”，给出一个完整的构造。

固定一个正规语义目标 E。定义：

- Sign：小正规范畴及正规函子；
- Sen(T)：三元组 `(X,P,Q)`，其中 P,Q∈Sub_T(X)，解释为 sequent `P⇒Q`；
- Mod_E(T)：正规函子 T→E 及其自然变换；
- 对 h:T→T'，句子沿 h 运输子对象，模型通过预复合 h 约化；
- `F ⊨ (X,P,Q)` 当且仅当 `F(P)≤F(Q)`。

### 定理 SG4：institution 满足条件

对 h:T→T'、F':T'→E，

\[
F'\models\operatorname{Sen}(h)(X,P,Q)
\iff
F'\circ h\models(X,P,Q).
\]

### 证明

两侧都断言 `F'(hP)≤F'(hQ)`。正规函子保持单态、拉回和像，因而子对象运输良定义，并与正规公式构造相容。证毕。

类似地，小有限乘积理论或有限极限理论、相应保持结构的模型函子、平行箭头相等的句子也组成 institution。

这个构造没有逐个指定需要哪些谓词：所有原生子对象都进入语言。但固定目标 E、采用哪一类结构保持函子，仍是公开的语义契约。

因此本稿不仅构造一个闭理论，还在这些 sector 中明确给出签名范畴、模型约化和满足条件。

---

## 7. 更细的依赖语言：修补结构本身可以成为语言恢复数据

Gabriel–Ulmer 从模型范畴恢复有限极限理论，但并不恢复所有依赖排序信息。

Frey 的 clan 对偶 [B4] 给出一个重要的精确扩展：在论文刻画的 clan-algebraic 条件下，局部有限可表示范畴**加上适当的弱分解系统**，反向恢复 Cauchy 完备 clan，即一种依赖代数理论的分类表示。

不能把这说成“任意弱分解系统都决定完整类型论”。需要保留该文的密度、正合性等条件。

### 自然对照：两种图语言

无依赖版本有两个 sorts V,E 和源靶 s,t:E→V；依赖版本有 V 及每对顶点上的 sort E(x,y)。它们的模型范畴都等价于有向图范畴。

但是它们引入自由边的方式不同：

- 一种自由边同时带来端点；
- 另一种把给定端点作为已存在上下文，再加入一条边。

Frey 精确展示这种差异由模型范畴上的不同弱分解系统反映。

**对 ENDO 的意义：**某些 ENDO-3 的提升/修补结构，不只是给定语法后的工具；在满足已知对偶定理的 sector 中，它们能反向恢复依赖语法的一部分。这是一个真正的结构桥梁，而非把“依赖”换个名字。

---

## 8. SG5：同伦 sector 必须恢复高阶探针语言

设 C 是 kappa-accessible 的无穷范畴，kappa 为一个指定的可达正则基数。令 A=C^kappa 为全部 kappa-紧对象的小代表。

经典可达性重建给出 [B6, §§5.3.5,5.4.2]

\[
\boxed{C\simeq\operatorname{Ind}_{\kappa}(A).}
\]

重建使用

\[
X\longmapsto\operatorname{Map}_C(-,X)|_A,
\]

其中全部映射空间及复合相干性都保留。

若 C 紧生成，kappa=omega 可以使用；一般 presentable C 需要选一个可达基数，不能声称有语法无关的唯一紧性尺度。

这个结果恢复的是高阶测试/图式语义。它没有自动给出唯一严格的类型论语法、唯一 universe hierarchy，或者某个偏好的 horn generator presentation。

### 无穷拓扑斯的更强正面结构

在无穷拓扑斯中，可使用完整 slice 语义：

\[
\mathsf{Type}(X)=C_{/X}.
\]

拉回是代入，复合给依赖和，局部笛卡尔闭性给依赖积：

\[
\Sigma_f\dashv f^*\dashv\Pi_f.
\]

它提供真正 proof-relevant 的依赖逻辑语义。把它严格编译成某个具体语法系统，以及加入大小受限 universe，仍需要相应模型/大小选择 [B6]。

---

## 9. SG6：稳定无穷范畴的子对象逻辑退化

### 定理 SG6

在稳定无穷范畴 C 中，每个单态都是等价。因此

\[
\boxed{\operatorname{Sub}_C(X)\simeq *}
\]

对每个 X 成立。

### 证明

设 f:X→Y 是单态，F=fib(f)。对每个 Z，Map(Z,f) 是空间中的单态，即其同伦纤维为空或可缩。

在零映射上取纤维，得到 Map(Z,F)。它至少包含零映射，因此非空，必可缩。对全部 Z 均如此，Yoneda 给出 F≃0。

稳定范畴中纤维为零等价于 f 为等价。反向显然。证毕。

### 含义

不能把普通 Sub-doctrine 直接当作 D(R)、谱或稳定同伦论的完整法律语言。它在这些世界里根本分不出对象。

可行替代是完整紧对象 nerve、谱丰富化、slice/依赖数据，或者明确给定 t-structure 后的心及其子对象。t-structure 一般不是从裸三角结构唯一决定。

这个反例把“哪些逻辑适合哪些 sector”从文化偏好变成了可验证的非退化条件。

---

## 10. 形式变形：控制语言可恢复，但不是从一阶数据恢复

固定特征零域 k，以及合适的增广 Artin 交换 dg / E_infinity 参数对象。

Lurie–Pridham 的等价给出 [B7]

\[
\boxed{\mathsf{FMP}_k\simeq\mathsf{dgLie}_k[\mathrm{qis}^{-1}].}
\]

因此完整形式模问题 F 恢复控制 dg Lie 对象，唯一性是导出等价意义下的唯一性；不是选定一个严格括号表。

### 一阶信息不够：直接反例

令 g0、g1 具有相同的分次向量空间

\[
g^1=ka\oplus kb,\qquad g^2=kw,\qquad d=0.
\]

g0 的括号全零。g1 只有

\[
[a,b]=[b,a]=w,
\]

且 w 为中心。所有嵌套括号为零，故 Jacobi 恒等式成立。

两者的切复形相同。但在

\[
B=k[\varepsilon,\eta]/(\varepsilon^2,\eta^2)
\]

上，`a epsilon+b eta` 在 g0 中满足 MC 方程；在 g1 中曲率是

\[
w\varepsilon\eta\ne0.
\]

加任意 `(pa+qb)epsilon eta` 也不能改变这个曲率，因为 d=0 且其与其它正参数项相乘均为零。

所以相同切复形并不确定相同变形规律。

### 控制 Lie 语言为什么出现？

更准确的答案是：交换 Artin 参数语义与 Lie 语义之间存在 Koszul 对偶。

在 Calaque–Campos–Nuiten [B8, Theorem 1.1] 的明确假设下，特征零、非正上同调次数的二元二次 Koszul operad P 所定义的形式模问题，对应其 Koszul 对偶 P! 的代数，带文中规定的移位。

因此“参数侧运算类型”能够强迫“控制侧运算类型”。这是真正的结构诱导语言，但 P 与参数语义仍是输入。正特征时不能直接沿用 dg Lie；partition Lie 理论提供相应替代 [B9]。

---

## 11. 度量与分析：有明确的定量正例，不只是覆盖空白

给定普通对称度量空间 (X,d)，且距离有限。令

\[
\mathsf{Pred}_1(X)=\{f:X\to\mathbb R: |f(x)-f(y)|\le d(x,y)\}.
\]

它是由度量自身定义的全部 1-Lipschitz 实值谓词。阈值判断可写为 f(x)≤r。

### 定理 SG7：度量谓词恢复

\[
\boxed{
d(x,y)=\sup_{f\in\mathsf{Pred}_1(X)}|f(x)-f(y)|.
}
\]

### 证明

上界是 Lipschitz 定义。固定 x，函数 f_x(z)=d(z,x) 为 1-Lipschitz，且 `|f_x(x)-f_x(y)|=d(x,y)`，给出下界。证毕。

这表明完整定量谓词是非退化且具有恢复能力的。Lawvere 的度量丰富化理论 [B10] 将距离值解释为丰富化 hom、组合解释为三角不等式。

### 不可删去的信息

同一两点集合可取距离 1 或 2，底集合和拓扑相同，但阈值 `d(x,y)<3/2` 的真值不同。

因此只给底集合或拓扑，不能忠实恢复两种度量语义；必须保留距离、值域和单位/丰富化契约。

本节不证明一般 Banach 或 PDE 的最佳逻辑可规范恢复，也不证明 coercivity、紧性、边界条件会被自动发现。

---

## 12. 精确的否定结果：忘却信息障碍，而不是“没有规范逻辑”

设 V:D→B 忘掉某些结构，目标恢复量为 Q:D→L。

若存在 d1,d2 满足 Vd1≃Vd2，而 Qd1 与 Qd2 在所要求的结构意义下不等价，则不存在 R:B→L 以及相容自然等价 `R V≃Q` 同时恢复全部输入。

证明：R 会把等价底数据送成等价输出，与 Qd1≄Qd2 矛盾。

适用例子：

- 忘掉原生载体/生成对象后，不能一般恢复指定单排序代数呈现；同一模范畴的不同生成对象产生不同矩阵环呈现。
- 忘掉指定覆盖后，不能一般恢复指定的层语义。
- 忘掉显示映射/弱分解系统后，不能恢复全部依赖排序信息。
- 忘掉高阶映射与括号后，不能恢复完整同伦/变形规律。
- 忘掉距离后，不能恢复定量阈值规律。

但这**不**排除从底数据构造另一个有用的规范逻辑。Gabriel–Ulmer 和子对象 doctrine 已经提供正例。

同样，存在 equational、Horn、first-order 等多种语言，不能单独证明不存在 canonical language construction；它只表明“唯一适合所有目标的逻辑”尚未由这些数据决定。

---

## 13. 对 ENDO-4 的接合：内部解释、模型重建与真正的修补输入

### 13.1 本轮减少了什么外部选择

在 SG2 范围内，ENDO-4 的 law universe 可以从 K 的有限可表示对象提取，而不是另行填写句法符号表。

在 SG3 范围内，谓词、合取、等号、可用的量词由子对象与伴随决定。

随后可以在所选小模型范围内运行 ENDO-4 的 `Th–Mod` 及 continuation 闭包。

### 13.2 仍需分开 continuation 与语义完成

`Mod(Th(X))` 可能包含并非由原结构操作直接构造出来的模型。它是所选语言允许的语义完成，不是“每个新增模型都有实际构造路径”的定理。

### 13.3 描述性真理不能自动变成有缺陷的目标约束

ENDO-4 有

\[
X_0\subseteq X^*,\qquad\Theta^*=Th(X^*).
\]

因此

\[
\forall M\in X^*,\quad M\models\Theta^*.
\]

所以针对 X* 内模型运行同一满足关系的“违反 Theta*”编译器，没有非空缺陷可以发现。

非平凡 ENDO-3 修补必须来自：拟议扩张不在 X* 内、结构运输不保既定规律、尚未实现的见证/相干性目标，或另一个明确的规范性约束。不能从安全描述理论本身自动推出必有新的修补步骤。

这不否定 ENDO-4 的 Galois 定理；它限定了“闭理论自动驱动创造”的解释。

---

## 14. Law-Universe Recovery Certificate

以后每个声称“sector 自身产生语言”的结果，应给出五项可核验数据：

1. **输入**：整个模型范畴、单个对象、忘却函子、enrichment、显示映射、基数等究竟哪些已经给定？
2. **提取对象**：有限可表示对象、自然运算、Sub-fibration、紧探针、完整形式模问题等。
3. **解释/满足**：怎样给出项、谓词、句子、模型和约化？
4. **充分性**：仅提供 sound interpretation，还是全忠实观察，或能恢复全部模型范畴？
5. **运输与边界**：对什么等价自然，忘掉什么数据以后必然失败？

这是一种研究证书格式，不是另加一个冻结公理。

| Sector | 足够输入 | 规范输出 | 准确强度 |
|---|---|---|---|
| 有限单子代数 | (K,U)，U 有限元单子性 | 全部自然运算与 Lawvere 理论 | 重建模型；依赖 U |
| 局部有限可表示 | 整个 K | (K_fp)^op 的有限极限语言 | 不需 U；重建级 |
| 正规范畴 | C 的有限极限与正规性质 | Sub、代入、像/存在 | 内部正规语义；可构成 institution |
| elementary topos | 完整范畴结构 | 分类器、幂对象、量词 | 高阶直觉主义内部语义 |
| clan-algebraic | K 及合适 WFS | 依赖代数 clan | 指定理论范围内的对偶恢复 |
| 可达无穷范畴 | C 及可达 kappa | 完整 kappa-紧 probe 语言 | 高阶语义重建；非严格句法唯一性 |
| 无穷拓扑斯 | 完整高阶范畴 | slice、Sigma/Pi、依赖语义 | 高阶解释；universe 大小仍须选定 |
| 形式变形 | 参数代数种类、基域、完整 FMP | dg Lie 或 Koszul 对偶控制器 | 控制语义重建，不由切复形决定 |
| 度量 | (X,d) 及值域 | 非扩张定量谓词 | 恢复距离；不是通用 PDE institution |
| 只给单个裸对象 | 过少 | 一般不能恢复上述全部输出 | 必须查明缺失数据 |

---

## 15. 实际执行的有限回归

脚本 `verify_endo5.py` 使用 Python 标准库和精确整数算术，没有随机采样。

实际结果见 `validation_results.json`：

- 有限 Set 上的左右量词伴随检查：4886；
- Frobenius 检查：2443；
- 有限拉回上的 Beck–Chevalley 检查：338；
- F2^2 的 5 个子空间，125 个分配律三元组中得到预期的 6 个反例；
- 相同切复形的两 dg Lie 模型，25 个顶系数选择中，非阿贝尔曲率恒不消失；
- 729 个四顶点带权完全图输入，经最短路化后检查 46656 次距离谓词 Lipschitz 条件和 11664 次距离恢复公式。不同输入可给出同一个度量，未把它们称作 729 个不同度量空间。

这些检验不证明 Gabriel–Ulmer、形式模问题对偶等一般定理；也不证明文献原创性。一般结论由本文证明和所列文献支持。

---

## 16. 最终研究结论

“语言从数学结构自身产生”在多个自然 sector 中已经有严格正面答案，但有两条主要路线：

\[
\boxed{
\text{模型范畴}\to\text{内在可表示/紧对象}\to\text{重建型语言}
}
\]

与

\[
\boxed{
\text{上下文与谓词纤维}\to\text{代入}\to\text{存在的伴随}\to\text{内部逻辑操作}.
}
\]

变形对偶、clan/WFS 对偶和丰富化度量语义为这些机制提供不同的结构增强。

本项目不应再只重复“law universe 是外部选择”，也不应宣称已经产生唯一的普适逻辑。应逐 sector 提供恢复证书，并研究哪些结构正好足以支撑所需表达能力。

最确定的推进是：**在局部有限可表示与正规/拓扑斯 sector，语言的一大部分不再需要逐项指定；它能由原模型范畴或原有替换结构恢复。**

---

## 参考文献（经典基础与原始研究）

[B1] J. A. Goguen and R. M. Burstall, *Institutions: Abstract Model Theory for Specification and Programming*. 原作者公开稿：
https://cseweb.ucsd.edu/~goguen/pps/ins.pdf

[B2] F. W. Lawvere, *Functorial Semantics of Algebraic Theories*, thesis, 1963; TAC reprint 5, 2004. 尤其自然运算与语义重建。
https://tac.mta.ca/tac/reprints/articles/5/tr5.pdf

[B3] P. Gabriel and F. Ulmer, *Lokal präsentierbare Kategorien*, Lecture Notes in Mathematics 221, 1971. 本文对核心重建给出证明；亦见 [B4] 导言中的准确对偶陈述。

[B4] Jonas Frey, *Duality for Clans: an Extension of Gabriel–Ulmer Duality*, arXiv:2308.11967, v2. 导言及主对偶，clan-algebraic 假设不可删除。
https://arxiv.org/html/2308.11967v2

[B5] F. W. Lawvere, *Adjointness in Foundations*, 1969; TAC reprint 16, 2006.
https://tac.mta.ca/tac/reprints/articles/16/tr16.pdf

[B6] J. Lurie, *Higher Topos Theory*, §§5.3.5, 5.4.2, 6.1. 尤其 Ind 的全忠实/本质满判据及可达性重建。
https://people.math.harvard.edu/~lurie/papers/HTT.pdf

[B7] J. Lurie, *DAG X: Formal Moduli Problems*, Theorem 2.0.2. 使用特征零及完整高阶参数语义。
https://www.math.ias.edu/~lurie/papers/DAG-X.pdf

[B8] D. Calaque, R. Campos and J. Nuiten, *Moduli problems for operadic algebras*, arXiv:1912.13495, Theorem 1.1 及相应更一般有条件版本。
https://arxiv.org/html/1912.13495

[B9] L. Brantner and A. Mathew, *Deformation Theory and Partition Lie Algebras*, arXiv:1904.07352.
https://arxiv.org/abs/1904.07352

[B10] F. W. Lawvere, *Metric Spaces, Generalized Logic, and Closed Categories*, 1973; TAC reprint 1, 2002.
https://tac.mta.ca/tac/reprints/articles/1/tr1.pdf
