from flask import Flask, request, redirect, render_template
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


@app.route('/tmp/<name>')
def render(name):
    return render_template('hellotemp.html', name=name)


@app.route('/tmp/dict/<int:key>')
def get_value(key):
    cdict = {
        1: 'один',
        2: 'тест'
    }
    return render_template('dicttemp.html', dict=cdict, key=key)


@app.route('/tmp/cycle')
def tmp_cycle():
    array = [0, 5, 8, 12, 9, 'FFF', 4, 8, 54, 84, 56, 84, 54]
    return render_template('cycletemp.html', array=array)

if __name__ == '__main__':
    manager.run()
