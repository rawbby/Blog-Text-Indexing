# Top-k Document Retrieval

## Document array (DA) — maps SA positions to document IDs for multi-document text
## Chain array (CA) — links first occurrence of each document within SA interval
## Optimal document listing — lists distinct docs in O(k) using RMQ on CA
## **Grid-RMQ top-k document retrieval** — retrieves k highest-scoring docs via range-maximum queries on a grid
