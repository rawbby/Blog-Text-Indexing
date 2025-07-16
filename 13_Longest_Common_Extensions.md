# Longest Common Extensions

## LCE(i, j) query — length of longest common prefix of suffixes at i and j

**Complexities (formal)**

* With ISA + LCP + RMQ: Query = O(1)

**Description**
Two positions map to SA indices; the RMQ on the LCP array between them returns the exact number of matching characters instantly.

## ISA + LCP + RMQ technique — constant-time LCE using pre-built inverse-SA and RMQ

*(covered above)*

## Karp–Rabin fingerprint LCE — probabilistic LCE via rolling hash comparisons

**Complexities (formal)**

* Pre-processing = O(n) hashes
* Query = O(1) expected, O(m) verify

**Description**
Two suffixes are compared by binary searching using constant-time substring hashes; a second pass verifies equality to remove the small false-positive chance.

## τ-synchronising sets — sparse anchor positions enabling compressed-text LCE preprocessing

**Complexities (formal)**

* Space = O(n/τ)
* LCE = O(τ)

**Description**
By checking matches only at carefully chosen anchor points every τ characters, the data structure cuts memory at the cost of an additive τ factor in query time.
