# Chapter 1: Introduction to Python and the Python Environment

## Objective
Understand the Python environment in detail, run your first Python program, and verify that you can execute `.py` files correctly.

## Prerequisites
- Python 3.x installed (from Week 2)
- A code editor (e.g., VS Code)
- Basic familiarity with the terminal/command line

---

## What is the Python Environment?

### Python Interpreter
The **Python interpreter** is the program that reads and executes your `.py` code. When you run `python filename.py`, the interpreter:
1. Reads the file
2. Translates the code into instructions the computer understands
3. Executes those instructions

Your code runs on **your computer** (the runtime), not inside the editor. The editor is just for writing; the interpreter runs the code.

### Script vs Interactive Mode
- **Script mode:** You write code in a `.py` file and run it with `python filename.py`. The whole file runs from top to bottom.
- **Interactive mode (REPL):** You run `python` with no file. You type one line at a time and press Enter to execute it immediately. Useful for quick tests. Type `exit()` to leave.

---

## python vs python3

Many systems have both `python` and `python3` commands.

- **Python 2** (legacy, end-of-life) – older version
- **Python 3** (current) – what we use in this course

**How to check:**
```bash
python --version
python3 --version
```

**Rule of thumb:** If `python` shows 3.x, use `python`. Otherwise use `python3`. On Windows, `python` usually points to Python 3. On macOS and Linux, `python3` is often required.

---

## Virtual Environments (venv)

### What is a venv?
A **virtual environment** is an isolated folder with its own Python interpreter and packages. It is separate from the system Python.

### Why use one?
- **Avoid conflicts** – Different projects may need different package versions
- **Keep system clean** – Do not install packages globally
- **Reproducibility** – Each project has its own dependencies

### How it works
1. **Create:** `python -m venv .venv` creates a `.venv` folder
2. **Activate:** Tells the shell to use the Python inside `.venv` instead of the system Python
3. **Visual cue:** Your prompt shows `(.venv)` when the venv is active

**Activation:**
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

**Deactivate:** Type `deactivate` to return to the system Python.

---

## Working Directory and Paths

The **working directory** is the folder your terminal is "in." It affects:
- Which files you can run with `python filename.py` (the file must be in or relative to the working directory)
- Relative paths like `data/file.csv` in your code

**Run from the right folder:** `python ch01_hello.py` works only if the terminal is in the folder containing `ch01_hello.py`.

**Or use a path:** From project root: `python week04/ch01_hello.py`

---

## Verification Steps (Hands-On)

Before writing code, verify your environment:

1. **Check Python version:**
   ```bash
   python --version
   ```
   Confirm you see Python 3.x.x.

2. **Try the REPL:**
   ```bash
   python
   ```
   Type `print("Hello")` and press Enter. Type `exit()` to leave.

3. **Run a script:** Create a file, save it, and run it (see Example 1 below).

4. **Optional – venv:** Create a folder, run `python -m venv .venv`, activate it, and run a script. Notice the `(.venv)` in the prompt.

---

## Example 1: Hello World

**What it does:** Prints a greeting to the console. This is the simplest Python program.

**Code:** Save as `ch01_hello.py`

```python
# ch01_hello.py
print("Hello, Python!")
print("Welcome to AUT561 Internet-of-Things Technologies.")
```

**Explanation:**
- `print()` outputs text to the terminal
- Anything in quotes `"..."` is a string literal
- Lines starting with `#` are comments and are ignored

**How to run:**
```bash
python ch01_hello.py
```
Or, if needed: `python3 ch01_hello.py`

**Expected output:**
```
Hello, Python!
Welcome to AUT561 Internet-of-Things Technologies.
```

---

## Example 2: Multiple Output Formats

**What it does:** Shows different ways to display information—useful for debugging and logging IoT data later.

**Code:** Save as `ch01_output.py`

```python
# ch01_output.py
print("=== IoT Device Status ===")
print("Device: TempSensor-01")
print("Status: ONLINE")
print("---")
print("Values can be", "combined", "with commas.")
print("Temperature:", 25.5, "°C")
```

**Explanation:**
- `print()` can take multiple arguments separated by commas; they are printed with a space between them
- You can mix strings and numbers in the same `print()` call

**How to run:**
```bash
python ch01_output.py
```

**Expected output:**
```
=== IoT Device Status ===
Device: TempSensor-01
Status: ONLINE
---
Values can be combined with commas.
Temperature: 25.5 °C
```

---

## Try It Yourself
1. Change the text in Example 1 and run it again.
2. Add a new `print` line that prints a number (e.g. `print(42)`).
3. Create a new file `my_first.py` and print your name and today's date.

---

## Key Takeaways
- The Python **interpreter** executes your `.py` code
- Use **Python 3** (`python` or `python3` depending on your system)
- **Virtual environments** isolate project dependencies
- **Working directory** matters when running scripts and using file paths
- `print()` outputs to the terminal; `#` starts a comment

---

## Next
→ [Chapter 2: Variables & Data Types](./Ch02-Variables-DataTypes.md)
