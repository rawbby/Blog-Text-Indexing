# Suffix Arrays

## Suffix array (SA) — lexicographically sorted array of suffix start positions

**Complexities (formal)**

* Space = n ⌈log₂ n⌉ bits
* Binary-search pattern = O(m log n)

**Description**
Only the starting positions are stored; a binary search ­compares the pattern against at most log₂ n suffixes, each comparison scanning up to m characters.

## SA-IS linear-time construction — induced-sorting algorithm in O(n) time and O(σ) extra space

**Complexities (formal)**

* Build = O(n) worst-case
* Extra workspace = O(σ)

**Description**
The text is partitioned into LMS substrings that are recursively sorted; each phase only scans or induces order from already sorted pieces, keeping overall linear work.

## pS⁵ parallel suffix sorting — multicore SA build using sampling and prefix-doubling

**Complexities (formal)**

* Build ≈ O((n/p) log n) per core plus synchronisation

**Description**
A sample of suffixes is sorted first; remaining suffixes are bucket-sorted via prefix-doubling, letting multiple cores handle disjoint buckets concurrently.

## Binary-search pattern matching with SA — O(m log n) search comparing pattern to text suffixes

*(see first SA item)*
