# 原稿索引、覆盖范围与版本对照

本包对 **49 个来源单元**建立ID；冻结原始包的8份文件全部保留，其中4份在正文单独建立了来源ID。相同文件的不同挂载副本去重。

这是一份来源完整性记录，不表示所有来源中的历史定理均经本次独立证明。原稿的旧评级与当前地位冲突时，以C1账本和订正表为准。

## 历史到当前模块

| 旧分支 | 当前位置 | 处理 |
|---|---|---|
| Frozen v1.0 | 骨架／研究契约 | 原文逐字节保留，不升版 |
| Strict v0.1/v0.2 | 空间值严格实现 | 保留域变化及丰富化边界；v0.1不替代一般core |
| GE-R1/R2 | 表示、Prof方差、probe/coprobes、饱和、无限塔 | 补回此前ENDO摘要容易遗漏的部分 |
| GE-R3–R12 | 实现／匹配／Coupl | 保留领域条件与局部系数；R13限制优先 |
| GE-R13/R14 | 现实性审计 | 算法/新增价值不因结构正确而自动成立 |
| GE-R15/R16 | primary元数与resolved Coupl | sharpness只在声明sector |
| GE-R17–R23 | 支撑／Massey | R22普通非平凡外推撤回 |
| GE-R24–R35 | pro-p与变形、sat corrections | fixed representation与全部choice区分 |
| ENDO-1/2 | 问题发生与结构闭包 | 语法/实际语义前提公开 |
| ENDO-3各版 | 修补 | 以1.2为历史基线，继续补Sat-Eval与一般方差边界 |
| ENDO-4/5 | 定律与语言 | 描述/规范、恢复/实际生成分开 |
| ENDO-6 | frontier与领域例 | 9D DGLA保留；512000图报告待证据 |
| Horizon系列 | 实现比较 | 重述不等于效性已证，ML按真实图式使用 |
| SNT/DHH | 应用接口附录 | 不当母理论前提；撤回错误映射截断路线 |

## 来源逐项

### S00 · 冻结核心原文

文件：[01_FROZEN_CORE.md](frozen_original/01_FROZEN_CORE.md)。

收录状态：原文完整保留；编纂版不更改。

字节数：9391。

SHA-256：`753f2cf7c6da8aae50cf4ea56d5807bae2747ce509c1d2d0522be2189ba6086d`。

### S01 · 冻结时派生结果

文件：[02_DERIVED_THEORY.md](frozen_original/02_DERIVED_THEORY.md)。

收录状态：原文保留；按总稿的精确条件使用。

字节数：8582。

SHA-256：`ea62123e8e433085ac86c4679acff40082c762c526d6a0c188d98581bedfeac9`。

### S02 · 冻结时禁用推理

文件：[03_NO_GO_AND_RETRACTIONS.md](frozen_original/03_NO_GO_AND_RETRACTIONS.md)。

收录状态：保留；一般绝对唯一性 no-go 按 ENDO-5 收窄。

字节数：7017。

SHA-256：`6472f5a13a9e3f0e0c9045c950792a4f677d2f77457491ab46268ffdfaef7e5e`。

### S03 · 研究治理规则

文件：[05_RESEARCH_PROTOCOL.md](frozen_original/05_RESEARCH_PROTOCOL.md)。

收录状态：保留；非数学存在性公理。

字节数：3624。

SHA-256：`1d7f1cf94ca9e919ea5d642357256552bb65ef00f3d5df6c24e40b0ae4ef2722`。

### S04 · Strict v0.1

文件：[Generative_Equipment_Strict_Space_Valued_v0_1.md](source_archive/Generative_Equipment_Strict_Space_Valued_v0_1.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：27205。

SHA-256：`55d19e853a88790515a1505f7f2c0c23ea270af50e751c78cfc8a4660dbc74bf`。

### S05 · Strict v0.2

文件：[Generative_Equipment_Strict_Space_Valued_v0_2_Candidate.md](source_archive/Generative_Equipment_Strict_Space_Valued_v0_2_Candidate.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：19546。

SHA-256：`3ef6d885a8bd39bf4661e459774bc2389e5c2c268907f709682e3476dca7a448`。

### S06 · Strict v0.2 审计

文件：[Generative_Equipment_Strict_v0_2_Mathematical_Audit_and_Stress_Test_R1.md](source_archive/Generative_Equipment_Strict_v0_2_Mathematical_Audit_and_Stress_Test_R1.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：26905。

SHA-256：`2fbdb8b766af7e96865e5c97fda4ee80a3968e62a33edf3b826ffe0435b47ff3`。

### S07 · GE-R1

文件：[Generative_Equipment_All_Main_Lines_Development_R1.md](source_archive/Generative_Equipment_All_Main_Lines_Development_R1.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：30208。

SHA-256：`8846467504ca9de1be6ec721791dc69298f6a39a33b37299aa322c3c5a160379`。

### S08 · GE-R2

文件：[Generative_Equipment_Remaining_Proofs_Completion_R2.md](source_archive/Generative_Equipment_Remaining_Proofs_Completion_R2.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：27851。

SHA-256：`12f39f5a7937f5aba43e5ef01cacaf8dbf9ec44f7ff6759808d4823f86c425c9`。

### S09 · GE-R3

文件：[Generative_Equipment_Effectivity_Obstruction_Program_R3.md](source_archive/Generative_Equipment_Effectivity_Obstruction_Program_R3.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：25649。

SHA-256：`a5864b6579d2405c07f4c340cc15365c15dac57fa05225c1d0b7e3228d81f4f8`。

### S10 · GE-R4

文件：[Generative_Equipment_Cohomological_Torsor_Obstruction_R4.md](source_archive/Generative_Equipment_Cohomological_Torsor_Obstruction_R4.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：23354。

SHA-256：`5d2862124269ffa11c596239c28134c8ad623ed2d21c8249e3dbd8db18d8bc84`。

### S11 · GE-R5

文件：[Generative_Equipment_R3_Postnikov_Natural_Comparison_R5.md](source_archive/Generative_Equipment_R3_Postnikov_Natural_Comparison_R5.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：28459。

SHA-256：`c1bd801681ecf4d45a5a85f9d9da6cc89ed8af1f3b0d34fb75b7fb1bbe426e92`。

### S12 · GE-R6

文件：[Generative_Equipment_Coupled_Obstruction_Calculus_R6.md](source_archive/Generative_Equipment_Coupled_Obstruction_Calculus_R6.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：16132。

SHA-256：`691d3857aa1fcd48e150f31d392f5b651d5289cb67e2dacffe5a54f596923e66`。

### S13 · GE-R7

文件：[Generative_Equipment_Viability_Kernel_and_Residual_Obstruction_R7.md](source_archive/Generative_Equipment_Viability_Kernel_and_Residual_Obstruction_R7.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：18124。

SHA-256：`a93d0d6756cf6f65be1f042fae095d26eed8237c78740abea14cf78dc3ad99a5`。

### S14 · GE-R8

文件：[Generative_Equipment_Obstruction_Fubini_and_Interchange_Defect_R8.md](source_archive/Generative_Equipment_Obstruction_Fubini_and_Interchange_Defect_R8.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：15235。

SHA-256：`5be9c0969c41287b9b1f774ad533ddd44b1de379630c89f1403e1147a777fd89`。

### S15 · GE-R9

文件：[Generative_Equipment_Coherent_Interchange_Descent_R9.md](source_archive/Generative_Equipment_Coherent_Interchange_Descent_R9.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：12678。

SHA-256：`742ab8868da57fff651b9b25f0d57975e04cb71acdc3efa2ff3454d01455be8e`。

### S16 · GE-R10

文件：[Generative_Equipment_Polynomial_Coupl_Calculus_R10.md](source_archive/Generative_Equipment_Polynomial_Coupl_Calculus_R10.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：13527。

SHA-256：`ad9a9032ff6f9e7a408dd6b41b8df1708fe4a8fe95e467afba99e5d262644a53`。

### S17 · GE-R11

文件：[Generative_Equipment_Nilpotent_Central_Refinement_R11.md](source_archive/Generative_Equipment_Nilpotent_Central_Refinement_R11.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：16061。

SHA-256：`a5ed9bfe134f3a2ab0cedc31000def80b5a724292717890a3ad0bc3b09b17dcf`。

### S18 · GE-R12

文件：[Generative_Equipment_Finite_Master_Theorem_R12.md](source_archive/Generative_Equipment_Finite_Master_Theorem_R12.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：14949。

SHA-256：`6dc694789b1a2916c2455d8f96281a040acb37b6683c5bab5411397d31fd4735`。

### S19 · GE-R13

文件：[Generative_Equipment_R9_R12_Strict_Reality_Audit_R13.md](source_archive/Generative_Equipment_R9_R12_Strict_Reality_Audit_R13.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：13382。

SHA-256：`7ff36153c75b0129ae2de27a5dfbdc5b7080ddef0d39286595b39a3ef0bf48c1`。

### S20 · GE-R14

文件：[Generative_Equipment_Reality_Benchmarks_R14.md](source_archive/Generative_Equipment_Reality_Benchmarks_R14.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：9521。

SHA-256：`841d28f6e5e5aa8559bf979918d37f0c64f8b1410e69cb3a156b817ffa5278f2`。

### S21 · GE-R15

文件：[Generative_Equipment_Higher_Coupl_and_Viability_Cubes_R15.md](source_archive/Generative_Equipment_Higher_Coupl_and_Viability_Cubes_R15.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：14223。

SHA-256：`c48d20b58055f23417c7a060b0dcbbeaa300ddc1b0a6eb068cf4f47590a0dd66`。

### S22 · GE-R16

文件：[Generative_Equipment_Optimal_Arity_Derived_Coupl_and_Massey_Matching_R16.md](source_archive/Generative_Equipment_Optimal_Arity_Derived_Coupl_and_Massey_Matching_R16.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：18349。

SHA-256：`96518894c8a5fe83ee9e02424034cf0120bac8c0a5a476e2df985e957a66450b`。

### S23 · GE-R17

文件：[Generative_Equipment_R17_Moment_Angle_Support_and_Cube_Universality.md](source_archive/Generative_Equipment_R17_Moment_Angle_Support_and_Cube_Universality.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：15000。

SHA-256：`e53cfe4dd93d556fa9a222863bb7311b0ec696c6de323b6921368b8b2f3634f5`。

### S24 · GE-R18

文件：[Generative_Equipment_R18_Graph_Holonomy_and_First_Nonlinear_Threshold.md](source_archive/Generative_Equipment_R18_Graph_Holonomy_and_First_Nonlinear_Threshold.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：13626。

SHA-256：`482df71a762589644c0c8ffac6e90b23a176512c455b50a939e8962efdb93549`。

### S25 · GE-R19–R23

文件：[Generative_Equipment_R19_R23_Five_Step_Generalization_and_Core_Audit.md](source_archive/Generative_Equipment_R19_R23_Five_Step_Generalization_and_Core_Audit.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：17607。

SHA-256：`53a5178b7587ae2e9adce67d9d49f8dbe25a24eb88826379cd860385b7d5ae3f`。

### S26 · GE-R24–R27

文件：[Generative_Equipment_R24_R27_ProP_Galois_and_Cech_Deformation.md](source_archive/Generative_Equipment_R24_R27_ProP_Galois_and_Cech_Deformation.md)。

收录状态：纳入整理；数学地位见定理账本，历史审计计数未重跑。

字节数：19108。

SHA-256：`0ec8868eb383c94c191bd5bad5758b98201bf3db52ab3b7377e604c087a1b3fc`。

### S27 · GE-R28–R35

文件：[Generative_Equipment_R28_R35_Saturation_and_NonSplit_Corrections.md](source_archive/Generative_Equipment_R28_R35_Saturation_and_NonSplit_Corrections.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：28502。

SHA-256：`99602533b0cdce9d729c7d0f8abd364f25e4cc99aaecdeafee4e0d48f8af6417`。

### S28 · R22/R27 独立审计原稿

文件：[Generative_Equipment_Independent_Audit_2026-09-29.md](source_archive/Generative_Equipment_Independent_Audit_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：11819。

SHA-256：`b5779413045a7ee73934f223a4e5b290a3ea6b9589eb918e2fdb7edbd30244a4`。

### S29 · ENDO-1

文件：[Generative_Equipment_ENDO1_Intrinsic_Problem_Generation_2026-09-29.md](source_archive/Generative_Equipment_ENDO1_Intrinsic_Problem_Generation_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：24872。

SHA-256：`766ea08efc227976941fa9374e9f8aa3ad3ec412d26f656688aa33c7a0b5289e`。

### S30 · ENDO-2

文件：[Generative_Equipment_ENDO2_Structural_Generation_and_Relative_Completeness_2026-09-29.md](source_archive/Generative_Equipment_ENDO2_Structural_Generation_and_Relative_Completeness_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：32789。

SHA-256：`08c856d7fb6eb71187cd042e6ec4295752f052b4a44baede55d0d0c41ebaabec`。

### S31 · ENDO-3 v1.0

文件：[Generative_Equipment_ENDO3_Grammar_Genesis_and_Universal_Repair_2026-09-29.md](source_archive/Generative_Equipment_ENDO3_Grammar_Genesis_and_Universal_Repair_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：30917。

SHA-256：`9b925c99f3a2fee5faa87bbc45c7399465994605ca980561f5ace1e3f0a4299c`。

### S32 · ENDO-3 v1.1

文件：[Generative_Equipment_ENDO3_v1_1_Repaired_Theorems_2026-09-29.md](source_archive/Generative_Equipment_ENDO3_v1_1_Repaired_Theorems_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：17168。

SHA-256：`ecdd15e1085279db9ac006670b7ceb2fcd194c5657fe0c8103daa5005034fb54`。

### S33 · ENDO-3 v1.1 压测

文件：[Generative_Equipment_ENDO3_v1_1_Large_Scale_Stress_Test_2026-09-29.md](source_archive/Generative_Equipment_ENDO3_v1_1_Large_Scale_Stress_Test_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：19762。

SHA-256：`249a4d23c3a4f39cf91e037f52d1c4e8cbe6256dc335c82e219d6ab79c060e57`。

### S34 · ENDO-3 v1.2

文件：[Generative_Equipment_ENDO3_v1_2_Coherent_Repair_and_Actualization_2026-09-29.md](source_archive/Generative_Equipment_ENDO3_v1_2_Coherent_Repair_and_Actualization_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：23463。

SHA-256：`eb6923324f74650cd7e6eac5e7c8fb1a4b2c0050f2584e1945de01a76dc8aebe`。

### S35 · ENDO-4

文件：[Generative_Equipment_ENDO4_Law_Signature_Genesis_2026-09-29.md](source_archive/Generative_Equipment_ENDO4_Law_Signature_Genesis_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：22213。

SHA-256：`afbd255c925c031a3bfe513d769e89128407ebca815169c4986dade3774abe50`。

### S36 · ENDO-5

文件：[Generative_Equipment_ENDO5_Structural_Logic_Recovery_2026-09-29.md](source_archive/Generative_Equipment_ENDO5_Structural_Logic_Recovery_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：27677。

SHA-256：`3637d4fc3ea1e02eb676d6bc05917fb0bb8d7e3c1b67381799763007122752a3`。

### S37 · ENDO-6

文件：[Generative_Equipment_ENDO6_Five_Step_Program_2026-09-29.md](source_archive/Generative_Equipment_ENDO6_Five_Step_Program_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：9935。

SHA-256：`3a29626d8a25703004db14684746e15f2f457f4a66ed4718dd5df7ea17ed02a8`。

### S38 · 512000 图分类报告

文件：[ENDO6_NextStage_MomentAngle_Ordinary_Fourfold_2026-09-29.md](source_archive/ENDO6_NextStage_MomentAngle_Ordinary_Fourfold_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：5160。

SHA-256：`c0c922871f3abe54cebce71415691347e1fd4c5a345fc2088435b0967615e1fb`。

### S39 · Two-cell SNT R1

文件：[Two_Cell_Loop_Space_Postnikov_Rigidity_R1_2026-09-29.md](source_archive/Two_Cell_Loop_Space_Postnikov_Rigidity_R1_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：7643。

SHA-256：`24501ad3f1d55fcfa02d9914de0f8b1d0ad26e516c75f61c6881815450b3a1e0`。

### S40 · Odd-spherical SNT 稿

文件：[Odd_Spherical_Loop_Postnikov_Rigidity_2026-09-29.md](source_archive/Odd_Spherical_Loop_Postnikov_Rigidity_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：7854。

SHA-256：`16ab597284b223514ea30d4f0f93b00a012dd7fafedc46bcb7c535dae0bc4991`。

### S41 · Horizon Effectivity

文件：[Generative_Equipment_Horizon_Effectivity_and_Coherence_at_Infinity_2026-09-29.md](source_archive/Generative_Equipment_Horizon_Effectivity_and_Coherence_at_Infinity_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：16232。

SHA-256：`0296a7882c867b2c34a617f453ab1863d3f8e966623bc6e6325a6af447ae50d4`。

### S42 · Exact Horizon Completeness

文件：[Generative_Equipment_Exact_Horizon_Completeness_2026-09-29.md](source_archive/Generative_Equipment_Exact_Horizon_Completeness_2026-09-29.md)。

收录状态：以实际挂载原文为准；适用边界及订正见总稿。

字节数：13601。

SHA-256：`dd0f5baa5c28ae2e7791fc793988e0ce44b42a0a242f23c84b2c3e6d59d4ea38`。

### S43 · DHH 旧证明策略

文件：[Undirected_Graph_DHH_Generative_Equipment_Proof_Strategy.md](source_archive/Undirected_Graph_DHH_Generative_Equipment_Proof_Strategy.md)。

收录状态：仅接口审计；映射截断建议被本版否定。

字节数：21895。

SHA-256：`5ee813d53f70efa3fb60ec71a4e6729c923bf2a822be56b2723a3b8801e42ced`。

### S44 · DHH-R96 阶段报告

文件：[Undirected_DHH_R96_Critical_Omnifacial_Six_Exclusion_and_PBFT6_2026-09-29.md](source_archive/Undirected_DHH_R96_Critical_Omnifacial_Six_Exclusion_and_PBFT6_2026-09-29.md)。

收录状态：记录报告状态；未重证整个 DHH 依赖链。

字节数：11448。

SHA-256：`74a7ad2b419d715090b847b33ee39c8ee3833d6b13d0a51a286bc375d8c2bc17`。

### S45 · R22 单例核验脚本

文件：[verify_r22_counterexample.py](source_archive/verify_r22_counterexample.py)。

收录状态：本次局部运行，不是 512000 图完整分类程序。

字节数：5812。

SHA-256：`08cdbe0f6cbda7c3ee1b06317c4add0b564a1f5ce526744c86419481800a27b7`。

### S46 · Strict v0.1 审计

文件：[Generative_Equipment_Strict_v0_1_Large_Scale_Stress_Test_R1.md](source_archive/Generative_Equipment_Strict_v0_1_Large_Scale_Stress_Test_R1.md)。

收录状态：历史审计记录，不视为全领域正确性证书。

字节数：37150。

SHA-256：`4f75acf87841e1334a70f5d434563ecb9c0ae0ba3766039dee25529d9940b80d`。

### S47 · 冻结后早期评估

文件：[Generative_Equipment_Frozen_v1_0_Detailed_Assessment.md](source_archive/Generative_Equipment_Frozen_v1_0_Detailed_Assessment.md)。

收录状态：历史评估，不作为新增定理依赖。

字节数：25565。

SHA-256：`ece3aba490d7001736316723c41f4efb1cec9a86583af87516b5734a14457a99`。

### S48 · R22 9/10边受限枚举程序

文件：[verify_r22_n4_extremal.py](source_archive/verify_r22_n4_extremal.py)。

收录状态：未重跑；不是普通 Massey 饱和分类程序。

字节数：7587。

SHA-256：`ba660a8855736833849ae26467b02f656fd84ba4763092a2a6a9b5c58aae14c3`。

## 未纳入完整审计的内容

本包不把整个独立DHH文件库、QWGS/Φ与其他数论物理项目归并为已重审母理论。更早的历史景/历史拓扑斯等动机以冻结核心的来源背景保留，若需要其原始独立版本，应另作专门档案。

此限定避免把“所有理论”写成对当前不可穷尽资料库的全覆盖承诺。本包的完整性是明确主线的文档、状态和接口覆盖。
