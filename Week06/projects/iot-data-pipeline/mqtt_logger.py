import paho.mqtt.client as mqtt
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# 1. Database Setup
Base = declarative_base()

class SensorData(Base):
    __tablename__ = 'sensor_readings'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    topic = Column(String)
    value = Column(Float)

# Create SQLite database file
engine = create_engine('sqlite:///iot_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

# 2. MQTT Callbacks
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected to broker with result {rc}")
    client.subscribe("sensors/#")

def on_message(client, userdata, msg):
    try:
        # Convert payload to float
        val = float(msg.payload.decode())
        print(f"Logging {msg.topic}: {val}")
        
        # Save to database
        new_reading = SensorData(topic=msg.topic, value=val)
        db_session.add(new_reading)
        db_session.commit()
    except Exception as e:
        print(f"Error processing message: {e}")

# 3. Main Loop
# Use CallbackAPIVersion.VERSION2 for newer paho-mqtt
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
