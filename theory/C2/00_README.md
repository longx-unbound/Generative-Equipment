# Generative Equipment C2

**目标：帮助 AI 提出、构造并验证数学，而不只生成看似合理的答案。**

C2 在 C1 的严格工作层上恢复丰富化、相对残差、实现尺度、信息压缩、量词提升和问题选择等派生功能。Frozen v1.0 的核心保持不变。

## 阅读

- [数学理论](01_C2_THEORY.md)：继承的基础、六个模块、限定定理与证明。
- [严格评估和测试](02_EVALUATION_AND_TESTS.md)：38个纸面审查点、模块删除试验和实际回归结果。
- [AI创造协议](03_AI_CREATIVITY_PROTOCOL.md)：可直接使用的工作指令和C1/C2对照实验设计。
- [Frozen核心原文](baseline/01_FROZEN_CORE.md)：只读基线。

C2 是当前派生工作版本，不是 Frozen v1.1。修改核心必须另行明确版本；C1 的领域结论仍携带其原有假设与证据状态。本包不重复收录全部历史研究文件。

## 检查

```bash
python tests/verify_finite.py
```

不需要额外Python库。实际运行的结果在 [tests/results.json](tests/results.json)。源材料哈希在 [source_integrity.json](source_integrity.json)。

已完成：限定数学证明、38个审查点、19组小型数学回归和1组核心完整性核对。未完成：同模型随机对照、形式化证明助理认证与穷尽原创性检索。测试不是AI能力提升的实证结果。

## 放入现有仓库

将本目录整体放到 `theory/C2/`，保留原来的 C1 和 Frozen 基线；修改仓库首页的当前理论入口指向 `theory/C2/00_README.md`。不要覆盖 C1 的文件或原校验清单。

本包只有四份当前说明／正文Markdown，加一份未改动的Frozen核心，不增加独立治理、宣传或研究日志文件。
