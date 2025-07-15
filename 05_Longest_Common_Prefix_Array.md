# Longest Common Prefix Array

## LCP array — stores LCP of adjacent suffixes in SA; size = n − 1 integers
## Kasai LCP construction — O(n) time using inverse-SA and running LCP
## Permuted LCP (PLCP) — LCP values rearranged to text order for cache locality
## Φ (Phi) algorithm for PLCP — computes PLCP in O(n) using next-smaller-suffix links
## RMQ on LCP for LCE / LCA — range-minimum queries give longest common extension in O(1)
