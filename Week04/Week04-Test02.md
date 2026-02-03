# **Week 4 Practice Set**

**Python programming exercises for Quiz 1 preparation**

> Complete these exercises to reinforce concepts from the Week 4 Python chapters and Week 3 workshops.

---

## Practice Set A — Python Fundamentals (Ch01–Ch08)

### **P1 — Variables and Formatted Output**

Write `p1_sensor_display.py` that:

* Stores in variables: `sensor_name = "TempSensor-01"`, `value = 25.5`, `unit = "°C"`
* Prints: `Sensor: TempSensor-01`, `Reading: 25.5 °C`, and a single formatted line using f-string: `TempSensor-01 = 25.5 °C`

**Submit:** `p1_sensor_display.py` + terminal output

---

### **P2 — Conditionals and Threshold Logic**

Write `p2_threshold.py` with:

* Variables: `temperature = 62`, `threshold = 60`
* Use `if`/`else`: if temperature exceeds threshold, print `ALERT: Temperature exceeds 60°C`, else print `Temperature within normal range`
* Test with both 62 and 55

**Submit:** `p2_threshold.py`

---

### **P3 — Loop and Sensor Simulation**

Write `p3_sampling.py` that:

* Uses `for i in range(5)` and `random.uniform(20, 30)` to simulate 5 temperature readings
* Prints each as: `Sample 1: 24.56 °C`
* Prints the average at the end

**Submit:** `p3_sampling.py`

---

### **P4 — Functions (Range Check)**

Write `p4_range_check.py` with:

* A function `is_in_range(value, min_val, max_val)` that returns `True` or `False`
* Call it with `(50, 0, 100)` and `(150, 0, 100)` and print the results

**Submit:** `p4_range_check.py`

---

### **P5 — Lists and Statistics**

Write `p5_stats.py` that:

* Creates a list: `readings = [22.5, 23.1, 24.0, 22.8, 23.5]`
* Prints: count, min, max, average using `len()`, `min()`, `max()`, `sum()`

**Submit:** `p5_stats.py`

---

## Practice Set B — Data Structures and File I/O (Ch09–Ch10)

### **P6 — Dictionaries (Sensor Reading)**

Write `p6_reading.py` that:

* Creates a dict: `reading = {"name": "TempSensor-01", "value": 25.5, "unit": "°C"}`
* Prints each field using bracket notation
* Updates `reading["value"]` to 26.1 and prints the updated dict

**Submit:** `p6_reading.py`

---

### **P7 — CSV Writing (Data Logger)**

Write `p7_logger.py` that:

* Uses the `csv` module
* Writes 5 rows to `p7_readings.csv`: header `timestamp,sensor,value,unit` plus 5 data rows with simulated timestamps and values

**Submit:** `p7_logger.py` + generated `p7_readings.csv`

---

### **P8 — CSV Reading (Data Processing)**

Write `p8_process.py` that:

* Reads `p7_readings.csv` (or create sample data if P7 not done)
* Skips the header
* Extracts the `value` column, converts to float, and prints min, max, average

**Submit:** `p8_process.py`

---

## Practice Set C — Classes and Error Handling (Ch11–Ch13)

### **P9 — Simple Sensor Class**

Write `p9_sensor_class.py` with:

* A class `Sensor` with `__init__(self, name, unit)` and method `read(self)` that returns `{"value": 25.0 + random.uniform(-1, 1), "unit": self.unit}`
* Create an instance, call `read()`, and print the result

**Submit:** `p9_sensor_class.py`

---

### **P10 — Error Handling (Input Validation)**

Write `p10_parse.py` that:

* Defines `parse_temperature(text)` which returns `float(text)` or raises `ValueError` with a clear message if conversion fails
* Uses `try`/`except` to call it with `"25.5"` and `"invalid"`—print the parsed value for the first, and `"Invalid input"` for the second

**Submit:** `p10_parse.py`

---

## Practice Set D — Integration (Quiz 1 Style)

### **P11 — Complete Sensor Simulator**

Write `p11_simulator.py` that combines:

* A loop for 10 samples
* Random temperature (20–50 °C)
* Threshold check: if > 45 print ALARM, elif > 40 print WARNING, else print OK
* Store valid readings (20–50) in a list
* At the end, print: sample count, min, max, average of valid readings

**Submit:** `p11_simulator.py` + sample output

---

### **P12 — Filter and Process**

Write `p12_filter.py` that:

* Has a list: `readings = [22.1, 105.2, 24.5, -1.0, 25.0, 99.0]`
* Uses a list comprehension to keep only values in 0–100
* Prints the filtered list and the average of filtered values

**Submit:** `p12_filter.py`

---

## Self-Check

* P1–P5 cover variables, conditionals, loops, functions, lists (Ch02–Ch08)
* P6–P8 cover dictionaries and CSV (Ch09–Ch10)
* P9–P10 cover classes and error handling (Ch11, Ch13)
* P11–P12 integrate multiple concepts (Quiz 1 style)

If any exercise is difficult, review the corresponding chapter in [Week 4 Materials](./README.md). **Quiz 1 is held in Week 5**—see [Week 5 Quiz 1 materials](../Week05/Quiz-01/) for preparation checklist and scoring policy.

---

**Last Updated:** 2026-02-03
