# Block Trees

## Block tree (LZ-compressed) — hierarchical block decomposition that stores repeated blocks once

**Complexities (formal)**

* Space = O(z τ log n) bits (z = LZ77 factors, τ = block size)
* access / rank / select = O(log n)

**Description**
The text is chunked into blocks which are themselves represented recursively; repeated blocks point to a single copy, so storage depends on the LZ factor count.

## Space bound O(z τ log n) — proved upper bound in terms of LZ77 factor z and block size τ

*(formal bound already above)*

## access(i) on block tree — random-access character retrieval in O(log n)

*(covered)*

## rank(c, i) on block tree — counts c up to i in O(log n)

*(covered)*

## select(c, k) on block tree — finds position of k-th c in O(log n)

*(covered)*
