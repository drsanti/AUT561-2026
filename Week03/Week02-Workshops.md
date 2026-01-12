# **AUT561 – Week 3 Lab (Revised)**

## **Python Fundamentals + Node-RED Data Flow for Automation Systems**

### **Lab Title**

**Python Foundations for IoT Automation + Node-RED Flow Logic**

### **Week**

Week 3 – Programming Foundations and Node-RED Introduction (Quiz 1 Foundation)

---

## **Lab Objectives (Python + Automation Focus)**

By completing this lab, students will be able to:

* Use Python **syntax, data types, functions, conditions, and loops**
* Create a **Python project folder** and run scripts properly
* Create and use a **virtual environment**
* Install and import a **Python package** (module usage)
* Simulate sensor signals using **random**
* Implement periodic monitoring using **time.sleep**
* Perform **basic file I/O** and simple data processing (min/max/avg)
* Build and test basic **Node-RED** flows for automation-style data flow

---

## **Required Tools**

* VS Code
* Python 3.x
* Node-RED
* Terminal access

---

# **Part A – Python Project Setup + Virtual Environment**

## **Task A1: Create a Python Project Folder**

Create a folder:

```
week03_lab_python/
```

Inside it create:

* `src/`
* `data/`
* `README.md`

☐ Folder structure created

---

## **Task A2: Create and Activate Virtual Environment**

Open terminal in `week03_lab_python/`.

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Verify:

```bash
python --version
pip --version
```

☐ Virtual environment activated
☐ Python and pip versions shown

---

## **Task A3: Install a Package**

Install one package used later in the course (example: MQTT library):

```bash
pip install paho-mqtt
```

Create `src/package_check.py`:

```python
import paho.mqtt.client as mqtt
print("paho-mqtt imported OK")
```

Run:

```bash
python src/package_check.py
```

☐ Package installed successfully
☐ Script runs and prints confirmation

---

# **Part B – Python Fundamentals (Sensor Simulation + Control Logic)**

## **Task B1: Sensor Simulator Using `random`**

Create `src/sensor_simulator.py`.

**Requirements**

* Use `random` to generate sensor values (temperature)
* Use a loop to generate at least 20 samples
* Use `time.sleep()` to simulate sampling time (e.g., 0.5 seconds)
* Print values clearly

Example skeleton (students may extend):

```python
import random
import time

for i in range(20):
    temp = round(random.uniform(25, 55), 2)
    print(f"Sample {i+1:02d}: Temperature = {temp} °C")
    time.sleep(0.5)
```

☐ Uses random
☐ Uses loop
☐ Uses sleep
☐ Runs correctly

---

## **Task B2: Alarm Logic (PLC-style Threshold Check)**

Create `src/alarm_logic.py`.

**Requirements**

* Use `if/else` logic
* Create a function `check_alarm(value, threshold)`
* Print `"NORMAL"` or `"ALARM"`
* Use random temperature values in a loop

Example pattern:

```python
import random
import time

THRESHOLD = 40.0

def check_alarm(value, threshold):
    return value > threshold

for _ in range(15):
    temp = round(random.uniform(25, 55), 2)
    alarm = check_alarm(temp, THRESHOLD)
    status = "ALARM" if alarm else "NORMAL"
    print(f"Temp={temp:5.2f} => {status}")
    time.sleep(0.4)
```

☐ Uses function
☐ Uses condition
☐ Output is correct

---

# **Part C – File I/O + Basic Data Processing**

## **Task C1: Log Sensor Data to a CSV File**

Create `src/data_logger.py`.

**Requirements**

* Generate at least 30 temperature samples
* Save to `data/temp_log.csv`
* Each row: `timestamp,temp,status`
* Use `time.time()` or a readable timestamp

Example approach:

```python
import random, time

THRESHOLD = 40.0
out_path = "data/temp_log.csv"

with open(out_path, "w", encoding="utf-8") as f:
    f.write("timestamp,temp,status\n")
    for _ in range(30):
        ts = time.time()
        temp = round(random.uniform(25, 55), 2)
        status = "ALARM" if temp > THRESHOLD else "NORMAL"
        f.write(f"{ts},{temp},{status}\n")
        time.sleep(0.2)

print("Log saved:", out_path)
```

☐ File created in `/data`
☐ CSV contains correct columns
☐ At least 30 rows logged

---

## **Task C2: Read the CSV and Compute Simple Statistics**

Create `src/data_processing.py`.

**Requirements**

* Read `data/temp_log.csv`
* Compute:

  * number of samples
  * minimum temperature
  * maximum temperature
  * average temperature
  * alarm count
* Print the result clearly

Example output format:

```
Samples: 30
Min: 26.10
Max: 54.87
Avg: 39.22
Alarms: 12
```

☐ Reads file successfully
☐ Prints min/max/avg
☐ Counts alarms

---

# **Part D – Optional Keyboard-Controlled Monitoring (Sleep + WaitKey / Key Press)**

Some students like interactive monitoring like an HMI test panel.

Choose **one option**:

### Option 1 (Recommended, no extra library): Press Enter to take a sample

Create `src/manual_sample.py`.

**Requirements**

* Program waits for user input each sample
* Each Enter generates a new random sensor value
* Type `q` to quit

☐ Manual sampling works
☐ Quit works

---

### Option 2 (Advanced): Use OpenCV `waitKey()`

Install:

```bash
pip install opencv-python
```

Create `src/waitkey_demo.py`.

**Requirements**

* Show a blank window
* Use `cv2.waitKey(200)` inside loop
* Press `q` to quit
* Print a sensor value each cycle

*(This is optional; only if you want to introduce `waitKey`.)*

☐ waitKey loop works
☐ Press q quits

---
Got it — here’s an upgraded **Week 3 Lab Sheet Node-RED section** that feels like a **real automation simulation**: continuous sampling (loop), timing (delay), decision logic (switch/if-else), alarms, and a simple “actuator” output. It still stays Week-3 friendly (no MQTT yet), but sets you up perfectly for Week 5.

You can **replace Part E** in the previous lab sheet with the version below.

---

## **Part E – Node-RED Realistic Automation Simulation (No MQTT Yet)**

### **Goal**

Build a small simulated automation cell in Node-RED:

* A “sensor” produces values periodically (like a PLC scan / sampling cycle)
* Logic checks thresholds and sets states (NORMAL/WARNING/ALARM)
* An “actuator” output (fan/relay) is turned ON/OFF based on conditions
* Debugging and visualization are included

> Think of this as a mini PLC program built using Node-RED blocks.

---

# **E1) Flow 1 — Continuous Sensor Simulation (Loop + Delay)**

### **What you build**

A periodic generator that outputs a sensor value every 0.5–1 second.

### **Nodes**

* **Inject**
* **Function**
* **Delay**
* **Debug**

### **Steps**

1. Add an **Inject** node

   * Set **Repeat** every `1 second`
   * Set payload type to **timestamp** (default is fine)

2. Add a **Function** node named: **Simulated Temperature Sensor**

   * Code:

   ```javascript
   // Simulated temperature sensor (25 to 55 °C)
   const temp = +(25 + Math.random() * 30).toFixed(2);
   msg.payload = temp;
   msg.topic = "temp";
   return msg;
   ```

3. Add a **Delay** node named: **Sampling Delay**

   * Mode: “Rate limit” or “delay each message”
   * Set delay to `0.5 seconds` (or 1 second)

4. Add a **Debug** node (output msg.payload)

5. Wire:

```
Inject → Function → Delay → Debug
```

6. Deploy and verify values continuously appear in Debug.

✅ **Check**

* Debug panel shows new temperature values continuously
* Timing feels periodic (like sampling)

---

# **E2) Flow 2 — Threshold Logic (Switch + If/Else Equivalent)**

### **What you build**

Logic that labels the system state:

* NORMAL: temp ≤ 40
* WARNING: 40 < temp ≤ 48
* ALARM: temp > 48

### **Nodes**

* **Switch**
* **Change** (or Function)
* **Debug**

### **Steps**

1. Add a **Switch** node named: **Temp State Switch**

   * Property: `msg.payload`
   * Add rules:

     * `<= 40`
     * `> 40 and <= 48`
     * `> 48`

2. Add three **Change** nodes (or Function nodes) to tag the state:

**Change node 1: NORMAL**

* Set `msg.state` to string `"NORMAL"`

**Change node 2: WARNING**

* Set `msg.state` to string `"WARNING"`

**Change node 3: ALARM**

* Set `msg.state` to string `"ALARM"`

3. Add a **Debug** node configured to show the **complete message object**.

4. Wire:

```
... Sensor Flow Output → Switch
Switch output 1 → Change(NORMAL) → Debug
Switch output 2 → Change(WARNING) → Debug
Switch output 3 → Change(ALARM) → Debug
```

✅ **Check**

* Debug shows both `msg.payload` (temperature) and `msg.state`
* State changes appropriately when temperature crosses thresholds

---

# **E3) Flow 3 — Actuator Simulation (Fan/Relay ON/OFF + Delay)**

### **What you build**

Simulate an actuator (fan/relay) controlled by temperature:

* If WARNING or ALARM → Fan ON
* If NORMAL → Fan OFF
* Add a small delay to avoid switching too rapidly (basic stability)

### **Nodes**

* **Switch**
* **Change**
* **Delay**
* **Debug**

### **Steps**

1. From the output after the state is set, add a **Switch** node named: **Fan Control**

   * Property: `msg.state`
   * Rules:

     * `== "NORMAL"`
     * `== "WARNING"`
     * `== "ALARM"`

2. Add **Change** nodes:

* For NORMAL branch: set `msg.fan = "OFF"`
* For WARNING and ALARM branches: set `msg.fan = "ON"`

3. Add a **Delay** node named **Actuator Update Delay**

   * Set to `0.2–0.5 seconds`

4. Add Debug node to show `msg.fan` and `msg.state`

✅ **Check**

* When state becomes WARNING/ALARM → fan becomes ON
* When state returns NORMAL → fan becomes OFF

---

# **E4) Flow 4 — Alarm Event Logger (File Logging like a Real System)**

### **What you build**

When ALARM happens, log the alarm event with timestamp to a file.

### **Nodes**

* **Switch**
* **Function**
* **File**

### **Steps**

1. Add a **Switch** node:

   * Property: `msg.state`
   * Rule: `== "ALARM"`

2. Add a **Function** node named: **Format Alarm Log**

   ```javascript
   const ts = new Date().toISOString();
   const temp = msg.payload;
   msg.payload = `${ts},TEMP_ALARM,${temp}\n`;
   return msg;
   ```

3. Add a **File** node:

   * Filename: `alarm_log.csv`
   * Action: “Append to file”
   * Create file if it doesn’t exist

✅ **Check**

* Alarm file is created
* Each ALARM adds a new line

> This directly matches real automation practice: alarms get logged, not just displayed.

---

# **E5) (Optional) Dashboard Mini-HMI (More Realistic Monitoring)**

If dashboard is installed:

* Add **Gauge** for temperature
* Add **Text** for state
* Add **LED / text indicator** for fan status

✅ **Check**

* Values update live like a simple HMI panel

---

## **What This Simulates (Real Automation Mapping)**

| Automation Concept    | Node-RED Equivalent   |
| --------------------- | --------------------- |
| Sensor sampling cycle | Inject repeat + Delay |
| PLC logic block       | Switch / Function     |
| Status states         | msg.state             |
| Actuator output       | msg.fan               |
| Alarm logging         | File append           |

---

---

# **Verification Checklist**

After completing all tasks, verify that everything is working correctly:

| Category               | Verification Check                  |
| ---------------------- | ----------------------------------- |
| Python fundamentals    | Types, loops, conditions, functions work correctly |
| Virtual environment    | Created and activated successfully  |
| Modules/packages       | Packages install and import without errors |
| File I/O               | CSV files are written and read correctly |
| Data processing        | Min/max/avg calculations and alarm counting work |
| Timing/automation      | Random data generation and sleep timing work correctly |
| Node-RED               | Flows run and threshold logic works as expected |

**Check that:**
- Python scripts run without errors
- Node-RED flows execute and display data correctly
- Data is being processed and logged properly
- All components work together as expected

⚠️ **If something is not working, review the troubleshooting sections and ask for help before moving to Week 4.**

---
