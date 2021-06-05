from flask import Flask, render_template, url_for, request, jsonify
from enum import Enum
# import mqtt_data
import paho.mqtt.client as mqtt
app = Flask(__name__)

class PaletteType(Enum):
    MONOTONE = 1
    DOUTONE = 2
    COLORFUL = 3

class HarmonyRule(Enum):
    COMPLEMENTARY = 1
    ANALOGOUS = 2
    TRIAD = 3
    SQUARE = 4
    BRISE_FAN = 5
    SPLIT_COMPLEMETARY = 6
    DOUBLE_SPLIT_COMPLEMENTARY = 7
    NONE = 8

res = {
    'primaryColor': '#FFFFFF',
    'paletteType': PaletteType(1).name,
    'DOUTONE': HarmonyRule(8).name,
    'COLORFUL': HarmonyRule(8).name,

}

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts, title='Hey')

@app.route('/about')
def about():
    my_var = request.args.get('my_var', None)
    return render_template('about.html', posts=posts, var=my_var)

@app.route('/test')
def test():
    # return 'This is my first API call!'
    global data
    broker = "io.adafruit.com"
    client = mqtt.Client('user1')
    client.username_pw_set(username="khanhdk0000",password="aio_mwIg04X7dgAqiO4gVjJ9QZG0LxXR")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect(broker, 1883, 60)
    client.subscribe('khanhdk0000/feeds/light')
    # client.publish("khanhdk0000/feeds/light", "123456779")
    client.loop_forever()
    return mqtt_data.getData()

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
    broker = "io.adafruit.com"
    client = mqtt.Client('user1')
    client.username_pw_set(username="khanhdk0000",password="aio_mwIg04X7dgAqiO4gVjJ9QZG0LxXR")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect(broker, 1883, 60)
    client.subscribe('khanhdk0000/feeds/light')
    # client.publish("khanhdk0000/feeds/light", "123456779")
    client.loop_forever()

@app.route('/test2', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True)
     domain = input_json['domain']
     if domain == 'Ecommerce':
         res['primaryColor'] = '#E1D89F'
         return jsonify(res)
     return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)


