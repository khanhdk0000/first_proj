from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return '<h1>Hello, fuck!</h1>'

@app.route('/about')
def about():
    return '<h1>Hello, about!</h1>'

if __name__ == '__main__':
    app.run(debug=True)