# WS 02 – Workshop: Data Analysis with Pandas

## Objective
Use the **Pandas** library to query your IoT database, clean the data, and calculate meaningful statistics (averages, min/max).

## Prerequisites
*   `iot_data.db` file from WS 01 (ensure it has at least 50-100 records).
*   Python virtual environment activated.

---

## Python environment

**Remember to be in your project folder and have your environment active.** If you are starting a new terminal:

```bash
cd Week06/projects/iot-data-pipeline
source .venv/Scripts/activate  # Windows Bash
```

---

## Task 2.1: Install Pandas

In your terminal, inside your activated virtual environment, install the data analysis library. Use the command that works on your machine:

```bash
# Option A: Standard
python -m pip install pandas

# Option B: Windows Launcher
py -m pip install pandas

# Option C: Direct Path
./.venv/Scripts/python -m pip install pandas
```

---

## Task 2.2: Basic SQLite Query with Pandas

Create a script `analyze_iot.py`. This script will load everything into a DataFrame.

```python
import pandas as pd
import sqlite3

# 1. Connect to database
conn = sqlite3.connect("iot_data.db")

# 2. Read table into a DataFrame
df = pd.read_sql_query("SELECT * FROM sensor_readings", conn)
conn.close()

# 3. Basic Inspection
print("--- Data Info ---")
print(df.info())
print("\n--- First 5 rows ---")
print(df.head())
```

---

## Task 2.3: Cleaning and Converting

Timestamps from SQLite often come in as strings. We need to convert them to "DateTime" objects for time-series analysis.

Add this to `analyze_iot.py`:

```python
# Convert timestamp column
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Filter only temperature data
temp_df = df[df['topic'] == 'sensors/temperature']

print("\n--- Temperature Statistics ---")
print(temp_df['value'].describe())
```

---

## Task 2.4: Time-Series Resampling

The sensor simulates data every few seconds. Let's calculate the average temperature per minute.

Add this to `analyze_iot.py`:

```python
# Set timestamp as index (required for resampling)
temp_df.set_index('timestamp', inplace=True)

# Resample to 1-minute intervals ('1min') and calculate mean
minute_stats = temp_df['value'].resample('1min').agg(['mean', 'min', 'max'])

print("\n--- Minute-by-Minute Averages ---")
print(minute_stats.head(10))
```

---

## Task 2.5: Exporting Results

You might want to share your findings with someone who doesn't use Python. Pandas makes exporting to CSV easy.

Add this to `analyze_iot.py`:
```python
minute_stats.to_csv("sensor_summary.csv")
print("\nExported results to sensor_summary.csv")
```

---

## Summary
You have learned how to:
1.  Load SQLite data into Pandas.
2.  Filter data by topic.
3.  Resample high-frequency data into low-frequency summaries (aggregation).
4.  Export processed data.

**Next:** [WS 03 – Workshop: Visualization with Plotly](./WS-03-Visualization.md)

**Last updated:** 2026-02-24
