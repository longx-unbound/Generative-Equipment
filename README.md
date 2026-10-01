# Generative Equipment / 数学内生生成性

Generative Equipment 是一个开放的数学研究项目，研究：**数学结构自身如何产生问题、实现条件、障碍、修补与新的结构？**

一个主要目标是帮助 AI 更可靠、更有创造性地思考数学。项目把表示与目标、形式与实际、有限与整体、逐点与相干、已证与待证的区别写成明确的数学接口。对 AI 数学能力的净提升仍需要实证评估。

## 快速入口

| 想了解什么 | 从这里开始 |
|---|---|
| 当前公开理论 | [C2 说明](theory/C2/00_README.md)与[数学理论](theory/C2/01_C2_THEORY.md) |
| C2 的证明边界与有限测试 | [严格评估和测试](theory/C2/02_EVALUATION_AND_TESTS.md) |
| 用于 AI 数学工作的协议与实验设计 | [C2 AI 数学创造协议](theory/C2/03_AI_CREATIVITY_PROTOCOL.md) |
| 项目目的与 AI 数学方向 | [AI_MATH.md](AI_MATH.md) |
| C1、Frozen 与历史材料 | [理论导航](theory/README.md) |
| 本次发布与实际验证范围 | [C2 发布核对](docs/C2_PUBLICATION_2026-10-01.md) |

## 版本与阅读优先级

| 层次 | 版本 | 地位与入口 |
|---|---|---|
| 冻结核心 | Frozen v1.0 · 2026-09-23 | [原始核心](theory/frozen_original/01_FROZEN_CORE.md)保持原文；[原始包](theory/evidence/Generative_Equipment_Frozen_v1_0_ORIGINAL.zip)保留 |
| 当前派生工作版本 | C2 · 2026-09-30 | [完整入口](theory/C2/00_README.md)：六个派生模块、限定证明、评估与 AI 工作协议 |
| 继承的严格工作层与领域附卷 | C1 · 2026-09-29 | [编纂入口](theory/00_README.md)、[定理账本](theory/02_THEOREM_LEDGER.md)与[订正表](theory/03_CORRECTIONS_AND_NO_GO.md) |
| 历史材料 | Strict、GE-R、ENDO、Horizon 等 | [来源索引](theory/07_SOURCE_INDEX_AND_VERSION_MAP.md)负责追溯；归档不代表全部旧结论仍有效 |

C2 保留 Frozen v1.0 的核心，在 C1 的严格工作层上补充丰富化、相对残差、实现尺度、信息压缩、量词提升和问题选择。它不是新的 Frozen 版本，也不把原有领域报告升级为定理。使用继承的领域结论时，仍须查阅 C1 的前提、证据状态与订正。

## 文件结构与来源

- `theory/C2/`：原始 C2 包的全部 8 个文件，按包内结构原样发布
- `theory/` 中既有编号正文、`registry/`：C1 公开整理版，保留原路径
- `theory/frozen_original/`、`theory/source_archive/`、`theory/evidence/`：Frozen 原文、历史源档案与证据包
- `docs/`：发布核对、快照校验清单和独立保存的本次复核输出

本仓库的 C1 公开整理版已有历史编辑，且合订文件曾被移除；它不是原 C1 压缩包的完整逐字节副本。[C1 核对记录](docs/REPOSITORY_AUDIT_2026-10-01.md)和原校验清单继续保留。本次 C2 8 文件则与[C2 原始 ZIP](theory/evidence/Generative_Equipment_C2_2026-09-30.zip)逐字节一致；包内 Frozen 核心也与既有 Frozen 核心相同。

## 数学与证据状态

C1 的 DEF、STD、DER、COND、REPORT、OPEN、RETRACT 七种状态及使用规则见[C1 总稿 §1](theory/01_MASTER_THEORY.md)。C2 的每条命题按其注明的范围、假设和证明使用。

C2 文稿包含 38 个纸面审查点。本次重跑通过 19 组有限数学回归及 1 组 Frozen 字节核对，共 20 组。文件完整性与有限回归不等于全部数学证明认证，也不构成 AI 数学创造力增益的实验结果。

## 复核

在仓库根目录运行，使用 Python 3.10 或更新版本，无需额外 Python 库：

```sh
sha256sum -c docs/C2_SOURCE_SHA256SUMS.txt
python3 theory/C2/tests/verify_finite.py --output /tmp/ge-c2-results.json
```

`--output` 把新结果写到另一个文件，保留原包的 `tests/results.json`。本次运行输出见[C2 有限回归记录](docs/C2_FINITE_REGRESSION_2026-10-01.json)。C1 的检查命令和已知清单差异见[C1 核对记录](docs/REPOSITORY_AUDIT_2026-10-01.md)。

## License

本仓库采用 [MIT License](LICENSE)。
