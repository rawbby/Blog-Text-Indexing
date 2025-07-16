# Compressed Suffix Array

## Compressed suffix array (CSA) — stores Ψ function instead of full SA

**Complexities (formal)**

* Space = n H₀ + o(n) bits
* SA\[i] access = O(t) with sample every t

**Description**
The Ψ mapping encodes SA as a near-sorted permutation; walking it t steps from the nearest sample reconstructs any suffix position.

## Ψ-function navigation — maps SA\[i] → SA\[i] + 1; permits sequential traversal

*(O(1) per step)*

## SA sampling every t positions — stores absolute SA to recover values in O(t) steps

*(formal above)*

## Elias–Fano encoding of Ψ — compresses monotone Ψ values to near-entropy space

**Complexities (formal)**

* Space ≈ n (H₀ + 2) bits
* Rank/select on Ψ = O(1)

**Description**
Splitting each integer into high and low parts plus a bitvector lets you compress a monotone sequence to within 2 bits/symbol of its zero-order entropy.

## log-log-n recursive lookup — multi-level sampling yields O(log log n) SA access

*(formal)*

## CSA space-vs-time trade-off — tuning sample rate balances memory and query speed

**Description**
Smaller sampling step t saves space linearly but increases SA lookup proportionally; the log-log-n recursion lessens this to sub-logarithmic time.
