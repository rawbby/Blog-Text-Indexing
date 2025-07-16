# Longest Common Prefix Array

## LCP array — stores LCP of adjacent suffixes in SA; size = n − 1 integers

**Complexities (formal)**

* Space = (n − 1) ⌈log₂ n⌉ bits
* Built with Kasai in O(n)

**Description**
For each neighbouring pair in SA the array tells how many characters they share; that information powers many string algorithms (e.g. RMQ-based LCE) with just linear extra space.

## Kasai LCP construction — O(n) time using inverse-SA and running LCP

*(covered above)*

## Permuted LCP (PLCP) — LCP values rearranged to text order for cache locality

**Complexities (formal)**

* Same size as LCP
* Convert = O(n)

**Description**
Reordering the LCP values to match text order means a linear walk of the text now touches consecutive memory cells, improving practical locality for later scans.

## Φ (Phi) algorithm for PLCP — computes PLCP in O(n) using next-smaller-suffix links

*(same bounds)*

## RMQ on LCP for LCE / LCA — range-minimum queries give longest common extension in O(1)

**Complexities (formal)**

* RMQ structure = 2n + o(n) bits
* Query = O(1)

**Description**
Reducing an LCE query to a minimum on the LCP subarray turns it into a constant-time problem with a succinct Cartesian-tree RMQ.
