# 本次整理的核对报告
## C1 · 2026-09-29

## 1. 本次完成的范围

本次产物是主线的完整文档整理、状态归并和选定数学接口订正；不是对全部历史长证明的形式化认证。

已定位49个来源单元，原始Frozen压缩包及其8个成员文件保留。来源索引包含原名、相对路径、大小与SHA-256。经典输入另列20条文献定位，并明确哪些本次核对了关键内容、哪些仅保留原稿定位。

## 2. 实际执行的检查

### 原文与登记结构

`verify_package.py` 检查：49个源单元的字节/散列；冻结zip与8份解压成员逐字节一致；101条登记项ID唯一、状态有效、来源存在、所声明依赖无环；被标记为STD/DER/COND的条目不直接依赖REPORT/OPEN/RETRACT；所有形式化验证标志为false。

**注意：**它只检查登记的一致性。没有验证证明文本确实推出结论，也没有穷尽发现正文所有潜在未声明依赖。

### R22普通Massey单例

实际执行原始 `source_archive/verify_r22_counterexample.py`，验证原proper方程、非零受限曲率、非区间闭元修正和最终零曲率。原始stdout在 `evidence/r22_counterexample_run.txt`。

它只核验那个十边图的指定输入，不证明全空间形式性，也不是整个8顶点sector分类。

### DGLA与有限闭包的精确检查

实际执行 `evidence/verify_refinements.py`，只用Python标准库、整数和有理数算术。结果在 `evidence/refinement_results.json`：

| 检查 | 数量 |
|---|---:|
| d²在全部基上的恒等式 | 9 |
| graded skew基对 | 81 |
| differential derivation基对 | 81 |
| graded Jacobi基三元组 | 729 |
| MC曲率的独立稀疏多项式系数比较 | 9 |
| 四因子中全部singleton／higher-support选择模式 | 20,736 |
| 二元Boolean格上全部单调扩张映射 | 9 |
| 这些映射的闭包幂等性点检查 | 36 |

方程正规形和无限／任意系数层面的结论由附卷的纸面证明给出，不从样本外推。20,736模式仅是四变量支撑组合，不是20,736个不同DGLA。

## 3. 没有执行与没有认证的事项

没有重新执行旧96案例审计的随机300,000组测试、全部ENDO1/2/5历史回归，也没有执行512,000图ordinary分类。

没有取得512000报告对应的全量verifier和逐例见证，因此它是REPORT，不作为后续定理依据。保留的9/10边旧脚本和十边单例脚本不能替代它。

没有完成完整DHH依赖链、CP²-SNT、全部高阶符号版Massey规范化、拓扑推论的文献首创性审计；没有使用Lean等证明助理。

本次审核是同一研究协助过程中的自检与来源核对，不冒充独立审稿人结论。

## 4. 新增或明确收窄的关键接口

本次明确删除错误的mapping-truncation引理；区分cofiber与fibration同伦长正合列；将Horizon“已解决”的解释降为精确重述；指出缺陷子空间不一般协变；增加Sat-Eval与pointwise/coherent选择差别；保留safe laws不会自动制造violation的限制。

26项订正见 `03_CORRECTIONS_AND_NO_GO.md`。3条账本RETRACT不是说只有3项修订：许多修订已进入对应COND/DEF条目的前提与范围。

## 5. 当前结论

**原文归档与登记一致性可以复核；若干显式数学例子已经精确核验。**

这不等于“整个理论已经被证明正确”。本包最重要的质量改进，是把已证、标准、条件性、待证和历史报告分离，使下一步证明不会不知不觉继承旧外推。

复核命令：

```sh
python verify_package.py
python source_archive/verify_r22_counterexample.py
python evidence/verify_refinements.py
```

第一次命令不需要任何第三方库；后两项也是标准库程序。不要运行归档中的大规模历史脚本，除非单独确定输入范围与计算预算。
