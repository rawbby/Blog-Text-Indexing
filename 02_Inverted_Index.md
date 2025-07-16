# Inverted Index

## Term dictionary (compressed trie) — maps each token to its posting-list ID in log σ per character

**Complexities (formal)**

* Space ≈ Θ(total term chars) bits (front-compressed)
* Lookup = O(|term|)

**Description**
The vocabulary itself is just a compact trie over tokens; traversing one character at a time gives linear-in-term search, while path compression keeps the dictionary near the raw text size.

## Posting list with doc-ID gaps — sorted list of documents where the term occurs, stored as Δ-encoded gaps

**Complexities (formal)**

* Space ≈ n H₀ bits (plus small overhead)
* Sequential scan = O(|list|)

**Description**
Because doc IDs are increasing, storing differences instead of absolute numbers reduces average gap to a small integer; entropy coding then approaches the H₀ bound of the gap stream.

## **Unary & variable-byte (VB/δ/ω) gap encodings** — simple universal codes for posting gaps

**Complexities (formal)**

* Code length ≤ 2 · ⌊log gap⌋ + 3 bits (γ); VB ≈ 1–2 bytes for small gaps
* Decode next gap = O(1)

**Description**
These codes write a short prefix that says “how many bits follow” and then the value itself; small gaps therefore cost only a few bits, and the byte-aligned versions keep decoding simple word arithmetic.

## Δ-gap variable-length encoding — stores small doc-ID differences in fewest bits

**Complexities (formal)**

* Length ≈ log gap + 2 log log gap bits
* Decode = O(1)

**Description**
A higher-order Elias code: its double-log prefix makes it closer to the optimal “universal” bound than γ while still using only shifts and masks to parse.

## γ-code gap encoding — universal code with unary length + binary payload (Elias γ)

*(see previous)*

## Golomb / Golomb-Rice gap encoding — parameter-tuned code ideal for geometric gap distributions

**Complexities (formal)**

* Expected bits per gap = (1 + log₂ e)·H geometrically
* Decode = O(1) (shift & add)

**Description**
With the right divisor parameter b, a geometric gap distribution becomes almost fixed-length after quotient–remainder splitting; decoding just counts zeroes then adds a masked remainder.

## Exponential-merge algorithm for AND queries — scans the shorter posting list and leaps exponentially in the longer one

**Complexities (formal)**

* Time = O(|short| · log(|long|/|short|))

**Description**
For each ID in the shorter list you binary-search its position inside the longer list using exponentially growing skip lengths, so cost is roughly linear in the small list with a logarithmic multiplier.

## Skip-pointer (two-level) intersection — embeds skip links in long lists to bypass unmatched segments

**Complexities (formal)**

* Extra space = Θ(|list|/s) skip entries (s ≈ √|list|)
* AND time = O(|short| + |long|/s)

**Description**
Placing a pointer every √n elements halves total comparisons: you either leap whole blocks at once or pay to read them only when needed.

## Randomised-bucket intersection — hashes long list into buckets for expected-linear AND processing

**Complexities (formal)**

* Space = Θ(|long|) for hash buckets
* Expected time = O(|short| + collisions) ≈ O(|M| + |N|)

**Description**
The longer list is split into random buckets; looking up each element of the shorter list needs only a constant-time hash and an expected-O(1) scan within its bucket, giving near-linear behaviour overall.

## OR (union) query evaluation — multi-way merge producing the union of posting lists

**Complexities (formal)**

* k-way merge time = O(total output) with loser-tree heap O(k)

**Description**
You repeatedly pull the smallest current doc ID among k heads using a heap; each output ID costs one heap pop & push, so total work is proportional to the size of the union.

## Phrase query evaluation — matches consecutive positions using positional posting lists

**Complexities (formal)**

* Time = O(sum |list| + occurrences)

**Description**
After intersecting the document IDs, you align positional offsets inside each list; because positions are sorted, merging them is as cheap as a sequential scan.

## Multiplicative string hashing for terms — fast hash to locate vocabulary entries in O(1) expected

**Complexities (formal)**

* Hash = O(|term|)
* Lookup = O(1) expected, O(|term|) worst if collision

**Description**
A multiplicative rolling hash maps the whole term to a machine-word key; a constant-size hash table then points to the exact trie entry, yielding constant average access time.
