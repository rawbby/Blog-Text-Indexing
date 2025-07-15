# FM-Index

## FM-index (BWT + rank) — compressed full-text index storing BWT and sampled SA
## Backward search — right-to-left pattern scan narrowing SA interval each step
## count(P) — returns number of pattern occurrences from interval size
## locate(P) with sampled SA — LF-walk until reaching stored SA sample to obtain position
## report/access text positions — retrieve occurrence list or text substrings
## Space O(n log σ) bits — full index in entropy-bounded space
