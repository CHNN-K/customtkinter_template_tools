import paho.mqtt.client as mqtt
import time
import random

letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
topicList = ["test","test2","test3","new1","new2"]

# Define the MQTT broker details
broker = "test.mosquitto.org"  # You can replace this with your broker address
port = 1883  # Default MQTT port

# Define the topic and message
topic = "test"

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker, port, 60)

client.publish("test", "", retain = True)

# Publish the message to the specified topic
for i in range (0, 9999):
    time.sleep(1)
    text = ""
    for j in range (0, random.randrange(3,9)):
        text += random.choice(letter)
    client.publish(random.choice(topicList), f"{text}")
    print(f"Publish : Test Message : {i} | To topic : {topic}")
print("End publish loop process")

# Disconnect from the broker
client.disconnect()