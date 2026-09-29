# 识别地图与依赖结构
## 不是一个覆盖一切的“超级定理”

这里把当前最可用的内容写成“给什么、检查什么、得到什么”。同一机制在多个领域可实例化；领域存在定理仍需独立证明。

| 目标 | 可用的充分条件／等价判据 | 得到的严格结论 | 未自动得到 |
|---|---|---|---|
| 问题余表示 | 元素范畴有初始对象 | 存在 `P(a,-)≃Map(Fa,-)` | 文献原创、实际新颖性 |
| 伴随识别 | presentable 环境，可达且保持所有极限 | 右伴随／代表对象 | 前提自动成立 |
| 对象实际化 | 比较 C 的 core fiber 非空 | 对象处于本质像 | 映射重建 |
| 完整比较 | C 本质满且全忠实 | C 等价 | 自动领域证明 |
| 相容有限填充 | 有限逆图，所经 matching fiber 非空 | 相容解存在 | 所有 branch 都可延伸 |
| 唯一相干填充 | 相关相对 matching fiber 可缩 | 给定边界的填充空间可缩 | 另一种问题的全部模空间可缩 |
| 无限实际化 | 真实 horizon 完备 + component ML + 每层非空 | 全局非空 | 自动 horizon 完备 |
| 无限刚性 | 对应基点分支 π1 塔 ML | 该分支 lim¹ 额外歧义消失 | 高阶群全消失 |
| Horizon识别 | relative comparison square 笛卡尔 | 相应纤维极限正确 | 笛卡尔性本身的领域证明 |
| 双侧重建 | A、F 各自从同一相容 horizon 重建 | 相对 horizon 完备 | 相反方向必要性 |
| 代数语言恢复 | U 单子性且单子有限元 | Lawvere语义重建 | 忘掉 U 后仍同一单排序呈现 |
| 无 U 的语言恢复 | 完整 K 局部有限可表示 | K≃Lex((Kfp)^op,Set) | 单个模型足够、最小符号基 |
| 存在量词 | 正规范畴，拉回稳定像 | ∃ 左伴随代入 | 内部蕴含／全称自动存在 |
| 安全法则 | 固定满足系统、集合范围、扩张型结构 continuation | 最小共同模型闭包及最大安全理论 | 实际可达与非空规范缺陷 |
| 带见证修补 | 相干 occurrence evaluation、小余极限 | 参数化 pushout 的 pointed 泛性质 | unpointed universality |
| 受约束修补 | 忘却 U 有左伴随 F | F(自由初始对象) 初始 | 所有保存契约都可行 |
| 无限契约极大保留 | 可行子集非空且链并仍可行 | Zorn 极大元 | 唯一、有效可算 |
| 普通Massey简化 | F2 支撑DGA全部相关 off-support H 消失 | fixed-input defining systems 可齐次化 | 非零时自动失败／一般系数版 |
| 三方向MC | pair equations可解 | intrinsic 商障碍零 iff full cube存在 | 四方向仍线性 |
| 小扩张MC提升 | mI=0与正确DGLA/系数条件 | H²⊗I曲率类完整检测提升 | 单个lift代表失败=全部方向失败 |
| pro-p中央粘合 | 局部lift存在，核中央，推积泛性质适用 | overlap H¹商类零 iff全局lift | 非中央/所有tuple自动解决 |
| 有限描述稳定 | 小加法C有弱核 | mod(C)核封闭 | 计算便宜 |
| 稳定生成保持完美 | 正则相干R | Perf标准截断封闭 | grammar-independent depth |
| 相对新颖性 | 事前观察 N 与旧可达世界 | OldMatch 空／非空 | 人类重要性、文献first |

## 依赖图（语义层）

```text
Frozen configuration / declared semantics
 ├─ saturated horizontal problem ──→ possibility category ──→ representability
 ├─ Actual→Formal comparison ──────→ fibers / diagram lifts
 │                                   ├─ finite matching
 │                                   ├─ Coupl / viability (sector)
 │                                   └─ horizon comparison
 │                                        ├─ internal limit branch + lim¹
 │                                        └─ actual reconstruction δ
 ├─ structural language recovery ──→ satisfaction / model semantics
 │                                   └─ safe-law closure
 │                                        (not automatically repair goals)
 ├─ law/defect + transport contract ─→ repair category
 │                                   ├─ pointed coherent pushout
 │                                   ├─ constrained adjoint
 │                                   └─ branching / infeasible frontier
 └─ old reachable baseline + N∞ ────→ observation-relative novelty

source proof histories are retained throughout; effective algorithms are a
separate overlay requiring encodings, decidability and a cost model.
```

## 依赖中的“断口”必须继续看得见

1. `语义同理论` 到 `实际可达` 没有自动箭头。
2. `恢复语言` 到 `选定非平凡修补目标` 没有自动箭头。
3. `等价不变缺陷空间` 到 `所有态射上的functor/profunctor` 没有自动箭头。
4. `所有局部修补分别存在` 到 `联合、无限相干修补存在` 没有自动箭头。
5. `形式doctrine极限` 到 `保持K的实际grammar极限` 没有自动箭头。
6. `一般recognition theorem` 到 `DHH/SNT等具体命题已证` 没有自动箭头。

## 能优先研究的三类新增识别结果

**A. 非循环的效性前提。** 寻找从有限表示性、适当性、衰减／连通增长、保守探针等可以独立核验的数据推出 δ 完备的定理，而不是把 δ 完备作为假设再宣布实际化。

**B. 语义陈述到带见证求解的编译。** 证明公式／关系的一个 presentation 与另一个 presentation 给出相同求解空间所需条件；在这里保留见证、相干性和方差。

**C. Saturation 的有限充分测试。** 给出小而可计算的消失条件，证明 reduced model 覆盖 ordinary solutions；R29 的受限版本是一种模板。非零缺陷群只表示可能有遗漏，不是完整 obstruction。

这些研究直接提升模型的求解能力。单纯增加更多经典例子的重命名，不计作同等级推进。
