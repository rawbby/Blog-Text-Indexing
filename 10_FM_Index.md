# FM-Index

## FM-index (BWT + rank) — compressed full-text index storing BWT and sampled SA

**Complexities (formal)**

* Space = n H₀ + o(n) bits
* count(P) = O(m)
* locate(P) = O(m · s) where s = sampling step

**Description**
Backward search uses rank to shrink an SA interval one character at a time, so counting matches costs exactly m rank queries; locating an occurrence then walks LF-mapping until a pre-sampled SA value is reached.

## Backward search — right-to-left pattern scan narrowing SA interval each step

*(complexities above)*

## count(P) — returns number of pattern occurrences from interval size

*(O(m))*

## locate(P) with sampled SA — LF-walk until reaching stored SA sample to obtain position

*(O(m · s))*

## report/access text positions — retrieve occurrence list or text substrings

*(locate plus block tree/CSA tricks)*

## Space O(n log σ) bits — full index in entropy-bounded space

*(formal bound already given)*
