# Generative Equipment / 数学内生生成性

Generative Equipment 是一个开放的数学研究项目，研究：**数学结构自身如何产生问题、实现条件、障碍、修补与新的结构？**

一个主要目标是帮助 AI 更可靠、更有创造性地思考数学。项目把表示与目标、形式与实际、有限与整体、逐点与相干、已证与待证的区别写成明确的数学接口。对 AI 数学能力的净提升仍需要实证评估。

## 快速入口

| 想了解什么 | 从这里开始 |
|---|---|
| 项目目的与 AI 数学方向 | [AI_MATH.md](AI_MATH.md) |
| 当前公开理论与阅读路线 | [理论导航](theory/README.md) |
| 完整理论 | [C1 总稿](theory/01_MASTER_THEORY.md) |
| 哪些结论可以使用、需要什么前提 | [定理账本](theory/02_THEOREM_LEDGER.md)与[订正表](theory/03_CORRECTIONS_AND_NO_GO.md) |
| 核心原始定义 | [Frozen v1.0 核心](theory/frozen_original/01_FROZEN_CORE.md) |
| 本仓库实际验证范围 | [仓库核对记录](docs/REPOSITORY_AUDIT_2026-10-01.md) |

## 版本与阅读优先级

| 层次 | 版本 | 地位与入口 |
|---|---|---|
| 冻结核心 | Frozen v1.0 · 2026-09-23 | [原始核心](theory/frozen_original/01_FROZEN_CORE.md)保持原文；[原始包](theory/evidence/Generative_Equipment_Frozen_v1_0_ORIGINAL.zip)保留 |
| 当前公开综合理论 | C1 · 2026-09-29 | [编纂入口](theory/00_README.md)：严格实现、派生结果、条件、订正和应用边界 |
| 历史材料 | Strict、GE-R、ENDO、Horizon 等 | [来源索引](theory/07_SOURCE_INDEX_AND_VERSION_MAP.md)负责追溯；归档不代表全部旧结论仍有效 |

Frozen v1.0 的核心是基础规范；派生结论使用 C1 的当前条件与订正。C1 不构成新的 Frozen 版本，也不静默改写冻结核心。

本仓库的 C1 公开整理版保留了源档案、Frozen 原始文件、登记数据和验证脚本；部分编纂正文已有公开编辑，合订文件也曾移除。因此不能把当前目录称为原 C1 压缩包的完整逐字节副本。原包校验清单仍保留，具体差异见[仓库核对记录](docs/REPOSITORY_AUDIT_2026-10-01.md)。

## 数学状态

理论区分七种状态：

- **DEF**：定义或数据契约
- **STD**：经典定理或标准推论
- **DER**：文稿给出可核对的派生证明，文献首创性另判
- **COND**：条件性结果，应用时必须验证前提
- **REPORT**：归档证据尚不足以完成独立核验的历史报告
- **OPEN**：待证接口或研究目标
- **RETRACT**：已撤回的结论或无效外推

详细使用规则见[C1 总稿 §1](theory/01_MASTER_THEORY.md)。文件完整性和有限回归通过，不等于全部数学证明已获认证；本项目也未建立通用数学创造算法或普遍的 AI 能力增益。

## 复核

在仓库根目录运行，使用 Python 3.10 或更新版本，无需额外 Python 库：

```sh
python3 theory/verify_package.py
python3 theory/source_archive/verify_r22_counterexample.py
python3 theory/evidence/verify_refinements.py
```

三项分别检查归档与登记一致性、一个指定的普通四重 Massey 反例、有限 DGLA 与闭包回归。第三项会重写其结果文件。原 C1 校验清单的已知差异、最新复核计数和未验证事项见[核对记录](docs/REPOSITORY_AUDIT_2026-10-01.md)。

## License

本仓库采用 [MIT License](LICENSE)。
