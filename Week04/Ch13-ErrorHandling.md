# Chapter 13: Error Handling

## Objective
Handle runtime errors with `try`, `except`, and `finally` to write robust programs.

## Prerequisites
- Chapter 12 (Modules)

---

## Concepts
Errors can occur at runtime (invalid input, missing data, etc.). Python provides:
- **`try`** – Wrap code that might raise an error
- **`except`** – Handle the error; specify the exception type
- **`finally`** – Runs whether or not an error occurred (cleanup)
- **`raise`** – Create and raise your own errors

---

## Example 1: Basic try/except

**What it does:** Wraps a risky operation (parsing user input) in try/except so invalid input does not crash the program—essential for IoT systems that receive external data.

**Code:** Save as `ch13_try_except.py`

```python
# ch13_try_except.py
def parse_temperature(input_str):
    value = float(input_str)
    if value < -273.15 or value > 1000:
        raise ValueError(f"Temperature {value} out of physical range")
    return value

inputs = ["25.5", "invalid", "30"]

for inp in inputs:
    try:
        temp = parse_temperature(inp)
        print(f"Parsed: {temp} °C")
    except ValueError as e:
        print(f"Error: {e}")
```

**Explanation:**
- `float(input_str)` raises `ValueError` for non-numeric strings
- `raise ValueError(...)` creates a custom error
- `except ValueError as e` catches that type; `e` holds the error message
- The loop continues even when one input fails

**How to run:**
```bash
python ch13_try_except.py
```

**Expected output:**
```
Parsed: 25.5 °C
Error: could not convert string to float: 'invalid'
Parsed: 30.0 °C
```

*(Note: The second error message may vary; `parse_temperature` raises before the range check for "invalid".)*

---

## Example 2: try/except/finally for Cleanup

**What it does:** Uses `finally` to ensure a "connection closed" step always runs—important for resources even when errors occur.

**Code:** Save as `ch13_finally.py`

```python
# ch13_finally.py
def simulate_sensor_read(should_fail):
    print("Opening sensor connection...")

    try:
        if should_fail:
            raise RuntimeError("Sensor communication timeout")
        print("Read value: 25.3 °C")
    except RuntimeError as e:
        print("Caught:", e)
    finally:
        print("Closing sensor connection.")

print("=== Successful read ===")
simulate_sensor_read(False)

print("\n=== Failed read ===")
simulate_sensor_read(True)
```

**Explanation:**
- `finally` runs after `try` (success) or `except` (error)
- Use `finally` for cleanup that must always execute
- Without `finally`, you would duplicate cleanup in both success and error paths

**How to run:**
```bash
python ch13_finally.py
```

**Expected output:**
```
=== Successful read ===
Opening sensor connection...
Read value: 25.3 °C
Closing sensor connection.

=== Failed read ===
Opening sensor connection...
Caught: Sensor communication timeout
Closing sensor connection.
```

---

## Try It Yourself
1. Add validation in `parse_temperature` to reject values outside 0–100.
2. Catch different exception types separately (e.g., `ValueError` vs `TypeError`).
3. Use `finally` to reset a counter or log "Attempt complete" after each try.

---

## Key Takeaways
- `try`/`except` prevent errors from crashing the program
- `except ExceptionType as e` catches specific errors; `e` holds the message
- `finally` runs regardless of success or failure—use for cleanup
- `raise ExceptionType("message")` creates custom errors
- Always handle errors at boundaries (user input, file I/O, network)

---

## Completion

You have completed the Python for Beginners learning track. You are now ready for:
- **Week 5+** – Node-RED, MQTT, and simulated IoT systems
- **Week 6+** – Database operations, data processing, visualization

Return to [Week 4 README](./README.md) or [Course Outline](../Outline.md).
