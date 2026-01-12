# **Week 2 – Software Installation and Development Environment Setup (Step-by-Step + Checks)**

Week 2 is where we turn your laptop into a **professional IoT + automation development workstation**. This week directly supports the course workflow (simulation → embedded hardware → full-stack integration) and prepares you for hands-on work and programming-based quizzes.  

> 📋 **Lab Activities:** For the formal lab tasks and submission requirements, see **[Week02-Workshops.md](./Week02-Workshops.md)**

---

## 0) Before You Install Anything (10–15 minutes)

### Create a clean course workspace

1. Make a folder: `AUT561/`
2. Inside it, create:

   * `week02_setup/`
   * `projects/`
   * `notes/`

### Recommended system habits (save you hours later)

* **Use one browser** for local tools (Chrome/Edge recommended)
* **Restart after big installs** (Docker, ModusToolbox often need it)
* Keep a text file: `week02_setup/checklist.txt` to record what worked / what failed

---

## 1) Install Python + Verify `python` and `pip`

Python is used throughout the course for IoT scripts, MQTT clients, data processing, and database work. 

### Step A — Install Python

* Install Python 3.x (recommended: latest stable)
* During install (Windows): **check “Add Python to PATH”**

### Step B — Verify version

In terminal (VS Code terminal is fine):

**Windows**

```bash
python --version
pip --version
```

**macOS/Linux**

```bash
python3 --version
pip3 --version
```

**Expected result:** both commands print versions (no “command not found”).

### Step C — Create a virtual environment (best practice)

Inside `AUT561/week02_setup/`:

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step D — Install basic course packages (starter set)

```bash
pip install --upgrade pip
pip install requests paho-mqtt
```

### Step E — Quick test script

Create `python_check.py`:

```python
import sys
print("Python OK:", sys.version)

import paho.mqtt.client as mqtt
print("paho-mqtt OK:", mqtt.__version__)
```

Run:

```bash
python python_check.py
```

**Expected result:** prints Python version and paho-mqtt version.

---

## 2) Install Visual Studio Code (VS Code) + Essential Extensions

### Step A — Install VS Code

* Install VS Code for your OS (Windows/macOS/Linux)
* Launch it once after installation

### Step B — Add extensions (minimum set)

Open VS Code → Extensions (Ctrl+Shift+X) → install:

1. **Python** (by Microsoft)
2. **Pylance**
3. **Jupyter** (optional but helpful)
4. **Docker**
5. **YAML** (nice-to-have for configs)

### Step C — Quick checks

Open VS Code → Terminal (Ctrl+`) and run:

* **Check terminal works**

  * You should be able to type commands and see output.

* **Check Python extension is active**

  * Create a file: `hello.py`
  * Paste:

    ```python
    print("AUT561 setup: VS Code OK")
    ```
  * Run it (right-click → Run Python File)

**Expected result:** you see the printed message in the terminal.

---

## 3) Install Node-RED + Confirm You Can Open the Editor

Node-RED is used for flow-based IoT logic and dashboards later.  

### Option A (recommended for simplicity): Install Node-RED with Node.js

1. Install **Node.js (LTS)**
2. Then install Node-RED:

```bash
npm install -g --unsafe-perm node-red
```

### Start Node-RED

```bash
node-red
```

Open browser:

* `http://localhost:1880`

**Expected result:** Node-RED editor loads.

### Basic functional check

In Node-RED:

1. Drag **Inject** node
2. Drag **Debug** node
3. Connect Inject → Debug
4. Deploy
5. Click Inject button

**Expected result:** Debug sidebar shows a message (timestamp/payload).

---

## 4) Install Docker Desktop + Verify Containers Run

Docker is required for simulated IoT environments and repeatable setups.  

### Step A — Install Docker Desktop

* Install Docker Desktop
* Start Docker Desktop and wait until it shows **Running**

### Step B — Verify Docker CLI works

Open terminal:

```bash
docker --version
docker info
```

**Expected result:** versions and system information print (not errors).

### Step C — Run a test container

```bash
docker run hello-world
```

**Expected result:** Docker downloads and prints a “Hello from Docker!” message.

### Step D — (Optional) Run Node-RED in Docker (power move)

This is optional, but helps when you want clean environments:

```bash
docker run -it -p 1880:1880 --name nodered nodered/node-red
```

Open:

* `http://localhost:1880`

---

## 5) Install ModusToolbox + Confirm Embedded Workspace Works

ModusToolbox is used later for PSoC 6 embedded development.  

### Step A — Install ModusToolbox

* Install and launch ModusToolbox
* Let it complete any first-run setup

### Step B — Basic check (no hardware needed yet)

Your goal today is simply to confirm:

* ModusToolbox opens without crashing
* You can create/open a workspace
* Toolchain components appear installed

**Expected result:** You can create a workspace folder and reach the IDE view.

(We’ll do meaningful firmware projects when hardware work begins.)

---

## 6) Verification Checklist (What You Must Prove Works)

By the end of Week 2, every student should be able to show:

### Python

* `python --version` works
* `pip --version` works
* Virtual environment activates
* `paho-mqtt` imports correctly

### VS Code

* Opens
* Terminal works
* Python extension runs a script

### Node-RED

* Editor opens at `localhost:1880`
* Inject → Debug flow runs

### Docker

* `docker run hello-world` succeeds

### ModusToolbox

* Opens successfully
* Workspace can be created/opened

---

## 7) Troubleshooting (Common Problems + Fast Fixes)

### “python is not recognized…”

* Windows PATH issue: reinstall Python and check **Add to PATH**
* Try:

  * `py --version`
  * `py -m pip --version`

### VS Code runs Python but wrong interpreter

* In VS Code: Ctrl+Shift+P → **Python: Select Interpreter**
* Choose the `.venv` interpreter inside your course folder

### Node-RED command not found

* Node.js not installed or npm not in PATH
* Verify:

  ```bash
  node --version
  npm --version
  ```

### Docker installed but `docker run` fails

* Docker Desktop not running
* WSL2 missing (Windows)
* Virtualization disabled in BIOS (common on lab PCs)

### Port 1880 already in use

* Another Node-RED is running
* Stop it (Ctrl+C in the terminal running Node-RED)
* Or run with a different port

---

## 8) Complete the Week 2 Workshops

> 📝 **Next Step:** Complete all tasks in **[Week02-Workshops.md](./Week02-Workshops.md)** to verify your development environment is properly set up.

The workshops will guide you through verifying that all installed tools are working correctly. This ensures your environment is ready for Week 3 programming + Node-RED foundations. 

---

**Last Updated:** 2026-01-12

---
