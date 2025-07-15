# Block Trees

## Block tree (LZ-compressed) — hierarchical block decomposition that stores repeated blocks once
## Space bound O(z τ log n) — proved upper bound in terms of LZ77 factor z and block size τ
## access(i) on block tree — random-access character retrieval in O(log n)
## rank(c, i) on block tree — counts c up to i in O(log n)
## select(c, k) on block tree — finds position of k-th c in O(log n)
