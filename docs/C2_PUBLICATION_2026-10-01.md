# C2 公开发布核对

> 目录迁移说明：本记录描述下文所列历史提交及当时路径。随后 C1 归入 `theory/C1/`，Frozen 原文独立到 `theory/Frozen-v1.0/`，原始 ZIP 移入 `docs/archives/`；正文中的历史命令与事实保留，当前运行路径及清单说明见[目录整理记录](DIRECTORY_REORGANIZATION_2026-10-01.md)。

日期：2026-10-01。对象：`longx-unbound/Generative-Equipment` 的 C2 公开更新。

本次以公开提交 [b93dae237aeab5cf6b393f2322f83bd5dcb3835f](https://github.com/longx-unbound/Generative-Equipment/commit/b93dae237aeab5cf6b393f2322f83bd5dcb3835f) 为基准，发布已有的 C2 包并整理阅读入口；没有增加数学结论或修改验证器。

## 1. 发布内容与目录

| 位置 | 用途 |
|---|---|
| [`theory/C2/`](../theory/C2/) | C2 原包的全部 8 个文件：说明、主文、评估、AI 协议、Frozen 核心、源摘要、验证器与原运行结果 |
| [`theory/evidence/Generative_Equipment_C2_2026-09-30.zip`](archives/Generative_Equipment_C2_2026-09-30.zip) | C2 原始压缩包，保留下载与字节核对依据 |
| [`C2_SOURCE_SHA256SUMS.txt`](C2_SOURCE_SHA256SUMS.txt) | 上述 8 文件及原始 ZIP 的 SHA-256；路径相对仓库根目录 |
| [`C2_FINITE_REGRESSION_2026-10-01.json`](C2_FINITE_REGRESSION_2026-10-01.json) | 本次重新运行的输出，独立于包内原记录保存 |

首页、`AI_MATH.md` 和 `theory/README.md` 更新为 C2 入口。C1 的 78 个既有理论文件、Frozen 原文、历史源档案、登记、原校验清单、旧核对记录和 LICENSE 均保留原路径与字节。新增 C2 采用独立版本目录，避免同名主文、结果文件或校验清单互相覆盖。

本次没有删除源文件：现有材料承担正文、来源、订正或证据职能，C1 合订重复稿已在先前历史中移除。清理的是导航中把 C1 写成仓库最新版本的表述。C1 文稿自身的历史版本措辞不改写；版本优先级由[理论导航](../theory/README.md)说明。

## 2. 原始字节与来源

- C2 ZIP 含 8 个文件；逐一解压比对，发布的 `theory/C2/` 与对应成员逐字节相同
- ZIP SHA-256：`09a5849b6825835f62ee6404050d4cfb51a67a4c2e6be1ebbb0aa2a94a816c6e`
- C2 中的 Frozen 核心为 9,391 字节，SHA-256 为 `753f2cf7c6da8aae50cf4ea56d5807bae2747ce509c1d2d0522be2189ba6086d`，与既有 Frozen 核心相同
- `source_integrity.json` 所列 C1 原始压缩包及原 C1 主文摘要已对源材料核对一致；它们指向原始版本，不能用来宣称当前公开 C1 编辑稿逐字节等同于原包

C1 公开编辑的既有差异仍由[C1 仓库核对记录](REPOSITORY_AUDIT_2026-10-01.md)披露。[C1 公开快照清单](archives/C1_PUBLIC_SNAPSHOT_2026-10-01.sha256)和 `theory/SHA256SUMS.txt` 均不重写，也不扩充为 C2 清单。

## 3. 本次实际复核

运行原包验证器，输出指定为独立文件，未覆盖 `theory/C2/tests/results.json`：

```sh
python3 theory/C2/tests/verify_finite.py --output /tmp/ge-c2-results.json
```

**20/20 组通过：19 组有限数学回归与 1 组 Frozen 字节核对。** 精确运行时间、Python 版本、检查项和范围见[本次 JSON 结果](C2_FINITE_REGRESSION_2026-10-01.json)。原包结果仍保留其 2026-09-30 的时间与原始字节。

文件复核包括：C2 原始 ZIP 的完整 8 文件成员、发布源文件 SHA-256、Frozen 核心同一性，以及本次新增或修改的 Markdown 导航的本地目标存在性。既有 C1 文件按基准 Git blob SHA 保持不变；此前 C1 的回归结果见旧核对记录，本次不重复执行历史大规模检查。

在仓库根目录可另行运行：

```sh
sha256sum -c docs/C2_SOURCE_SHA256SUMS.txt
sha256sum -c docs/C1_PUBLIC_SNAPSHOT_2026-10-01.sha256
```

## 4. 验证边界

- 38 个纸面审查点是 C2 文稿的既有审查范围，本次发布没有重新独立认证全部证明
- 有限回归不证明无限范围结论、文献首创性或全部领域结果
- C1/C2 同模型同预算随机对照仍是协议设计，没有新增 AI 能力实验数据
- 本次为直接执行的文件和有限回归检查，不称为 GitHub Actions CI 通过

C2 保留 Frozen v1.0 的核心，继承 C1 领域结论的条件与证据状态。原文、纸面证明、有限验证与 AI 能力实证需要分别判断。
