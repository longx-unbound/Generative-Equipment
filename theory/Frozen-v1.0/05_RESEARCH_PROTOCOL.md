# 05 — Research Protocol After Freeze

## 1. Core Freeze Rule

未来每一轮研究先问：

\[
\boxed{
\text{新结果是否直接否定 Frozen Core 的某个声明？}
}
\]

如果没有，则：

- 不修改 core；
- 新结构放入 derived theory；
- 新领域条件记为 sector theorem；
- 新数值/obstruction记为 diagnostic。

---

## 2. 三种测试判定

### CORE PASS

新例子可由冻结核心自然表达，无需改 core。

### PASS + DERIVED STRUCTURE

核心正确，但发现：
- 新 obstruction；
- 新 rank；
- 新 spectrum；
- 新 sector theorem；
- 新 effectivity engine；
- 新 compression theorem。

这些进入派生理论，不升级 primitive。

### CORE FAIL

只有当例子导致：

\[
\text{core predicts }A
\quad\text{但数学严格给出 }\neg A
\]

时，才允许修改核心。

---

## 3. Predictive Power Standard

理论不能只做到“事后翻译”。

一个结果只有在至少满足下列之一时，才算 predictive progress：

1. **New necessary condition**  
   在未手工输入答案的情况下推出新的必要条件。

2. **New sufficient criterion**  
   给出跨领域可用的 realization / effectivity / representability 充分条件。

3. **New no-go**  
   排除某类此前看似可能的构造。

4. **New problem generation**  
   从理论结构自然提出 theory-independent、领域专家可直接研究的新问题。

5. **New reduction theorem**  
   把无限/复杂问题压缩到小的 test family 或 compact sector。

---

## 4. Anti-Tautology Discipline

以下情况不计作预测：

- 把目标 theorem 直接写进 \(\Omega\)；
- 为了得到答案事后选择 \(Q\)；
- 先知道 obstruction group，再把它定义成 residue；
- 事后挑 test shape 只为了复现已知证明；
- 把领域结论重新命名为“generative law”。

必须事前固定：

\[
\Xi,\quad P,\quad P^\sharp,\quad C,\quad N^\infty
\]

的来源。

---

## 5. Known-vs-New Discipline

必须明确区分：

### 经典数学
例如：
- adjoint functor theorem；
- Barr–Beck；
- Pro-categories；
- Brown representability；
- Schlessinger；
- Grothendieck existence；
- GAGA；
- Hasse–Minkowski；
- etc.

### 本理论的贡献候选
只能主张：
- 新的组织结构；
- 新的跨领域 bridge theorem（若确有证明）；
- 新的 no-go；
- 新的 theory-generated but theory-independent problem；
- 新的 obstruction/reduction derived from frozen axioms。

禁止把已知 theorem 重新包装后宣称为原创。

---

## 6. Preferred Next Research Directions

冻结后优先研究：

### A. Effectivity image characterization

给：

\[
C_\Xi:\mathsf{Actual}_\Xi\to\mathsf{Formal}_\Xi
\]

尝试刻画：

\[
\operatorname{EssIm}(C_\Xi).
\]

### B. Universal obstruction extraction

从 comparison functor 导出真正的 enriched/derived obstruction，而不是 scalar。

### C. Predictive test sectors

优先选可以穷举或控制的 sector：
- finite categories；
- finite posets；
- finite simplicial sets；
- low Postnikov stages；
- finite-dimensional toric/fan combinatorics；
- small algebraic examples。

### D. New theory-independent problems

理论若提出问题，问题本身应能脱离本理论独立表述。

Toric IH Image Problem 属于此类。

---

## 7. Modification Protocol

若确实发现 CORE FAIL：

1. 记录反例；
2. 指明被否定的精确 statement；
3. 不修改无关部分；
4. 提出最小 repair；
5. 用至少三个不同 sector 重新测试 repair；
6. 通过后才发布 Frozen v1.1。

否则 Frozen v1.0 保持不变。
