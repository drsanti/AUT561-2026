import random
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.loop_start()

try:
    while True:
        temp = round(random.uniform(20.0, 35.0), 1)
        client.publish("sensors/temperature", str(temp))
        print(f"Published temperature: {temp}")
        time.sleep(2)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
