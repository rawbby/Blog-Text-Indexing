# Prerequisites

## Asymptotic Analysis - Big-O Notation

Good algorithms need **correctness** and **scalability**.
Asymptotic notation gives us a compact language for the second part:
how running time or memory demand scales when the input size `n` becomes large.
This chapter builds intuition first, then refines it with formal definitions
and practical patterns.

---

### The Big-O Family

| Symbol           | Reads as              | What it promises                                                                                                                      | Formal                                                                 |
|------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `f(n) ∈ O(g(n))` | “Big-O of *g*”        | **upper bound**        — beyond some threshold `n₀`, `f` never exceeds some constant `c`·`g`                                          | `∃c>0,     ∃n₀ : ∀n≥n₀, f(n) ≤ c·g(n)`                                 |
| `f(n) ∈ Ω(g(n))` | “Omega of *g*”        | **lower bound**        — beyond some threshold `n₀`, `f` never drops below some constant `c`·`g`                                      | `∃c>0,     ∃n₀ : ∀n≥n₀, f(n) ≥ c·g(n)`                                 |
| `f(n) ∈ o(g(n))` | “little-o of *g*”     | **strict upper bound** — `f` eventually\* stays below every constant `c`·`g`                                                          | `∀c>0,     ∃n₀ : ∀n≥n₀, f(n) < c·g(n)` (equivalently `limₙ→∞ f/g = 0`) |
| `f(n) ∈ ω(g(n))` | “little-omega of *g*” | **strict lower bound** — `f` eventually\* outgrows every constant `c`·`g`                                                             | `∀c>0,     ∃n₀ : ∀n≥n₀, f(n) > c·g(n)` (equivalently `limₙ→∞ f/g = ∞`) |
| `f(n) ∈ Θ(g(n))` | “Theta of *g*”        | **tight bound**        — `f` and `g` eventually\* grow at the same rate <br> (staying within constant-factor multiples of each other) | `∃c₁,c₂>0, ∃n₀ : ∀n≥n₀, c₁·g(n) ≤ f(n) ≤ c₂·g(n)`                      |

\* eventually means “beyond some threshold `n₀`”, is just sounds better in some places.

**Quick examples:**

* `n ∈ O(n log n)` — adding log n makes the right hand side grow faster
* `log n ∈ o(√n)` — every root beats every logarithm
* `n log n ∉ O(n)` — the extra log n factor cannot be hidden by a constant
* `3 n² + 7 n ∈ Θ(n²)` — constants and lower-order terms vanish in Θ
* `log₁₀ n ∈ Θ(log₂ n)` — base change is just a constant factor
* `n / log n ∈ o(n)` — dividing by a (slow) log makes it strictly smaller than n
* `n² ∈ Ω(n log n)` — quadratic is always at least as big as linear-log
* `2^{√n} ∈ ω(n¹⁰⁰)` — even a “slow” exponential eventually beats any fixed-degree polynomial
* `n^{\log n} ∈ ω(2ⁿ)` — raising n to log n grows faster than any fixed-base exponential

---

### Amortised Analysis

Some data structures fluctuate between cheap and expensive operations.
**Amortised analysis** proves that **over any long sequence**,
the **average cost** per operation is small even if individual ops spike.

1. **Aggregate method** — Sum the total work of the whole sequence, divide by the number of ops.
   <br>*Example*: doubling dynamic array: total work for `m` pushes is `< 3m`, so amortised `O(1)` each.
2. **Accounting method** — Charge each cheap op a little extra “credit” to pre-pay future expensive ones.
3. **Potential method** — Define a numerical potential Φ(state).
   Amortised cost = *actual* + ΔΦ. If Φ never falls below zero, the aggregate bound holds.

Key takeaway: amortised `O(1)` often beats worst-case `O(k)` if the spikes are rare.

---

### Worst-Case, Expected and “With High Probability”

| Flavour                            | Statement                                                        | When to use                                                            |
|------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------|
| **Worst-case**                     | Time bound holds for every input of size `n`.                    | Mission-critical, adversarial inputs                                   |
| **Expected**                       | Average over random choices (from algorithm or input model).     | Probabilistic data structures, average-case tuning                     |
| **With high probability (w.h.p.)** | Bound holds with probability `1 − n^{−c}` for some constant `c`. | Hash tables, skip lists: failures are astronomically rare as `n` grows |

**Example — Hash-table search:**

- *Expected* `O(1)`
- *w.h.p.* `O(log n)` (chains stay short)
- *Worst-case* `O(n)` (if all keys collide)

Rule of thumb: report **all three** if they differ; otherwise state the strongest one that is still honest.

---

### Typical Growth Classes (Your Mental Speedometer)

```
1          —  constant
log log n  —  double-logarithmic
log n      —  logarithmic
(log n)^c  —  polylogarithmic
                                 ↑ almost constant
n          —  linear
n log n    —  linear-log
n²         —  quadratic
n^k        —  polynomial (k>2)
                                 ↓ almost infeasible
cⁿ         —  exponential (c>1)
n!         —  factorial
```

**How to read it:**

* one step up the ladder can turn an “impossible” problem into a practical solution
* anything *polylogarithmic* often acts “almost constant” for realistic `n` (≤ 2³²)
* crossing from *polynomial* to *exponential* is where algorithms usually become infeasible

---
