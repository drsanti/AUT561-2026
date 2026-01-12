# **Week 1 – Internet of Things for Embedded Systems and PLC-Based Automation**

## 1. From Classical Automation to Connected Automation

Automation engineering has traditionally been centered around **PLCs, sensors, actuators, and control panels** operating inside closed and well-defined industrial networks. These systems are deterministic, reliable, and safe—but they are also **isolated**. Data typically remains inside the machine or production line and is only visible through local HMIs or SCADA systems.

The Internet of Things (IoT) extends classical automation by **connecting PLC-based and embedded systems to wider IP-based networks**, enabling:

* Remote monitoring and diagnostics
* Centralized data collection
* Historical data storage and analytics
* Predictive maintenance
* Integration with higher-level IT systems

For modern automation engineers, IoT is not a replacement for PLCs or embedded controllers. Instead, it represents a **natural evolution of automation systems toward connectivity and data-driven operation**.

---

## 2. What IoT Means in an Embedded and PLC Context

In consumer technology, IoT often refers to smart home devices. In industrial automation, IoT has a very different meaning and set of requirements.

In an embedded and PLC context, IoT refers to systems where:

* Sensors are connected to **PLCs or microcontrollers**
* Embedded firmware or PLC programs collect real-time process data
* Data is transmitted using **industrial or IP-based communication**
* Central systems analyze data and support monitoring, optimization, or supervisory control

Industrial IoT systems prioritize **reliability, determinism, safety, and maintainability**, not convenience or novelty.

---

## 3. Core Elements of an Embedded IoT Automation System

### 3.1 Sensors and Actuators (Field Level)

At the lowest level, IoT systems interact with the physical world through the same devices used in traditional automation:

* Analog sensors (temperature, pressure, flow, level)
* Digital sensors (limit switches, proximity sensors, encoders)
* Actuators (motors, valves, relays, solenoids)

IoT does not change the physical layer—it changes **how data from this layer is used and shared**.

---

### 3.2 Controllers: PLCs and Embedded MCUs

This is the core domain of automation engineers.

**PLCs** are responsible for:

* Deterministic control loops
* Safety-critical logic
* Interlocking and sequencing
* Real-time I/O control

**Embedded Microcontrollers (MCUs)** are responsible for:

* High-speed sensor acquisition
* Signal conditioning and filtering
* Data formatting and preprocessing
* Communication using modern protocols
* Edge-level computation

In IoT-based automation systems, **PLCs and MCUs coexist**, each handling tasks suited to their strengths.

---

### 3.3 Communication Networks

Traditional automation relies on fieldbus and industrial Ethernet protocols such as:

* Modbus
* CAN / CANopen
* Profibus
* EtherCAT

IoT-based systems introduce **IP-based communication**, including:

* Ethernet
* Wi-Fi
* MQTT messaging

The key concept is **bridging the field level with supervisory and data systems** while preserving deterministic control behavior.

---

### 3.4 Data Processing and Supervisory Systems

Instead of relying only on local HMIs or SCADA systems, IoT introduces:

* Edge processing near the machine
* Centralized servers
* On-premise or cloud-based data systems

Data from PLCs and MCUs can be:

* Logged continuously
* Analyzed over time
* Used for predictive maintenance
* Visualized remotely

---

### 3.5 Human–Machine Interfaces and Dashboards

IoT systems provide additional interfaces such as:

* Web-based dashboards
* Mobile monitoring tools
* Advanced visualization and analytics

These interfaces **complement** traditional HMIs rather than replacing them.

---

## 4. How IoT Enhances PLC-Based Automation

IoT does not remove the PLC from the system. Instead, it **extends the PLC’s visibility and reach**.

**Traditional PLC Systems**

* Local I/O and control
* Limited historical data
* Manual fault diagnosis

**PLC + IoT Systems**

* Remote monitoring
* Long-term data storage
* Centralized analytics
* Predictive maintenance
* Remote diagnostics

For example, a PLC may control a motor locally, while IoT systems monitor vibration, temperature, and runtime data across many machines.

---

## 5. PLC–MCU Integration in Modern Automation Systems

### 5.1 Why PLC–MCU Integration Is Necessary

While PLCs excel at control, they are not always optimal for:

* High-frequency data sampling
* Complex signal processing
* Advanced communication protocols
* Edge analytics

MCUs complement PLCs by handling these tasks while leaving deterministic control untouched.

---

### 5.2 Roles of PLCs and MCUs

**PLCs**

* Execute control logic
* Enforce safety and interlocks
* Interface with actuators

**MCUs**

* Acquire and preprocess sensor data
* Translate protocols
* Publish data to IoT systems
* Support edge intelligence

IoT systems **wrap connectivity and intelligence around PLC-based control**, rather than replacing it.

---

## 6. Common PLC–MCU Integration Architectures

### PLC as Master, MCU as Smart Sensor

The MCU performs advanced sensing and preprocessing, while the PLC uses the results in control logic.

### PLC for Control, MCU as IoT Gateway

The MCU reads PLC data and exposes it to IoT systems without modifying PLC programs.

### Bidirectional PLC–MCU Communication

The MCU enables supervisory commands while the PLC validates and executes them safely.

### MCU as Edge Intelligence, PLC as Executor

The MCU detects conditions or anomalies, and the PLC performs physical actions.

---

## 7. Practical Automation Use Cases

* Motor condition monitoring and predictive maintenance
* Energy monitoring at machine and plant level
* Environmental monitoring in factories and clean rooms
* Retrofitting legacy PLC systems for remote monitoring

These use cases reflect **real industrial IoT deployments**, not experimental prototypes.

---

## 8. Architecture Models Used in This Course

This course follows a progressive structure aligned with industrial practice:

### Model 1: Simulated IoT Systems

Understanding data flow, messaging, and system integration without hardware risk.

### Model 2: Embedded and PLC-Oriented IoT Systems

Working with real MCUs, sensors, and industrial-style communication.

### Model 3: Integrated Automation Systems

Combining embedded devices, PLC-style logic, backend processing, and monitoring dashboards.

---

## 9. Skills You Are Building as an Automation Engineer

By the end of this course, students will be able to:

* Interface sensors and actuators at hardware level
* Program embedded systems for data acquisition
* Integrate PLC-based control with IoT communication
* Design scalable automation architectures
* Connect shop-floor systems to supervisory and analytics layers

These skills directly support **Industry 4.0 and smart factory environments**.

---

## 10. Week 1 Takeaway

After Week 1, students should clearly understand:

* How IoT fits into embedded and PLC-based automation
* Why PLC–MCU integration is essential
* How classical automation evolves into connected automation
* What types of systems will be built throughout the course

---

## Looking Ahead

Week 1 answers:
**“Why do embedded and PLC engineers need IoT?”**

Week 2 will focus on:
**“What tools and environments are required to start building these systems?”**

---

**Last Updated:** 2026-01-12

---
