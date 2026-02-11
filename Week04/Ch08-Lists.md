# Chapter 8: Lists

## Objective
Create and manipulate lists: access elements, use `len`, `append`, and iterate with `for`.

## Prerequisites
- Chapter 7 (Lambda & List Comprehensions)

---

## Concepts
Lists store ordered collections of values:
- Indexing: `arr[0]` is the first element (zero-based)
- `len(arr)` – number of elements
- `arr.append(item)` – add to the end
- `for item in arr` – iterate over values
- Negative index: `arr[-1]` is the last element

---

## Example 1: Creating and Accessing Lists

**What it does:** Stores multiple sensor readings in a list and computes statistics—common in IoT data logging.

**Code:** Save as `ch08_lists.py`

```python
# ch08_lists.py
readings = [22.5, 23.1, 24.0, 22.8, 23.5]

print("Readings:", readings)
print("Count:", len(readings))
print("First:", readings[0])
print("Last:", readings[-1])

# Sum and average
total = sum(readings)
average = total / len(readings)
print("Average:", round(average, 2))

# Max and min
print("Max:", max(readings), "Min:", min(readings))
```

**Explanation:**
- Lists use square brackets `[]`
- `readings[0]` and `readings[-1]` access first and last
- `sum()`, `max()`, `min()` are built-in functions for lists of numbers

**How to run:**
```bash
python ch08_lists.py
```

**Expected output:**
```
Readings: [22.5, 23.1, 24.0, 22.8, 23.5]
Count: 5
First: 22.5
Last: 23.5
Average: 23.18
Max: 24.0 Min: 22.5
```

---

## Example 2: Building Lists with append

**What it does:** Simulates collecting sensor samples in a loop and storing them for later analysis.

**Code:** Save as `ch08_append.py`

```python
# ch08_append.py
import random

samples = []
base_value = 25
num_samples = 5

for i in range(num_samples):
    noise = (random.random() - 0.5) * 2
    samples.append(base_value + noise)

print("Collected samples:", samples)

# Filter valid (20-30 range)
valid_samples = [s for s in samples if 20 <= s <= 30]
print("Valid (20-30 range):", valid_samples)
print("Valid count:", len(valid_samples))
```

**Explanation:**
- `samples = []` creates an empty list
- `append(value)` adds an element to the end
- Lists can be built gradually and processed afterward

**How to run:**
```bash
python ch08_append.py
```

**Expected output (varies):**
```
Collected samples: [25.2, 24.1, 26.0, 23.8, 25.5]
Valid (20-30 range): [25.2, 24.1, 26.0, 23.8, 25.5]
Valid count: 5
```

---

## Try It Yourself
1. Add a sixth reading to the list in Example 1 and recompute the average.
2. Use a loop to find the index of the maximum value.
3. Create a list of sensor names (strings) and use `for` to print each.

---

## Key Takeaways
- Lists are zero-indexed; first element is `arr[0]`
- `append` adds to the end; `len` gives the size
- `for item in list` iterates over values
- `sum()`, `max()`, `min()` work on lists of numbers

---

## Next
→ [Chapter 9: Dictionaries](./Ch09-Dictionaries.md)
