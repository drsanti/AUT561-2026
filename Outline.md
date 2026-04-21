# **Course Outline – AUT561: Internet-of-Things Technologies**

---

## **Week 1: Course Introduction and Internet-of-Things Overview**

* Course overview, objectives, and expected learning outcomes
* Introduction to **Internet-of-Things (IoT)** concepts and application domains
* Definition, characteristics, and key components of IoT systems
* Real-world IoT use cases in **industrial automation and monitoring**
* Overview of **IoT system architecture**: devices, networks, servers, and applications
* Course structure, learning format, software tools, and assessment requirements

---

## **Week 2: Software Installation and Development Environment Setup**

* Overview of required development tools for IoT application development
* Installation and configuration of essential software tools:

  * **Visual Studio Code (VS Code)** installation and essential extensions
  * **Python** runtime environment installation and version verification
  * **Node-RED** installation and initial setup
  * **Docker Desktop** installation and basic container management
  * **ModusToolbox** installation and configuration for embedded development
* Verification and testing of installed tools:

  * Checking VS Code installation and extensions
  * Checking Python and pip functionality
  * Testing Docker container operations
  * Confirming Node-RED installation and accessibility
  * Verifying ModusToolbox installation and workspace setup
* Troubleshooting common installation issues
* **Hands-on:** Verifying all software tools are properly installed and functional

---

## **Week 3: Programming Foundations and Node-RED Introduction**

> **Foundation for Quiz 1**

* Overview of the IoT application development workflow
* **Python programming fundamentals**:

  * Python syntax, data types, functions, and basic program structures
  * Setting up Python projects and virtual environments
  * Running Python programs and scripts
  * Working with Python modules and packages
  * Basic file I/O and data processing in Python
* **Node-RED flow-based programming**:

  * Node-RED workspace overview and navigation
  * Basic flow design and node connections
  * Understanding input/output nodes and data flow
  * Working with function nodes and JavaScript code in Node-RED
* **Node-RED Dashboard (UI)**:

  * Dashboard installation and configuration
  * Creating basic UI components (gauges, charts, buttons, text displays)
  * Connecting data flows to dashboard widgets
  * Building simple interactive dashboards
* **Hands-on:**

  * Writing and running Python programs for IoT data handling
  * Building simple Node-RED flows with dashboard-based data visualization

---

## **Week 4: Python for Beginners**

* **Python Programming for Beginners (self-study)**

  * Hands-on chapters Ch01–Ch13: introduction and Python environment, variables, conditionals, loops, functions, lambda and list comprehensions, lists, dictionaries, file I/O and CSV, classes, modules, error handling
  * Each chapter includes runnable examples and exercises; supports Quiz 1 preparation
  * See [Week 4 Materials](./Week04/) for chapter index and links

---

## **Week 5: Simulated IoT Systems Using Node-RED and MQTT & Quiz 1**

* Introduction to **Model 1: Simulated IoT Systems** and its role in IoT system learning
* Overview of **Node-RED** as a flow-based development platform for IoT applications
* Design and configuration of **MQTT brokers**, topics, and publish/subscribe patterns
* Integration of **simulated IoT devices** with Node-RED flows
* **Python MQTT client programming**:

  * Using Python libraries (e.g., paho-mqtt) for MQTT communication
  * Creating Python scripts to publish and subscribe to MQTT topics
  * Integrating Python MQTT clients with Node-RED flows
* **IoT data flow design**, message processing, and event-driven logic
* Basic techniques for **system monitoring and debugging** in simulated environments
* **Hands-on:** Designing and implementing a complete simulated IoT system using Node-RED and MQTT, including Python MQTT clients

* **Quiz 1: Basic Knowledge and Basic Programming**

  * Paper-based (handwritten): IoT concepts, architectures, communication models, and Node-RED fundamentals
  * Programming: Basic Python coding, simple IoT data processing, and Node-RED flow development with dashboard UI

---

## **Week 6: IoT Data Storage, Processing, and Visualization**

* Overview of **database technologies** for IoT applications
* Comparison of **time-series** and **relational** databases
* IoT data ingestion, storage, and retrieval strategies
* **Python for database operations**:

  * Connecting to databases using Python (SQLAlchemy, database-specific libraries)
  * Inserting and querying IoT data with Python
  * Working with time-series and relational databases
* **Python for data processing and analysis**:

  * Using Python libraries (pandas, numpy) for IoT data processing
  * Real-time data processing with Python
  * Data transformation and aggregation techniques
* **Python for data visualization**:

  * Creating charts and graphs using Python visualization libraries (matplotlib, plotly)
  * Building custom dashboards with Python
* Introduction to **real-time data processing** concepts
* Designing effective **IoT dashboards** for monitoring applications
* **Hands-on:** Storing, processing, and visualizing IoT data from simulated devices using Python

---

## **Week 7: IoT Data Storage, Processing, and Visualization (Continued)**

* **Continued exploration of database technologies** for IoT applications
* **Advanced Python for database operations**:
  * Complex queries and data transformation
  * Managing high-frequency data ingestion
* **Real-time dashboard optimization**:
  * Improving UI response and data throughput
  * Finalizing system monitoring and debugging tools
* **Hands-on:** Refining the storage, processing, and visualization flows from Week 06

---

## **Week 8: Quiz 2 – IoT Data Storage, Processing, and Visualization**

* **Quiz 2: Frontend and Backend Programming**
  * Paper-based (handwritten): IoT architectures, MQTT communication, Node-RED integration, and database concepts
  * Programming: Integration of simulated devices with IoT backend systems and real-time data handling

---

## **Week 9: Embedded & IoT Programming using PSoC 6**

* **Sensor reading and data acquisition**:

  * Reading data from multiple sensors on **PSoC 6 MCU**
  * Analog and digital sensor interfacing
  * Sensor data sampling and filtering techniques
  * Timestamping and data validation
* **Sensor fusion**:

  * Combining data from multiple sensors
  * Sensor fusion algorithms and techniques
  * Data correlation and cross-validation
  * Improving accuracy and reliability through sensor fusion
* **JSON data formatting**:

  * Structuring sensor data in JSON format
  * JSON encoding and decoding on embedded devices
  * Efficient JSON payload design for IoT applications
  * Data serialization and deserialization
* **MQTT for real-time data exchange**:

  * Publishing sensor data as JSON messages over MQTT
  * MQTT topic design for sensor data streams
  * Quality of Service (QoS) levels for reliable data transmission
  * Real-time data streaming and message queuing
  * Subscribing to control commands via MQTT
* **Hands-on:** Implementing sensor reading, sensor fusion, JSON formatting, and real-time MQTT data exchange using hardware-based IoT devices

---

## **Week 10: Embedded & IoT Programming using PSoC 6 (Continued)**

* Introduction to **Digital Twin** concepts and applications in IoT systems
* Overview of **Digital Twin** as a virtual representation of physical devices
* **VS Code Digital Twin Extension**:

  * Installation and configuration of Digital Twin extension in VS Code
  * Working with digital twin models (robot arm, machines, and other devices)
  * Understanding digital twin interfaces and data structures
* **MCU firmware development for Digital Twin communication**:

  * Developing firmware on **PSoC 6 MCU** to interface with digital twin
  * Implementing communication protocols for digital twin data exchange
  * Sensor data acquisition and formatting for digital twin
  * Actuator control commands from digital twin
* **Bidirectional data exchange**:

  * Sending sensor data from MCU to digital twin
  * Receiving control commands from digital twin to MCU
  * Real-time synchronization between physical device and digital twin
  * Data mapping and protocol translation
* **Hands-on:** Developing MCU firmware and establishing data communication with digital twin models (robot arm, machines) using VS Code extension

---

## **Week 11: Embedded & IoT Programming using PSoC 6 (Continued)**

* **Reference:** [drsanti/bitstream-app](https://github.com/drsanti/bitstream-app) (repository) · [Getting started tutorial](https://github.com/drsanti/bitstream-app/blob/main/docs/Tutorial.md)
* **Bitstream CLI, firmware, and React frontend workspace**
* **Prerequisites: Git, Node.js, ModusToolbox**
* **Install Bitstream and prepare the workspace (ROOT layout)**
* **Initialize project, validate config, fetch libraries, build, and program the kit**
* **Hands-on:** Bitstream end-to-end setup through firmware flash

---

## **Week 12: Embedded & IoT Programming using PSoC 6 (Continued)**

* **Embedded MQTT broker (Bitstream)**
* **MCU simulator workflow (no hardware)**
* **Starting and stopping broker and simulator processes**
* **React dashboard: dependencies, dev server, live telemetry**
* **Hands-on:** Broker, publisher (board or simulator), and dashboard together

---

## **Week 13: Quiz 3 – Embedded & IoT Systems Integration**

* **Quiz 3: Embedded & IoT Systems Integration**
  * Paper-based (handwritten): Embedded system architecture, hardware integration, MQTT and connectivity, and UI application integration for IoT
  * Programming: End-to-end IoT application—embedded firmware, broker/data path, and UI—demonstrating system integration (Weeks 09–12 focus)

---

## **Course Progression Summary**

This course is structured into three progressive phases, each increasing in system complexity and integration depth.

### **Phase 1: Foundations and Simulation** (Weeks 1–4) ✅ (Done)

* **Learning Focus:** IoT fundamentals, communication models, and basic programming
* **Resources:** Week 3 workshops; Week 4 Python for Beginners chapters (Ch01–Ch13)
* **Assessment:** **Quiz 1** (Week 5) – 20%

### **Phase 2: Data Systems and Backend Integration** (Weeks 5–7) ✅ (Done)

* **Learning Focus:** Node-RED, MQTT, database operations, and Python data processing
* **Assessment:** **Quiz 2** (Week 8) – 25%

### **Phase 3: Embedded & IoT Programming using PSoC 6** (Weeks 9–12)

* **Learning Focus:** PSoC 6 embedded IoT—sensor reading and MQTT/JSON telemetry, firmware tooling and deployment (including Bitstream), broker and data-path integration, and UI application connectivity for end-to-end IoT systems
* **Assessment:** **Quiz 3** (Week 13) – 35%

**Continuous Assessment:** Assignments throughout the semester – 20%

---

**Last Updated:** 2026-04-21

---
