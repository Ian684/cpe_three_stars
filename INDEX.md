# CPE three-star index

This repository contains 174 source files: 171 Python solutions and 3 C++
solutions. It is the advanced tier of the CPE practice collection.

## What to compare

Several problems have multiple implementations:

- `fast.py` — optimized implementation
- `slow.py` — slower or brute-force comparison
- `good.py` — cleaner accepted implementation
- `other.py` — alternative approach
- `wrong.py` — intentionally retained experimental version

Compare correctness first, then time and memory complexity. A faster file is
not automatically preferable if it changes input handling or assumptions.

## Review checklist

For each advanced problem, record the state/model, invariant, complexity,
boundary cases, and why the chosen algorithm is correct. Test disconnected
graphs, duplicate values, empty cases, large integers, and multiple datasets
when the statement allows them.

Run a solution with:

```bash
python3 10000.py < input.txt
python3 10273.py < input.txt
```

The files remain standalone for direct online-judge submission.
