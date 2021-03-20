from flask import Flask, request, redirect
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/whoiam')
def whoiam():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/map')
def url_map():
    return str(app.url_map)


@app.route('/bad_page')
def bad_page():
    return '<h1>Bad Request</h1>', 400


@app.route('/google')
def googleredir():
    return redirect('http://www.google.com')


if __name__ == '__main__':
    manager.run()
