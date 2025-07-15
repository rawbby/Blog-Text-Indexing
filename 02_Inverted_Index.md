# Inverted Index

## Term dictionary (compressed trie) — maps each token to its posting-list ID in log σ per character
## Posting list with doc-ID gaps — sorted list of documents where the term occurs, stored as Δ-encoded gaps
## **Unary & variable-byte (VB/δ/ω) gap encodings** — simple universal codes for posting gaps
## Δ-gap variable-length encoding — stores small doc-ID differences in fewest bits
## γ-code gap encoding — universal code with unary length + binary payload (Elias γ)
## Golomb / Golomb-Rice gap encoding — parameter-tuned code ideal for geometric gap distributions
## Exponential-merge algorithm for AND queries — scans the shorter posting list and leaps exponentially in the longer one
## Skip-pointer (two-level) intersection — embeds skip links in long lists to bypass unmatched segments
## Randomised-bucket intersection — hashes long list into buckets for expected-linear AND processing
## OR (union) query evaluation — multi-way merge producing the union of posting lists
## Phrase query evaluation — matches consecutive positions using positional posting lists
## Multiplicative string hashing for terms — fast hash to locate vocabulary entries in O(1) expected
