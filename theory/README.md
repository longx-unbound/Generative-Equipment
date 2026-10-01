# 理论导航

当前公开派生工作版本为 **C2 · 2026-09-30**，基础规范仍为 **Frozen v1.0 · 2026-09-23**。C1 保留为继承的严格工作层与领域附卷。

## 从 C2 开始

1. [C2 说明](C2/00_README.md)：版本关系、收录范围与证据边界
2. [C2 数学理论](C2/01_C2_THEORY.md)：继承的基础、六个模块、限定定理与证明
3. [严格评估和测试](C2/02_EVALUATION_AND_TESTS.md)：38 个纸面审查点、模块删除试验与有限回归
4. [AI 数学创造协议](C2/03_AI_CREATIVITY_PROTOCOL.md)：可直接使用的工作指令与待执行的对照实验
5. [发布核对](../docs/C2_PUBLICATION_2026-10-01.md)：原包一致性、本次重跑与未验证范围

C2 全部 8 个源文件置于 `C2/`，保留包内路径与原始字节。六个模块为 EC（丰富化与定量观察）、RG（相对残差、复合与扭曲）、ES（pro 对象、统一化与失效尺度）、IC（目标相对压缩与安全搜索）、PR（检测、误差与量词提升）、DG（问题目录、对称性与生成路径）。按问题选择模块，不要求每次全部调用。

## 查阅 C1 与 Frozen

| 用途 | 文件 |
|---|---|
| 查冻结基础规范 | [Frozen v1.0 核心](frozen_original/01_FROZEN_CORE.md)、[冻结版本清单](frozen_original/00_MANIFEST.md) |
| 阅读 C1 编纂正文 | [C1 说明](00_README.md)、[理论总稿](01_MASTER_THEORY.md) |
| 使用继承的领域结论 | [定理账本](02_THEOREM_LEDGER.md)、[订正与 no-go](03_CORRECTIONS_AND_NO_GO.md) |
| 定位前提与具体工具 | [识别与依赖地图](04_RECOGNITION_MAP_AND_DEPENDENCIES.md)、[领域与应用](05_SECTORS_AND_APPLICATIONS.md) |
| 理解 C1 研究与验证要求 | [核心精炼与研究协议](06_CORE_MINIMALITY_AND_RESEARCH_PROTOCOL.md) |
| 追溯旧版本 | [来源与版本地图](07_SOURCE_INDEX_AND_VERSION_MAP.md)、[源档案](source_archive/) |
| 核对经典输入 | [参考文献](08_BIBLIOGRAPHY.md) |
| 查看 C1 当时的检查及公开编辑差异 | [C1 审计报告](09_AUDIT_REPORT.md)、[C1 公开仓库核对](../docs/REPOSITORY_AUDIT_2026-10-01.md) |
| 读取 C1 机器记录 | [结论登记](registry/claim_registry.json)、[来源登记](registry/source_manifest.json)、[文献登记](registry/bibliography.json) |

## 版本与目录的使用规则

- Frozen 原文规定冻结核心；冻结包中的派生材料仍可能受后续订正限制
- C2 补充派生模块，不替代 C1 各领域附卷，也不修改 Frozen 核心
- C1 文稿中的“当前”是其编纂时的版本措辞；仓库当前阅读入口以本页和首页为准
- 历史源档案用于追溯，旧稿的完成度、新颖性和测试表述不能绕过适用条件与订正

C1 既有文件留在原位，避免破坏外部引用、来源登记与旧校验清单。`C2/baseline/01_FROZEN_CORE.md` 是原包自带的基线副本，用于独立复核，保留它才能维持整包字节一致性。

回到[项目首页](../README.md)。
