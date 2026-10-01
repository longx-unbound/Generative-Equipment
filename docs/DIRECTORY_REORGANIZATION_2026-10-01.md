# C1 目录整理记录

日期：2026-10-01。迁移基准：[9278f7194256ff63befc667395a69ffcc87d9226](https://github.com/longx-unbound/Generative-Equipment/commit/9278f7194256ff63befc667395a69ffcc87d9226)。本次只整理目录、导航和校验路径，不增加数学结论。

## 路径变化

| 迁移前 | 迁移后 |
|---|---|
| `theory/00_README.md` 至 `09_AUDIT_REPORT.md` | `theory/C1/` 下同名文件 |
| `theory/frozen_original/`、`source_archive/`、`registry/` | `theory/C1/` 下同名目录 |
| C1 的 `theory/evidence/` 内容 | `theory/C1/evidence/` |
| `theory/verify_package.py`、`theory/SHA256SUMS.txt` | `theory/C1/` 下同名文件 |
| `theory/evidence/Generative_Equipment_C2_2026-09-30.zip` | [`docs/archives/Generative_Equipment_C2_2026-09-30.zip`](archives/Generative_Equipment_C2_2026-09-30.zip) |

`theory/` 仅保留版本索引 `README.md`、`C1/` 和 `C2/`。新增 [C1 归档导航](../theory/C1/README.md)，更新首页、AI 方向页与文档链接；不在旧位置留下重复文件或重定向占位文件。旧路径仍可通过上述历史提交访问。

## 字节与历史记录

- C1 的 78 个既有文件整体搬迁，内容与基准提交完全相同；包内相对链接、登记和验证器依赖结构不变
- `theory/C2/` 的 8 个文件及其路径完全不变；C2 ZIP 只改变存放位置
- Frozen 的 8 份原文与原始压缩包不变；核心 SHA-256 仍为 `753f2cf7c6da8aae50cf4ea56d5807bae2747ce509c1d2d0522be2189ba6086d`
- LICENSE 不变，提交历史保留
- [C1 公开快照清单](C1_PUBLIC_SNAPSHOT_2026-10-01.sha256)仅给 78 个路径增加 `C1/` 前缀，摘要值不变；[C2 清单](C2_SOURCE_SHA256SUMS.txt)仅调整 ZIP 路径
- 原 C1 包清单 `theory/C1/SHA256SUMS.txt`、登记结果和 C2 原运行结果保持原样，不用本次输出覆盖

[旧 C1 核对记录](REPOSITORY_AUDIT_2026-10-01.md)与[C2 发布记录](C2_PUBLICATION_2026-10-01.md)中的“保留原路径”等表述描述各自历史操作，仍按文中基准提交理解。本次为随后进行的物理迁移；旧记录仅增加迁移提示并修正可点击链接的目标。

## 当前复核命令

在仓库根目录运行：

```sh
sha256sum -c docs/C1_PUBLIC_SNAPSHOT_2026-10-01.sha256
sha256sum -c docs/C2_SOURCE_SHA256SUMS.txt
python3 theory/C1/verify_package.py --output /tmp/ge-c1-integrity.json
python3 theory/C1/source_archive/verify_r22_counterexample.py
python3 theory/C2/tests/verify_finite.py --output /tmp/ge-c2-results.json
```

`verify_refinements.py` 会覆写相邻结果文件，应在隔离副本运行，例如：

```sh
workdir=$(mktemp -d)
cp theory/C1/evidence/verify_refinements.py "$workdir/"
python3 "$workdir/verify_refinements.py"
```

原 C1 包清单的历史核对命令现为：

```sh
(cd theory/C1 && sha256sum -c SHA256SUMS.txt)
```

该旧清单仍报告既有差异：`00_README.md`、`01_MASTER_THEORY.md`、`05_SECTORS_AND_APPLICATIONS.md` 的内容摘要不同，`10_ALL_IN_ONE.md` 已在先前提交中删除。本次未改写清单或补回重复合订稿；其余条目通过。

## 本次迁移复核

C1 公开快照 78/78 和 C2 文件/ZIP 9/9 摘要核对通过；C1 原校验器通过，核对 49 个来源单元、8 个 Frozen 成员、101 条结论、51 条依赖边与 58 个正文链接。原有 R22 反例及 refinement 有限回归通过；C2 原校验器 20/20 组通过。新输出保存在仓库外，未修改归档结果。

这些是迁移后的文件、引用和既有有限回归检查，不是一般数学证明、全量历史大规模测试或 AI 能力增益认证。

[理论版本索引](../theory/README.md) · [项目首页](../README.md)
