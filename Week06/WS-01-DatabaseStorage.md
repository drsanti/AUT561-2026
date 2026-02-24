# WS 01 – Workshop: Database Storage

## Objective
Store simulated sensor data from MQTT topics into a **SQLite** database using Python and **SQLAlchemy**.

## Prerequisites
*   MQTT Broker running in Docker (from Week 5).
*   Sensor Simulators running (from Week 5).
*   Python virtual environment activated.
*   **Git** (Recommended for managing your project files) – Download at [git-scm.com/install](https://git-scm.com/install/).

---

## Python environment

**Use a Python virtual environment** for all Python work in this workshop. This keeps dependencies (e.g. `sqlalchemy`, `paho-mqtt`) isolated.

**Windows (Command Prompt / PowerShell):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Windows (Git Bash / VS Code Bash):**
```bash
python -m venv .venv
source .venv/Scripts/activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

When active, your prompt shows `(.venv)`. Run all commands below from this environment.

> **Note for Windows Bash users:** If the command `python` is not found after activation, try using `python.exe` or the full path `./.venv/Scripts/python.exe`.

---

## Task 1.1: Install Dependencies

In your terminal, inside your activated virtual environment, install the database and MQTT libraries. Use the command that works on your machine:

```bash
# Option A: Standard
python -m pip install sqlalchemy paho-mqtt

# Option B: Windows Launcher (if python not found)
py -m pip install sqlalchemy paho-mqtt

# Option C: Direct Path (Most reliable in Bash)
./.venv/Scripts/python -m pip install sqlalchemy paho-mqtt
```

---

## Task 1.2: Create the Database Bridge

Create a file named `mqtt_logger.py`. This script will act as a subscriber that saves every message it receives into a SQLite file.

```python
import paho.mqtt.client as mqtt
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# 1. Database Setup
Base = declarative_base()

class SensorData(Base):
    __tablename__ = 'sensor_readings'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    topic = Column(String)
    value = Column(Float)

# Create SQLite database file
engine = create_engine('sqlite:///iot_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

# 2. MQTT Callbacks
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected to broker with result {rc}")
    client.subscribe("sensors/#")

def on_message(client, userdata, msg):
    try:
        # Convert payload to float
        val = float(msg.payload.decode())
        print(f"Logging {msg.topic}: {val}")
        
        # Save to database
        new_reading = SensorData(topic=msg.topic, value=val)
        db_session.add(new_reading)
        db_session.commit()
    except Exception as e:
        print(f"Error processing message: {e}")

# 3. Main Loop
# Use CallbackAPIVersion.VERSION2 for newer paho-mqtt
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
```

---

## Task 1.3: Run and Verify

1.  **Start your Broker:** Navigate to the `AUT561/Week06/docker` folder and run:
    ```bash
    docker-compose up -d
    ```
    *(See [Docker README](./docker/README.md) for details.)*
2.  **Start your Simulators:** Open two new terminals. In **each** one, you must navigate to your project folder and activate the virtual environment:
    ```bash
    # Step A: Navigate to project folder
    cd Week06/projects/iot-data-pipeline
    
    # Step B: Activate Environment (Windows Bash)
    source .venv/Scripts/activate
    
    # Step C: Run the script
    python sensor_temperature.py   # Or: py sensor_temperature.py
    ```
    *(Do the same for `sensor_humidity.py` in the second new terminal.)*

3.  **Run the Logger:** In another terminal, remember to **CD and activate** before running:
    ```bash
    cd Week06/projects/iot-data-pipeline
    source .venv/Scripts/activate
    python mqtt_logger.py
    ```
4.  **Check the Database:** After a minute, stop the script (Ctrl+C). You should see a file named `iot_data.db` in your folder.

### verify using Python:
Create a small script `check_db.py`:
```python
import sqlite3
conn = sqlite3.connect("iot_data.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM sensor_readings LIMIT 10")
for row in cursor.fetchall():
    print(row)
conn.close()
```
Run it: `python check_db.py`. You should see 10 rows of sensor data with timestamps.

---

## Summary
You have built a persistent storage layer for your IoT system. Data now survives even if the Python script or Node-RED is restarted.

**Next:** [WS 02 – Workshop: Data Analysis with Pandas](./WS-02-DataAnalysis.md)

**Last updated:** 2026-02-24
