# Text Compression

## Huffman coding — optimal variable-length prefix code by symbol frequency

**Complexities (formal)**

* Compressed size = n H₀ + O(σ log σ) bits
* Encode = O(n log σ), decode = O(n)

**Description**
The code assigns shorter bit patterns to frequent characters; expected bits per symbol match the zero-order entropy within a small additive redundancy.

## Canonical Huffman codes — normalised Huffman representation that stores only code-lengths

**Complexities (formal)**

* Same compressed size
* Extra header ≈ O(σ log σ) bits
* Decode faster (table-based)

**Description**
Because codes of the same length are lexicographically ordered, you need store only each symbol’s length; a simple table then reconstructs the exact bit patterns.

## Shannon–Fano coding & zero-order entropy H₀ — early entropy code illustrating H₀ bound

**Complexities (formal)**

* Size ≤ n (H₀ + 1) bits

**Description**
While not optimal, splitting the probability mass into near-halves per bit yields at most 1 extra bit per symbol over the theoretical optimum.

## **Bounded-dictionary (sliding window) LZ77** — limits dictionary size for streaming compression

**Complexities (formal)**

* Size ≤ (1+ε) n Hₖ for window covering k-length contexts
* Encode = O(n), decode = O(n)

**Description**
Pointers are restricted to the last W characters; in highly repetitive text, long matches within the window replace many symbols, pushing size toward the k-th-order entropy.

## LZ78 factorisation with dynamic trie — builds dictionary of distinct phrases while scanning input

*(similar encode/decode O(n); compressed size ≈ z (log z + log σ) bits)*

## LZ77 factorisation via SA/LCP — finds longest previous factors with suffix structures in O(n)

**Complexities (formal)**

* Factorisation time = O(n) given SA+LCP
* Same compressed bounds as LZ77

**Description**
A sliding window match becomes a nearest-neighbour query on SA/LCP, which can be answered in constant time per position once the suffix structures are built.

## k-th-order empirical entropy Hₖ — compressibility metric measuring context dependency

**Formal** Hₖ = (1/n) Σᵤ nᵤ H₀(P(\*|u))
**Description**
It averages the zero-order entropy of the distribution after every length-k context u; lower Hₖ means better predictability and higher potential compression.
