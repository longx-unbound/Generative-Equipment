# Generative Equipment / 数学内生生成性

Generative Equipment 是一个开放的数学研究项目，研究：**数学结构自身如何产生问题、实现条件、障碍、修补与新的结构？**

一个主要目标是帮助 AI 更可靠、更有创造性地思考数学。项目把表示与目标、形式与实际、有限与整体、逐点与相干、已证与待证的区别写成明确的数学接口。对 AI 数学能力的净提升仍需要实证评估。

## 从这里开始

- **当前理论 C2**：[版本说明](theory/C2/00_README.md) · [数学理论](theory/C2/01_C2_THEORY.md) · [严格评估与测试](theory/C2/02_EVALUATION_AND_TESTS.md)
- **AI 数学方向**：[项目目的](AI_MATH.md) · [C2 AI 数学创造协议](theory/C2/03_AI_CREATIVITY_PROTOCOL.md)
- **C1 归档**：[归档导航](theory/C1/README.md) · [定理账本](theory/C1/02_THEOREM_LEDGER.md) · [订正表](theory/C1/03_CORRECTIONS_AND_NO_GO.md)
- **Frozen v1.0**：[原始核心](theory/Frozen-v1.0/01_FROZEN_CORE.md) · [原始包](docs/archives/Generative_Equipment_Frozen_v1_0_ORIGINAL.zip)

完整版本关系见[理论版本索引](theory/README.md)。C2 是当前派生工作版本，继承 C1 的严格工作层与领域附卷，并保留 Frozen v1.0 核心；使用领域结论时，仍须遵守 C1 的前提、证据状态与订正。

## 仓库结构

```text
Generative-Equipment/
├── README.md          项目入口
├── AI_MATH.md         AI 数学方向
├── LICENSE
├── theory/
│   ├── README.md      版本索引
│   ├── C2/            当前理论，8 个原包文件
│   ├── C1/            C1 正文、来源与证据
│   └── Frozen-v1.0/   独立的 Frozen 原始版本
└── docs/              发布核对、校验清单与迁移记录
    └── archives/      Frozen、C2 原始 ZIP 与历史清单
```

C1 材料集中在 `theory/C1/`，Frozen v1.0 的 8 份原文独立放在同级 `theory/Frozen-v1.0/`。数学正文与原档字节保留，仅调整必要的导航与校验路径。C2 的 8 个文件与[C2 原始 ZIP](docs/archives/Generative_Equipment_C2_2026-09-30.zip)逐字节一致。整理范围和路径变化见[目录整理记录](docs/DIRECTORY_REORGANIZATION_2026-10-01.md)。

## 数学与证据状态

C1 使用 DEF、STD、DER、COND、REPORT、OPEN、RETRACT 七种状态，详见[C1 总稿 §1](theory/C1/01_MASTER_THEORY.md)。C2 的命题按各自注明的范围、假设和证明使用。

C2 文稿包含 38 个纸面审查点。发布时重跑通过 19 组有限数学回归及 1 组 Frozen 字节核对，共 20 组。文件完整性与有限回归不等于全部数学证明认证，也不构成 AI 数学创造力增益的实验结果。详见[C2 发布核对](docs/C2_PUBLICATION_2026-10-01.md)。

C1 公开整理版已有历史编辑，且合订文件曾被移除，并非原 C1 压缩包的完整逐字节副本；这些既有差异见[C1 核对记录](docs/REPOSITORY_AUDIT_2026-10-01.md)。

## 复核

在仓库根目录运行，使用 Python 3.10 或更新版本，无需额外 Python 库：

```sh
sha256sum -c docs/C2_SOURCE_SHA256SUMS.txt
sha256sum -c docs/C1_FROZEN_SHA256SUMS.txt
python3 theory/C1/verify_package.py --output /tmp/ge-c1-integrity.json
python3 theory/C2/tests/verify_finite.py --output /tmp/ge-c2-results.json
```

`--output` 把新结果写到独立文件，保留归档中的历史输出。更多 C1 复核路径及原清单的已知差异见[目录整理记录](docs/DIRECTORY_REORGANIZATION_2026-10-01.md)。

## License

本仓库采用 [MIT License](LICENSE)。
