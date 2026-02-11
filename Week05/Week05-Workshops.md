# AUT561 – Week 5 Workshop: Simulated IoT with MQTT and Node-RED

## Workshop objectives

By completing this workshop, you will be able to:

* Run an **MQTT broker** in Docker
* Use **Python (paho-mqtt)** to publish and subscribe to MQTT topics
* Build **sensor simulators** in Python that publish to MQTT
* Use **Node-RED** as an MQTT client to subscribe and display data on the Dashboard

**Order:** Part 1 → Part 2 → Part 3 → Part 4 (broker first, then client, then simulators, then Node-RED).

---

## Required tools

* Docker Desktop (from Week 2)
* Python 3.x and pip
* Node-RED and Dashboard (from Week 2/3)
* VS Code (or any editor) and terminal

---

## Python environment (Parts 2 and 3)

**Use a Python virtual environment** for all Python work in this workshop (Parts 2 and 3). This keeps dependencies (e.g. `paho-mqtt`) isolated and avoids conflicts with other projects.

**Create and activate a virtual environment** before Part 2:

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

When active, your prompt shows `(.venv)`. Run all Python commands and scripts (**Part 2 and Part 3**) from this environment. Install `paho-mqtt` inside it (Task 2.1).

---

# Part 1 – MQTT Broker using Docker

## Objective

Run an MQTT broker (Eclipse Mosquitto) in Docker so that Python and Node-RED clients can connect to it in later parts.

## Prerequisites

* Docker Desktop installed and running (Week 2)
* Terminal access

## Steps

### Task 1.1: Pull and run the Mosquitto broker

**Pull the image (optional; `docker run` will pull if missing):**

```bash
docker pull eclipse-mosquitto:latest
```

**Run the broker with port 1883 exposed:**

```bash
docker run -d --name mosquitto -p 1883:1883 eclipse-mosquitto:latest
```

* `-d` runs the container in the background
* `--name mosquitto` gives the container a name
* `-p 1883:1883` maps host port 1883 to container port 1883 (MQTT default)

### Task 1.2: Check that the broker is running

```bash
docker ps
```

You should see a container named `mosquitto` with port `0.0.0.0:1883->1883/tcp`.

## Verify

* `docker ps` shows the `mosquitto` container running.
* In Part 2 you will confirm the broker by connecting a Python client; if the client connects and receives or sends messages, the broker is working.

---

# Part 2 – MQTT Client using Python

## Objective

Use Python and the **paho-mqtt** library to publish and subscribe to the broker from Part 1.

## Prerequisites

* Python 3.x and pip
* MQTT broker running (Part 1)
* **Python virtual environment** – Create and activate one (see [Python environment](#python-environment-parts-2-and-3) above) before installing paho-mqtt

## Steps

### Task 2.1: Install paho-mqtt

**Make sure your virtual environment is activated** (you should see `(.venv)` in your prompt). Then run:

```bash
pip install paho-mqtt
```

### Task 2.2: Create a subscriber script

Create a file `subscribe.py` in a folder (e.g. `week05_mqtt/`):

```python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
```

### Task 2.3: Create a publisher script

Create `publish.py` in the same folder:

```python
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.publish("test/topic", "Hello from Python")
client.disconnect()
```

### Task 2.4: Run subscriber and publisher

1. In one terminal, run the subscriber: `python subscribe.py`. Leave it running.
2. In another terminal, run the publisher: `python publish.py`.
3. The subscriber terminal should print: `test/topic: Hello from Python`.

## Verify

* Subscriber stays connected and prints messages when the publisher runs.
* You can run `publish.py` multiple times; each message appears in the subscriber window.

---

# Part 3 – Sensor Simulators (Python MQTT client)

## Objective

Implement Python scripts that act as sensor simulators: they publish simulated values (e.g. temperature, humidity) to MQTT topics at a fixed interval.

## Prerequisites

* Part 1 (broker) and Part 2 (Python client) completed
* **Same Python virtual environment** as Part 2 (activated), with `paho-mqtt` already installed

## Steps

### Task 3.1: Create a temperature simulator

Create `sensor_temperature.py`:

```python
import random
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.loop_start()

try:
    while True:
        temp = round(random.uniform(20.0, 35.0), 1)
        client.publish("sensors/temperature", str(temp))
        print(f"Published temperature: {temp}")
        time.sleep(2)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
```

* Publishes to topic `sensors/temperature` every 2 seconds with a random value between 20 and 35.

### Task 3.2: Create a humidity simulator (optional)

Create `sensor_humidity.py`:

```python
import random
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.loop_start()

try:
    while True:
        humidity = random.randint(40, 80)
        client.publish("sensors/humidity", str(humidity))
        print(f"Published humidity: {humidity}")
        time.sleep(3)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
```

* Publishes to topic `sensors/humidity` every 3 seconds.

### Task 3.3: Verify with the Part 2 subscriber

Modify `subscribe.py` to subscribe to `sensors/#` (if your broker supports `#` wildcard) or to `sensors/temperature` and `sensors/humidity`. Run the subscriber, then run `sensor_temperature.py` (and optionally `sensor_humidity.py`). You should see values printed in the subscriber terminal.

## Verify

* Running `sensor_temperature.py` causes temperature values to appear in a subscriber (or in Node-RED in Part 4).
* Topic names: `sensors/temperature`, `sensors/humidity`. Message format: plain number as string.

---

# Part 4 – Node-RED application as MQTT client

## Objective

Use Node-RED to subscribe to the MQTT topics from Part 3 and display the data on the Node-RED Dashboard.

## Prerequisites

* Node-RED and Dashboard installed (Week 2/3)
* MQTT broker running (Part 1)
* Sensor simulators from Part 3 (optional but recommended: run them to see live data)

## Steps

### Task 4.1: Add MQTT broker configuration

1. Open Node-RED in the browser.
2. Drag an **mqtt in** node onto the canvas.
3. Double-click it; next to **Server**, click the pencil icon to add a new broker.
4. Set **Server** to `localhost` (or `127.0.0.1`) and **Port** to `1883`. Click **Add**, then **Done**.

### Task 4.2: Subscribe to sensor topics

1. In the **mqtt in** node, set **Topic** to `sensors/temperature` (or `sensors/#` to get all sensor topics).
2. Add a **dashboard gauge** (or **dashboard chart**, **dashboard text**) node. Install the **node-red-dashboard** palette if you have not already (Week 2/3).
3. Wire the **mqtt in** output to the **dashboard** node input.
4. The payload from MQTT is often a string; if the gauge expects a number, add a **function** node between mqtt in and gauge:

   ```javascript
   msg.payload = Number(msg.payload);
   return msg;
   ```

5. Deploy the flow (red **Deploy** button).

### Task 4.3: Open the Dashboard

1. Open the Dashboard tab (usually http://localhost:1880/ui).
2. You should see the gauge (or chart/text) for the topic you subscribed to.
3. Run `sensor_temperature.py` (and optionally `sensor_humidity.py`) from Part 3; the Dashboard should update with the published values.

### Task 4.4: Add more topics (optional)

* Add another **mqtt in** node for `sensors/humidity`, wire it to a second gauge or chart, and deploy. Run `sensor_humidity.py` to see humidity on the Dashboard.

## Verify

* With sensor simulators running, the Node-RED Dashboard shows updating temperature (and optionally humidity) values.
* End-to-end: Broker (Docker) → Python simulators (publish) → Node-RED (subscribe) → Dashboard (display).

---

## Summary

| Part | Topic                         | Outcome                                      |
|------|-------------------------------|----------------------------------------------|
| 1    | MQTT Broker using Docker      | Mosquitto running on port 1883               |
| 2    | MQTT Client using Python      | Python can publish and subscribe via paho-mqtt |
| 3    | Sensor Simulators (Python)   | Python scripts publish to `sensors/*` on a timer |
| 4    | Node-RED as MQTT client      | Node-RED subscribes and displays data on Dashboard |

**Next:** Week 6 – IoT Data Storage, Processing, and Visualization.

**Last updated:** 2026-02-03
