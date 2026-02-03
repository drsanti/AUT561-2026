# **AUT561 – Week 3 Lab: Node-RED Automation Simulation**

## **Node-RED Flow-Based Programming for Automation Systems**

### **Lab Title**

**Node-RED Realistic Automation Simulation**

### **Week**

Week 3 – Programming Foundations and Node-RED Introduction (Quiz 1 Foundation)

---

## **Lab Objectives**

By completing this lab, students will be able to:

* Build and test basic **Node-RED** flows for automation-style data flow
* Create continuous sensor simulation with periodic sampling
* Implement threshold logic and state management (NORMAL/WARNING/ALARM)
* Simulate actuator control (fan/relay ON/OFF)
* Log alarm events to files
* Create simple dashboards for monitoring (optional)

---

## **Required Tools**

* Node-RED (installed and running)
* Web browser
* Node-RED Dashboard (optional, for Part E5)

---

## **Part E – Node-RED Realistic Automation Simulation (No MQTT Yet)**

### **Goal**

Build a small simulated automation cell in Node-RED:

* A "sensor" produces values periodically (like a PLC scan / sampling cycle)
* Logic checks thresholds and sets states (NORMAL/WARNING/ALARM)
* An "actuator" output (fan/relay) is turned ON/OFF based on conditions
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

   * Mode: "Rate limit" or "delay each message"
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
   * Add rules (in this order; Node-RED Switch uses one operator per rule, not combined conditions):

     * `<= 40` → output 1 (NORMAL)
     * **is between** `40` and `48` → output 2 (WARNING)
     * `> 48` → output 3 (ALARM)

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
   * Action: "Append to file"
   * Create file if it doesn't exist

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

# **Verification Checklist**

After completing all tasks, verify that everything is working correctly:

| Category               | Verification Check                  |
| ---------------------- | ----------------------------------- |
| Node-RED flows         | All flows deploy and run without errors |
| Sensor simulation      | Continuous temperature values appear in Debug |
| Threshold logic        | State changes correctly (NORMAL/WARNING/ALARM) |
| Actuator control       | Fan turns ON/OFF based on state |
| Alarm logging          | Alarm events are logged to file |
| Dashboard (optional)   | Values update live in dashboard |

**Check that:**
- Node-RED flows execute and display data correctly
- State transitions work as expected
- Actuator control responds to state changes
- Alarm logging captures events properly

⚠️ **If something is not working, review the troubleshooting sections and ask for help before moving to Week 4.**

---

**Previous:** Complete **[Week03-Workshops-Python.md](./Week03-Workshops-Python.md)** for Python fundamentals.

---

**Last Updated:** 2026-01-12

---
