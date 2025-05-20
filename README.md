# BWT-Based-Pattern-Matching


This project implements an efficient pattern matching algorithm using the Burrows–Wheeler Transform (BWT). It includes:

* Construction of the BWT from a given text
* Building auxiliary data structures: first occurrence map and checkpoints for fast symbol counting
* An improved backward search algorithm to find all occurrences of given patterns in the original text
* Conversion of BWT match positions back to original text positions

# Features
* Supports multiple pattern queries
* Uses checkpoints for faster rank queries and efficient matching
* Handles exact pattern matching in linear time relative to pattern length

# Usage
Run the script to see an example where it finds all occurrences of patterns ATCG and GGGT in the input text "AATCGGGTTCAATCGGGGT".
```
python bwt_pattern_matching.py
```
# Output:

ATCG: 2 2
GGGT: 2 2

# Functions

* build_bwt(text): Builds the Burrows–Wheeler Transform of the input text
* build_first_occurrence(bwt): Maps each character to its first occurrence in the sorted BWT
* build_checkpoints(bwt, interval): Builds checkpoints to speed up counting symbol occurrences
* count_symbol_up_to(...): Counts occurrences of a symbol up to a given index using checkpoints
* better_bw_matching(...): Performs backward search over BWT to find pattern matches
* find_pattern_positions(text, patterns, interval): Coordinates the process and returns pattern positions in the original text

# Applications

*  Bioinformatics: Fast searching of DNA/RNA sequences for specific motifs or genes
*  Text Compression: Underlying step in compression algorithms like bzip2
*  Information Retrieval: Efficient substring search in large text databases
*  Data Mining: Pattern discovery in large datasets and logs

# License
This project is licensed under the MIT License.
