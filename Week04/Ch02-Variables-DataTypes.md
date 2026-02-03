# Chapter 2: Variables and Data Types

## Objective
Declare variables and use types `int`, `float`, `str`, and `bool` for IoT data representation.

## Prerequisites
- Chapter 1 (Introduction)
- Ability to run Python files with `python filename.py`

---

## Concepts
Variables store values for reuse. Python uses dynamic typing—you do not declare types explicitly; Python infers them.

Common types in IoT applications:
- **`int`** – Integers (counters, IDs)
- **`float`** – Decimal numbers (sensor values: temperature, pressure)
- **`str`** – Strings (names, messages, units)
- **`bool`** – True/False (ON/OFF, fault/no fault)

---

## Example 1: Basic Variable Declaration

**What it does:** Stores sensor name, value, and unit in variables and prints formatted output—common in IoT monitoring.

**Code:** Save as `ch02_variables.py`

```python
# ch02_variables.py
sensor_name = "TempSensor-01"
sensor_value = 25.5
unit = "°C"

print("Sensor:", sensor_name)
print("Reading:", sensor_value, unit)
print(f"Formatted: {sensor_name} = {sensor_value} {unit}")
```

**Explanation:**
- Variables are assigned with `=`
- `f"..."` is an f-string; `{variable}` embeds the value in the string
- Python infers `sensor_value` is float, `sensor_name` and `unit` are strings

**How to run:**
```bash
python ch02_variables.py
```

**Expected output:**
```
Sensor: TempSensor-01
Reading: 25.5 °C
Formatted: TempSensor-01 = 25.5 °C
```

---

## Example 2: Different Data Types and Operations

**What it does:** Demonstrates int, float, bool, and simple arithmetic—used for counters and status in IoT systems.

**Code:** Save as `ch02_types.py`

```python
# ch02_types.py
is_online = True
sample_count = 0
sample_count = sample_count + 1

print("System online:", is_online)
print("Samples taken:", sample_count)

max_samples = 10
status = "High capacity" if max_samples > 5 else "Low capacity"
print("Status:", status)
```

**Explanation:**
- `is_online` is a boolean; `sample_count` is an int
- Variables can be reassigned
- The ternary expression `x if condition else y` chooses a value based on a condition

**How to run:**
```bash
python ch02_types.py
```

**Expected output:**
```
System online: True
Samples taken: 1
Status: High capacity
```

---

## Try It Yourself
1. Add variables for sensor min and max range; print them.
2. Store `alarm_active = False` and print it.
3. Use `type()` to check the type of a variable: `print(type(sensor_value))`.

---

## Key Takeaways
- Variables are assigned with `=`
- `int`, `float`, `str`, `bool` are the main types
- F-strings `f"{var}"` format strings with embedded values
- Python infers types automatically

---

## Next
→ [Chapter 3: Operators](./Ch03-Operators.md)
