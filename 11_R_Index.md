# r-Index

## Run-length FM (r-index) — FM-index that samples only run heads of BWT
## Move structure — stores pointer from each run head to preceding SA sample to enable locate
## Space O(r) where r = #runs in BWT — index size proportional to repetitiveness
