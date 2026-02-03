# **Week 4 Self-Test Quiz**

**Topic: Python Fundamentals and Quiz 1 Preparation**

---

## **Questions**

### **1. Multiple Choice**

Which command is used to check if Python 3 is installed on your system?

A. `python check`
B. `python --version`
C. `python status`
D. `python info`

---

### **2. True or False**

A virtual environment (venv) isolates project dependencies from the system Python installation.

---

### **3. Short Answer**

Why is the working directory important when running `python filename.py`?

---

### **4. Multiple Choice**

Which Python data type is most appropriate for storing a **sensor reading value** such as 25.5?

A. `int`
B. `str`
C. `float`
D. `bool`

---

### **5. Code Understanding (Python)**

Consider the following code:

```python
if temperature > 60:
    print("ALERT: High temperature")
elif temperature > 50:
    print("WARNING: Elevated")
else:
    print("OK")
```

If `temperature = 55`, what will be printed?

---

### **6. Multiple Choice**

Which Python keyword is used to define a function?

A. `function`
B. `def`
C. `func`
D. `fn`

---

### **7. True or False**

A list comprehension `[x for x in items if x > 0]` returns a new list containing only items greater than zero.

---

### **8. Short Answer**

In Python, what is the difference between `d["key"]` and `d.get("key")` when accessing a dictionary?

---

### **9. Multiple Choice**

Which module is used for reading and writing CSV files in Python?

A. `json`
B. `file`
C. `csv`
D. `io`

---

### **10. Code Understanding (Python)**

Explain what this code does:

```python
try:
    value = float(user_input)
except ValueError:
    print("Invalid number")
```

---

### **11. True or False**

In a Python class, `self` refers to the current instance of the class.

---

### **12. Multiple Choice**

Which statement correctly imports a function named `clamp` from a module named `utils`?

A. `import clamp from utils`
B. `from utils import clamp`
C. `import utils.clamp`
D. `include utils clamp`

---

### **13. Short Answer**

Why is error handling with `try`/`except` important when processing sensor data from external sources (e.g., user input, files, network)?

---

### **14. Scenario-Based Question**

You have a list of sensor readings: `[22.1, 105.2, 24.5, -1.0, 25.0]`. You need to:
1. Filter out invalid values (assume valid range is 0–100)
2. Calculate the average of valid readings

Write the Python code (or describe the approach) to do this.

---

## **Answers**

### **1.**

**B. `python --version`** (or `python3 --version` on some systems)

---

### **2.**

**True**

A virtual environment creates an isolated folder with its own Python and packages, separate from the system installation.

---

### **3.**

The working directory is the folder the terminal is "in." The command `python filename.py` only works if the terminal's current directory contains that file, or if you provide the correct path (e.g., `python path/to/filename.py`).

---

### **4.**

**C. `float`**

Sensor values like temperature, pressure, and speed typically use decimal numbers, which are represented by `float` in Python.

---

### **5.**

**WARNING: Elevated**

The condition `temperature > 60` is False (55 is not > 60). The condition `temperature > 50` is True (55 > 50), so the `elif` branch executes.

---

### **6.**

**B. `def`**

---

### **7.**

**True**

---

### **8.**

`d["key"]` raises a `KeyError` if the key does not exist. `d.get("key")` returns `None` (or a default value if provided) if the key does not exist, which is safer when the key might be missing.

---

### **9.**

**C. `csv`**

---

### **10.**

The code attempts to convert `user_input` to a float. If the conversion fails (e.g., the user typed "abc" instead of a number), Python raises `ValueError`. The `except` block catches that error and prints "Invalid number" instead of crashing the program.

---

### **11.**

**True**

---

### **12.**

**B. `from utils import clamp`**

---

### **13.**

External data (user input, files, network) can be invalid, malformed, or unavailable. Error handling with `try`/`except` prevents the program from crashing and allows you to handle errors gracefully—e.g., logging the issue, returning a default value, or prompting the user to retry.

---

### **14.**

Example approach:

```python
readings = [22.1, 105.2, 24.5, -1.0, 25.0]
valid = [r for r in readings if 0 <= r <= 100]
average = sum(valid) / len(valid) if valid else 0
```

Or using a loop and conditionals. Valid readings: 22.1, 24.5, 25.0. Average = (22.1 + 24.5 + 25.0) / 3 ≈ 23.87.

---

**Last Updated:** 2026-02-03

---

### Self-Check Guidance for Students

* You should be able to **explain the reasoning**, not just choose answers
* Questions 5, 10, and 14 are especially important for **programming-based Quiz 1**
* Review [Week 4 Python chapters](./README.md#python-for-beginners--chapter-index) if any concepts are unclear
* Quiz 1 also covers IoT concepts (Week 1) and Node-RED (Week 3)—review those materials as well
