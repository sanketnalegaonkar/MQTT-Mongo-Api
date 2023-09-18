import time
import random
import paho.mqtt.client as mqtt


def on_publish(client, userdata, mid):
    print("sent a message")


mqttClient = mqtt.Client("Temperature_Sensor")
mqttClient.on_publish = on_publish
mqttClient.connect('127.0.0.1', 1883)
# start a new thread
mqttClient.loop_start()

# Why use msg.encode('utf-8') here
# MQTT is a binary based protocol where the control elements are binary bytes and not text strings.
# Topic names, Client ID, Usernames and Passwords are encoded as stream of bytes using UTF-8.
while True:
    msg = f'{random.randint(15,50)}'
    info = mqttClient.publish(
        topic='sensors/temp',
        payload=msg.encode('utf-8'),
        qos=0,
    )
    # Because published() is not synchronous,
    # it returns false while he is not aware of delivery that's why calling wait_for_publish() is mandatory.
    info.wait_for_publish()
    print(info.is_published())
    time.sleep(3)
   