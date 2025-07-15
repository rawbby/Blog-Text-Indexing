# Compressed Suffix Array

## Compressed suffix array (CSA) — stores Ψ function instead of full SA
## Ψ-function navigation — maps SA\[i] → SA\[i] + 1; permits sequential traversal
## SA sampling every t positions — stores absolute SA to recover values in O(t) steps
## Elias–Fano encoding of Ψ — compresses monotone Ψ values to near-entropy space
## log-log-n recursive lookup — multi-level sampling yields O(log log n) SA access
## CSA space-vs-time trade-off — tuning sample rate balances memory and query speed
