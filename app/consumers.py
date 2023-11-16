import json
import threading
import paho.mqtt.client as paho
from paho import mqtt
from channels.generic.websocket import AsyncWebsocketConsumer
import time
import asyncio
from .models import Data
from asgiref.sync import sync_to_async
import datetime



def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

async def send_mqtt_message(consumer, message):
    # Gửi thông điệp từ MQTT đến consumer WebSocket
    await consumer.send(text_data=json.dumps({'message': message}))



def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))



def mqtt_loop(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(client.loop_forever())
    except Exception as e:
        print(f"MQTT Loop Exception: {e}")
    finally:
        loop.close()

def start_mqtt_thread(client):
    mqtt_thread = threading.Thread(target=mqtt_loop, args=(client,))
    mqtt_thread.start()
    return mqtt_thread



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
        client.on_connect = on_connect
        client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        # client.username_pw_set("django", "Thang123456")
        # client.connect("a612099c8cef47249fb4fc1f7cbcb44e.s2.eu.hivemq.cloud", 8883)
        client.connect('broker.hivemq.com', 8883)
        client.on_subscribe = on_subscribe
        
        client.on_publish = on_publish
        

        client.subscribe("doamkhongkhi/iot/thang", qos=1)
        client.subscribe("nhietdo/iot/thang", qos=1)
        client.subscribe("doamdat/iot/thang", qos=1)

        # client.publish("thang", payload="hot", qos=1)


        

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        
        
        await self.accept()
        
        
        
        mqtt_thread = start_mqtt_thread(client)


        @sync_to_async
        def save_data_to_database(payload):
            mess = {'message': str(payload)}
            inputString = str(payload)
            numeric_part = inputString[1:]
            numeric_part = ''.join(char for char in numeric_part if char.isdigit() or char == '.')
            numeric_value = float(numeric_part)
            data = Data.objects.create(temperature=numeric_value)
            data.save()
            print(str(payload))

        async def on_message(client, userdata, msg):  
            
            await save_data_to_database(msg.payload)
            now = datetime.datetime.now()
            data = str(str(msg.payload) + " " + str(now))
            mess = {'message': data}
            await self.send(text_data=json.dumps(mess))

        def on_message_wrapper(client, userdata, msg):
            asyncio.run(on_message(client, userdata, msg))


        client.on_message = on_message_wrapper

           
        

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        name = text_data_json['name']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'name': name
            }
        )

    async def chat_message(self, event):
        message = event['message']
        name = event['name']

        await self.send(text_data=json.dumps({
            'message': message,
            'name': name
        }))
