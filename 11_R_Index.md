# r-Index

## Run-length FM (r-index) — FM-index that samples only run heads of BWT

**Complexities (formal)**

* Space = O(r) words
* count = O(m)
* locate = O(m + occ log σ)

**Description**
Because rank queries can be answered by scanning runs, sampling just one position per run suffices; in repetitive inputs r ≪ n, so the index is tiny.

## Move structure — stores pointer from each run head to preceding SA sample to enable locate

*(same locate complexity)*

## Space O(r) where r = #runs in BWT — index size proportional to repetitiveness

*(formal bound already shown)*
