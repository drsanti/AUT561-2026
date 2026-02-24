# Week 06 – IoT Data Storage, Processing, and Visualization

This week focuses on the **Backend and Analytics** layer of IoT systems. You will learn how to move from real-time message passing (Week 5) to persistent data storage, analysis, and dashboard visualization.

## Learning Objectives
By the end of this week, you will be able to:
*   Identify the roles of SQL, NoSQL, and Time-Series databases in IoT.
*   Setup a **SQLite** database and log MQTT data using Python (**SQLAlchemy**).
*   Perform data cleaning and resampling using **Pandas**.
*   Create interactive IoT dashboards with **Plotly**.

## 🛠️ Preparation
*   Ensure **Docker Desktop** is running.
*   Verify your **Python** environment.
*   Install **Git** for version control: [git-scm.com/install](https://git-scm.com/install/).
*   Install **Python Libraries** (inside your virtual environment):
    ```bash
    # Use 'py' or 'python' depending on your machine
    python -m pip install sqlalchemy paho-mqtt pandas plotly
    ```

## 📖 Reading Materials
1.  [Read 01 – Database Technologies for IoT](./Read-01-Databases.md)
2.  [Read 02 – Data Processing with Pandas](./Read-02-DataProcessing.md)
3.  [Read 03 – IoT Data Visualization](./Read-03-Visualization.md)

## 🛠️ Workshops
1.  [WS 01 – Database Storage (MQTT to SQLite)](./WS-01-DatabaseStorage.md)
2.  [WS 02 – Data Analysis with Pandas](./WS-02-DataAnalysis.md)
3.  [WS 03 – Visualization with Plotly](./WS-03-Visualization.md)

## 📝 Assessments
*   [Test 01 – Theory (Week 06)](./Test01-theory.md)
*   [Test 02 – Coding (Week 06)](./Test02-coding.md)

## 📁 Repository Structure
```text
Week06/
├── docker/                   # Docker Compose setup for MQTT
├── projects/
│   ├── Architecture.md       # System Architecture & Diagrams
│   └── iot-data-pipeline/    # Python Backend & Analytics Pipeline
├── Read-01-Databases.md      # Database concepts
├── Read-02-DataProcessing.md # Pandas fundamentals
├── Read-03-Visualization.md  # Visualization principles
├── WS-01-DatabaseStorage.md  # SQLite + SQLAlchemy + MQTT
├── WS-02-DataAnalysis.md     # Querying & Aggregation
├── WS-03-Visualization.md    # Plotly dashboards
├── Test01-theory.md          # Theory assessment
├── Test02-coding.md          # Coding assessment
└── README.md                 # This file
```

---
**Last updated:** 2026-02-24
