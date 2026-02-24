# Read 03 – IoT Data Visualization

A dashboard is the "face" of an IoT system. In this chapter, we look at how to turn your processed Pandas dataframes into charts that help users understand the system's state.

## 1. Why Visualise?

Numbers in a database are hard for humans to scan. Visuals help us identify:
*   **Trends:** Is the temperature rising steadily?
*   **Cycles:** Does humidity drop every time the AC turns on?
*   **Anomalies:** Was there a sudden spike that shouldn't be there?

## 2. Python Visualization Libraries

Depending on your goal, you might choose different libraries.

### Matplotlib
*   **Type:** Static plotting.
*   **Usage:** Best for reports, research papers, or pre-generating images for a simple web interface.
*   **Style:** Very customizable but "old-school" look and no interactivity.

### Plotly
*   **Type:** Interactive plotting (Web-based).
*   **Usage:** Standard for modern IoT dashboards. Can zoom, pan, and hover over data points.
*   **Style:** Modern and sleek. Works well inside browser-based apps.

### Seaborn
*   **Type:** Statistical visualization.
*   **Usage:** Built on top of Matplotlib. Makes advanced charts (like correlation heatmaps) look beautiful with minimal code.

## 3. Common IoT Chart Types

### Line Charts (Time-Series)
The most common IoT chart. X-axis is Time, Y-axis is the sensor value.
*   **Best for:** Temperature, Pressure, Voltage over time.

### Gauges
Shows the *current* value against a minimum and maximum.
*   **Best for:** Real-time monitoring of speed, tank level, or CPU usage.

### Histograms
Shows the distribution of values.
*   **Best for:** Understanding how often a value falls into certain ranges (e.g. "How many hours a day is the temp between 20-25°C?").

### Heatmaps
Shows data density over two dimensions (often Time vs. Day of the week).
*   **Best for:** Energy consumption patterns or facility occupancy.

## 4. Dashboard Design Principles

When building a dashboard, keep these in mind:
*   **Low Cognitive Load:** Don't clutter the screen with too many charts. Focus on the "Vital Signs".
*   **Appropriate Scaling:** Don't start your Y-axis at zero if the variation is only between 24.5 and 25.1 (unless the zero baseline is critical).
*   **Color Meanings:** Use Red for danger/hot, Blue for cold/normal, Green for safe.
*   **Update Frequency:** Match the refresh rate to the data source. If a sensor sends data every 10 minutes, don't refresh the chart every second.

## 5. Summary of the Flow

1.  **Ingestion:** Python script listens to MQTT and saves to SQLite.
2.  **Selection:** Pandas queries the SQLite database for a specific time range.
3.  **Refinement:** Pandas resamples or cleans the data.
4.  **Display:** Plotly or Matplotlib generates the chart from the Pandas DataFrame.

---
**Next:** [WS-01 – Workshop: Database Storage](./WS-01-DatabaseStorage.md)

**Last updated:** 2026-02-24
