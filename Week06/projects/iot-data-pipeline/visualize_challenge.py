import pandas as pd
import sqlite3
import plotly.express as px
import os

# 1. Database Path
# Adjust path if script is run from Week06/ instead of the backend folder
db_path = "projects/iot-data-pipeline/iot_data.db"
if not os.path.exists(db_path):
    db_path = "iot_data.db"

if not os.path.exists(db_path):
    print(f"Error: Could not find database at {db_path}")
    exit()

# 2. Load Data
conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM sensor_readings", conn)
conn.close()

# 3. Preparation & Cleaning
df['timestamp'] = pd.to_datetime(df['timestamp'])
temp_df = df[df['topic'] == 'sensors/temperature'].copy()

# 4. Aggregation (1-minute intervals)
# We aggregate Mean, Min, and Max. '1min' is used for minute-by-minute resampling.
minute_stats = temp_df.set_index('timestamp')['value'].resample('1min').agg(['mean', 'min', 'max']).reset_index()

# 5. Create Interactive Chart
fig = px.line(minute_stats, 
              x='timestamp', 
              y=['mean', 'min', 'max'],
              title='Temperature Analysis: Mean, Min, and Max per Minute',
              labels={
                  'timestamp': 'Time',
                  'value': 'Temperature (°C)',
                  'variable': 'Stat Type'
              },
              template='plotly_dark') # Adding a dark theme for a premium look

# 6. Save and Show
fig.write_html("temperature_analysis.html")
print("Analysis complete. Saved to temperature_analysis.html")
fig.show()
