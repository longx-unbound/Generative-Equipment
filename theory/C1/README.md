# C1 归档

**C1 · 2026-09-29** 是继承的严格工作层与领域附卷。当前公开派生工作版本见 [C2](../C2/00_README.md)，各版本关系见[理论版本索引](../README.md)。

原来散落在 `theory/` 下的 C1 材料已归入本目录。Frozen v1.0 独立放在同级目录；C1 的来源登记、来源索引和校验器仅调整对应路径，所记录的来源摘要不变。原 C1 文稿中 `frozen_original/` 等写法属于旧包结构，当前路径以本页为准。

## 正文

| 文件 | 用途 |
|---|---|
| [00 · C1 说明](00_README.md) | 版本关系、收录范围与证据边界 |
| [01 · 理论总稿](01_MASTER_THEORY.md) | 冻结骨架、发生、实现、修补与观察 |
| [02 · 定理账本](02_THEOREM_LEDGER.md) | 结论的前提、地位、来源与依赖 |
| [03 · 订正与 no-go](03_CORRECTIONS_AND_NO_GO.md) | 撤回、收窄与禁止重引入的推理 |
| [04 · 识别与依赖](04_RECOGNITION_MAP_AND_DEPENDENCIES.md) | 从假设定位可使用的结论 |
| [05 · 领域与应用](05_SECTORS_AND_APPLICATIONS.md) | 具体工具及适用边界 |
| [06 · 核心与研究协议](06_CORE_MINIMALITY_AND_RESEARCH_PROTOCOL.md) | 核心精炼边界与验证要求 |
| [07 · 来源与版本地图](07_SOURCE_INDEX_AND_VERSION_MAP.md) | 追溯原稿和历史版本 |
| [08 · 参考文献](08_BIBLIOGRAPHY.md) | 经典输入及文献核对范围 |
| [09 · 原审计报告](09_AUDIT_REPORT.md) | 当时的检查结果及未复现事项 |

## 配套材料

- [Frozen v1.0](../Frozen-v1.0/)：同级独立目录中的 8 份原文；[核心](../Frozen-v1.0/01_FROZEN_CORE.md) · [原始 ZIP](../../docs/archives/Generative_Equipment_Frozen_v1_0_ORIGINAL.zip)
- [source_archive/](source_archive/)：历史源稿与原有验证脚本
- [registry/](registry/)：结论、来源、文献登记及历史检查输出
- [evidence/](evidence/)：ENDO 原始压缩包与既有回归证据
- [verify_package.py](verify_package.py)：文件完整性、引用与依赖检查，不检查数学证明真值
- [SHA256SUMS.txt](SHA256SUMS.txt)：原 C1 包的历史清单，保留已披露的差异

## 当前复核路径

在仓库根目录运行：

```sh
sha256sum -c docs/C1_FROZEN_SHA256SUMS.txt
python3 theory/C1/verify_package.py --output /tmp/ge-c1-integrity.json
```

公开 C1 编辑稿不是原 C1 压缩包的完整逐字节副本。原包清单保留历史路径与摘要；既有三处内容差异和缺失合订稿，见[历史仓库核对](../../docs/REPOSITORY_AUDIT_2026-10-01.md)；本次搬迁不改写这些事实。其他命令与路径映射见[目录整理记录](../../docs/DIRECTORY_REORGANIZATION_2026-10-01.md)。

[理论版本索引](../README.md) · [项目首页](../../README.md)
