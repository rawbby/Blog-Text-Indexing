# Wavelet Trees

## Level-wise wavelet tree — balanced binary tree supporting rank/select/access in O(log σ)

**Complexities (formal)**

* Space = n log σ + o(n log σ) bits
* Query = O(log σ)

**Description**
Each level stores one bit of every symbol; following those bits from root to leaf identifies the character or counts how often it appears before a position.

## Huffman-shaped wavelet tree — height proportional to −log p(c); reduces average query time

**Complexities (formal)**

* Expected query = O(H₀)
* Same space bound

**Description**
By biasing the tree shape to the symbol distribution, frequent characters end up nearer the root, decreasing the average number of levels traversed.

## Wavelet matrix — pointer-free variant that rearranges bits per level

**Complexities (formal)**

* Same space and asymptotic query time

**Description**
All bitvectors are kept contiguous; level-to-level mapping is arithmetic instead of pointers, improving cache behaviour without changing complexity.

## **RRR compressed bit-vector rank/select** — entropy-bounded bit-vector with O(1) ops

*(see rank/select earlier; same formal bounds)*

## rank(c, i) on wavelet tree — counts c up to i

*(O(log σ))*

## select(c, k) on wavelet tree — position of k-th c

*(O(log σ))*

## access(i) on wavelet tree — symbol at position i

*(O(log σ))*
