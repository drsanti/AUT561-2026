# **Week 2 Self-Test Quiz**

**Topic: Software Tools and Development Environment for IoT Automation**

---

## **Questions**

### **1. Short Answer**

Why is it important to correctly set up and verify the software development environment *before* starting IoT and automation programming tasks?

---

### **2. Multiple Choice**

Which software tool is primarily used in this course as the **main code editor and development interface**?

A. Docker Desktop
B. Visual Studio Code
C. Node-RED
D. ModusToolbox

---

### **3. True or False**

A Python program can run correctly even if the `pip` package manager is not installed or working.

---

### **4. Short Answer**

What is the purpose of using a **Python virtual environment** (`venv`) in an automation or IoT project?

---

### **5. Multiple Choice**

Which command is used to verify that Python is correctly installed and accessible from the command line?

A. `pip list`
B. `python --version`
C. `node --version`
D. `docker info`

---

### **6. Short Answer**

What problem can occur if multiple projects use different Python package versions without virtual environments?

---

### **7. True or False**

Node-RED is mainly used in this course to replace Python programming for all automation tasks.

---

### **8. Multiple Choice**

Which Node-RED node is most commonly used to **manually trigger or simulate input data** during testing?

A. Debug
B. Function
C. Inject
D. Switch

---

### **9. Short Answer**

Why is Docker useful when developing or simulating IoT systems?

---

### **10. Scenario-Based Question**

A student installs Docker successfully, but the command `docker run hello-world` fails with a permission or connection error.

Give **one likely cause** and **one possible fix**.

---

## **Answers**

### **1.**

Correct setup ensures that tools work reliably together, prevents configuration-related errors, and allows students to focus on learning automation concepts instead of troubleshooting environment issues later in the course.

---

### **2.**

**B. Visual Studio Code**

---

### **3.**

**False**

Most modern Python workflows depend on `pip` to install required libraries. Without it, many scripts and projects cannot run correctly.

---

### **4.**

A virtual environment isolates project-specific Python packages and versions, preventing conflicts between different projects and ensuring consistent behavior across systems.

---

### **5.**

**B. `python --version`**

---

### **6.**

Package version conflicts can occur, causing programs to behave unpredictably or fail because required libraries may be missing, outdated, or incompatible.

---

### **7.**

**False**

Node-RED complements Python by providing flow-based logic and visualization; it does not replace Python programming.

---

### **8.**

**C. Inject**

---

### **9.**

Docker allows developers to run applications in isolated, reproducible environments, making it easier to simulate IoT systems, avoid dependency conflicts, and deploy consistent setups across different machines.

---

### **10.**

Example answer:
A likely cause is that Docker Desktop is not running or the user lacks permission to access Docker. A possible fix is to start Docker Desktop, ensure required services (such as WSL2 on Windows) are running, or restart the system.

---

### ✔ Self-Check Guidance for Students

* If you miss Questions **4, 6, or 10**, revisit the **Week 2 setup and troubleshooting steps**
* You should be able to explain *why* each tool is needed, not just name it
* A correct setup is essential for **Week 3 programming** and **Quiz 1**

---

**Last Updated:** 2026-01-12

---