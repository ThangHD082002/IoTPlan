from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.



# import paho.mqtt.client as paho

# client = paho.Client(client_id="a612099c8cef47249fb4fc1f7cbcb44e", userdata=None, protocol=paho.MQTTv5)
# # client.tls_set(tls_version=paho.client.ssl.PROTOCOL_TLS)

# client.username_pw_set("django", "Thang123456")

# client.connect("a612099c8cef47249fb4fc1f7cbcb44e.s2.eu.hivemq.cloud", 8883)

# client.publish("encyclopedia/temperature", payload="hot", qos=1)

# client.subscribe("encyclopedia/#", qos=1)
# print(client.subscribe("encyclopedia/#", qos=1))


# import paho.mqtt.client as paho
# import time

# def on_publish(client, userdata, mid):
#     print("mid: "+str(mid))
 
# client = paho.Client()
# client.on_publish = on_publish
# client.connect('broker.mqttdashboard.com', 1883)
# client.loop_start()

# while True:
#     temperature = read_from_imaginary_thermometer()
#     (rc, mid) = client.publish('encyclopedia/temperature', str(temperature), qos=1)
#     time.sleep(30)

