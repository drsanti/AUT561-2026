# Chapter 12: Modules and Packages

## Objective
Organize code across files using `import` and `from...import` for maintainable projects.

## Prerequisites
- Chapter 11 (Classes)
- Multiple `.py` files in the same folder (or proper package structure)

---

## Concepts
- **Module** – A `.py` file that can be imported
- **`import module`** – Use `module.name` to access items
- **`from module import name`** – Import specific items directly
- **Package** – A folder containing `__init__.py` and modules
- Modules run in the same directory or on `PYTHONPATH`

---

## Example 1: Creating and Importing a Module

**What it does:** Puts a utility function in a separate file, then imports it—typical structure for shared helpers.

**File 1:** Save as `ch12_utils.py`

```python
# ch12_utils.py
def clamp(value, min_val, max_val):
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value

def format_reading(name, value, unit):
    return f"{name}: {value} {unit}"
```

**File 2:** Save as `ch12_main.py`

```python
# ch12_main.py
from ch12_utils import clamp, format_reading

reading = {"name": "Temp-01", "value": 105, "unit": "°C"}
safe_value = clamp(reading["value"], 0, 100)
print("Original:", reading["value"], "Clamped:", safe_value)
print(format_reading(reading["name"], safe_value, reading["unit"]))
```

**Explanation:**
- `ch12_utils.py` defines functions
- `from ch12_utils import clamp` imports the function directly
- Both files must be in the same folder (or the module must be on the path)

**How to run:**
```bash
python ch12_main.py
```

**Expected output:**
```
Original: 105 Clamped: 100
Temp-01: 100 °C
```

---

## Example 2: Importing Standard Library Modules

**What it does:** Uses Python's built-in modules—you will use these often in IoT applications.

**Code:** Save as `ch12_stdlib.py`

```python
# ch12_stdlib.py
import random
from datetime import datetime

# random - for sensor simulation
value = random.uniform(20, 30)
print("Random reading:", round(value, 2))

# datetime - for timestamps
now = datetime.now()
print("Timestamp:", now.isoformat())
print("Date only:", now.strftime("%Y-%m-%d"))
```

**Explanation:**
- `import random` – access with `random.uniform()`
- `from datetime import datetime` – use `datetime` directly
- The standard library has many useful modules (json, csv, math, etc.)

**How to run:**
```bash
python ch12_stdlib.py
```

**Expected output (varies):**
```
Random reading: 24.56
Timestamp: 2026-02-03T12:34:56.789012
Date only: 2026-02-03
```

---

## Try It Yourself
1. Add another function to `ch12_utils.py` (e.g., `scale`) and import it in `ch12_main.py`.
2. Use `import ch12_utils` and call `ch12_utils.clamp(...)`.
3. Create a file with only constant definitions and import them elsewhere.

---

## Key Takeaways
- A `.py` file is a module; use `import` to load it
- `from module import name` imports specific items
- Standard library modules (random, datetime, csv, json) are always available
- Modules must be in the same directory or on Python's path

---

## Next
→ [Chapter 13: Error Handling](./Ch13-ErrorHandling.md)
