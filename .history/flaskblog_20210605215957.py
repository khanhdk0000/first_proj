from flask import Flask, render_template, url_for, request, jsonify
from enum import Enum
import mqtt_data
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
    return get

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


