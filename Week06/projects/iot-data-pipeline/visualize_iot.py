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



# Filter for temperature only
temp_only = df[df['topic'] == 'sensors/temperature']

# Create Histogram
fig_hist = px.histogram(temp_only, x="value", 
                         title="Temperature Distribution",
                         nbins=20)

fig_hist.write_html("temp_histogram.html")
print("Histogram saved to temp_histogram.html.")
fig_hist.show()