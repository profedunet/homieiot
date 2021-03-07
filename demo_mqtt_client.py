import paho.mqtt.client as mqtt
from secret import credentials

broker_address = credentials.get('host')
username = credentials.get('username')
password = credentials.get('password')

# create a client instance
client = mqtt.Client()


# The callback for when the client recieves a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("connected with the result code "+str(rc))
    print("usrData: "+str(userdata))
    print("client: " +str(client))
    print("flags: " +str(flags))

# efine any topics you would like the pi to
# automatically subscribe to here

# The callback for when this client publishes to the server.
def on_publish(client, userdata, mid):
    print("message published")


# The callback for when a PUBLISH message is recieve from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def on_log(client, userdata, level, buf):
    print(str(level)+" "+str(buf))


# set callbacks
def setup():
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_log = on_log



# setup connection to broker
def connect(username, password):
    client.username_pw_set(username, password)
    client.connect(host=broker_address)

# publish to a topic
def publish(topic, message):
    client.publish(topic, message)


def loop():
    client.loop()
