# Top-k Document Retrieval

## Document array (DA) — maps SA positions to document IDs for multi-document text

**Complexities (formal)**

* Space = n ⌈log₂ D⌉ bits
* Query distinct docs = O(k) with chain array

**Description**
Each suffix inherits its document ID; restricting an SA interval to the documents it covers becomes a simple RMQ plus linear scan over at most k outputs.

## Chain array (CA) — links first occurrence of each document within SA interval

*(same space as DA; used for optimal O(k) listing)*

## Optimal document listing — lists distinct docs in O(k) using RMQ on CA

*(formal above)*

## **Grid-RMQ top-k document retrieval** — retrieves k highest-scoring docs via range-maximum queries on a grid

**Complexities (formal)**

* Pre-processing space = O(n)
* top-k query = O(k + log n)

**Description**
Scores are stored in a 2-D range-max tree; repeatedly selecting the current maximum and marking its cell deleted yields k results with only a logarithmic overhead.
