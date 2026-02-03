# Week 4: Python Programming for Beginners

> Self-study Python chapters and Quiz 1 preparation. **Quiz 1 is held in Week 5**—see [Week 5 Quiz 1 materials](../Week05/Quiz-01/) for details and scoring policy.

---

## From Week 3 to Week 4

In **[Week 3](../Week03/)**, you learned how **Python** supports IoT and automation systems. You used it to:

* **Simulate sensor data** – Using `random` and `time.sleep` for periodic sampling
* **Implement threshold logic** – Conditions and alarm checking for sensor values
* **Perform file I/O** – Reading and writing CSV files for data logging
* **Process data** – Calculating min, max, average from sensor readings
* **Build Node-RED flows** – Automation-style data flow with sensor simulation and actuator control

Python gave you **readable code** for data handling, **modular logic** with functions, and **file-based logging** for IoT applications. Week 4 helps you strengthen these foundations: the chapters below break down each concept step-by-step, with runnable examples. Use them to fill gaps, reinforce what you built in the workshops, or work through from scratch if you are new to Python.

---

## Overview

**Week 4** serves two purposes:

1. **Python self-study** – Hands-on chapters for beginners (Ch01–Ch13)
2. **Quiz 1 preparation** – Quiz 1 is held in **Week 5**; use this week to prepare (see [Week 5 Quiz 1](../Week05/Quiz-01/) for quiz details and scoring policy)

---

## Python Environment

Before running the chapter examples, ensure your Python environment is ready.

**Prerequisite:** Python 3.x installed (from [Week 2](../Week02/)). See [Week 2 Workshops](../Week02/Week02-Workshops.md) for full setup.

**Verify installation:**
```bash
python --version
# or
python3 --version
```
You should see `Python 3.x.x`. Use whichever command returns 3.x on your system.

**Recommended:** Create a virtual environment for Week 4 examples:
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux
```
When active, your prompt shows `(.venv)`.

**Run commands:** From the folder containing the `.py` file:
```bash
python ch01_hello.py
# or
python3 ch01_hello.py
```

**Working directory:** Run from the folder containing your script, or use `python path/to/file.py`.

---

## Python for Beginners – Chapter Index

These chapters provide a hands-on introduction to Python, aligned with AUT561 IoT and automation applications.

Each chapter contains:
- **Objective** and **Prerequisites**
- **At least two examples** with full code, explanation, and how to run
- **Try it yourself** exercises
- **Key takeaways** and link to the next chapter

**Run command:** `python filename.py` or `python3 filename.py` (from the folder containing the `.py` file).

### Phase 1: First Steps
- [Ch01: Introduction](./Ch01-Introduction.md) – Python environment (detailed), interpreter, venv, first program, `print()`
- [Ch02: Variables & Data Types](./Ch02-Variables-DataTypes.md) – `int`, `float`, `str`, `bool`

### Phase 2: Control Flow
- [Ch03: Operators](./Ch03-Operators.md) – Arithmetic, comparison, logical
- [Ch04: Conditionals](./Ch04-Conditionals.md) – `if`, `elif`, `else`
- [Ch05: Loops](./Ch05-Loops.md) – `for`, `while`, `break`, `continue`

### Phase 3: Reusable Logic
- [Ch06: Functions](./Ch06-Functions.md) – `def`, parameters, `return`
- [Ch07: Lambda & List Comprehensions](./Ch07-Lambda-ListComprehensions.md) – Lambda, list comprehensions
- [Ch08: Lists](./Ch08-Lists.md) – Create, access, `append`, iterate

### Phase 4: Data & Structure
- [Ch09: Dictionaries](./Ch09-Dictionaries.md) – Key-value pairs, access
- [Ch10: File I/O and CSV](./Ch10-FileIO-CSV.md) – Read/write files, CSV for IoT logging
- [Ch11: Classes](./Ch11-Classes.md) – `class`, `__init__`, `self`, methods

### Phase 5: Practical Skills
- [Ch12: Modules and Packages](./Ch12-Modules.md) – `import`, `from...import`
- [Ch13: Error Handling](./Ch13-ErrorHandling.md) – `try`, `except`, `finally`, `raise`

**Suggested order:** Follow chapters 1–13 in sequence. Each builds on the previous.

---

## Self-Assessment

**[Week 4 Self-Test Quiz](./Week04-Test01.md)** – Test your understanding of:
* Python environment, variables, data types, operators
* Conditionals, loops, functions, lambda, list comprehensions
* Lists, dictionaries, file I/O, CSV
* Classes, modules, error handling

**[Week 4 Practice Set](./Week04-Test02.md)** – Python coding exercises for Quiz 1 preparation

---

## Quiz 1 – IoT Fundamentals and Basic Programming

**Quiz 1 is held in Week 5.** See [Week 5 Quiz 1 materials](../Week05/Quiz-01/) for full details, preparation checklist, and the **programming examination scoring policy**.

Quiz 1 covers:
- **Paper-based:** IoT concepts, architectures, communication models, Node-RED fundamentals
- **Programming:** Basic Python coding, simple IoT data processing, Node-RED flow development with dashboard UI

**Preparation (complete before Week 5):**
- Review Week 1–3 materials
- Complete Week 3 workshops (Python and Node-RED)
- Work through Python chapters Ch01–Ch13 (or at least Ch01–Ch11)
- Complete [Week 4 Self-Test Quiz](./Week04-Test01.md) and [Practice Set](./Week04-Test02.md)
- Complete Week 3 self-assessment tests

---

## Quick Links

- [Course Outline](../Outline.md)
- [Week 2 Materials](../Week02/)
- [Week 3 Materials](../Week03/)
- [Week 5 Quiz 1](../Week05/Quiz-01/) – Preparation checklist and scoring policy
