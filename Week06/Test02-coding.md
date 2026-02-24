# Test 02 – Coding: Data Pipeline & Visualization

**Topic:** AUT561 Week 06 – Coding tasks (Pandas and Plotly). You may use AI tools to help write code.

**Total: 5 marks** (each question shows mark allocation).

---

## Question 1: Data Filtering with Pandas

Assume you have a Pandas DataFrame `df` loaded from `iot_data.db` with columns `['timestamp', 'topic', 'value']`.

Write a **Python function** `get_sensor_subset(df, sensor_name)` that:
1. Filters the DataFrame to include only rows where the `topic` matches the provided `sensor_name`.
2. Converts the `timestamp` column to actual Python `datetime` objects.
3. Returns the filtered and converted DataFrame.

**(1.5 marks)**

**Submit:** A Python file (e.g., `t2_filter.py`) containing the function.

---

## Question 2: Resampling & Summary

Using the filtered DataFrame from Question 1, write a short code snippet that:
1. Sets the `timestamp` column as the index.
2. **Resamples** the data into **5-minute intervals**.
3. Calculates the **Maximum** value for each interval.
4. Returns/Prints the first 5 rows of the resulting summary.

**(1.5 marks)**

**Submit:** A Python file (e.g., `t2_summary.py`) with the resampling logic.

---

## Question 3: Visualization Logic

Write a Python script using **Plotly Express** (`px`) to create a **Line Chart** from a DataFrame called `summary_df`. The chart must include:
- `timestamp` on the X-axis.
- `value` on the Y-axis.
- A custom title: **"Machine Temperature: 5-Minute Maximums"**.
- Custom labels for the axes.
- A **Dark Theme** template.

**(2 marks)**

**Submit:** A Python file (e.g., `t2_viz.py`) that exports the figure to an HTML file named `test_chart.html`.

---

**End of Test 02 – Total: 5 marks**
