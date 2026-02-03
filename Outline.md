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

## **Week 7: Hardware-Based IoT Systems and Embedded Devices**

* Introduction to **Model 2: Hardware-Based IoT Systems** and transition from simulation to physical devices
* Overview of **PSoC 6 MCU** architecture and fundamental **embedded system concepts**
* Embedded firmware architecture, development workflow, and build process
* Using **ModusToolbox** for firmware configuration, coding, and debugging
* **Sensor and actuator interfacing** principles, including digital and analog I/O
* Basic techniques for **testing and debugging embedded IoT devices**
* **Hands-on:** Setting up PSoC 6 hardware and developing basic embedded firmware for sensor interaction

---

## **Week 8: Quiz 2 – Hardware Integration and IoT Applications**

* **Quiz 2: Frontend and Backend Programming**

  * Paper-based (handwritten): IoT architectures, MQTT communication, Node-RED integration, and embedded system concepts
  * Programming: Integration of hardware devices with IoT systems and real-time data handling

---

## **Week 9: Sensor Reading, Sensor Fusion, and Real-Time Data Exchange via MQTT**

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

## **Week 10: IoT Devices to Digital Twin Integration**

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

## **Week 11: Backend Data Processing and Integration with Node-RED and Python**

* **Processing sensor fusion data streams**:

  * Receiving and parsing JSON sensor data from MQTT in Python
  * Processing fused sensor data streams in real-time
  * Data validation and error handling for sensor fusion outputs
  * Storing processed sensor data in databases
* **Node-RED integration for data flow**:

  * Subscribing to MQTT topics for sensor data streams
  * Processing JSON messages in Node-RED flows
  * Integrating sensor fusion data with Node-RED dashboard
  * Creating data pipelines from MQTT to visualization
* **Python backend services**:

  * Building Python services to process MQTT sensor data
  * Real-time data aggregation and analysis
  * Integrating Python services with Node-RED via HTTP/MQTT
  * Data transformation and enrichment pipelines
* **Digital Twin data processing**:

  * Processing data streams from digital twin models
  * Correlating physical sensor data with digital twin state
  * Synchronizing data between MCU and digital twin
  * Handling bidirectional data flows
* **Hands-on:** Building backend services in Python and Node-RED to process sensor fusion data and digital twin streams from MQTT

---

## **Week 12: AI/ML Integration with Sensor Fusion and Digital Twin**

* **AI/ML for sensor fusion data**:

  * Applying machine learning models to fused sensor data
  * Pattern recognition and anomaly detection in sensor streams
  * Predictive analytics using historical sensor fusion data
  * Real-time classification and decision-making
* **Python for AI/ML in IoT**:

  * Using Python ML libraries (scikit-learn, TensorFlow Lite) for edge analytics
  * Training models on sensor fusion datasets
  * Deploying lightweight ML models for real-time inference
  * Model integration with MQTT data streams
* **Digital Twin with AI/ML**:

  * Using digital twin data for predictive maintenance
  * AI-driven simulation and optimization in digital twin
  * Machine learning models for digital twin state prediction
  * Intelligent control algorithms based on digital twin analytics
* **Intelligent decision-making**:

  * Automated responses based on sensor fusion analysis
  * AI-driven control commands to MCU via MQTT
  * Feedback loops between physical sensors and digital twin
  * Edge computing versus cloud-based ML processing
* **Hands-on:** Implementing AI/ML models in Python to analyze sensor fusion data and digital twin streams, with intelligent decision-making and control

---

## **Week 13: Complete IoT System Integration: MCU Sensors to Digital Twin to User Interface**

* **End-to-end system architecture**:

  * Complete data flow: **PSoC 6 MCU sensors** → **Sensor fusion** → **JSON/MQTT** → **Python backend** → **Node-RED** → **Digital Twin** → **User interfaces**
  * System integration architecture and design patterns
  * Data flow synchronization across all system components
* **Full-stack integration**:

  * Integrating MCU firmware with MQTT broker
  * Connecting Python backend services with Node-RED flows
  * Synchronizing digital twin with physical device state
  * Building user interfaces (web/mobile) for monitoring and control
* **System testing and validation**:

  * Testing sensor fusion accuracy and reliability
  * Validating MQTT data transmission and reception
  * Testing digital twin synchronization with physical device
  * Performance evaluation and optimization
* **Security and reliability**:

  * Security fundamentals for IoT systems
  * Secure MQTT communication (authentication, encryption)
  * Data privacy and protection in sensor fusion systems
  * Error handling and system resilience
* **Hands-on:** Developing and integrating a complete IoT system from MCU sensors through sensor fusion, MQTT, Python backend, Node-RED, digital twin, to user interfaces with full bidirectional control

---

## **Week 14: Quiz 3 – Control and Monitoring IoT Applications**

* **Quiz 3: Control and Monitoring Application Development**

  * Paper-based (handwritten): System architecture, integration strategies, and intelligent IoT concepts
  * Programming: Complete IoT application development and system integration

---

## **Course Progression Summary**

This course is structured into three progressive phases, each increasing in system complexity and integration depth.

### **Phase 1: Foundations and Simulation** (Weeks 1–4)

* **Learning Focus:** IoT fundamentals, communication models, and basic programming
* **Resources:** Week 3 workshops; Week 4 Python for Beginners chapters (Ch01–Ch13)
* **Assessment:** **Quiz 1** (Week 5) – 20%

### **Phase 2: Hardware-Based IoT Systems** (Weeks 5–7)

* **Learning Focus:** Node-RED, MQTT, data handling, and embedded device integration
* **Assessment:** **Quiz 2** (Week 8) – 25%

### **Phase 3: Full-Stack and Intelligent IoT Applications** (Weeks 9–13)

* **Learning Focus:** Full-stack development, mobile applications, AI integration, and system-level design
* **Assessment:** **Quiz 3** (Week 14) – 35%

**Continuous Assessment:** Assignments throughout the semester – 20%

---

**Last Updated:** 2026-02-03

---
