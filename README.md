# AUT561: Internet-of-Things Technologies

> This course introduces the principles and applications of **Internet-of-Things (IoT) technologies** in **three phases**: (1) **Foundations and Simulation**—IoT concepts, Python, Node-RED, and tool setup; (2) **Data Systems and Backend Integration**—MQTT, databases, and Python processing and visualization; (3) **Embedded & IoT Programming using PSoC 6**—sensor telemetry (JSON, MQTT), firmware tooling and deployment (including **Bitstream**), broker and data-path integration, and **UI application connectivity** for end-to-end IoT systems. Students gain **theory** and **hands-on programming**, from simulation through data pipelines to hardware and integrated frontends.

---

[**Syllabus**](./Syllabus.md) | [**Course Outline**](./Outline.md) | [**Weekly Materials**](#-weekly-materials) | [**GitHub**](https://github.com/drsanti/AUT561-2026)

![Course Code](https://img.shields.io/badge/Course-AUT561-blue) ![Year](https://img.shields.io/badge/Year-2026-green) ![Language](https://img.shields.io/badge/Language-Python%20%7C%20Node--RED-orange)

---

![alt text](assets/cover.png)

---

> [!TIP]
> If you have a **microcontroller board** and/or you want to learn **IoT application development** in a practical way, see the [**drsanti/bitstream-app**](https://github.com/drsanti/bitstream-app) repository.

---

## 📋 Course Information

| **Details** | **Information** |
|------------|----------------|
| **Learning Format** | Hybrid (Onsite + Online) |
| **Classroom (Onsite)** | CB40610(1) |
| **Zoom Link (Online)** | [Zoom Meeting](https://kmutt-ac-th.zoom.us/j/91070941196?pwd=uBsClotSLtJJQD7eiyNJAzOIK2oXpc.1), Meeting ID: **910 7094 1196**, Passcode: **989846** |
| **Schedule** | Tuesday, 16:30 – 19:30 |
| **Evaluation** | Assignments: **20%**, Quizzes: **80%**|

---

## 🎯 Learning Outcomes

Upon successful completion of this course, students will be able to:

1. **Understand** the operations of the **internet and Internet-of-Things** systems, including communication protocols, network architectures, and device operations.
2. **Explain** the **database systems, data processing, and data visualization** techniques used in Internet-of-Things applications, including time-series data management and real-time analytics.
3. **Develop Internet-of-Things applications** using **standard software tools** such as Node-RED, MQTT brokers, containerized environments, and embedded development platforms.
4. **Design and apply** the **Internet-of-Things for industrial automation systems** appropriately, integrating hardware devices, communication protocols, data processing, and application-layer connectivity (including dashboards and embedded-to-UI data paths).

---

## 📚 Course Resources

### **Course Documents**
- **[Syllabus](./Syllabus.md)** - Complete course syllabus with detailed information
- **[Course Outline](./Outline.md)** - Weekly schedule and topics

### **Weekly Materials**
- **[Week 1: Course Introduction and IoT Overview](./Week01/)** - Introduction to Internet of Things for embedded systems and PLC-based automation
- **[Week 2: Software Installation and Development Environment Setup](./Week02/)** - Installing and configuring development tools (Python, VS Code, Node-RED, Docker, ModusToolbox)
- **[Week 3: Programming Foundations and Node-RED Introduction](./Week03/)** - Python fundamentals and Node-RED flow-based programming
- **[Week 4: Python for Beginners](./Week04/)** - Self-study chapters (Ch01–Ch13) and Quiz 1 preparation
- **[Week 5: Simulated IoT & Quiz 1](./Week05/Quiz-01/)** - Node-RED, MQTT, Python MQTT clients, and **Quiz 1** (see [Quiz 1 preparation](./Week05/Quiz-01/Quiz1-Prepare.md) for checklist and [Scoring Policy](./Week05/Quiz-01/Scoring-Policy.md))
- **[Week 6: IoT Data Storage, Processing, and Visualization](./Week06/)** - Databases (SQL/Time-series), Python data processing (Pandas/Numpy), and Dashboard visualization
- **[Week 7: IoT Data Storage, Processing, and Visualization (Cont.)](./Week07/)** - Continuation of database operations and real-time data processing
- **[Week 8: Quiz 2 – IoT Data Storage, Processing, and Visualization](./Week08/)** - Assessment on data storage, processing, and system integration
- **[Week 9: Embedded & IoT Programming using PSoC 6](./Week09/)** - Hardware reading, sensor fusion, JSON formatting, and real-time MQTT exchange
- **[Week 10: Embedded & IoT Programming using PSoC 6 (Cont.)](./Week10/)** - Digital Twin concepts, VS Code extension, and bidirectional MCU–twin communication ([outline](./Outline.md))
- **[Week 11: Embedded & IoT Programming using PSoC 6 (Cont.)](./Week11/)** - Bitstream workspace: CLI, ModusToolbox firmware, and React frontend; init, build, and program the kit ([outline](./Outline.md))
- **[Week 12: Embedded & IoT Programming using PSoC 6 (Cont.)](./Week12/)** - Embedded MQTT broker, MCU simulator, process lifecycle, and React dashboard with live telemetry ([outline](./Outline.md))
- **[Week 13: Quiz 3 – Embedded & IoT Systems Integration](./Week13/)** - Embedded architecture, MQTT/connectivity, UI integration; end-to-end firmware, broker/data path, and UI (Weeks 09–12 focus) ([outline](./Outline.md))

---

## 🛠️ Technologies & Tools

This course uses the following technologies and tools:

- **Python** - Programming language and runtime environment
- **Node-RED** - Visual flow-based programming for IoT applications
- **Docker Desktop** - Containerization platform
- **MQTT Broker** - Message queuing telemetry transport protocol (e.g., Mosquitto, HiveMQ)
- **Visual Studio Code** - Code editor (Digital Twin extension used in Week 10 per [outline](./Outline.md))
- **Database Software** - Time-series database (e.g., InfluxDB) or relational database (e.g., PostgreSQL, MySQL)
- **Python libraries** - e.g. pandas, numpy, matplotlib/plotly (data weeks); **paho-mqtt** where used
- **Git** and **Node.js (v20+)** - For Bitstream workflow and React frontend (Weeks 11–12 per [outline](./Outline.md))
- **Bitstream CLI** (`@ternion/bitstream`) - Workspace, firmware helpers, embedded broker, and simulator ([bitstream-app](https://github.com/drsanti/bitstream-app))
- **ModusToolbox** - Integrated development environment for PSoC devices
- **PSoC 6 Development Kit** - Hardware development board (e.g. CY8CKIT-062S2-AI in Bitstream materials)

---

## 📊 Assessment Breakdown

| Assessment Component | Weight |
|---------------------|--------|
| Assignments          | 20%    |
| Quiz 1               | 20%    |
| Quiz 2               | 25%    |
| Quiz 3               | 35%    |
| **Total**            | **100%** |

### Quiz Structure

Each quiz consists of **two parts**:
1. **Paper-based (handwritten)** - Theoretical knowledge and core concepts
2. **Programming** - Practical coding and implementation tasks

**Quiz Topics:**
- **Quiz 1:** Basic knowledge and basic programming (IoT fundamentals, Python, Node-RED)
- **Quiz 2:** IoT Data Storage, Processing, and Visualization (Databases, Data Processing, MQTT Integration)
- **Quiz 3:** Embedded & IoT Systems Integration (embedded architecture, hardware integration, MQTT/connectivity, UI integration; programming: firmware, broker/data path, and UI)

---

## **Assignment Submission and Quiz Attendance Policy**

* Late submissions will be considered as not submitted.
* All quizzes will be conducted **onsite at CB40610(1)** according to the scheduled class date and time.
* If a student misses a quiz **without a valid reason**, they will receive **0 points** for that quiz.
* If a student misses a quiz **with a valid reason** (supported by an official leave form or evidence), they may request a make-up quiz and will receive **70% of the score earned** (actual score × 0.7).

---

## 📈 Course Progression

This course is structured in **three progressive phases**:

### Phase 1: Foundations and Simulation (Weeks 1–4)
- IoT fundamentals and communication models (self-study)
- Python programming fundamentals (self-study)
- Node-RED flow-based programming and dashboard UI (self-study)
- Development environment setup (self-study)
- Week 4 Python for Beginners chapters (Ch01–Ch13) for extra practice
- **Assessment:** Quiz 1 (Week 5) – 20%

### Phase 2: Data Systems and Backend Integration (Weeks 5–7)
- Simulated IoT systems using Node-RED and MQTT
- Python MQTT client programming
- IoT data storage, processing, and visualization with Python
- Database operations and real-time dashboard optimization
- **Assessment:** Quiz 2 (Week 8) – 25%

### Phase 3: Embedded & IoT Programming using PSoC 6 (Weeks 9–12)
- **Learning focus:** PSoC 6 embedded IoT—sensor reading and MQTT/JSON telemetry, firmware tooling and deployment (including Bitstream), broker and data-path integration, and UI application connectivity for end-to-end IoT systems (see [Course Outline](./Outline.md))
- **Assessment:** Quiz 3 (Week 13) – 35%

**Continuous Assessment:** Assignments throughout the semester – 20%

---

## 📖 Course Description

This course covers the principles and applications of **Internet-of-Things (IoT) technologies** through a progressive three-model learning approach. Topics include **Internet networks and wireless communication protocols**, **client-server systems**, **MQTT and other IoT communication protocols**, **operations of IoT devices**, **database systems for IoT data storage**, **real-time data processing and visualization**, and **designing and applying IoT systems in industrial automation**.

The course progresses in three phases aligned with the [Course Outline](./Outline.md): (1) **Foundations and Simulation**—IoT fundamentals, Python, Node-RED, dashboards, and environment setup; (2) **Data Systems and Backend Integration**—simulated devices, MQTT, databases, Python processing and visualization; (3) **Embedded & IoT Programming using PSoC 6**—on-device sensors, JSON/MQTT telemetry, digital twin lab (Week 10), Bitstream-based firmware and React UI with broker and simulator workflows (Weeks 11–12), and integrated end-to-end IoT applications. Emphasis is on **hands-on implementation**, **real-world applications**, and **scalable system design** for industrial and automation environments.

---

## ⚙️ Prerequisites & Requirements

To successfully participate in this course, students must have access to:

- **Computer** (Laptop or Desktop)
- **Python** (Programming language and runtime environment)
- **Visual Studio Code (VS Code)** – Code editor
- **Docker Desktop** – Containerization platform
- **Node-RED** – Visual flow-based programming for IoT applications
- **MQTT Broker** – Message queuing telemetry transport protocol
- **Git** and **Node.js (v20+)** – For Bitstream and React frontend (Weeks 11–12; see [Course Outline](./Outline.md))
- **PSoC 6 Development Kit** – Hardware development board (embedded phase, Weeks 9–12)
- **ModusToolbox** – Integrated development environment for PSoC devices (embedded phase)
- **Database Software** – Time-series or relational database (e.g., InfluxDB, PostgreSQL, MySQL)

---

## 📅 Weekly Schedule Overview

| Week | Topic | Activities |
|------|-------|------------|
| 1 | Course Introduction and Internet-of-Things Overview | Learn & Practice |
| 2 | Software Installation and Development Environment Setup | Learn & Practice |
| 3 | Programming Foundations and Node-RED Introduction | Learn & Practice |
| 4 | Python for Beginners (Ch01–Ch13) | Self-study |
| 5 | Simulated IoT (Node-RED, MQTT) & **Quiz 1** | **Quiz 1 (20%)** + Learn |
| 6-7 | IoT Data Storage, Processing, and Visualization | Learn & Practice |
| 8 | **Quiz 2** – IoT Data Storage, Processing, and Visualization | **Quiz 2 (25%)** |
| 9-12 | Embedded & IoT Programming using PSoC 6 | Learn & Practice |
| 13 | **Quiz 3** – Embedded & IoT Systems Integration | **Quiz 3 (35%)** |

Note: another 20% of the grade is from assignments.

For detailed weekly topics, see the [Course Outline](./Outline.md).

---

## 📝 Grading Scale

| Score Range | Grade |
|-------------|-------|
| 80 – 100    | A     |
| 75 – 79     | B+    |
| 70 – 74     | B     |
| 65 – 69     | C+    |
| 60 – 64     | C     |
| 55 – 59     | D+    |
| 50 – 54     | D     |
| 0 – 49      | F     |

---

## 🔗 Quick Links

- [Course Syllabus](./Syllabus.md)
- [Detailed Course Outline](./Outline.md)
- [Week 1 Materials](./Week01/)
- [Week 2 Materials](./Week02/)
- [Week 3 Materials](./Week03/)
- [Week 4 Materials](./Week04/)
- [Week 5 Quiz 1 Materials](./Week05/Quiz-01/) – Quiz 1 preparation, scoring policy
- [Week 6 Materials](./Week06/)
- [Week 7 Materials](./Week07/)
- [Week 8 Quiz 2 Index](./Week08/)
- [Week 9 Materials](./Week09/)
- [Week 10 Materials](./Week10/)
- [Week 11 Materials](./Week11/)
- [Week 12 Materials](./Week12/)
- [Week 13 Quiz 3 Materials](./Week13/)

---

## 🚀 Getting Started

**New to this course?** Start here:

1. **Read the [Course Syllabus](./Syllabus.md)** to understand course objectives and requirements
2. **Review the [Course Outline](./Outline.md)** to see the full schedule
3. **Begin with [Week 1](./Week01/)** - Course Introduction and IoT Overview
4. **Complete [Week 2](./Week02/)** - Set up your development environment
5. **Start [Week 3](./Week03/)** - Learn Python and Node-RED programming
6. **Review [Week 4](./Week04/)** - Python for Beginners chapters (Quiz 1 preparation)
7. **See [Week 5 Quiz 1](./Week05/Quiz-01/)** - Quiz 1 (held in Week 5), preparation checklist, scoring policy
8. **Continue with [Week 6](./Week06/)** - IoT data storage, processing, and visualization (databases, Python, dashboards)
9. **Follow [Week 7](./Week07/)** - Databases and real-time processing (continuation of Week 6 themes)
10. **Take [Week 8 Quiz 2](./Week08/)** - IoT data storage, processing, and visualization assessment
11. **Move to [Week 9](./Week09/)** - Embedded IoT on PSoC 6: sensors, JSON, and MQTT
12. **Study [Week 10](./Week10/)** - Digital Twin concepts and MCU–twin communication (VS Code extension)
13. **Use [Week 11](./Week11/)** - Bitstream workspace: init, build, and program firmware with the React frontend layout
14. **Finish [Week 12](./Week12/)** - Embedded broker, MCU simulator, and live React dashboard telemetry
15. **Prepare for [Week 13 Quiz 3](./Week13/)** - Embedded and IoT systems integration (Weeks 09–12), paper and programming parts

---

**Last Updated:** 2026-04-21

---
