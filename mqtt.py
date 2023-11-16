import paho.mqtt.client as paho
from paho import mqtt
import time
import random

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("django", "Thang123456")
client.connect('a612099c8cef47249fb4fc1f7cbcb44e.s2.eu.hivemq.cloud', 8883)
# client.connect('broker.hivemq.com', 8884)

client.loop_start()

while True:
    temperature1 = random.uniform(18, 40)
    temperature2 = random.randint(65, 90)

    (rc, mid) = client.publish('nhietdo', str(temperature1 ) + " nhietdo", qos=1)
    (rc, mid1) = client.publish('doam', str(temperature2) + " doam", qos=1)
    time.sleep(4)


# import threading
# import asyncio

# # Hàm chạy trong luồng 1
# def loop1():
#     for i in range(5):
#         print(f"Thread 1 - Iteration {i}")

# # Hàm chạy trong luồng 2
# def loop2():
#     for i in range(5):
#         print(f"Thread 2 - Iteration {i}")

# thread2 = threading.Thread(target=loop2)
# thread1 = threading.Thread(target=loop1)

# thread2.start()
# thread1.start()


# thread1.join()
# thread2.join()

# print("All threads have completed.")
