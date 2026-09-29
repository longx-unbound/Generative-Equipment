# 04 — Pressure Test Ledger

本表只记录测试对象、主要机制和冻结后的判定。  
`PASS` 表示核心无需修改。  
`DERIVED` 表示发现了新的派生工具，但不改核心。  
`REPAIR-HIST` 表示该例曾经迫使旧版本修正，修正已经吸收到 Frozen v1.0。

---

## A. 代数 / 交换代数 / 表示论

| 例子 | 判定 | 主要测试点 |
|---|---|---|
| finitely presented modules | PASS | compact factorization，\(\forall f\exists i\) 非 uniform |
| Noetherian ideals | PASS | lattice compactness / stabilization |
| Hilbert basis theorem | PASS | global finite-generation sector |
| derived category localization | PASS | law-generated localization |
| perfect complexes | PASS | compact detection |
| stable category of Frobenius category | PASS | arrow-level quotient，不只是 object residue |
| group completion | PASS | reflection 可同时 collapse + extend |
| free group | PASS | comma universal object / adjunction |
| universal enveloping algebra | PASS | carrier-changing non-idempotent generation |
| algebraic closure | PASS | unique type + isotropy，非 universal |
| perfect closure | PASS | rigid universal closure |
| injective hull | PASS | weak universality + isotropy |
| minimal free resolution | PASS | unique type ≠ contractible moduli |
| primary decomposition | PASS | branching but stable invariant |
| universal central extension | PASS | \(H_2\) obstruction |
| profinite completion | PASS | completion 不必 idempotent reflection |
| henselization | PASS | finite-resolution blindness |
| Hensel lifting | PASS | lifting + inverse-limit realization |
| normalization | PASS | admissible comma universality，非全局 adjunction |
| Dedekind–MacNeille completion | PASS | extremal/minimal rigidification |
| exact completion | PASS | world-level quotient horizon |

---

## B. 代数几何 / 几何

| 例子 | 判定 | 主要测试点 |
|---|---|---|
| formal completion | PASS | support coarse-graining 的 future-context descent |
| finite presentation in completion | PASS | intra-witness uniformization |
| elimination of imaginaries | PASS | quotient representability vs horizon expansion |
| \(T^{eq}\) | PASS | quotient horizon completion |
| ACVF geometric sorts | PASS | compressed adequate horizon |
| formal moduli / dg Lie | PASS | semantic coordinatization ≠ ordinary representability |
| blow-up | PASS | terminal polarity / admissible universal property |
| Hilbert scheme | PASS | moduli functor本身 representable |
| Picard functor | PASS | raw problem需先 descent saturation |
| Néron model | PASS | test-doctrine-relative representability |
| Albanese variety | PASS | clean universal mapping problem |
| Grothendieck existence | PASS | formal-to-actual algebraization |
| Grothendieck algebraization | PASS | formal subschemes effectivity |
| Artin approximation | PASS | approximation ≠ algebraization |
| Artin algebraicity criteria | PASS | effectivity为独立条件 |
| Beauville–Laszlo gluing | PASS | whole comparison equivalence |
| Riemann existence theorem | PASS | coordinatization / equivalence |
| GAGA | PASS | coordinatization / algebraization |
| functorial resolution of singularities | PASS | functoriality ≠ universality |

---

## C. 同伦论 / 高阶范畴 / 拓扑

| 例子 | 判定 | 主要测试点 |
|---|---|---|
| Postnikov tower | PASS | uniform truncation / higher coherence |
| homotopy groups | PASS | conservative ≠ reconstructive |
| Bousfield localization | PASS | law/doctrine-relative localization |
| hyperdescent vs Čech descent | PASS | shape horizon matters |
| suspension-loop | PASS | adjunction ≠ generativity |
| universal covering space | PASS | framing kills isotropy |
| plus construction | PASS | homotopy-universal + observation-relative novelty |
| stabilization / spectra | PASS | world-level universal construction |
| presheaf free cocompletion | PASS | world-level generation |
| Ind-completion | PASS | scale polymorphism |
| Pro-completion | PASS | dual world-level completion |
| Karoubi/Cauchy completion | PASS | Morita-inert completion |
| sobrification | PASS | rigid reflection but locale-observationally inert |
| left-complete \(t\)-structure | PASS | tower effectivity |
| non-left-complete derived categories | PASS | all truncations ≠ actual recovery |
| phantom maps | PASS | finite observations can miss global information |
| Brown representability | PASS | internal representability criterion |
| spectral sequences | REPAIR-HIST | stage information can be revised/killed |

---

## D. 分析 / 泛函分析 / PDE

| 例子 | 判定 | 主要测试点 |
|---|---|---|
| Banach completion | PASS | approximation ≠ realization |
| \(c_{00}\subset c_0\) | PASS | pointwise vs uniform approximation |
| Goldstine | PASS | weak-* density ≠ realization |
| conditional expectation | PASS | enriched universal projection |
| martingale convergence | PASS | exact failure + approximate convergence |
| Dini theorem | PASS | compactness-driven promotion |
| Arzelà–Ascoli | PASS | equicontinuity + compactness |
| Stone–Weierstrass | PASS | target-dependent approximation complexity |
| Uniform Boundedness | PASS | Baire + algebraic propagation |
| Rellich–Kondrachov | PASS | subsequence extraction promotion |
| Banach–Alaoglu | PASS | nets vs sequences |
| Fredholm alternative | PASS | kernel/cokernel obstruction |
| Lax–Milgram | PASS | coercivity effectivity engine |
| Michael selection theorem | PASS | existence without rigidity |
| Kirszbraun extension | PASS | extension effectivity without uniqueness |
| GNS construction | PASS | quotient + completion + cyclic rigidity |
| RKHS / Moore–Aronszajn | PASS | kernel → rigid Hilbert realization |
| Riesz–Markov | PASS | coordinatization rather than active generation |
| Stinespring dilation | PASS | minimality + gauge quotient |
| Hodge theorem | PASS | configuration-dependent rigidification |

---

## E. 概率 / 测度

| 例子 | 判定 | 主要测试点 |
|---|---|---|
| Kolmogorov extension | PASS | unbounded finitary reconstruction |
| regular conditional distributions | PASS | a.s. gauge saturation |
| Egorov theorem | PASS | almost-uniform promotion |
| Radon–Nikodym | PASS | a.e.-unique realization |
| Carathéodory extension | PASS | existence vs uniqueness hypotheses |
| Prokhorov theorem | PASS | extraction promotion, not effectivity |
| Hamburger moment problem | PASS | finite positivity → global measure |
| multidimensional moment problem | PASS | same local positivity doctrine may fail |

---

## F. 逻辑 / 模型论 / 组合

| 例子 | 判定 | 主要测试点 |
|---|---|---|
| first-order compactness | PASS | finitary consequence closure |
| \(L_{\omega_1,\omega}\) compactness failure | PASS | genuine infinitary witness |
| Henkin construction | PASS | procedural branch choice |
| \(\kappa\)-saturated models | PASS | cardinal-relative effectivity |
| Fraïssé limit | PASS | finite amalgamation → global structure |
| Rado graph | PASS | countable-scale rigidity |
| Helly theorem | PASS | finite promotion compression rank \(d+1\) |
| de Bruijn–Erdős coloring | PASS | finite local → global compactness |
| Kőnig lemma | PASS | finite branching → infinite branch |
| Aronszajn tree | PASS | transfinite failure of bounded compactness |
| Tutte deletion–contraction | PASS-NEGATIVE | structurally compatible but low predictive content |

---

## G. 算术 / 局部到整体 / 上同调障碍

| 例子 | 判定 | 主要测试点 |
|---|---|---|
| Hasse–Minkowski | PASS | local contexts complete in quadratic sector |
| Hasse principle failures | PASS | local solvability ≠ global effectivity |
| Grunwald–Wang | PASS | local-to-global with exceptional obstruction |
| Tate–Shafarevich group | PASS | explicit local-global obstruction object |
| banded gerbes / \(H^2\) | PASS | local nonempty connected but no global object |
| Mittag–Leffler | PASS | stabilization effectivity engine |
| \(R^1\!\lim\) | PASS | derived inverse-limit obstruction |
| infinite CRT / profinite residues | PASS | every finite subsystem effective, global integer may fail |

---

## H. 对偶 / 协调化 / 表示理论型重构

| 例子 | 判定 | 主要测试点 |
|---|---|---|
| Stone duality | PASS | coordinatization ≠ generation |
| Sullivan minimal model | PASS | rational homotopy coordinatization |
| formal moduli ↔ dg Lie | PASS | controller equivalence sector |
| GAGA | PASS | algebraic/analytic semantic equivalence |

---

# Overall Pressure-Test Verdict

Frozen v1.0 核心在当前测试集中：

\[
\boxed{\text{CORE PASS}}
\]

已出现的真正 repair 均已吸收到冻结版本，包括：

- fiber → general horizontal problem；
- adjunction降级为 sector；
- moduli-first；
- whole-moduli-collapse 修正；
- pro-effectivity降级为 sector；
- monotone resolution撤回；
- scalar detection height撤回；
- direct Reach\(\dashv\)Obs撤回。

自冻结核心提出后，新例子默认不再触发 core modification，除非构成明确反例。
