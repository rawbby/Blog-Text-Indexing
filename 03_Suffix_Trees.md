# Suffix Trees

## **Enhanced suffix tree** — edge-compacted suffix tree with suffix links and leaf-label references

**Complexities (formal)**

* Space ≈ O(n) nodes (practically 10–20 n bytes)
* Build (Ukkonen) = O(n)
* Exact string search = O(m)

**Description**
By storing only branching edges and adding “suffix links”, the tree fits linear space while every pattern character is matched exactly once during search.

## Ukkonen online construction — linear-time algorithm that inserts characters left-to-right

**Complexities (formal)**

* Build = O(n) incremental
* Extra space same as suffix tree

**Description**
It keeps an implicit buffer (the “active point”) so that each new character causes amortised constant work, achieving total linear build time without rescanning the text.

## Pattern search on suffix tree — O(m) traversal to find all pattern occurrences

*(covered above)*
