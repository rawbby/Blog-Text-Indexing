# Burrows–Wheeler Transform

## Forward BWT — sorts all text rotations; groups similar contexts for compression

**Complexities (formal)**

* Transform = O(n log n) suffix-sort (O(n) with SA)
* Space = n log σ bits

**Description**
Sorting rotations puts characters with similar left contexts together, yielding long runs of equal symbols that later compressors exploit.

## Inverse BWT with LF-mapping — reconstructs original text using cumulative counts

**Complexities (formal)**

* Time = O(n)
* Space = n log σ bits (in-place possible)

**Description**
LF-mapping follows a permutation induced by cumulative character counts; a single pointer chase reconstructs the text linearly.

## Run count r in BWT — number of equal-letter runs; key repetitiveness parameter

**Formal** r ≤ n; smaller r ⇒ more repetitive
**Description**
Indexes like the r-index store data proportional to r rather than n, making highly repetitive texts dramatically cheaper.

## Move-to-front + RLE + entropy pipeline — standard BWT post-processing for high compression

**Complexities (formal)**

* Overall size ≈ n H₀ + runs overhead
* Encode/decode = O(n)

**Description**
MTF turns locality into small integers, RLE collapses integer runs, and entropy coding finishes the job, often approaching the k-th-order entropy.
