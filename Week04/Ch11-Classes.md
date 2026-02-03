# Chapter 11: Classes

## Objective
Define classes with constructors, properties, and methods to combine data and behavior.

## Prerequisites
- Chapter 10 (File I/O and CSV)

---

## Concepts
Classes are blueprints for objects:
- **`__init__`** – Constructor; runs when creating an instance with the class name
- **`self`** – Refers to the current instance
- **Methods** – Functions defined inside the class; first parameter is `self`
- **Instantiation** – `obj = ClassName(args)` creates an instance

---

## Example 1: Simple Sensor Class

**What it does:** Defines a `Sensor` class with name, unit, and a `read()` method that returns a simulated reading—models IoT components in software.

**Code:** Save as `ch11_classes.py`

```python
# ch11_classes.py
import random

class Sensor:
    def __init__(self, name, unit, base_value=25):
        self.name = name
        self.unit = unit
        self.base_value = base_value

    def read(self):
        noise = (random.random() - 0.5) * 2
        value = self.base_value + noise
        return {"value": value, "unit": self.unit}

temp_sensor = Sensor("TempSensor-01", "°C", 25)
reading = temp_sensor.read()

print("Sensor:", temp_sensor.name)
print("Reading:", reading["value"], reading["unit"])

# Second sensor
pressure_sensor = Sensor("PressureSensor-01", "kPa", 101)
p_reading = pressure_sensor.read()
print("Pressure:", p_reading["value"], p_reading["unit"])
```

**Explanation:**
- `__init__` initializes the instance; `self.name` stores instance data
- `read()` is a method; `self.unit` accesses instance attributes
- `Sensor(...)` creates an instance; each instance has its own state

**How to run:**
```bash
python ch11_classes.py
```

**Expected output (values vary):**
```
Sensor: TempSensor-01
Reading: 25.34 °C
Pressure: 101.2 kPa
```

---

## Example 2: Class with State and Multiple Methods

**What it does:** Models a simple thermostat controller that tracks state and makes decisions—combines data with behavior.

**Code:** Save as `ch11_thermostat.py`

```python
# ch11_thermostat.py
class ThermostatController:
    def __init__(self, setpoint):
        self.setpoint = setpoint
        self.heating_on = False

    def update(self, current_temp):
        if current_temp < self.setpoint - 1:
            self.heating_on = True
            print(f"Heat ON (temp {current_temp} < setpoint {self.setpoint})")
        elif current_temp > self.setpoint + 1:
            self.heating_on = False
            print(f"Heat OFF (temp {current_temp} > setpoint {self.setpoint})")

    def is_heating(self):
        return self.heating_on

thermostat = ThermostatController(25)
thermostat.update(22)  # Heat ON
thermostat.update(26)  # Heat OFF
print("Heating?", thermostat.is_heating())
```

**Explanation:**
- `setpoint` and `heating_on` are instance attributes
- `update()` modifies internal state based on current temperature
- Hysteresis (±1°C) avoids rapid on/off switching
- `is_heating()` exposes state without allowing direct mutation

**How to run:**
```bash
python ch11_thermostat.py
```

**Expected output:**
```
Heat ON (temp 22 < setpoint 25)
Heat OFF (temp 26 > setpoint 25)
Heating? False
```

---

## Try It Yourself
1. Add `min` and `max` to the Sensor class and clamp the reading in `read()`.
2. Add a `get_setpoint()` method to ThermostatController.
3. Create an `Actuator` class with `turn_on()` and `turn_off()` methods.

---

## Key Takeaways
- Classes combine data (attributes) and behavior (methods)
- `__init__` runs when you create an instance
- `self` refers to the current instance
- Use `ClassName(args)` to create an instance

---

## Next
→ [Chapter 12: Modules and Packages](./Ch12-Modules.md)
