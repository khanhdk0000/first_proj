import paho.mqtt.client as mqtt
import mqtt_data as

data = ''
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    if rc == 0:
        print('good')
    else:
        print('no good')

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_log(client, userdata, level, buf):
    print("log: " + buf)


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code " + str(rc))

def on_message(client, userdata, message):
    global data
    print("message received  "  ,str(message.payload.decode("utf-8")))
    data += str(message.payload.decode("utf-8"))

def getData():

    global data
    broker = "io.adafruit.com"
    client = mqtt.Client('user1')
    client.username_pw_set(username="khanhdk0000",password="aio_mwIg04X7dgAqiO4gVjJ9QZG0LxXR")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message


    client.connect(broker, 1883, 60)
    client.subscribe('khanhdk0000/feeds/light')
    yield data
    # client.publish("khanhdk0000/feeds/light", "123456779")
    client.loop_forever()