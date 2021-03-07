import paho.mqtt.client as mqtt
from secret import credentials

broker_address = credentials.get('host')
username = credentials.get('username')
password = credentials.get('password')

base_path = 'controllers/controller_id'

client = mqtt.Client("P1")
client.username_pw_set(username, password)
client.connect(broker_address)
client.publish(f'{base_path}/$name', 'Solar Controller')
client.publish(f'{base_path}/$state', 'ready')
client.publish(f'{base_path}/$notes', 'testnode')
client.publish(f'{base_path}/testnode/$name', 'Temp Sensor')
client.publish(f'{base_path}/testnode/$type', 'Type')
client.publish(f'{base_path}/testnode/$properties', 'switchy')
client.publish(f'{base_path}/testnode/switchy/$name', 'My switchy')

client.publish(f'{base_path}/testnode/switchy/$setable', 'true')
client.publish(f'{base_path}/testnode/switchy/$datatype', 'boolean')
client.publish(f'{base_path}/testnode/switchy/$name', 'My switchy')

client.publish(f'{base_path}/$homie', '3.0')
client.publish(f'{base_path}/$stats/interval', '60')
