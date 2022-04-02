# Import packages
# - Python Native
import datetime
import glob
import sys
import time
from sys import stdout
# # - Numpy
# import numpy as np
import paho.mqtt.client as mqtt

mqtt_broker = "192.168.1.107"
mqtt_user = "laptop"
mqtt_pass = "MQTTPASS"
mqtt_topic = "outTopic"
broker_port = 1885

filename = 'log.csv'
# Create header
# with open(filename, 'a') as file:
#     file.write(f"TIME,READING\n")

def on_message(client, userdata, message):
    print(f"Message Recieved: {message.topic}: {message.payload.decode()}")
    if message.topic == mqtt_topic:
        # Create the reading
        timestamp = datetime.datetime.now()
        reading = message.payload.decode()
        # DO THE DATA CLEANING ON READING VALUE HERE
        print ("Writing the reading of sensor...")
        #  Print it and flush standard output
        with open(filename, 'w') as file: #a - additive and w - write
            file.write(f"{timestamp},{reading}\n")
            file.close()
        sys.stdout.flush()

client = mqtt.Client(clean_session = True)
client.on_message = on_message
client.username_pw_set(username = mqtt_user, password = mqtt_pass)
client.connect(mqtt_broker, broker_port)


# Subscribe to your topic here
client.subscribe(mqtt_topic, qos=0)


# Start looping (non-blocking)
client.loop_start()

while True:
    continue
# 	# Read data here
# 	sensor_reading = read_sensor()
# 	# Publish data here
# 	client.publish(topic="input", payload=sensor_reading, qos = 1, retain = False)
# 	time.sleep(5)



