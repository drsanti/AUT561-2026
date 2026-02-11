# **AUT561 – Week 2 Lab**

## **Software Tool Setup and Verification**

### **Lab Title**

**Setting Up the IoT & Automation Development Environment**

### **Week**

Week 2 – Software Installation and Development Environment Setup

---

## **Lab Objectives**

By completing this lab, students will be able to:

* Set up a professional **IoT and automation development environment**
* Verify correct installation of **Python, VS Code, Node-RED, Docker, and ModusToolbox**
* Demonstrate readiness for **programming, simulation, and embedded development**
* Identify and resolve common setup issues early in the course

This lab ensures your system is ready for **Week 3 programming**, **Node-RED flows**, and **later embedded + PLC-style integration work**.

---

## **Required Software Tools**

Each student must successfully install and verify:

* Visual Studio Code (VS Code)
* Python 3.x + pip
* Node-RED
* Docker Desktop
* ModusToolbox (no hardware required this week)

---

## **Part A – Node-RED Setup**

### **Task A1: Node-RED Launch**

Start Node-RED and open:

```
http://localhost:1880
```

☐ Node-RED editor opens
☐ Editor does not open

---

### **Task A2: Flow Test**

Create the following flow:

* Inject node → Debug node
* Deploy
* Click Inject

☐ Debug output appears
☐ No output / error

---

## **Part B – VS Code and Python Setup**

### **Task B1: VS Code Verification**

* VS Code opens normally
* Integrated terminal works
* Python extension is installed

**Check**

* Create and run a Python file:

```python
print("VS Code + Python OK")
```

☐ Passed
☐ Not yet working

---

### **Task B2: Python Environment Verification**

Run the following commands in the terminal:

```bash
python --version
pip --version
```

☐ Python version displayed
☐ pip version displayed

Create and activate a virtual environment, then install:

```bash
pip install paho-mqtt
```

Run a test script that imports `paho.mqtt.client`.

☐ Import successful
☐ Errors encountered

---

## **Part C – Docker Setup**

### **Task C1: Docker Verification**

Run:

```bash
docker --version
docker run hello-world
```

☐ Docker version displayed
☐ Hello-world container runs successfully

---

## **Part D – ModusToolbox Setup**

### **Task D1: ModusToolbox Check**

* ModusToolbox opens successfully
* Workspace can be created or opened

☐ Tool opens without errors
☐ Workspace accessible

*(No coding or hardware required this week)*

---

## **Verification Checklist**

By completing this lab, you should verify that all tools are working correctly:

| Item             | Requirement                 |
| ---------------- | --------------------------- |
| VS Code + Python | Working and verified        |
| Node-RED         | Editor opens, flow runs     |
| Docker           | Container runs successfully |
| ModusToolbox     | Opens and workspace works   |

⚠️ **Incomplete setups will cause problems in Week 3 and Quiz 1**

---

## **Important Notes**

* This lab is **foundational**. Do not skip steps.
* Ask questions **now**, not during Quiz 1.
* A working setup is considered part of your **professional engineering responsibility**.

---

## **Next Week Preview**

**Week 3:**
Python programming foundations + Node-RED flow development
(You will use **everything installed this week**)

---

**Last Updated:** 2026-01-12

---
