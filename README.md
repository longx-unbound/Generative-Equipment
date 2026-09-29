# Generative Equipment / 数学内生生成性

Generative Equipment 是一个开放的数学研究项目。

它研究一个核心问题：

> 数学结构自身如何产生问题、实现条件、障碍、修补与新的结构？

本项目当前特别关注一个实际方向：

> **能否帮助 AI 更可靠、更有创造性地思考数学。**

这里的目标不是让 AI 只做更多计算，而是帮助它更好地区分：

- 一个表示失败，与问题本身无解；
- 形式上相容，与真正可实现；
- 局部或有限阶段成立，与整体或无限阶段成立；
- 单点构造，与参数化、相干构造；
- 已证明、条件性结果、开放问题与已撤回结论。

## 从哪里开始

- 想先了解项目目的：阅读 [`AI_MATH.md`](AI_MATH.md)
- 想直接阅读完整数学理论：进入 [`theory/`](theory/)

## 理论文件

`theory/` 中保存的是 **Generative Equipment Consolidated 2026-09-29 / C1** 的完整原始内容。

开源整理没有修改这些理论文件的内容。原包中的主理论、定理账本、订正、领域应用、Frozen v1.0、source archive、registry、evidence 与验证脚本均保留。

建议严格阅读顺序：

1. `theory/00_README.md`
2. `theory/01_MASTER_THEORY.md`
3. `theory/02_THEOREM_LEDGER.md`
4. `theory/03_CORRECTIONS_AND_NO_GO.md`
5. `theory/05_SECTORS_AND_APPLICATIONS.md`

## 数学状态

本项目是持续发展的研究项目，而不是已经完成的通用数学创造算法。

理论内部使用以下状态区分不同结论：

`DEF / STD / DER / COND / REPORT / OPEN / RETRACT`

具体含义以 `theory/01_MASTER_THEORY.md` 和 `theory/02_THEOREM_LEDGER.md` 为准。

## License

本仓库采用 MIT License。详见 [`LICENSE`](LICENSE)。