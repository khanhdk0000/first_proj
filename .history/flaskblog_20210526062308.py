from flask import Flask, render_template, url_for, request, jsonify
import enum
app = Flask(__name__)

Tem = enum.

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
    return 'This is my first API call!'

@app.route('/test2', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)

if __name__ == '__main__':
    app.run(debug=True)


