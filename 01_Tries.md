# Tries – Complexities, Use‑Cases, and Notation

## Notation (local to this section)

* **N** – total number of characters stored across all keys
* **m** – length of the query key
* **σ** – alphabet size (number of distinct symbols that appear in any key)
* **k** – number of distinct stored prefixes / internal nodes
* **p** – number of hardware threads / distributed nodes
* **L** – bit‑length of a key (only for bit‑wise Patricia variants)
* **H₀** – zero‑order empirical entropy of a bitvector

Unless stated otherwise, runtimes are **worst‑case**. When an *expected* or *with‑high‑probability (w.h.p.)* bound is
tighter, it is listed in brackets.

---

## Plain trie — naive prefix tree (one character per edge)

A **plain trie** is a rooted tree that spells every stored string, character‑by‑character, along a unique root‑to‑leaf
path. Every internal node owns an array of pointers of length **σ**—one slot per possible outgoing character—so the
structure supports direct **child lookup in O(1)** and records *exactly which keys exist*.

| Metric                         | Bound                                       | Notes                                  |
|--------------------------------|---------------------------------------------|----------------------------------------|
| **Space**                      | Θ(N · σ) pointers ≈ O(N σ) bits             | each node holds a σ‑length child array |
| **Lookup / insert / delete**   | O(m)                                        | follows one edge per character         |
| **Cache behaviour (expected)** | O(m / B) block loads (B = cache‑line chars) | array layout is contiguous per node    |

**Typical use‑cases**  • exact dictionary membership • simple auto‑complete on small alphabets (e.g. DNA, ASCII).

---

## Compact trie — path‑compressed trie (a.k.a. radix or crit‑bit tree)

A **compact trie** merges every unary chain into one edge that stores the entire substring label, shrinking the node
count to the true branching points. It still stores the full set of keys and preserves prefix queries, but slashes
pointer overhead on long, skinny paths.

| Metric              | Bound      | Notes                                           |
|---------------------|------------|-------------------------------------------------|
| **Space**           | Θ(k) nodes | chains of unary nodes merged into a single edge |
| **Lookup / update** | O(m)       | must compare the label substring on each edge   |

**Use‑cases**  • in‑memory dictionaries with long common prefixes (URLs, config keys) • command completion.

---

## Patricia (blind) trie — binary compressed trie on bitstrings

A **Patricia trie** treats each key as a bitstring and stores only the *branching bit position* at each node. Instead of
edge labels, the path decision is “does bit *b* equal 0 or 1?”. This yields minimal node count while supporting
longest‑prefix search.

| Metric                    | Bound           | Notes                              |
|---------------------------|-----------------|------------------------------------|
| **Space**                 | Θ(k) nodes      | only branching bit position stored |
| **Longest‑prefix search** | O(L) bit probes | one probe per discriminating bit   |

**Use‑cases**  • IP routing tables • longest‑prefix match in networking • malware signature matching.

---

## Blind‑search on Patricia — skip label compare

The **blind‑search** algorithm walks the Patricia trie by reading only the branching bits, never re‑examining full key
substrings.

| Metric     | Bound                                              | Notes                                |
|------------|----------------------------------------------------|--------------------------------------|
| **Search** | O(L) worst‑case; touches only O(branch‑bits) (< L) | jumps straight to next branching bit |

**Use‑cases**  • high‑throughput packet classification where saving a handful of bit tests per lookup matters.

---

## Parallel / distributed Patricia construction

Keys are split across processors; each builds a local Patricia fragment which are then merged by global order.

| Metric              | Bound                        | Notes                             |
|---------------------|------------------------------|-----------------------------------|
| **Build (p cores)** | O(N/p + sort(N)/p + N log p) | last term = communication / merge |
| **Space**           | Θ(k) nodes total             | identical to sequential result    |

**Use‑cases**  • bulk loading of routing tables • preprocessing huge keysets (certificates) on clusters.

---

## Trie child‑representation trade‑offs

Picking a *child map* changes both RAM footprint and per‑step lookup cost.

| Representation                 | Lookup time (Contains) | Space (words)    | Notes                                        |
|--------------------------------|------------------------|------------------|----------------------------------------------|
| Variable‑size array (unsorted) | **O(m · σ)**           | O(N)             | scan child list                              |
| Fixed‑size array (σ slots)     | **O(m)**               | O(N · σ)         | constant‑time child access; high RAM         |
| Hash Table                     | **O(m)** w.h.p.        | O(N) + hash meta | efficient for very large Σ                   |
| Balanced search tree (AVL/RB)  | **O(m · log σ)**       | O(N)             | deterministic bounds                         |
| Weight‑balanced tree           | **O(m + log k)**       | O(N)             | log k depends on branching factor below node |
| Two‑level (array + WB tree)    | **O(m + log σ)**       | O(N)             | dense top array, sparse tail tree            |

---

## Succinct tree encodings (BP, DFUDS, LOUDS)

Succinct encodings store only the *shape* of the tree in a 2‑bit parenthesis or degree sequence, plus rank/select
support arrays, letting you navigate with **constant time** while using space near the information‑theoretic lower
bound.

| Metric         | Bound                       | Notes                                  |
|----------------|-----------------------------|----------------------------------------|
| **Space**      | 2 n + o(n) bits (n = nodes) | within 1 bit per edge                  |
| **Navigation** | O(1) rank/select            | parent, child(i), degree, subtree‑size |

**Use‑cases**  • static tries in compressed indices • read‑only dictionaries on mobile devices.

---

## `rank(c, i)` bit‑vector primitive

`rank` answers “how many occurrences of bit value **c** appear up to index **i**?” in **O(1)** via a two‑level
directory.

| Metric    | Bound                            | Notes                       |
|-----------|----------------------------------|-----------------------------|
| **Space** | n + o(n) bits (RRR: n H₀ + o(n)) | entropy‑bounded when sparse |
| **Query** | O(1)                             | two table look‑ups          |

---

## `select(k)` bit‑vector primitive

`select` is the inverse of `rank`: “where is the *k*‑th 1?”. Implementation reuses the same directory tables.

| Metric            | Bound          | Notes |
|-------------------|----------------|-------|
| **Space / query** | same as `rank` |       |

**Use‑cases**  • required for constant‑time navigation in BP/LOUDS, wavelet trees, FM‑index.
