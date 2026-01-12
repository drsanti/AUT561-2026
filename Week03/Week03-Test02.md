## Practice Set A — Python (Week 3 core)

### **P1 — Sensor Sampling Loop (random + sleep)**

Write `p1_sampling.py` that:

* Samples a simulated temperature sensor every **0.5 s** for **20 samples**
* Temperature range: **25.0–55.0 °C** using `random.uniform`
* Prints lines like: `t=05 temp=41.23`
* At the end prints: `min=... max=... avg=...`

**Submit:** `p1_sampling.py` + terminal output screenshot/text.

---

### **P2 — Alarm Logic with Function (PLC-style block)**

Write `p2_alarm.py` with:

* A function `classify_temp(temp)` returning `"NORMAL"`, `"WARNING"`, `"ALARM"` using thresholds:

  * `<= 40` → NORMAL
  * `> 40 and <= 48` → WARNING
  * `> 48` → ALARM
* Run for **30 samples**, every **0.2 s**
* Print: `temp=xx.xx state=STATE`

**Submit:** `p2_alarm.py`

---

### **P3 — Data Logger to CSV (file I/O)**

Write `p3_logger.py` that:

* Creates `data/temp_log.csv`
* Logs **timestamp,temp,state** for **50 samples**
* Uses `time.time()` (or ISO time) for timestamp
* Uses the same state classification as P2

**Submit:** `p3_logger.py` + generated `data/temp_log.csv`

---

### **P4 — CSV Processing (min/max/avg + alarm count)**

Write `p4_process.py` that reads `data/temp_log.csv` and prints:

* Sample count
* Min, max, average temperature
* Count of WARNING and ALARM samples

Example output format:

```
samples=50
min=...
max=...
avg=...
warning=...
alarm=...
```

**Submit:** `p4_process.py` + output

---

### **P5 — Anti-Chatter Control (Hysteresis)**

Implement a simple actuator control with hysteresis in `p5_hysteresis.py`:

Rules:

* Maintain a variable `fan_state` initially `"OFF"`
* If `temp >= 48` → set `"ON"`
* If `temp <= 40` → set `"OFF"`
* Otherwise keep previous state

Run for **40 samples** with random temps. Print:
`temp=xx.xx fan=ON/OFF`

**Submit:** `p5_hysteresis.py`

---

### **P6 — “REQ vs ACT” Simulation (Safety override)**

Write `p6_req_act.py` to model separation between:

* `req` (controller request)
* `act` (actual actuator state)

Rules:

* Controller request: `req="ON"` if `temp > 42` else `"OFF"`
* Safety rule: if sensor quality is `"BAD"`, force `act="OFF"` regardless of req
* Sensor quality is randomly `"GOOD"` 90% and `"BAD"` 10%

Print each cycle:
`temp=.. quality=GOOD req=ON act=ON`

**Submit:** `p6_req_act.py`

---

## Practice Set B — Node-RED (Week 3 realistic simulation)

> These are “build this flow” tasks. Export your flow JSON to submit.

### **N1 — Periodic Sensor + Delay**

Build a flow:
`Inject (repeat 1s) → Function (random temp) → Delay (0.5s) → Debug`

Requirements:

* Function outputs `msg.payload` = temperature (25–55, 2 decimals)
* Debug shows payload continuously

**Submit:** `n1_flow.json`

---

### **N2 — Switch-Based State Classifier**

Extend N1:

* Add a `Switch` node on `msg.payload`
* Route to 3 branches:

  * NORMAL (<=40)
  * WARNING (40–48]
  * ALARM (>48)
* Each branch sets `msg.state` accordingly (Change node or Function)
* Debug full message (see both payload and state)

**Submit:** `n2_flow.json`

---

### **N3 — Actuator + Minimum ON/OFF Time**

Build actuator simulation with anti-chatter:

* Use `msg.state` to request fan ON for WARNING/ALARM, OFF for NORMAL
* Implement **minimum off time**: once fan turns OFF, it cannot turn ON again for **2 seconds**

  * Hint: use `context` in a Function node (store last change time), or Delay + gating logic

**Submit:** `n3_flow.json` + short note explaining your logic (3–5 lines).

---

### **N4 — Alarm Event Logger**

When state is ALARM:

* Append a CSV line to a file: `timestamp,temp,state`
* Use `File` node in append mode
* Timestamp should be ISO string

**Submit:** `n4_flow.json` + `alarm_log.csv`

---

## Practice Set C — Mini “Programming Quiz” (mixed)

### **M1 — Build a Python “Sensor Publisher” Text Stream**

Write `m1_stream.py` that prints one JSON per line (like a simple data stream):

* `{"ts":..., "temp":..., "state":..., "fan":...}`
* Use hysteresis rules for fan (like P5)
* Run 30 lines, 0.2s delay

**Submit:** `m1_stream.py` + sample output (first 5 lines)

---

### **M2 — Node-RED “Parser + Dashboard-ready Message”**

In Node-RED, simulate receiving JSON text (use Inject with a JSON object), then:

* Ensure output contains: `msg.payload.temp`, `msg.payload.state`, `msg.payload.fan`
* Add a Debug node that shows the structured object
* (Optional) Add Dashboard widgets if available

**Submit:** `m2_flow.json`

---

**Last Updated:** 2026-01-12

---

