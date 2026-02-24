# Read 01 – Database Technologies for IoT

In an IoT system, a **database** is where you store sensor data, device status, and metadata for long-term records. This chapter explains why we need databases and the difference between **Relational (SQL)** and **Time-Series** data storage.

## 1. Why use a database for IoT?

In Week 5, we saw data moving in real-time via MQTT. However:
*   **Volatile data:** If the subscriber (Node-RED) is offline, messages are lost (unless using persistent MQTT sessions).
*   **No history:** You can see *current* temperature, but not *yesterday's* average.
*   **Scalability:** Databases allow you to query millions of records efficiently.

## 2. SQL vs. NoSQL vs. Time-Series

### Relational Databases (SQL)
*   **Examples:** SQLite, PostgreSQL, MySQL.
*   **Schema:** Fixed tables with rows and columns.
*   **Good for:** Metadata (device owner names, location, settings) and structured sensor data.
*   **Strength:** ACID compliance (reliability) and structured relationship modeling.

### NoSQL / Document Databases
*   **Examples:** MongoDB, CouchDB.
*   **Schema:** Flexible JSON-like documents.
*   **Good for:** Varying data structures from different types of devices.

### Time-Series Databases (TSDB)
*   **Examples:** InfluxDB, Prometheus, TimescaleDB.
*   **Model:** Optimized for sequences of "timestamp + value".
*   **Good for:** High-frequency sensor streams.
*   **Strength:** Fast ingestion and efficient storage of timestamp-indexed data.

## 3. SQLite: The Lightweight Choice

For this course, we use **SQLite**.
*   **Serverless:** The entire database is just one file on your disk. No server installation needed.
*   **Zero Configuration:** Perfect for local development and edge devices (like a Raspberry Pi or PSoC 6 with SD card).
*   **Compatibility:** Supported natively by Python and many other languages.

### IoT Schema Design in SQLite
A typical table for IoT sensor data:
```sql
CREATE TABLE sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    topic TEXT NOT NULL,
    value REAL NOT NULL
);
```

## 4. SQLAlchemy: The Python Bridge

Instead of writing raw SQL strings inside Python, we use an **ORM (Object Relational Mapper)** like **SQLAlchemy**.

*   **Abstraction:** Treat database tables as Python classes.
*   **Safety:** Prevents common bugs like SQL Injection.
*   **Portability:** Use the same code for SQLite, PostgreSQL, or MySQL by just changing the connection string.

In the workshop, you will use SQLAlchemy to automatically save MQTT messages into a SQLite file.

---
**Next:** [Read 02 – Data Processing with Pandas](./Read-02-DataProcessing.md)

**Last updated:** 2026-02-24
