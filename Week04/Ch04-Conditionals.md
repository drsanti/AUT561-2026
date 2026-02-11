# Chapter 4: Conditionals (if / elif / else)

## Objective
Make decisions in code using `if`, `elif`, and `else` to branch based on conditions.

## Prerequisites
- Chapter 3 (Operators)

---

## Concepts
Conditionals let your program choose different actions based on values:
- **`if condition:`** – Execute block only when condition is true
- **`elif condition:`** – Alternative condition if the first fails (Python uses `elif`, not "else if")
- **`else:`** – Fallback when no condition matches

Use indentation (4 spaces) for blocks. Colon `:` ends the condition line.

---

## Example 1: Single and Multi-Branch Conditions

**What it does:** Implements a simple threshold check—if temperature exceeds a limit, print an alert. Common in IoT monitoring.

**Code:** Save as `ch04_conditionals.py`

```python
# ch04_conditionals.py
temperature = 62
threshold = 60

if temperature > threshold:
    print("ALERT: Temperature exceeds threshold!")
    print(f"Current: {temperature}°C, Limit: {threshold}°C")
else:
    print("Temperature within normal range.")
```

**Explanation:**
- `temperature > threshold` is the condition (evaluates to True or False)
- The indented block runs only when the condition is True
- `else` runs when the condition is False

**How to run:**
```bash
python ch04_conditionals.py
```

**Expected output:**
```
ALERT: Temperature exceeds threshold!
Current: 62°C, Limit: 60°C
```

---

## Example 2: Multiple Branches with elif

**What it does:** Classifies a sensor reading into severity levels—useful for status displays and alarm prioritization.

**Code:** Save as `ch04_multibranch.py`

```python
# ch04_multibranch.py
pressure = 85  # psi

if pressure > 100:
    print("CRITICAL: Pressure too high - shutdown recommended")
elif pressure > 90:
    print("WARNING: Pressure elevated")
elif pressure < 20:
    print("WARNING: Pressure too low")
else:
    print("OK: Pressure within operating range")
```

**Explanation:**
- Conditions are checked from top to bottom
- The first True condition runs; the rest are skipped
- `else` catches all cases that did not match above

**How to run:**
```bash
python ch04_multibranch.py
```

**Expected output:**
```
WARNING: Pressure elevated
```

---

## Try It Yourself
1. Change `temperature` to 55 and run Example 1 again.
2. Add a new branch in Example 2 for pressure > 95 as CRITICAL.
3. Create a variable `quality` = "GOOD" or "BAD" and use `if` to print different messages.

---

## Key Takeaways
- `if`/`elif`/`else` control flow based on conditions
- Use `elif` for additional conditions (not "else if")
- Indentation defines blocks—use 4 spaces
- Only one branch executes; conditions are evaluated in order

---

## Next
→ [Chapter 5: Loops](./Ch05-Loops.md)
