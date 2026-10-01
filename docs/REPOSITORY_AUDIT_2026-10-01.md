# 公开仓库核对记录

> 目录迁移说明：本记录描述下文所列历史提交及当时路径。随后 C1 整包移入 `theory/C1/`，C2 原始 ZIP 移入 `docs/archives/`；正文中的历史命令与事实保留，当前运行路径及清单说明见[目录整理记录](DIRECTORY_REORGANIZATION_2026-10-01.md)。

日期：2026-10-01。对象：`longx-unbound/Generative-Equipment` 的公开 C1 文件快照。

基准提交：[bf3387918979b54036cec1524f2d1dc1836f562a](https://github.com/longx-unbound/Generative-Equipment/commit/bf3387918979b54036cec1524f2d1dc1836f562a)。本次是文件、导航与既有回归核对，没有新增数学研究，也没有重新认证全部历史证明。

## 1. 公开版本的准确地位

基准提交有 81 个文件：根目录 3 个文件与 `theory/` 中的 78 个文件。公开理论为 C1，冻结核心为 Frozen v1.0（2026-09-23）。

提交历史已包含编纂正文的编辑及 `theory/10_ALL_IN_ONE.md` 的删除，因此当前公开目录与原 C1 压缩包不是完整逐字节副本。需要分开看待：

- Frozen 原始压缩包及其 8 份展开文件
- 按来源登记保留的 49 个源单元
- 已有公开编辑的 C1 编纂正文
- 记录原包状态的校验清单及当时的检查结果

本次导航整理不移动或覆盖这 78 个既有理论文件；原校验清单和旧检查结果也保留原样。

## 2. 已实际执行的复核

从上述提交取得的 81 个文件逐一与 Git blob SHA 核对一致。以下检查在该精确快照上运行。

| 检查 | 本次结果 | 能支持的结论 |
|---|---|---|
| `python3 theory/verify_package.py` | PASS | 49 个来源单元的字节及 SHA-256 一致；Frozen 压缩包的 8 个成员与展开文件逐字节一致；登记、依赖及所检查链接一致 |
| `python3 theory/source_archive/verify_r22_counterexample.py` | PASS | 指定十边图的普通四重 Massey 输入，经非区间修正后顶曲率为零；不推出整个空间形式性 |
| `python3 theory/evidence/verify_refinements.py` | PASS | 既有有限 DGLA 恒等式、支撑模式与 Boolean 闭包回归通过 |
| `(cd theory && sha256sum -c SHA256SUMS.txt)` | FAIL，差异如下 | 原包清单不再完整匹配当前公开编纂正文 |

复核时，第三项在隔离副本运行，未覆盖公开快照中原有的结果文件。

### 原 C1 清单的已知差异

- `00_README.md`：内容哈希与原清单不同
- `01_MASTER_THEORY.md`：内容哈希与原清单不同
- `05_SECTORS_AND_APPLICATIONS.md`：内容哈希与原清单不同
- `10_ALL_IN_ONE.md`：清单仍列出，但公开仓库已无此文件

清单中其余条目通过。本记录不通过重写旧清单掩盖这些差异，也不据此断言 Frozen 原始字节发生变化。

### 登记检查的新旧计数

| 字段 | 原保存结果 | 本次实际运行 |
|---|---:|---:|
| 编纂文档 | 11 | 10 |
| 来源／文献引用出现次数 | 596 | 297 |
| 本地文件链接 | 108 | 58 |

`registry/integrity_results.json` 保留的是先前运行记录，不能当作当前公开目录的最新运行输出。两次均登记 101 条结论、51 条依赖边和 20 条文献；这些数字是文档和登记范围，不是数学正确率。

本次有限回归包括 9 个 d² 基检查、81 对 graded skew、81 对 differential derivation、729 组三元 Jacobi、9 个曲率系数恒等式、20,736 个支撑模式、9 个单调扩张映射与 36 个闭包幂等点检查。

## 3. 当前公开快照的附加字节清单

[`C1_PUBLIC_SNAPSHOT_2026-10-01.sha256`](C1_PUBLIC_SNAPSHOT_2026-10-01.sha256) 记录基准提交中 `theory/` 既有 78 个文件的 SHA-256。它用于确认这批公开文件在本次导航整理中未变，不替换原 C1 包清单，也不作数学真值认证。

在仓库根目录执行：

```sh
sha256sum -c docs/C1_PUBLIC_SNAPSHOT_2026-10-01.sha256
```

本清单不包括随后新增的导航、核对说明或其他版本。

## 4. 未验证与未认证事项

- 没有重新执行 512,000 图 ordinary Massey 全分类或全部历史大规模回归
- 没有重新逐行审查全部领域证明或穷尽文献首创性
- 没有进行证明助理形式化或 AI 能力的同预算随机对照
- 截至核对时，仓库无 GitHub Actions 工作流文件及运行记录；上述结果来自本次直接执行，不称为 CI 通过

项目内既有结论仍按[定理账本](../theory/C1/02_THEOREM_LEDGER.md)、[订正表](../theory/C1/03_CORRECTIONS_AND_NO_GO.md)与各自条件使用。文件校验通过、有限回归通过和一般数学命题成立是不同的判断。
