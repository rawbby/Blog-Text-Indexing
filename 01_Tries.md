# Tries

## Plain trie — naive prefix tree that stores one character per edge for fast dictionary look-ups
## Compact trie — path-compressed trie that merges single-child edges to save memory
## Patricia (blind) trie — binary compressed trie storing bitstrings; optimised for longest-prefix search
## Blind-search algorithm on Patricia — bit-wise walk that compares only branch bits, not full labels
## Parallel / distributed Patricia construction — scalable build that partitions keys across cores or nodes
## **Trie child-representation trade-offs** — unsorted, sorted, hashed, bit-packed child arrays and their time/space costs
## Succinct tree encodings (BP, DFUDS, LOUDS) — 2 n + o(n)-bit bit-vector layouts of ordered trees
## rank(c, i) bit-vector primitive — count of set bits ≤ i, used throughout succinct structures
## select(k) bit-vector primitive — position of the k-th set bit, inverse of rank
