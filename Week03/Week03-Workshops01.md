# **AUT561 – Week 3 Lab: Python Fundamentals**

## **Python Programming Foundations for IoT Automation**

### **Lab Title**

**Python Foundations for IoT Automation**

### **Week**

Week 3 – Programming Foundations and Node-RED Introduction (Quiz 1 Foundation)

---

## **Lab Objectives**

By completing this lab, students will be able to:

* Use Python **syntax, data types, functions, conditions, and loops**
* Create a **Python project folder** and run scripts properly
* Create and use a **virtual environment**
* Install and import a **Python package** (module usage)
* Simulate sensor signals using **random**
* Implement periodic monitoring using **time.sleep**
* Perform **basic file I/O** and simple data processing (min/max/avg)

---

## **Required Tools**

* VS Code
* Python 3.x
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

**Check that:**
- Python scripts run without errors
- Data is being processed and logged properly
- All Python components work as expected

⚠️ **If something is not working, review the troubleshooting sections and ask for help before moving to the Node-RED workshop.**

---

**Next:** Complete **[Week03-Workshops-NodeRED.md](./Week03-Workshops-NodeRED.md)** for Node-RED automation flows.

---

**Last Updated:** 2026-01-12

---
