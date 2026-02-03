# Chapter 6: Functions

## Objective
Define functions with parameters and return values to encapsulate reusable logic.

## Prerequisites
- Chapter 5 (Loops)

---

## Concepts
Functions are blocks of code that:
- Take **parameters** (inputs)
- Optionally **return** a value
- Can be **called** from anywhere in your code

```python
def name(param1, param2):
    # body
    return value
```

---

## Example 1: Function with Parameters and Return

**What it does:** Converts Celsius to Fahrenheit—a common conversion in temperature monitoring.

**Code:** Save as `ch06_functions.py`

```python
# ch06_functions.py
def celsius_to_fahrenheit(celsius):
    return (celsius * 9) / 5 + 32

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)

print(f"{temp_c} °C = {temp_f} °F")
print("0 °C =", celsius_to_fahrenheit(0), "°F")
print("100 °C =", celsius_to_fahrenheit(100), "°F")
```

**Explanation:**
- `def` defines a function; `celsius` is the parameter
- `return` sends the computed value back to the caller
- Functions can be called multiple times with different arguments

**How to run:**
```bash
python ch06_functions.py
```

**Expected output:**
```
25 °C = 77.0 °F
0 °C = 32.0 °F
100 °C = 212.0 °F
```

---

## Example 2: Multiple Parameters and Conditional Logic

**What it does:** Checks if a value is within a safe range—useful for validating sensor readings before use.

**Code:** Save as `ch06_range_check.py`

```python
# ch06_range_check.py
def is_in_range(value, min_val, max_val):
    return value >= min_val and value <= max_val

temperature = 75
min_safe = 0
max_safe = 100

if is_in_range(temperature, min_safe, max_safe):
    print("Temperature is within safe operating range.")
else:
    print("WARNING: Temperature out of range!")

print("Pressure 50 in 0-80?", is_in_range(50, 0, 80))   # True
print("Pressure 90 in 0-80?", is_in_range(90, 0, 80))   # False
```

**Explanation:**
- Multiple parameters are separated by commas
- The function returns a boolean for use in conditionals
- Same function can validate different values and ranges

**How to run:**
```bash
python ch06_range_check.py
```

**Expected output:**
```
Temperature is within safe operating range.
Pressure 50 in 0-80? True
Pressure 90 in 0-80? False
```

---

## Try It Yourself
1. Add a function `fahrenheit_to_celsius(f)` that converts Fahrenheit to Celsius.
2. Create `format_reading(name, value, unit)` that returns a formatted string.
3. Write a function with no return (returns `None`) that just prints a status message.

---

## Key Takeaways
- Functions group reusable logic
- `def name(params):` defines a function
- Parameters receive values; `return` sends a value back
- Functions reduce duplication and improve readability

---

## Next
→ [Chapter 7: Lambda & List Comprehensions](./Ch07-Lambda-ListComprehensions.md)
