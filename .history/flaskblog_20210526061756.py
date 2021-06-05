from flask import Flask, render_template, url_for, request, jsonify
app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(debug=True)


