import paho.mqtt.client as mqtt
import datetime
from pymongo import MongoClient


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sensors/temp")

def on_message(client, userdata, msg):
    receiveTime=datetime.datetime.now()
    message=msg.payload.decode("utf-8")
    isfloatValue=False
    try:
        # Convert the string to a float so that it is stored as a number and not a string in the database
        val = float(message)
        isfloatValue=True
    except:
        isfloatValue=False

    if isfloatValue:
        print(str(receiveTime) + ": " + msg.topic + " " + str(val))
        post={"time":receiveTime,"topic":msg.topic,"value":val}
    else:
        print(str(receiveTime) + ": " + msg.topic + " " + message)
        post={"time":receiveTime,"topic":msg.topic,"value":message}

    collection.insert_one(post)

# Set up client for MongoDB
mongoClient=MongoClient()
db=mongoClient.SensorData
collection=db.home_data


# Initialize the client that should connect to the Mosquitto broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1", 1883, 60)

# Blocking loop to the Mosquitto broker
client.loop_forever()
