# Generative Equipment / 数学内生生成性
## 完整整理与精炼包 C1 · 2026-09-29

这是 Generative Equipment 的**编纂、去重和订正版本**。C1 不是 Frozen v1.1，也不是新的母理论冻结；它是在 Frozen v1.0 基础上的当前综合版本。


## Frozen v1.0 与 C1 的地位

- **Frozen v1.0（2026-09-23）是冻结的基础版本。** 其中 `01_FROZEN_CORE.md` 是 primitive core 与核心语义边界的规范基线。
- **C1 是当前综合版本。** 它不覆盖 Frozen core，而是在该核心之上整理严格实现、派生结果、订正、证据状态与应用接口。
- Frozen v1.0 中的**核心**与其**派生材料**必须区分：核心除非出现明确反例、内部矛盾、良定义性失败或核心无法表达其明确承诺覆盖的现象，否则不修改；派生材料则可以被后续证明与反例收窄。
- 因此，读取 **primitive core** 时以 Frozen v1.0 为基线；使用**当前派生结论、订正、状态和应用边界**时以 C1 为准。
- “Frozen”表示版本冻结，不等同于对全部派生陈述的独立正确性认证。若 Frozen core 本身需要修改，应显式发布新的 Frozen 版本，而不是由 C1 静默改写。


## 阅读入口

| 文件 | 用途 |
|---|---|
| [01_MASTER_THEORY.md](01_MASTER_THEORY.md) | 连续阅读的理论总稿；统一定义、四个模块、主要判据与适用边界 |
| [02_THEOREM_LEDGER.md](02_THEOREM_LEDGER.md) | 每条结论的地位、前提、来源、依赖与原创性边界 |
| [03_CORRECTIONS_AND_NO_GO.md](03_CORRECTIONS_AND_NO_GO.md) | 正式撤回、收窄、证据降级和禁止重引入的推理 |
| [04_RECOGNITION_MAP_AND_DEPENDENCIES.md](04_RECOGNITION_MAP_AND_DEPENDENCIES.md) | 从可检查假设到可使用结论的地图 |
| [05_SECTORS_AND_APPLICATIONS.md](05_SECTORS_AND_APPLICATIONS.md) | 代表性领域定理的独立表述、证明与应用状态 |
| [06_CORE_MINIMALITY_AND_RESEARCH_PROTOCOL.md](06_CORE_MINIMALITY_AND_RESEARCH_PROTOCOL.md) | 核心精炼边界、研究与验证规则、下一阶段任务 |
| [07_SOURCE_INDEX_AND_VERSION_MAP.md](07_SOURCE_INDEX_AND_VERSION_MAP.md) | 原稿索引、历史版本与当前模块的对应 |
| [08_BIBLIOGRAPHY.md](08_BIBLIOGRAPHY.md) | 经典输入的来源与文献核对范围 |
| [09_AUDIT_REPORT.md](09_AUDIT_REPORT.md) | 审计结果、原文完整性与未复现事项 |

`registry/claim_registry.json` 是机器可读定理账本；`registry/source_manifest.json` 为原稿字节与 SHA-256 索引。`verify_package.py` 检查归档完整性、引用和依赖；**它不验证数学证明的真值**。


## 当前理论的精简结构

> 冻结语义骨架 + 发生／实现／修补／观察四个模块 + 带条件的识别定理 + 独立领域工具。

不要把这些模块排列成无条件自行运行的算法。一个领域需要验证哪些接口，本身属于研究内容。

## 收录范围

收录 Frozen 原始包、Strict v0.1/v0.2 及审计、GE-R1–R35、ENDO-1–6、Horizon 系列，以及 C1 纳入的 moment-angle、DGLA、SNT 等接口文件。



## 原文保护与证据地位

`frozen_original/` 保留原始压缩包中 8 份文件的原始字节；`evidence/Generative_Equipment_Frozen_v1_0_ORIGINAL.zip` 是原始包本身。`source_archive/` 保存其余已定位的原稿。原稿保留旧措辞，**不意味着旧结论被本版认可**。

本版采用 DEF、STD、DER、COND、REPORT、OPEN、RETRACT 七种数学地位。历史版本中的完成度或价值评级不作为独立数学证据。

归档证据包括证明核对、显式反例和小型精确回归，但不包含全量形式化证明，也没有完整复现 512,000 图的 ordinary Massey 分类。因此该全称分类保持为待补证的 REPORT，不作为已核验定理使用。

## 使用优先级

Frozen v1.0 的冻结核心原始语义保持不变；派生结论的当前使用规则，以 C1 总稿、定理账本和订正表为准。若后续出现明确反例，应记录受影响的结论与依赖，不能通过改名或改变目标掩盖失败。

本包是 Generative Equipment 的公开研究与版本追踪入口；它不是已完成同行评议、文献首创认证或普遍预测能力认证的论文。
