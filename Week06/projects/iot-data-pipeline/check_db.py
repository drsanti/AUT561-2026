import sqlite3
conn = sqlite3.connect("iot_data.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM sensor_readings LIMIT 10")
for row in cursor.fetchall():
    print(row)
conn.close()
