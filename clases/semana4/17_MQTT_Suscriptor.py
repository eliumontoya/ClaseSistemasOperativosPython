'''
Created on 11 dic. 2023

@author: eliumontoya
'''


# Suscriptor MQTT
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()} en el tema {msg.topic}")

client = mqtt.Client()
client.on_message = on_message
client.connect('localhost', 1883)

client.subscribe('topic/sensores')
client.loop_forever()