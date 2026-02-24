import random
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.loop_start()

try:
    while True:
        humidity = random.randint(40, 80)
        client.publish("sensors/humidity", str(humidity))
        print(f"Published humidity: {humidity}")
        time.sleep(3)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
