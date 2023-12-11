'''
Created on 11 dic. 2023

@author: eliumontoya

pip3 install paho-mqtt


'''

# Publicador MQTT
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost', 1883)

client.publish('topic/sensores', 'Mensaje de temperatura: 25°C')
client.disconnect()