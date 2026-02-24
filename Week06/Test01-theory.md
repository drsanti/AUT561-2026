# Test 01 – Theory: IoT Data Storage & Analysis

**Topic:** AUT561 Week 06 (Databases for IoT, SQLite/SQLAlchemy, Pandas Data Processing, Visualization)

**Total: 15 marks** (each question shows mark allocation)

---

## Questions

### 1.
Besides persistence (data surviving a restart), state one reason why an IoT system needs a database instead of relying only on real-time MQTT messages. **(1 mark)**

---

### 2.
In the context of database types, explain the primary difference between **Relational (SQL)** and **Time-Series (TSDB)** data models. **(1 mark)**

---

### 3.
State one reason why **SQLite** is a popular choice for "Edge" devices or local IoT development compared to a database like MySQL or PostgreSQL. **(1 mark)**

---

### 4.
What is an **ORM (Object-Relational Mapper)** like SQLAlchemy? In one sentence, explain how it changes the way a Python programmer interacts with a database. **(2 marks)**

---

### 5.
In **Pandas**, what is the difference between a **Series** and a **DataFrame**? **(2 marks)**

---

### 6.
Consider the term **"Vectorization"** in Pandas. Why is it generally preferred to use Pandas built-in functions (like `.mean()`) instead of writing a Python `for` loop to calculate an average of 1 million records? **(1 mark)**

---

### 7.
What does the process of **"Resampling"** do to a high-frequency sensor data stream (e.g., data coming every 1 second)? **(1 mark)**

---

### 8.
List two key differences between **Matplotlib** and **Plotly** when used for IoT data visualization. **(2 marks)**

---

### 9.
True or False: In IoT dashboard design, you should always start your Y-axis at **zero**, regardless of the sensor's measurement range, to avoid misleading the user. **(1 mark)**

---

### 10.
In one sentence, why is **color meaning** (e.g., using Red, Green, or Blue) important in an IoT monitoring interface? **(1 mark)**

---

### 11.
If an IoT sensor is configured to send data once every **10 minutes**, explain why it might be a poor design choice to set the web dashboard to refresh its charts once every **1 second**. **(2 marks)**

---

**End of Test 01 – Total: 15 marks**
