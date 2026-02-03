# Chapter 9: Dictionaries

## Objective
Create and use dictionaries to store key-value pairs—ideal for structured IoT data like sensor readings.

## Prerequisites
- Chapter 8 (Lists)

---

## Concepts
Dictionaries store key-value pairs:
- **Syntax:** `{key: value, key2: value2}`
- **Access:** `d["key"]` or `d.get("key")`
- **Nested:** Dictionaries can contain other dicts or lists
- **Keys** must be unique; typically strings or numbers

---

## Example 1: Basic Dictionary – Sensor Reading

**What it does:** Represents a sensor reading as a dictionary—a natural structure for IoT monitoring data.

**Code:** Save as `ch09_dicts.py`

```python
# ch09_dicts.py
from datetime import datetime

reading = {
    "name": "TempSensor-01",
    "value": 25.5,
    "unit": "°C",
    "timestamp": datetime.now().isoformat(),
}

print("Sensor:", reading["name"])
print("Value:", reading["value"], reading["unit"])
print("Full dict:", reading)

# Access with .get() - returns None if key missing
print("Unit (get):", reading.get("unit"))
```

**Explanation:**
- Dictionary literal `{}` defines key-value pairs
- `reading["name"]` accesses by key
- `reading.get("key")` returns None if key is missing (safer than `[]`)
- `datetime.now().isoformat()` gives current time in ISO format

**How to run:**
```bash
python ch09_dicts.py
```

**Expected output:**
```
Sensor: TempSensor-01
Value: 25.5 °C
Full dict: {'name': 'TempSensor-01', 'value': 25.5, 'unit': '°C', 'timestamp': '2026-02-03T...'}
Unit (get): °C
```

---

## Example 2: Nested Dictionaries and Updates

**What it does:** Models a device with nested configuration and status—common in IoT device representations.

**Code:** Save as `ch09_nested.py`

```python
# ch09_nested.py
device = {
    "id": "DEV-001",
    "type": "Temperature Controller",
    "config": {
        "min_temp": 20,
        "max_temp": 80,
        "unit": "°C",
    },
    "status": {
        "online": True,
        "last_reading": 45.2,
    },
}

print("Device:", device["id"], "-", device["type"])
print("Range:", device["config"]["min_temp"], "-", device["config"]["max_temp"], device["config"]["unit"])
print("Online?", device["status"]["online"])

# Update a value
device["status"]["last_reading"] = 46.1
print("Updated reading:", device["status"]["last_reading"])
```

**Explanation:**
- `config` and `status` are nested dictionaries
- Access nested values with chained brackets: `device["config"]["min_temp"]`
- Dictionaries are mutable; you can change values after creation

**How to run:**
```bash
python ch09_nested.py
```

**Expected output:**
```
Device: DEV-001 - Temperature Controller
Range: 20 - 80 °C
Online? True
Updated reading: 46.1
```

---

## Try It Yourself
1. Add a `quality` key with value "GOOD" to the reading dictionary.
2. Create a dictionary with a list of recent readings: `"readings": [22, 23, 24]`.
3. Use `.keys()` and `.values()` to iterate over a dictionary.

---

## Key Takeaways
- Dictionaries store key-value pairs with `{key: value}`
- Access with `d["key"]` or `d.get("key")`
- Nested dicts model complex structures
- Dictionaries are mutable

---

## Next
→ [Chapter 10: File I/O and CSV](./Ch10-FileIO-CSV.md)
