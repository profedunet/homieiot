import paho.mqtt.client as mqtt
from secret import credentials

broker_address = credentials.get('host')
username = credentials.get('username')
password = credentials.get('password')

client = mqtt.Client("P1")
client.username_pw_set(username, password)
client.connect(broker_address)
client.publish("test", "OFF")
