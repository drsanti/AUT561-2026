# Chapter 5: Loops

## Objective
Repeat code with `for` and `while` loops, and use `break` and `continue` to control iteration.

## Prerequisites
- Chapter 4 (Conditionals)

---

## Concepts
Loops run a block of code multiple times:
- **`for`** – Iterate over a sequence (range, list) or a fixed number of times
- **`while`** – Repeats while a condition is true
- **`break`** – Exit the loop immediately
- **`continue`** – Skip to the next iteration

---

## Example 1: For Loop – Simulated Sensor Readings

**What it does:** Simulates 5 sensor readings in a loop, as IoT systems sample at regular intervals.

**Code:** Save as `ch05_for_loop.py`

```python
# ch05_for_loop.py
import random

sensor_name = "TempSensor-01"
base_temp = 25

print("=== Simulated Sensor Sampling ===")
for i in range(5):
    noise = (random.random() - 0.5) * 2  # ±1°C noise
    reading = base_temp + noise
    print(f"Sample {i + 1}: {reading:.2f} °C")
print("Sampling complete.")
```

**Explanation:**
- `range(5)` produces 0, 1, 2, 3, 4
- `random.random()` returns 0–1; we shift and scale for small noise
- `{reading:.2f}` formats the float to 2 decimal places
- `i + 1` in output shows sample numbers 1–5 instead of 0–4

**How to run:**
```bash
python ch05_for_loop.py
```

**Expected output (values vary due to random noise):**
```
=== Simulated Sensor Sampling ===
Sample 1: 25.34 °C
Sample 2: 24.12 °C
...
Sampling complete.
```

---

## Example 2: While Loop with Break

**What it does:** Continues sampling until a reading exceeds a threshold, then stops—simulating a safety trip.

**Code:** Save as `ch05_while_break.py`

```python
# ch05_while_break.py
import random

threshold = 80
reading = 70
count = 0
max_samples = 20

print(f"Monitoring until temperature exceeds {threshold} °C")
while count < max_samples:
    reading = reading + (random.random() - 0.3) * 5  # Drift upward with noise
    count += 1
    print(f"Sample {count}: {reading:.1f} °C")

    if reading > threshold:
        print("TRIP: Threshold exceeded! Stopping.")
        break
```

**Explanation:**
- `while` runs as long as `count < max_samples`
- `break` exits the loop immediately when temperature exceeds the limit
- `count += 1` is shorthand for `count = count + 1`

**How to run:**
```bash
python ch05_while_break.py
```

**Expected output (varies):**
```
Monitoring until temperature exceeds 80 °C
Sample 1: 71.2 °C
Sample 2: 73.5 °C
...
TRIP: Threshold exceeded! Stopping.
```

---

## Try It Yourself
1. Change the loop in Example 1 to run 10 times.
2. Use `continue` to skip printing when `reading < 20` in Example 2.
3. Write a loop that counts down from 5 to 1 and prints each number.

---

## Key Takeaways
- `for i in range(n)` iterates n times (0 to n-1)
- `while` is useful when the end condition depends on runtime values
- `break` exits the loop; `continue` skips to the next iteration
- `import random` provides `random.random()` for random numbers

---

## Next
→ [Chapter 6: Functions](./Ch06-Functions.md)
