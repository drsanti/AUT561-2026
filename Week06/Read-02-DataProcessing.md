# Read 02 – Data Processing with Pandas

Storing data is only the first step. To make IoT systems "smart," we must process the raw data into useful information. In Python, the most powerful tool for this is **Pandas**.

## 1. What is Pandas?

**Pandas** is a fast, powerful, and flexible open-source data analysis and manipulation library. It is the industry standard for Python data science.

### Key Data Structures:
*   **Series:** A 1D array (like a single column in Excel).
*   **DataFrame:** A 2D table (like a whole spreadsheet). This is what we use most for IoT databases.

## 2. Reading Data into Pandas

Pandas can read directly from SQLite. This makes it easy to analyzed the data stored by your MQTT-to-Database bridge.

```python
import pandas as pd
import sqlite3

# Connect and read
conn = sqlite3.connect("iot_data.db")
df = pd.read_sql_query("SELECT * FROM sensor_data", conn)

# Close connection
conn.close()

# Preview data
print(df.head())
```

## 3. Cleaning and Transforming

Raw sensor data often needs work:
*   **Data Types:** Converting string timestamps into actual Python `datetime` objects.
*   **Missing Values:** Filling in gaps caused by network drops.
*   **Unit Conversion:** Converting Celsius to Fahrenheit, or raw ADC values to physical units (Voltage, Pressure).

Example: Converting timestamp column
```python
df['timestamp'] = pd.to_datetime(df['timestamp'])
```

## 4. Aggregation and Resampling

IoT devices generate *too much* data. A sensor might send a reading every second, but you only need to show the average temperature **per hour** on your dashboard. This is called **Resampling**.

```python
# Set timestamp as the index for time-series operations
df.set_index('timestamp', inplace=True)

# Resample to Hourly ('H') and calculate Mean
hourly_avg = df['value'].resample('H').mean()
```

### Common Aggragates:
*   `.mean()` – Average.
*   `.min()` / `.max()` – Extremes.
*   `.count()` – How many readings were received.
*   `.std()` – Standard deviation (useful for detecting noise or instability).

## 5. Why use Pandas instead of simple Python loops?

*   **Vectorization:** Pandas operations are written in C/C++, making them hundreds of times faster than `for` loops on large datasets.
*   **Built-in Logic:** Complex tasks like "find the rolling average of the last 10 samples" take only one line of code in Pandas.

---
**Next:** [Read 03 – IoT Data Visualization](./Read-03-Visualization.md)

**Last updated:** 2026-02-24
