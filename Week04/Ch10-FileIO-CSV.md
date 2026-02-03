# Chapter 10: File I/O and CSV

## Objective
Read and write files, and work with CSV format for IoT data logging.

## Prerequisites
- Chapter 9 (Dictionaries)
- Understand working directory (Chapter 1)

---

## Concepts
- **Open a file:** `open("filename", "r")` for read, `"w"` for write
- **Context manager:** `with open(...) as f:` ensures the file is closed
- **CSV module:** `import csv` for reading and writing CSV files
- **Working directory** affects relative paths like `data/readings.csv`

---

## Example 1: Reading and Writing Text Files

**What it does:** Writes a simple log message to a file and reads it back—basics of file I/O for IoT logging.

**Code:** Save as `ch10_fileio.py`

```python
# ch10_fileio.py
# Write to file
with open("ch10_log.txt", "w") as f:
    f.write("=== IoT Device Log ===\n")
    f.write("Device: TempSensor-01\n")
    f.write("Status: ONLINE\n")

# Read from file
with open("ch10_log.txt", "r") as f:
    content = f.read()
    print(content)
```

**Explanation:**
- `"w"` overwrites the file; `"r"` reads it
- `with` ensures the file is closed even if an error occurs
- `f.read()` returns the entire file as a string

**How to run:**
```bash
python ch10_fileio.py
```

**Expected output:**
```
=== IoT Device Log ===
Device: TempSensor-01
Status: ONLINE
```

**Note:** `ch10_log.txt` is created in the current working directory.

---

## Example 2: CSV for Sensor Data Logging

**What it does:** Writes sensor readings to CSV and reads them back—typical IoT data logging pattern.

**Code:** Save as `ch10_csv.py`

```python
# ch10_csv.py
import csv
from datetime import datetime

# Write sensor readings to CSV
readings = [
    ["timestamp", "sensor", "value", "unit"],
    [datetime.now().isoformat(), "TempSensor-01", 25.5, "°C"],
    [datetime.now().isoformat(), "TempSensor-01", 26.1, "°C"],
    [datetime.now().isoformat(), "TempSensor-01", 24.8, "°C"],
]

with open("ch10_readings.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(readings)

# Read and process
with open("ch10_readings.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    values = [float(row[2]) for row in reader]

print("Header:", header)
print("Values:", values)
print("Average:", sum(values) / len(values) if values else 0)
```

**Explanation:**
- `csv.writer(f)` writes rows; `writer.writerows(list)` writes multiple rows
- `csv.reader(f)` reads rows as lists
- `next(reader)` skips the header row
- `newline=""` in `open` prevents extra blank lines in CSV on Windows

**How to run:**
```bash
python ch10_csv.py
```

**Expected output:**
```
Header: ['timestamp', 'sensor', 'value', 'unit']
Values: [25.5, 26.1, 24.8]
Average: 25.466666666666665
```

---

## Try It Yourself
1. Append a new reading to the CSV file instead of overwriting (use `"a"` mode).
2. Create a CSV with columns: name, min, max, unit. Read it and print each sensor's range.
3. Use a relative path like `data/readings.csv` and ensure the `data` folder exists.

---

## Key Takeaways
- Use `with open(...) as f` for safe file handling
- `"r"` read, `"w"` write, `"a"` append
- `csv.writer` and `csv.reader` handle CSV format
- Working directory affects relative paths

---

## Next
→ [Chapter 11: Classes](./Ch11-Classes.md)
