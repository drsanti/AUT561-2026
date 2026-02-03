# Chapter 7: Lambda and List Comprehensions

## Objective
Use lambda expressions for short functions and list comprehensions for concise list creation and filtering.

## Prerequisites
- Chapter 6 (Functions)

---

## Concepts
- **Lambda:** A small anonymous function: `lambda x: x * 2` (takes x, returns x*2)
- **List comprehension:** Build a list in one line: `[x for x in items if condition]`
- Both are used for filtering, transforming, and building lists compactly

---

## Example 1: Lambda with filter and map

**What it does:** Uses lambda to filter valid sensor readings and transform values—common in data processing.

**Code:** Save as `ch07_lambda.py`

```python
# ch07_lambda.py
def clamp(value, min_val, max_val):
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value

# Lambda: scale from one range to another
scale = lambda x, from_lo, from_hi, to_lo, to_hi: (
    (x - from_lo) / (from_hi - from_lo)
) * (to_hi - to_lo) + to_lo

raw_reading = 5.2
clamped = clamp(raw_reading, 0, 5)
print("Raw:", raw_reading, "Clamped:", clamped)

percent = scale(2.5, 0, 5, 0, 100)
print("2.5 in 0-5 scale =", percent, "%")
```

**Explanation:**
- `lambda` defines a one-expression function
- `clamp` keeps a value between min and max (common in IoT)
- `scale` maps a value from one range to another

**How to run:**
```bash
python ch07_lambda.py
```

**Expected output:**
```
Raw: 5.2 Clamped: 5
2.5 in 0-5 scale = 50.0 %
```

---

## Example 2: List Comprehensions and filter

**What it does:** Filters valid readings and maps them to status strings—typical IoT data processing.

**Code:** Save as `ch07_listcomp.py`

```python
# ch07_listcomp.py
readings = [22.1, 105.2, 24.5, -1.0, 25.0, 150.0]

# Filter: keep only valid readings (0-100)
valid_readings = [r for r in readings if 0 <= r <= 100]

# Or using filter with lambda
valid_readings2 = list(filter(lambda r: 0 <= r <= 100, readings))

# Map: convert each to status
statuses = ["HIGH" if r > 80 else "LOW" if r < 20 else "OK" for r in valid_readings]

print("Original:", readings)
print("Valid:", valid_readings)
print("Statuses:", statuses)
```

**Explanation:**
- `[r for r in readings if condition]` builds a list of items that pass the condition
- `filter(lambda, list)` does the same; `list()` converts the result to a list
- List comprehension can include a conditional expression for transformation

**How to run:**
```bash
python ch07_listcomp.py
```

**Expected output:**
```
Original: [22.1, 105.2, 24.5, -1.0, 25.0, 150.0]
Valid: [22.1, 24.5, 25.0]
Statuses: ['OK', 'OK', 'OK']
```

---

## Try It Yourself
1. Use a list comprehension to keep only readings greater than 24.
2. Use a list comprehension to convert Celsius values [0, 10, 20, 30] to Fahrenheit.
3. Write a lambda that takes two numbers and returns the larger one.

---

## Key Takeaways
- `lambda x: expr` creates a small one-expression function
- List comprehensions: `[expr for item in iterable if condition]`
- `filter()` and `map()` work with lambda for functional-style code
- List comprehensions are often more readable than loops for simple transformations

---

## Next
→ [Chapter 8: Lists](./Ch08-Lists.md)
