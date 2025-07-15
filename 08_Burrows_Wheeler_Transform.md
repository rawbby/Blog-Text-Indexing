# Burrows–Wheeler Transform

## Forward BWT — sorts all text rotations; groups similar contexts for compression
## Inverse BWT with LF-mapping — reconstructs original text using cumulative counts
## Run count r in BWT — number of equal-letter runs; key repetitiveness parameter
## Move-to-front + RLE + entropy pipeline — standard BWT post-processing for high compression
