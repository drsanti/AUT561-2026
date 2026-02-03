# Chapter 3: Operators

## Objective
Use arithmetic, comparison, and logical operators to build expressions for conditionals and loops.

## Prerequisites
- Chapter 2 (Variables & Data Types)

---

## Concepts
Operators perform operations on values:
- **Arithmetic:** `+`, `-`, `*`, `/`, `//` (integer division), `%` (remainder), `**` (power)
- **Comparison:** `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical:** `and`, `or`, `not`

---

## Example 1: Arithmetic and Comparison

**What it does:** Calculates average temperature and checks if it exceeds a threshold—common in IoT control logic.

**Code:** Save as `ch03_operators.py`

```python
# ch03_operators.py
reading1 = 22.5
reading2 = 24.0
reading3 = 23.1

average = (reading1 + reading2 + reading3) / 3
threshold = 25
over_threshold = average > threshold

print("Average temperature:", round(average, 2), "°C")
print("Threshold:", threshold, "°C")
print("Over threshold?", over_threshold)
```

**Explanation:**
- `(a + b + c) / 3` computes the average
- `average > threshold` produces a boolean
- `round(average, 2)` rounds to 2 decimal places

**How to run:**
```bash
python ch03_operators.py
```

**Expected output:**
```
Average temperature: 23.2 °C
Threshold: 25 °C
Over threshold? False
```

---

## Example 2: Logical Operators

**What it does:** Combines conditions for safe operation checks—e.g., allow control only when multiple permissives are met.

**Code:** Save as `ch03_logical.py`

```python
# ch03_logical.py
temperature = 75   # °C
pressure_ok = True
door_closed = True

# and: all must be true
safe_to_run = temperature < 80 and pressure_ok and door_closed

# or: at least one must be true
needs_attention = temperature > 90 or not pressure_ok

print("Safe to run?", safe_to_run)
print("Needs attention?", needs_attention)
```

**Explanation:**
- `and` requires all conditions to be true
- `or` requires at least one to be true
- `not` negates a boolean

**How to run:**
```bash
python ch03_logical.py
```

**Expected output:**
```
Safe to run? True
Needs attention? False
```

---

## Try It Yourself
1. Change `temperature` to 85 and observe the output.
2. Use `%` to check if a sample index is even: `index % 2 == 0`.
3. Write an expression: alarm if temp > 100 or pressure < 50.

---

## Key Takeaways
- Arithmetic operators work on numbers
- Use `==` for equality, `!=` for not equal
- `and`, `or`, `not` combine and negate booleans
- `round(x, n)` rounds a number to n decimal places

---

## Next
→ [Chapter 4: Conditionals](./Ch04-Conditionals.md)
