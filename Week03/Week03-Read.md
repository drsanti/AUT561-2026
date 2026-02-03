# **Week 3 – Programming Foundations and Node-RED for Automation Systems**

## Why Week 3 Matters for Automation Engineers

Automation engineers do not program for the sake of programming.
They program to **move data**, **make decisions**, and **control systems reliably**.

In modern automation systems:

* PLCs execute deterministic control
* Embedded systems acquire and preprocess data
* Software systems move, visualize, and analyze that data

Week 3 provides the **software foundation** that connects embedded devices and PLC-based systems to IoT platforms. The focus is not computer science theory, but **engineering-oriented programming skills** you will repeatedly use in later weeks.

---

## Part 1 – Programming Foundations for Automation Engineers

### Programming as an Engineering Tool

In automation, programming is used to:

* Read sensor values
* Process signals
* Format data for communication
* Apply logic and conditions
* Interface with other systems

In this course, **Python** is used because it is:

* Easy to read and maintain
* Widely used in industrial IoT
* Excellent for data handling and integration
* Common in backend and edge systems

Python complements PLC programming rather than replacing it.

---

## Python Concepts You Must Master (Automation Context)

### 1. Variables and Data Types

Automation systems deal with **values**, not abstract data.

Examples:

* Temperature readings
* Motor speed
* Alarm states
* Counters

Key data types:

* `int` → counters, IDs
* `float` → sensor values
* `bool` → status flags
* `str` → labels, messages

Example:

```python
temperature = 36.5
motor_running = True
alarm_message = "Overtemperature"
```

---

### 2. Conditions and Logic (Like PLC Logic)

Python logic directly maps to PLC concepts:

* `if` statements → conditional logic
* Comparisons → thresholds and limits
* Boolean logic → interlocks

Example:

```python
if temperature > 40:
    alarm = True
else:
    alarm = False
```

This mirrors **PLC ladder or structured text logic**.

---

### 3. Loops (Continuous Monitoring)

Automation systems run continuously.

Python loops simulate:

* Continuous monitoring
* Periodic sampling
* Background services

Example:

```python
while True:
    read_sensor()
    process_data()
```

This prepares you for:

* Data acquisition loops
* MQTT publishing loops
* Monitoring scripts

---

### 4. Functions (Reusable Logic Blocks)

Functions are equivalent to **PLC function blocks**.

Example:

```python
def check_temperature(temp):
    return temp > 40
```

Functions help:

* Keep code structured
* Avoid repetition
* Improve reliability

---

### 5. Basic File and Data Handling

Automation systems often need to:

* Log data
* Store configuration values
* Save system states

Python makes this straightforward and readable.

---

## Part 2 – From Python Scripts to Automation Data Flow

At this stage, Python is not used to control machines directly.
Instead, it acts as:

* A **data handler**
* A **communication endpoint**
* A **bridge between devices and systems**

Typical Python roles in automation:

* Simulated sensor data generator
* MQTT publisher or subscriber
* Data processor before storage
* Backend logic engine

This prepares you for **Week 5 onward**, where Python communicates with Node-RED and embedded devices.

---

## Part 3 – Introduction to Node-RED for Automation Logic

### What Is Node-RED?

Node-RED is a **flow-based programming tool** widely used in:

* Industrial IoT
* Automation dashboards
* Rapid system integration

Instead of writing long code files, you **connect functional blocks** (nodes) visually.

For automation engineers, Node-RED feels similar to:

* Function block diagrams
* Signal flow diagrams
* Control system block diagrams

---

## Node-RED Concepts You Must Understand

### 1. Nodes and Flows

* **Nodes** perform individual tasks
* **Flows** define how data moves between nodes

Automation analogy:

* Nodes = function blocks
* Wires = signal paths

---

### 2. Messages and Payloads

Node-RED passes **messages**, usually stored in:

```text
msg.payload
```

The payload might contain:

* Sensor values
* Status flags
* Commands
* JSON objects

Understanding `msg.payload` is critical for later MQTT and dashboard work.

---

### 3. Inject Node (Data Source)

The Inject node is used to:

* Simulate sensor values
* Trigger events manually
* Start flows

This is useful for:

* Testing logic
* Debugging flows
* Simulating PLC inputs

---

### 4. Debug Node (System Visibility)

The Debug node shows:

* Data values
* Message structures
* Flow behavior

In automation terms, it is your **online monitoring tool**.

---

### 5. Function Node (Logic Processing)

The Function node allows you to write **JavaScript-based logic** inside Node-RED.

This is similar to:

* PLC structured text
* Embedded C logic blocks

Example logic:

```javascript
if (msg.payload > 40) {
    msg.payload = "ALARM";
}
return msg;
```

---

## Part 4 – Node-RED Dashboard (Basic Operator Interface)

Automation systems need **visibility**.

Node-RED dashboards allow you to:

* Display values
* Show status indicators
* Trigger actions (buttons)

This is not meant to replace industrial HMIs, but it:

* Enables fast prototyping
* Demonstrates data flow clearly
* Helps understand monitoring concepts

Later in the course, dashboards represent:

* Operator panels
* Supervisory interfaces
* Remote monitoring systems

---

## Part 5 – Connecting Python Thinking and Node-RED Thinking

By the end of Week 3, students should understand:

| PLC Concept   | Python Equivalent | Node-RED Equivalent |
| ------------- | ----------------- | ------------------- |
| Input         | Variable          | Inject / MQTT In    |
| Logic         | if / functions    | Function node       |
| Output        | Variable / print  | Debug / Dashboard   |
| Program cycle | Loop              | Flow execution      |

This conceptual mapping is intentional.
It prepares you to integrate **embedded devices, PLC logic, and IoT systems** smoothly.

---

## Hands-On Focus for Week 3

By the end of this week, students should be able to:

* Write basic Python scripts for automation-style logic
* Create Node-RED flows using Inject, Debug, and Function nodes
* Understand how data flows through a system
* Debug logic and data visually

These skills are **directly tested in Quiz 1**.

---

## What You Should Take Away from Week 3

After this week, you should clearly understand:

* How programming supports automation systems
* How Python complements PLC logic
* How Node-RED represents automation data flow
* How software layers connect to physical systems

---

## Looking Ahead

**Week 3 answers:**
“How do we program logic and data flow for automation-oriented IoT systems?”

**Week 4 (Python for Beginners & Quiz 1):**

* **Python for Beginners** chapters (Ch01–Ch13) – hands-on exercises for variables, functions, loops, lists, dicts, file I/O, classes, etc. See [Week 4 Materials](../Week04/).
* **Quiz 1** – IoT fundamentals, Python basics, Node-RED flow logic

**Week 5:**

* Simulated IoT systems using MQTT and Node-RED

---

**Last Updated:** 2026-02-03

---
