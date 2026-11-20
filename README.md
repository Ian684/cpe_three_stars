# cpe_three_stars

Python solutions for CPE three-star programming problems. This repository focuses on more advanced competitive programming problems and algorithmic practice.

Reference problem list:

- https://par.cse.nsysu.edu.tw/~advprog/star.php

## Repository Structure

Most files are independent Python scripts named after UVa problem numbers or practice problem IDs.

```text
cpe_three_stars/
├── 10000.py
├── 10003.py
├── 10023.py
├── 10023fast.py
├── 10023good.py
├── 10023slow.py
├── ...
└── README.md
```

## File Naming Rules

| Suffix | Meaning |
|---|---|
| `fast.py` | Optimized version. |
| `slow.py` | Brute-force or slower version used for comparison. |
| `good.py` | Cleaner or improved accepted solution. |
| `other.py` | Alternative approach. |
| `wrong.py` | Incorrect or experimental version kept for debugging/reference. |

## Requirements

- Python 3.x

Most solutions use only the Python standard library.

## Usage

Clone the repository:

```bash
git clone https://github.com/Ian684/cpe_three_stars.git
cd cpe_three_stars
```

Run a solution:

```bash
python3 10000.py < input.txt
```

Or provide input directly from the terminal:

```bash
python3 10000.py
```

## Topics Covered

This repository may include practice on:

- Dynamic programming
- Shortest path and graph algorithms
- Depth-first search / breadth-first search
- Number theory
- Recursion and backtracking
- Data structures
- Advanced simulation
- Input/output optimization

## Notes

The repository contains multiple versions for some problems. These versions are kept to compare performance, correctness, and implementation style.
