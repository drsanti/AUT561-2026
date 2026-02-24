# WS 03 – Workshop: Visualization with Plotly

## Objective
Create interactive charts from your IoT sensor data using **Plotly Express**.

## Prerequisites
*   `iot_data.db` file from WS 01.
*   Python virtual environment activated.

---

## Python environment

**Remember to be in your project folder and have your environment active.** If you are starting a new terminal:

```bash
cd Week06/projects/iot-data-pipeline
source .venv/Scripts/activate  # Windows Bash
```

---

## Task 3.1: Install Plotly

In your terminal, inside your activated virtual environment, install the visualization library. Use the command that works on your machine:

```bash
# Option A: Standard
python -m pip install plotly

# Option B: Windows Launcher
py -m pip install plotly

# Option C: Direct Path
./.venv/Scripts/python -m pip install plotly
```

---

## Task 3.2: Create a Line Chart

Create a script `visualize_iot.py`. This script will generate an HTML file with an interactive chart.

```python
import pandas as pd
import sqlite3
import plotly.express as px

# 1. Load Data
conn = sqlite3.connect("iot_data.db")
df = pd.read_sql_query("SELECT * FROM sensor_readings", conn)
conn.close()

# 2. Preparation
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 3. Create Line Chart
# We use 'color' to separate lines by topic (temp vs humidity)
fig = px.line(df, x="timestamp", y="value", color="topic",
              title="IoT Sensor Readings Over Time",
              labels={"timestamp": "Time", "value": "Reading", "topic": "Sensor Type"})

# 4. Save and Show
fig.write_html("iot_chart.html")
print("Chart saved to iot_chart.html. Open this file in your browser!")
fig.show()
```

---

## Task 3.3: Create a Distribution Histogram

Let's see how often the temperature hits certain ranges.

Add this code to `visualize_iot.py`:

```python
# Filter for temperature only
temp_only = df[df['topic'] == 'sensors/temperature']

# Create Histogram
fig_hist = px.histogram(temp_only, x="value", 
                         title="Temperature Distribution",
                         nbins=20)

fig_hist.write_html("temp_histogram.html")
print("Histogram saved to temp_histogram.html.")
fig_hist.show()
```

---

## Task 3.4: Challenge – Compare Averages

Let's combine what you learned in WS 02 and WS 03. Your goal is to create a chart that shows the **Average**, **Minimum**, and **Maximum** temperature per minute on the same graph.

### Steps:
1.  Create a new file `visualize_challenge.py`.
2.  Follow the logic from **WS 02** to load the data, filter for temperature, and resample it into 1-minute averages (`.agg(['mean', 'min', 'max'])`).
3.  Use `px.line()` to plot the resulting DataFrame.

### Code Hint:
```python
# ... (load and resample data like in WS 02) ...
minute_stats = temp_df['value'].resample('1min').agg(['mean', 'min', 'max']).reset_index()

# Plotting multiple columns
fig = px.line(minute_stats, x='timestamp', y=['mean', 'min', 'max'],
              title='Temperature Analysis: Mean, Min, and Max per Minute',
              labels={'value': 'Temperature (°C)', 'timestamp': 'Time'})

fig.show()
```

*Note: We use `.reset_index()` so the 'timestamp' becomes a regular column that Plotly can read as your X-axis.*

---

## Summary
You have built a complete IoT data pipeline:
1.  **Ingest:** Bridge MQTT to SQLite.
2.  **Process:** Use Pandas for aggregation.
3.  **Visualize:** Use Plotly for interactive dashboards.

**Next:** Review the [Week 6 README](./README.md) for a summary of learning objectives.

**Last updated:** 2026-02-24
