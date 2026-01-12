# **Week 3 Self-Test Quiz**

**Topic: Programming Foundations and Node-RED Logic for Automation Systems**

---

## **Questions**

### **1. Short Answer**

Why is programming an essential skill for modern automation engineers, even when PLCs are used for real-time control?

---

### **2. Multiple Choice**

Which Python data type is most appropriate for representing a **temperature sensor value**?

A. `string`
B. `boolean`
C. `float`
D. `list`

---

### **3. True or False**

In automation-style Python programs, `while` loops are commonly used to represent continuous monitoring or cyclic execution.

---

### **4. Short Answer**

How does a **Python function** relate to a **PLC function block** in terms of software design?

---

### **5. Code Understanding (Python)**

Consider the following Python code:

```python
import random
import time

for i in range(5):
    value = random.uniform(20, 50)
    print(value)
    time.sleep(1)
```

Explain **two things** this code is simulating in an automation or IoT context.

---

### **6. Multiple Choice**

Which Python module is commonly used to introduce **delays or timing behavior** in automation simulations?

A. `math`
B. `random`
C. `time`
D. `sys`

---

### **7. True or False**

Writing sensor data to a file (such as CSV) is useful only for debugging and has no real application in automation systems.

---

### **8. Short Answer**

Why is **basic file I/O and data processing** (min, max, average) important in automation and IoT applications?

---

### **9. Multiple Choice**

In Node-RED, which node is typically used to represent **decision logic** similar to `if / else` conditions in PLC or Python programs?

A. Inject
B. Debug
C. Switch
D. Delay

---

### **10. Code Understanding (Node-RED Logic)**

A Node-RED flow uses:

* an **Inject** node repeating every 1 second
* a **Function** node generating a random temperature
* a **Delay** node
* a **Switch** node that outputs NORMAL or ALARM

What real automation behavior does this flow simulate?

---

### **11. True or False**

The **Debug** node in Node-RED serves a role similar to online monitoring or watch variables in PLC programming tools.

---

### **12. Scenario-Based Question**

A Node-RED flow rapidly switches an actuator simulation ON and OFF when the sensor value is near a threshold.

1. What is this problem called?
2. Name **one technique** that can be used to reduce or prevent it.

---

## **Answers**

### **1.**

Programming allows automation engineers to implement flexible logic, data processing, communication, monitoring, and integration with IoT systems, extending traditional PLC-based control beyond local and fixed functionality.

---

### **2.**

**C. `float`**

---

### **3.**

**True**

Continuous loops are commonly used to simulate cyclic scanning, monitoring, and periodic sampling.

---

### **4.**

A Python function, like a PLC function block, encapsulates reusable logic, improves code organization, and allows consistent behavior across multiple parts of a program.

---

### **5.**

The code simulates:

* Periodic sensor sampling using a loop and timed delay
* Random variation in sensor readings to mimic real-world measurement noise

---

### **6.**

**C. `time`**

---

### **7.**

**False**

File logging is essential for historical analysis, diagnostics, trend monitoring, and predictive maintenance in automation systems.

---

### **8.**

Basic data processing allows engineers to understand system behavior over time, detect abnormal conditions, evaluate performance, and support maintenance and optimization decisions.

---

### **9.**

**C. Switch**

---

### **10.**

This flow simulates a real-time automation system where a sensor is sampled periodically, data is processed with timing constraints, and control decisions (NORMAL or ALARM) are made based on threshold logic.

---

### **11.**

**True**

The Debug node provides visibility into system variables and message values, similar to monitoring tools in PLC environments.

---

### **12.**

1. The problem is called **actuator chattering**.
2. It can be reduced using techniques such as **hysteresis**, **delays**, **minimum ON/OFF times**, or filtering noisy sensor signals.

---

**Last Updated:** 2026-01-12

---

### ✔ Self-Check Guidance for Students

* You should be able to **explain the reasoning**, not just choose answers
* Questions 5, 10, and 12 are especially important for **programming-based Quiz 1**
* If Node-RED questions feel unclear, revisit the **Week 3 lab flows**

---

**Last Updated:** 2026-01-12

---

