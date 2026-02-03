# Week 5 – Simulated IoT Systems Using Node-RED and MQTT

This week introduces **Model 1: Simulated IoT Systems**. You will use **MQTT** (Message Queuing Telemetry Transport) to connect a broker, Python clients, sensor simulators, and Node-RED in one simulated system.

**Prerequisites:** Week 2 (Docker, Python), Week 3 (Python, Node-RED).

**How the four pieces fit together:**

* **MQTT Broker (Docker)** – Central message hub; all clients connect to it.
* **MQTT Client (Python)** – Programs that publish and/or subscribe to topics.
* **Sensor Simulators (Python MQTT client)** – Python scripts that publish simulated sensor data (e.g. temperature, humidity) to MQTT topics on a timer.
* **Node-RED as MQTT client** – Node-RED flows that subscribe to those topics and display data on the Dashboard.

---

## 1. MQTT Broker using Docker

### What is an MQTT broker?

An **MQTT broker** is a server that receives messages from **publishers** and delivers them to **subscribers** by **topic**. Clients do not talk to each other directly; they all connect to the broker.

### Why use Docker?

Running the broker in **Docker** gives you:

* **Portable setup** – Same broker image on any machine (Windows, macOS, Linux).
* **Isolated environment** – No conflict with other software; easy to start and stop.
* **Consistent with the course** – Week 2 already introduced Docker; you reuse that skill.

### Typical setup

* **Image:** Eclipse Mosquitto (or another MQTT broker image used in the course).
* **Port:** MQTT usually uses port **1883** (unencrypted) or 8883 (TLS).
* **Command:** Run the container with port 1883 exposed to the host (e.g. `docker run -p 1883:1883 ...`). Optionally use `docker compose` for a one-command start.

### Verifying the broker

* List running containers (e.g. `docker ps`) and confirm the broker container is up.
* Check that port 1883 is exposed and listening.
* In the workshop you will verify by connecting a Python client (Part 2).

---

## 2. MQTT Client using Python

### Role of a client

An **MQTT client** can **publish** messages to a topic, **subscribe** to one or more topics, or both. The broker routes messages from publishers to subscribers by topic name (e.g. `sensors/temperature`).

### Library: paho-mqtt

The standard Python library for MQTT is **paho-mqtt**. Install it inside a **Python virtual environment** (create and activate one first, e.g. `python -m venv .venv` then activate). Then run:

```text
pip install paho-mqtt
```

### Concepts you need

* **Connect** – Client connects to the broker (host, port, e.g. `localhost`, `1883`).
* **Topic** – String that identifies the message channel (e.g. `test/topic`, `sensors/temp`).
* **Publish** – Send a message to a topic; only subscribers to that topic receive it.
* **Subscribe** – Tell the broker you want messages for a given topic (or topic pattern).
* **Callbacks** – The library calls your function when a message arrives (e.g. `on_message`).
* **Loop** – `client.loop_start()` or `loop_forever()` keeps the client running and processing messages.

### Minimal usage pattern

* **Publisher:** Connect → publish one or more messages to a topic → disconnect (or keep running).
* **Subscriber:** Connect → subscribe to a topic → set a callback for incoming messages → start the loop so messages are delivered.

Code examples and full scripts are in the [Week 5 Workshop](./Week05-Workshops.md) (Part 2).

---

## 3. Sensor Simulators (Python MQTT client)

### What are sensor simulators?

**Sensor simulators** are Python programs that behave like sensors: they produce values (e.g. temperature, humidity) at a fixed interval and **publish** those values to MQTT topics. No real hardware is required; you use `random` and `time.sleep` (or similar) to generate and pace the data.

### Topic naming and message format

* **Topics:** Use clear, hierarchical names, e.g. `sensors/temperature`, `sensors/humidity`. Subscribers can subscribe to `sensors/#` to get all sensor topics if your broker supports wildcards.
* **Message format:** Keep it simple at first: send a single number (e.g. temperature as string or number). Later you can send **JSON** (e.g. `{"temp": 25.3, "humidity": 60}`) for multiple values in one message.

### Relation to the Python MQTT client

Sensor simulators **are** Python MQTT clients: they use the same **paho-mqtt** connect/publish pattern as in Section 2. The difference is **what** they do: instead of one-off publish or subscribe, they run a **loop** that periodically publishes simulated readings to specific topics. The workshop (Part 3) gives full small scripts.

---

## 4. Node-RED application as MQTT client

### Node-RED and MQTT

Node-RED can act as an **MQTT client**: it connects to the same broker as your Python clients and can **subscribe** to topics (and optionally **publish**). This lets you visualize sensor data from the Python simulators on the Node-RED Dashboard without writing more Python.

### Key nodes

* **mqtt in** – Subscribes to one or more MQTT topics. When a message arrives, it outputs `msg.payload` (and topic info) to the next node.
* **mqtt out** – Publishes a message to a topic (optional; useful if you want Node-RED to send commands or data back to MQTT).

You must **configure the MQTT broker** once (e.g. server `localhost`, port `1883`); then each **mqtt in** node selects that config and a topic name.

### From MQTT to Dashboard

* Wire **mqtt in** (subscribed to e.g. `sensors/temperature`) to a **dashboard** node (e.g. gauge, chart, or text). The payload will usually need to be a number; if you publish JSON, use a **function** node to parse it and set `msg.payload` to the value you want to show.
* **Deploy** the flow. While your Python sensor simulators (Part 3) are running and publishing, the Node-RED Dashboard will update with the latest values.

### Flow structure (conceptual)

* **Configuration node:** MQTT broker, localhost:1883.
* **mqtt in** nodes: one per topic (or one with a wildcard if supported), e.g. `sensors/temperature`, `sensors/humidity`.
* **Optional:** function nodes to convert payload (e.g. string to number, or JSON parse).
* **Dashboard nodes:** gauge, chart, text – wired to the mqtt in (or function) output.

The [Week 5 Workshop](./Week05-Workshops.md) (Part 4) walks through the exact steps.

---

**Next:** [Week 5 Workshop](./Week05-Workshops.md) – hands-on in four parts (broker, Python client, sensor simulators, Node-RED).

**Last updated:** 2026-02-03
