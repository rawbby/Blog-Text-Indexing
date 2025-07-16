# Tries

## Plain trie — naive prefix tree that stores one character per edge for fast dictionary look-ups

**Complexities (formal)**

* Space ≃ Θ(N · σ) pointers ≈ O(N σ) bits
* Lookup / insert / delete = O(m) where m = key length

**Description**
Memory grows with both the total text size N and the alphabet size σ because every node keeps a σ-wide child reference array. Each operation just follows one edge per character, so cost is linear in the length of the searched or inserted key.

## Compact trie — path-compressed trie that merges single-child edges to save memory

**Complexities (formal)**

* Space = Θ(k) nodes (k = distinct stored prefixes)
* Query / update = O(m)

**Description**
By collapsing chains of unary nodes into single edges, the structure now stores only branching points; memory is proportional to the number of unique prefixes, yet you still traverse one character per step, so work stays linear in the pattern length.

## Patricia (blind) trie — binary compressed trie storing bitstrings; optimised for longest-prefix search

**Complexities (formal)**

* Space = Θ(k) nodes
* Longest-prefix search = O(L) bit inspections (L = bits in key)

**Description**
Keys are treated as bitstrings; every node stores only the branching bit position, so memory is minimal. A search just tests each discriminating bit once, leading to time proportional to the key’s bit-length.

## Blind-search algorithm on Patricia — bit-wise walk that compares only branch bits, not full labels

**Complexities (formal)**

* Search = O(L) worst-case, but compares **only** O(#branch bits) < L actual bits

**Description**
Instead of rereading entire edge labels, the algorithm jumps directly between branching positions, touching far fewer bits than a character-wise scan while keeping the same asymptotic bound.

## Parallel / distributed Patricia construction — scalable build that partitions keys across cores or nodes

**Complexities (formal)**

* Build ≈ O(N / p + sort(N)/p) with p cores, plus O(N log p) communication in the distributed model
* Final space as above (Θ(k))

**Description**
Each processor builds a partial trie for its slice and the slices are merged; work per core is linear in its share of the input, so build time scales almost inversely with the number of cores until merge overhead dominates.

## **Trie child-representation trade-offs** — unsorted, sorted, hashed, bit-packed child arrays and their time/space costs

**Complexities (formal)**

| representation  | search             | min space     | notes                       |
| --------------- | ------------------ | ------------- | --------------------------- |
| unsorted array  | O(σ)               | Θ(σ) ptrs     | fastest insert, slow search |
| sorted array    | O(log σ)           | Θ(σ) ptrs     | binary search               |
| hash table      | O(1) expected      | Θ(σ) ptrs     | extra hash memory           |
| bit-packed mask | O(1) (rank/select) | σ bits + o(σ) | alphabet must be small      |

**Description**
Choosing how to map outgoing characters to child links trades RAM against per-step time: bit-packed succinct layouts shrink to one bit per letter at the cost of extra rank/select logic, whereas a simple array wastes memory but gives constant-time pointer indexing.

## Succinct tree encodings (BP, DFUDS, LOUDS) — 2 n + o(n)-bit bit-vector layouts of ordered trees

**Complexities (formal)**

* Space = 2n + o(n) bits for n nodes (≈ < 1 bit/edge)
* Parent/child/sibling/navigation = O(1)

**Description**
The whole tree topology is written as a balanced parenthesis or degree sequence bitvector; with constant-time rank/select primitives you can jump between nodes in O(1) while using space close to the information-theoretic minimum.

## rank(c, i) bit-vector primitive — count of set bits ≤ i, used throughout succinct structures

**Complexities (formal)**

* Space = n + o(n) bits (RRR: n H₀ + o(n))
* Query = O(1)

**Description**
An auxiliary directory on top of the bitvector lets you answer “how many 1s up to position i?” with two or three memory accesses, while the compression term n H₀ ties the footprint to the entropy of the bit distribution.

## select(k) bit-vector primitive — position of the k-th set bit, inverse of rank

**Complexities (formal)**

* Same space as rank
* Query = O(1)

**Description**
The data structure stores small lookup tables per block so it can binary-search inside a machine word, giving constant-time location of any k-th 1 without scanning the bits linearly.
